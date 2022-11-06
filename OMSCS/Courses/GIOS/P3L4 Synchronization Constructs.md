---
tags: OMSCS, GIOS, Synchronization
---
# P3L4: Synchronization Constructs

## Overview
- more synchronization constructs
- hardware supported synchronization

Supplemental paper: [[P3L4 Anderson Paper.pdf]]
- efficient implementation of spinlock (sync) alternative

## More About Synchronization
- mutexes
- condition variables
- limitations of both
	- error prone / correctness / ease-of-use
	- unlock wrong mutex, signal wrong CV
	- lack of expressive power
	- helper variables for access or priority control
- low-level support
	- requires hardware atomic instructions to guarantee correctness

## Spinlocks (basic sync construct)
A spinlock is like a mutex
- mutual exclusion
- lock and unlock (free)

`spinlock_lock(s)` and `spinlock_unlock(s)`

A thread that is spinning is busy, NOT blocked

## Semaphores
- common sync construct in OS kernels
- like a traffic light, stop and go
- similar to a mutex, but more general

Semaphores have an integer value, and use a count-based syntax.
- On init, they're assigned some max value. This is a max count for the critical section.
- On try (wait), if non-zero, decrement and proceed. Counting semaphore.
- If initialized with one, the semaphore is a mutex (a binary semaphore).
- on exit, post. Increments the counter.

### POSIX Semaphore API

```c
#include <semaphore.h>

sem_t sem;
sem_init(sem_t *sem, int pshared, int count);
sem_wait(sem_t *sem);
sem_post(sem_t *sem);
```

`sem_init(&sem, 0, 1)` behaves identically to a PThreads mutex.

## Reader/Writer Locks
- read = never modify
	- shared access
- write = always modify
	- exclusive access

RWLocks
- specify the type of access, then lock behaves accordingly

Linux example usage:

```c
#include <linux/spinlock.h>

rwlock_t m;
read_lock(&m);
	// critical section
read_unlock(&m);

write_lock(&m);
	// critical section
write_unlock(&m);
```

- rwlock support in Windows (.NET), Java, POSIX...
- read/write = shared/exclusive
- semantic differences
	- recursive read_lock -> what happens on read_unlock?
	- upgrade / downgrade priority?
	- interaction with scheduling policy
		- e.g. a reader could block if a higher priority writer waiting

## Monitors
- higher-level synchronization concept
	- MESA by XEROX PARC
	- Java
		- synchronized methods generate monitor code
		- `notify()` explicitly called by programmer
- explicity specify:
	- what is the shared resource?
	- entry procedures?
	- possible condition variables?
- on entry
	- lock, check
- on exit
	- unlock, check, signal

monitors use a programming style

## Additional Constructs
- serializers to define priorities
- path expressions, specify regex to capture sync behavior
- barriers, opposite of a semaphore, waits until n-threads arrive at the mutex/condition
- redezvous points, waits for threads to arrive before releasing them all
- optimistic wait-free sync, (example: read-copy-update (RCU)), bet on the fact that there won't be conflicts on writes, and allow reads to proceed

ALL CONSTRUCTS REQUIRE HARDWARE SUPPORT.

## Re: Spinlocks
- most basic sync construct
- Callback to the supplemental paper
	- alternative implementations of spinlocks
	- generalizes techniques to other constructs
- Not possible to implement directly in software:

```c
while(lock == BUSY);
lock = BUSY;
```

The code above is not an atomic instruction, and therefore it's a race condition. 2 threads may both evaluate the condition simultaneously, and end up setting the lock to BUSY twice.

Therefore we need hardware-supported atomic instructions.

## Hardware Support: Atomic Instructions
Examples of atomic instructions 
	- `test_and_set`
	- `read_and_increment`
	- `compare_and_swap`
- Guarantees
	- atomicity, atomic instructions perform compound instructions
	- mutual exclusion, only one instruction may perform the appropriate instruction at a time
	- queue all concurrent instructions but one
- The atomic instruction is the critical section, with hardware-supported synchronization

```c
while(test_and_set(lock) == busy);
```

`test_and_set(lock)` atomically returns (tests) original value of lock and sets the new value to 1 (busy) if it's free.

Each CPU has to list the atomic instructions that it supports.

## Shared Memory Multiprocessors

![[Pasted image 20221105205512.png]]

![[Pasted image 20221105205528.png]]

- reminder, shared memory multiprocessor systems are multiple CPUs that access shared memory locations
- caches
	- each CPU can have caches, which hides memory latency. More important because memory is "further away" due to resource contention.
	- no-write: some systems don't allow CPUs to write to cache memory. They instead write directly to main memory
	- write-through: some systems allow the CPU to write to both the cache location and then also the main memory location.
	- write-back: write is applied in cache, but updating the main-memory location happens later

### Cache Coherence
- what happens when multiple CPUs reference the same data?
- data can appear in multiple caches
- non-cache-coherent (NCC) architectures don't try to ensure that caches are coherent. Conflicts must be solved in software
- cache-coherent (CC) architectures ensure that caches are kept up to date

**write-invalidate (WI)**
- one CPU changes X
- hardware invalidates cache locations that also contain X
- pros
	- lower bandwidth, only need to pass an address to fix coherence
	- amortizes coherence costs over multiple changes
	- data only invalidated once

**write-update (WU)**
- one CPU changes X
- hardware automatically updates cache locations that also contain X
- pros
	- updates are available immediately

This is determined by hardware architecture. Programmers have no say, apart from when they choose the hardware they want to run their program on.

