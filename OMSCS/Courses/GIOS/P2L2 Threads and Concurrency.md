---
tags: #OMSCS, #GIOS, #Threads, #Processes
---

# P2L2 Threads and Concurrency
Processes are represented by their address space (virtual address space) and their execution context (subset of the PCB).
- Registers
- Stack
- Stack pointer etc

If we want a process to be able to take advantage of multiple CPU cores, it must be multithreaded.
- Single threaded processes have one execution context
- Multithreaded processes have multiple execution contexts
- Each thread has its own execution context

This lecture covers
- What threads are
- How threads are different from processes
- The data structures that are used to implement and manage threads

Andrew D. Birrell's paper, An Introduction to Programming with Threads ([[Birrell Paper.pdf]]), is supplemental to this lecture.

## Visual Metaphor
A thread is like a worker in a toy shop
- active entity. Actively executing a unit of work.
- works simultaneously with others. Many workers completing similar or different tasks.
- requires coordination with other workers. Share tools, parts, workstations.

## Process vs Thread
> Worst Marvel crossover movie to date. However surprisingly more engaging than Dr. Strange 2.

A **single-threaded** process is represented by its address space. It's also represented by its execution context. All of this info is recorded in the process's Process Control Block ( #PCB).

A **multi-threaded** process still is represented by a single address space. The process has multiple execution contexts for the process.
- Each ex context has its own register.
- Each ex context has its own stack.
- Both share the same heap.

This is all still stored in a single PCB, but the structure is more complicated than the PCB of a single-threaded process.

![[Pasted image 20220925143032.png]]

## Benefits of Multi-Threading
- **parallelization**
	- Threads can split a large task into smaller subtasks that can be executed concurrently.
- **specialization**
	- Threads can also execute completely different components of the program, each with their own priorities.
	- Another benefit of this approach is that each CPU core has its own cache/registers, so its more likely that a specialized threaded program will have a hotter cache than an equivalent singlethreaded program.
	- This also has a memory usage benefit over an equivalent multi-process implementation because all of the threads share an address space. More memory efficient. Application is more likely to fit in memory. Fewer swaps. Synchronizing between threads is easier than synchronizing between processes.
- **non-blocking I/O** alternatively **latency hiding**
	- You can also offload I/O waits onto different threads so the I/O waits don't block the execution of the main thread.
	- If the time that a thread spends idle waiting on I/O or some other event takes longer than the time it takes for the OS to perform 2 context switches between threads, then it makes sense to use multiple threads, even if you only have s single CPU.
	- This effectively "hides" latency.

**Note:** The time it takes to context switch between different threads is _shorter_ than the time it takes to context switch between different processes.

The OS kernel can also be multithreaded, which allows the OS to more efficiently support multiple multithreaded applications.
- OS threads working on behalf of apps
- OS-level services like daemons or drivers

## How to support threads
- thread data structure
	- identify threads, keep track of resource usage
- mechanisms to
	- create and manage threads
	- safely coordinate among threads running concurrently in the same address space
		- thread waiting on results from another thread
		- threads not stepping on eachother's toes (overwriting each other's memory)

The OS ensures that 2 processes don't have access to a single physical addresses. Multi-threaded programs share the same virtual address space, so the multi-threaded programs themselves must be able to ensure that guarantee on their own, using **synchronization mechanisms**.

These **synchronization mechanisms** include
- mutexes
	- Mutual Exclusion locks
	- exclusive access to only one thread at a time
- condition variables
	- waiting on other threads
	- specific condition must be met before proceeding

## Thread Creation
This lesson is just explaining the concepts at a more fundamental level.

**Thread type**
- thread data structure (contains thread ID, PC, SP, registers, stack, attributes, etc)

**Fork (proc, args)**
- creates a thread
- not to be confused with the UNIX system call `fork()`. This fork executes a procedure with the specified arguments
- This creates a new thread data structure (PC = proc, stack = args)
- Once fork completes, the process contains one additional thread.
- Once the new thread finishes, and returns a result or status code, general practice has the thread store the result in a "well-defined" location, in a space that's accessible to all other threads.
- More generally, we need a mechanism to determine when a thread is done, and hold the results/status of the computation. Parent thread also needs a way to wait on a child thread's result.

**Join (thread)**
- Typically called by a parent thread on a child thread
- the calling thread will block until the other thread finishes, and will receive the results returned by the other thread.

