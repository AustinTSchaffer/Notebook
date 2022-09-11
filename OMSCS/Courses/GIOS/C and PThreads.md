---
tags: GIOS, OMSCS, C, Threads, PThreads
---

# Intro to POSIX Threads (PThreads)
https://hpc-tutorials.llnl.gov/posix/

> In shared memory multiprocessor architectures, threads can be used to implement parallelism. Historically, hardware vendors have implemented their own proprietary versions of threads, making portability a concern for software developers. For UNIX systems, a standardized C language threads programming interface has been specified by the IEEE POSIX 1003.1c standard. Implementations that adhere to this standard are referred to as POSIX threads, or Pthreads.
>
> Source: Trust Me Bro
> (Source: https://hpc-tutorials.llnl.gov/posix/abstract/)

## The PThreads API
The original Pthreads API was defined in the ANSI/IEEE POSIX 1003.1 - 1995 standard. The POSIX standard has continued to evolve and undergo revisions, including the Pthreads specification.

The subroutines which comprise the Pthreads API can be informally grouped into four major groups:

- Thread management
	- Routines that work directly on threads - creating, detaching, joining, etc.
	- They also include functions to set/query thread attributes (joinable, scheduling etc.)
- Mutexes
	- Routines that deal with synchronization, called a "mutex", which is an abbreviation for "mutual exclusion"
	- Mutex functions provide for creating, destroying, locking and unlocking mutexes.
	- These are supplemented by mutex attribute functions that set or modify attributes associated with mutexes
- Condition variables
	- Routines that address communications between threads that share a mutex.
	- Based upon programmer specified conditions.
	- This group includes functions to create, destroy, wait and signal based upon specified variable values.
	- Functions to set/query condition variable attributes are also included.
- Synchronization
	- Routines that manage read/write locks and barriers.

The Pthreads API contains around 100 subroutines. Though there is a naming convention that helps programmers identify the role of each subroutine. All identifiers in the threads library begin with `pthread_`. Some examples of common prefixes:

| Routine Prefix       | Functional Group                                 |
| -------------------- | ------------------------------------------------ |
| `pthread_`           | Threads themselves and miscellaneous subroutines |
| `pthread_attr`       | Thread attributes objects                        |
| `pthread_mutex_`     | Mutexes                                          |
| `pthread_mutexattr_` | Mutex attributes objects                         |
| `pthread_cond_`      | Condition variables                              |
| `pthread_condattr_`  | Condition attributes objects                     |
| `pthread_key_`       | Thread-specific data keys                        |
| `pthread_rwlock_`    | Read/write locks                                 |
| `pthread_barrier_`   | Synchronization barriers                         |

The concept of **opaque objects** pervades the design of the API. The basic calls work to create or modify opaque objects. The opaque objects can be modified by calls to attribute functions, which deal with opaque attributes. This is effectively how C handles objects with private members.

For portability, the `pthread.h` header file should be included in each source file using the Pthreads library.

The current POSIX standard is defined only for the C language.

## What are Threads?
- A thread is an independent stream of instructions that can be scheduled to run by an OS
- To a programmer, threads are procedures that can be executed in isolation from the main runtime of a program. This is typically to accomplish many similar tasks in parallel, making for better utilization of the compute hardware.
- Programs that use threads to accomplish tasks in parallel are referred to as "multi-threaded".

First, to recap, UNIX Processes are created by the OS. Processes contain metadata about program resources and execution state, like:
- IDs
	- Process ID
	- Process Group ID
	- User ID
	- Group ID
- Environment
- Working directory
- Program instructions
- Registers
- The program's stack and heap
- File descriptors
- Signal actions
- Shared libraries
- Inter-process communication tools
	- Message queues
	- pipes
	- semaphores
	- shared memory

**A Unix Process**
![[Pasted image 20220911143819.png]]

**Threads Within a Unix Process**
![[Pasted image 20220911143858.png]]

Threads use and exist within these process resources, yet are able to be scheduled by the OS and run as independent entities. They duplicate only the bare essential resources that enable them to exist as executable code.

This independent flow of control is accomplished because threads maintain their own:
- Stack pointer
- Registers
- Scheduling properties (policy/priority)
- Set of pending and blocked signals
- Thread specific data

In a Unix environment, a thread:
- Exists within  a process and uses the process's resources
- Has its own independent flow of control as long as
	- its parent process exists, and
	- the OS supports it
- Duplicates only the essential resources it needs to be independently schedulable
- May share the process resources with other threads that act equally independently (and dependently)
- Dies if the parent process dies, or something similar
- Is "lightweight" because most of the overhead has already been accomplished through the creation of its parent process.

Because threads within the same process share resources:
- Changes made by one thread to shared system resources (such as closing a file) will be seen by all other threads.
- All threads share the same memory page table and virtual memory address space. An identical pointer that exists in 2 threads points to the same physical address.
- Reading and writing to the same memory locations is possible, and therefore requires explicit synchronization by the programmer.

## What are PThreads?
Historically, hardware vendors have implemented their own proprietary versions of threads. These implementations differed substantially from each other making it difficult for programmers to develop portable threaded applications.

In order to take full advantage of the capabilities provided by threads, a standardized programming interface was required.

- For UNIX systems, this interface has been specified by the IEEE POSIX 1003.1c standard (1995).
- Implementations adhering to this standard are referred to as POSIX threads, or "Pthreads".
- Most hardware vendors now offer Pthreads in addition to their proprietary API’s.

The POSIX standard has continued to evolve and undergo revisions, including the Pthreads specification. Some useful links:
-   [standards.ieee.org/findstds/standard/1003.1-2008.html](http://standards.ieee.org/findstds/standard/1003.1-2008.html)
-   www.opengroup.org/austin/papers/posix_faq.html

Pthreads are defined as a set of C language programming types and procedure calls, implemented with a `pthread.h` header/include file and a thread library. This library may be part of another library, such as `libc`, in some implementations.

## Why Pthreads?
- Lightweight
	- Threads are lightweight compared to creating a new process
	- `fork()` is an example of creating a new processes within a process.
	- Using `pthread_create()` is (can be) faster than using `fork()`
- Efficient communication and data exchange
	- Threads enable optimal performance
	- Pthreads don't require an intermediate memory copy, because threads share the same address space within a process. This means that there is effectively no data exchange. Pthreads can just pass pointers between each other and/or the main thread.
	- In the worst case, pthread communication become more of a cache-to-CPU or memory-to-CPU bandwidth issue.
- Other common reasons
	- Overlapping CPU work with I/O
		- A program may have sections where it is performing a long I/O operation.
		- While one thread is waiting for an I/O system call to complete, CPU intensive work can be performed by other threads.
	- Priority/real-time scheduling
		- tasks which are more important can be scheduled to supersede or interrupt lower priority tasks.
	- Asynchronous event handling
		- tasks which service events of indeterminate frequency and duration can be interleaved
		- For example, a web server can both transfer data from previous requests and manage the arrival of new requests.
- Examples
	- web browsers can interleave tasks happening at the same time and tasks can vary in priority.
	- modern operating systems make use of threads

## Designing Threaded Programs
### Parallel Programming
On modern, multi-core computing systems, pthreads are ideally suited for parallel programming. Whatever applies to parallel programming in general applies to parallel pthread programs

There are many considerations for designing parallel programs, such as
- What type of parallel programming model to use?
- How do we partition the problem?
- How do we balance load between each thread? Is that a necessary consideration for single-node parallelization?
- How much communication is required between threads?
- What data does each thread depend on?
- How do we synchronize and prevent race conditions?
- How do we handle issues such as
	- memory issues?
	- I/O issues?
- How do we manage program complexity, i.e. programmer effort/costs/time?

In general, in order for a program to take advantage of PThreads, it must be able to be organized into discrete, independent tasks, which can execute concurrently. For example, if `routine1` and `routine2` can be interchanged, interleaved, and/or overlapped in real time, they are candidates for threading.

![[Pasted image 20220911151756.png]]

Programs having the following characteristics may be well suited for pthreads:
- Work that can be executed, or data that can be operated on, by multiple tasks simultaneously:
- Block for potentially long I/O waits
- Use many CPU cycles in some places but not others
- Must respond to asynchronous events
- Some work is more important than other work (priority interrupts)

Several common models for threaded programs exist:
- **Manager/worker**
	- a single thread, the manager assigns work to other threads, the workers
	- Typically, the manager handles all input and parcels out work to the other tasks
	- At least two forms of the manager/worker model are common: **static worker pool** and **dynamic worker pool**.
- **Pipeline**
	- a task is broken into a series of suboperations
	- each is handled in series, but concurrently, by different threads
	- An automobile assembly line best describes this model.
- **Peer**
	- similar to the manager/worker model, but after the main thread creates other threads, it participates in the work.

### Shared Memory Model

All threads have access to the same global, shared memory. Threads also have their own private data. Programmers are responsible for synchronizing (and protecting) access to globally shared data.

![[Pasted image 20220911152916.png]]

### Thread-safety
Thread-safeness and thread-safety: refer to an application’s ability to execute multiple threads simultaneously without clobbering shared data or creating race conditions.

For example, suppose that your application creates several threads, each of which makes a call to the same library routine:

- This library routine accesses/modifies a global structure or location in memory.
- As each thread calls this routine it is possible that they may try to modify this global structure/memory location at the same time.
- If the routine does not employ some sort of synchronization constructs to prevent data corruption, then it is not thread-safe.

![[Pasted image 20220911153027.png]]
The implication to users of external library routines is that if you aren’t 100% certain the routine is thread-safe, then you take your chances with problems that could arise.

**Recommendation:** Be careful if your application uses libraries or other objects that don’t explicitly guarantee thread-safeness. When in doubt, assume that they are not thread-safe until proven otherwise. This can be done by "serializing" the calls to the uncertain routine, using a PThread mutex lock for example.

### Thread Limits
Although the Pthreads API is a standard (ANSI/IEEE), implementations can, and usually do, vary in ways not specified by the standard. Because of this, a program that runs fine on one platform, may fail or produce wrong results on another platform. For example, the maximum number of threads permitted, and the default thread stack size are two important limits to consider when designing your program.