### Cache Coherence and Atomics
- Situation
	- CPU_A performs `atomic(X)`
	- CPU_B performs `atomic(X)`
	- X in caches for both A and B
- What to do?

- Atomics are always issued to the memory controller
	- can be ordered and synchronized
	- atomic instructions always take longer
	- generates coherence traffic, regardless of whether `X` changes
- Atomics & SMP
	- expensive because of bus or I/C contention
	- expensive because they bypass the cache, also because it generates coherence traffic

## Spinlock Performance Metrics
- useful performance metrics

1. reduce latency
	- time to acquire a free lock
	- ideally, immediately execute atomic
2. reduce waiting time (delay)
	- time to stop spinning and acquire a lock that has been freed
	- ideally, immediately
3. reduce contention
	- bus/network I/C traffic
	- ideally zero

Metric 3 conflicts with metrics 1 and 2, regardless of implementation.

It's kind of crazy how the issues present in distributed computing are also present between different processors within a computer.

### Test-And-Set Spinlock
```c
while(test_and_set(lock) == busy);
```

- lowest latency, just atomic
- potentially lowest waiting time, depending on hardware implementation
- loads of contention traffic. processors go to memory on each spin.

Biggest problem with this implementation is that it spins on an atomic! Not the best usage of atomics nor the hardware that implemented the atomic.

### Test-And-Test-And-Set Spinlock
```c
while((lock == busy) OR (test_and_set(lock) == busy));
```

Similar to test-and-set, except the first test uses the cached copy of the lock.
- spin on read
- spin on cached value
- ok latency
- ok delay
- better contention, but
	- NCC? no difference from `test_and_set`
	- CC with WU, works ok
	- CC with WI, terrible performance! Threads end up spending a lot of time trying to read from an invalidated memory location.

### Spinlock "Delay" Alternatives
#### Delay after lock release
```c
while((lock == busy) OR (test_and_set(lock) == busy)) {
	// failed to acquire lock
	while(lock == busy);
	delay();
}
```

- introduce a delay after lock is released.
	- everyone sees that the lock is free
	- not everyone attempts to acquire the lock
- contention: improved, fewer threads fighting the hardware for the lock, using atomic instructions as swords
- latency: acquiring a free lock is efficient
- delay: much worse. Acquiring a locked lock means your thread has to incur an explicit delay, and probably still won't acquire the lock.

#### Delay after each lock reference
```c
while((lock == busy) OR (test_and_set(lock) == busy))
{
  delay();
}
```

- doesn't spin constantly
- works on NCC architectures
- can hurt delay even more
- contention is improved
- latency is ok
- delay is much worse

#### Picking a Delay
- static delay
	- based on fixed value, also based on CPU ID to ensure that delays are different per-cpu
	- simple approach
	- **unnecessary delay under low contention**
- dynamic delay
	- retry-backoff
	- random delay in a range that increases with "perceived" contention
	- How do we know how much contention there is in the system?
	- "perceived" can be driven by failed `test_and_set` operations
	- delay after each reference will keep growing based on contention AND/OR the length of the critical section
	- Need to guard against length of the critical section causing the delay to grow exponentially

Both should behave similarly at high load.

## Queuing Lock
Common problem in spinlock implementations
- everyone tries to acquire a lock at the same time once lock is freed
- everyone sees the lock is free at the same time
	- use a queuing lock to make sure not everyone sees the lock is free at the same time

![[Pasted image 20221105222039.png]]

- set unique ticket for arriving threads
- assigned `queue[ticket]` is private lock
- enter critical section when you have lock
	- `queue[ticket] == must_wait` ? spin
	- `queue[ticket] == has_lock` ? enter critical section
- signal/set next lock holder on exit
	- `queue[(ticket + 1) % N] = has_lock`

- downsides:
	- assumes `read_and_increment` is atomic
	- $O(N)$ space complexity per resource/lock

### Queuing Lock (Anderson Lock) Implementation
```c
p = N

init:
	flags[0] = has_lock;
	flags[1 .. p-1] = must_wait;
	queuelast = 0; // global var

lock:
	// "mod p" because the array wraps around
	myplace = read_and_increment(queuelast) % p;
	// spin
	while(flags[myplace] == must_wait);
	// critical section
	flags[myplace] = must_wait;

unlock:
	// notify the next thread in line
	flags[(myplace + 1) % p] = has_lock;
```

- Latency? More costly to perform `read_and_increment` than `test_and_set`
- Delay? Great. Directly signal next CPU/thread to run.
- Contention? better! requires CC and cacheline aligned elements
	- "cacheline aligned elements" means every element needs a separate cache line. Cache line sizes depends, 64-bytes is a real-world example.

Best benefit, only 1 CPU/thread sees that the lock is free and tries to acquire the lock at a time.

## Performance Comparison
![[Pasted image 20221105223723.png]]

**Note: Spin on Read and queue have their colors swapped in the legend.**

- Setup
	- N processes running critical section 1million times
	- N varied based on system. Anderson's machine had 20 processors.
- Metrics
	- overhead compared to ideal performance.
	- theoretical limit based on # of critical sections to be run.

Graph doesn't include `test_and_set` because it would just go straight up off the charts.

**Under high loads**
- queue is the best overall (when number of processors/processes is above 6).
- `test_and_test_and_set` is the worst
- for delay implementations
	- static is better than dynamic
	- ref is better than release (avoids extra invalidations)

**Under light loads**
- `test_and_test_and_set` is good (low latency)
- dynamic is better than static (lower delay)
- queuing lock is the worst (high latency due to `read_and_increment`)

This graph points to the fact that there is no one true ideal system design.