### Example
```c
Thread thread1;
Shared_list list;

void safe_insert(int integer) {
	list.insert(integer);
}

void main() {
	thread1 = fork(safe_insert, 4);
	safe_insert(6);
	join(thread1); // optional
	return;
}
```

list may end up as:
- `4 -> 6 -> null` or
- `6 -> 4 -> null`

Join is not really necessary in this case except to block the main thread, since the result of the computation is being stored in a "well-defined location".

In actuality, `safe_insert` would need to use a mutex lock to exclude multiple threads from attempting to make changes to the list at the same time, or ensuring that one thread isn't reading an old copy of the list (if that might cause an issue, might not matter).

## Mutual Exclusion
A key challenge of multi-threaded applications is ensuring that multiple threads can coordinate access to shared resources.

A mutex is implemented by the OS and threading libraries. It's like a lock. When a thread locks a mutex, it gets exclusive access to run instructions guarded by the mutex. Note that mutex locks can cover entirely different sections of code as well.

Threads need to acquire the lock. If a thread has the lock and another thread attempts to acquire it, the other thread will block until the thread that has the mutex lock releases/unlocks it.

The OS and/or threading library will maintain a (possibly unordered) list of threads that are blocked waiting to acquire the mutex lock. It also needs to maintain a reference to the current owner of the mutex lock. When the owner of a lock releases the lock, **any one** of the threads waiting on the lock may then acquire the lock and continue execution.

A portion of code that is protected by a mutex is referred to as a **critical section**. Programmers should attempt to minimize the amount of code that lives in the critical section, since critical sections necessarily reduce the amount of code that can be executed concurrently. All other sections of code are free to execute concurrently (or not 🤷).

threading API's commonly have 2 separate functions to lock and unlock mutexes.

**Example:**
```c++
list<int> mylist;
Mutex m;
void safe_insert(int i) {
	Lock(m) {
		mylist.insert(i);
	} // implied "unlock" in this fake threading library
}
```

**Producer / Consumer Example**
> What if the processing you wish to perform with **mutual exclusion** needs to occur only under certain **conditions**?

![[Pasted image 20220925161716.png]]

Adding/removing entries from list, and verifying whether the list is "full", are all operations that would be protected by the mutex. The "only when the list is full" is the **condition**.

```C
for i=0..10
	producers[i] = fork(safe_insert, NULL);
consumer = fork(print_and_clear, my_list);

// producers: safe_insert
Lock(m) {
	list->insert(my_thread_id)
} // unlock;

// consumer: print_and_clear
Lock(m) {
	if (my_list.full) {
		/* print; clear up to limit of elements of list */
	}
	else {
		/* release lock and try again */
	}
} // unlock;
```

This is **WASTEFUL!!!** The consumer will burn tons of CPU cycles just checking the size of the list.

## Condition Variables
Used in conjunction with mutexes to control the execution of programs.

Threads can lock a mutex and release the lock by calling a function to **wait** on a condition variable, in conjunction with the mutex. Other threads can then **signal** the condition variable. The original thread then waits to re-acquire the mutex lock, and continues its execution from the next statement after the call to the "wait function".

![[Pasted image 20220925162442.png]]

In cases where "wait for condition" calls are intended to wait on a "signal condition" call, they are typically surrounded by a while loop.
- This ensures that a "signal condition" call doesn't put a thread into a bad state, where it's about to process a condition that isn't actually valid.
- Also ensures that threads don't enter the waiting condition if there's already a valid condition that they can process. 
- This also allows support for multiple consumer threads.
- You can't guarantee access to the mutex once the condition is signaled
- The list could also change before the consumer gets access again.

A common Condition Variable API has the following features

- **condition type**
	- mutex ref
	- waiting threads
	- ...
- **wait(mutex, condition)**
	- mutex is automatically released and reacquired on wait
	- thread added to queue/list of waiting threads
	- on signal/broadcast, thread is removed from the queue, and is free to reacquire the mutex. 
- **signal(condition)**
	- notifies only one thread waiting on a condition
- **broadcast(cond)**
	- notifies all **waiting** threads (important that it only notifies threads that _are_ waiting)
	- the library will still ensure that only one thread acquires the mutex

## Reader / Writer Problem
TODO: Continue from P2L2 section 19 of 42.

https://gatech.instructure.com/courses/270294/pages/19-reader-slash-writer-problem?module_item_id=2665896