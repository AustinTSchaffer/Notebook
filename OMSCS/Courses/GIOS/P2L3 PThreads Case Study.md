---
tags: OMSCS, GIOS, PThreads
---
# P2L3: PThreads Case Study
- [[#PThread Creation|PThread Creation]]
	- [[#PThread Creation#Detaching PThreads|Detaching PThreads]]
- [[#Compiling PThreads|Compiling PThreads]]
- [[#PThread Gotchas|PThread Gotchas]]
- [[#PThread Mutexes|PThread Mutexes]]
	- [[#PThread Mutexes#Other Mutex Operations|Other Mutex Operations]]
	- [[#PThread Mutexes#Safety Tips|Safety Tips]]
- [[#PThread Condition Variables|PThread Condition Variables]]
	- [[#PThread Condition Variables#Other Condition Variable Operations|Other Condition Variable Operations]]
	- [[#PThread Condition Variables#Safety Tips|Safety Tips]]
- [[#Producer-Consumer Example in PThreads|Producer-Consumer Example in PThreads]]
	- [[#Producer-Consumer Example in PThreads#Producer Code|Producer Code]]
	- [[#Producer-Consumer Example in PThreads#Consumer Code|Consumer Code]]

## Overview
Callback to Birrell's paper, which talks about threads in a fairly universal and generic way. This lecture talks about #PThreads (POSIX Threads) which is a concrete multithreading standard.

#POSIX = Portable Operating System Interface

PThreads describes the threading API that OSes need to support. Specifies syntax and semantics of the operations.

Supplemental materials for this lecture
- [[P2 Birrell Paper.pdf]] ([[P2 Birrell Paper Notes]])
- [Lawrence Livermore National Laboratory's series on PThreads](https://hpc-tutorials.llnl.gov/posix/)

## PThread Creation
| Birrell's Abstractions | PThreads                                        |
| ---------------------- | ----------------------------------------------- |
| Thread                 | `pthread_t`                                     |
| Fork(proc, args)       | `int pthread_create(pthread, attr, func, args)` |
| Join(thread)           | `int pthread_join(pthread)`                     |

PThread Attributes
- `pthread_attr_t`
	- specified in pthread create
	- define features of the new thread
		- stack size
		- inheritance
		- joinable
			- requires particular attention
		- scheduling policy
		- priority
		- system/process scope
	- has default behavior when NULL is passed to pthread create

### Detaching PThreads
By default, threads are "joinable", meaning threads can wait on the completion of other threads. If a parent thread exits early, child threads can become "zombie threads".

In PThreads, it's possible for threads can become "detached" via `int pthread_detach()`. They can also be created in a detached state using `pthread_attr_setdetachstate(attr, PTHREAD_CREATE_DETACHED)`, and passing `attr` to pthread create. This makes parents and children threads "on the same level". If the parent exits/dies, the child can live on.

![[Pasted image 20220929194352.png]]

Since the parent thread doesn't need to wait for detached children, it can exit with `pthread_exit()`.

## Compiling PThreads
- include `<pthread.h>` in the main file
- Compile source with `-lpthread` or `-pthread`
- Check return values of common function. Good practice in general, always check the return code, especially for production code.

## PThread Gotchas
- Be sure to call `pthread_join` on each thread ID, unless each threads are "detached". You may need to store an array of thread IDs.
- To ensure that data passed to one thread doesn't alter data passed to other threads, use arrays to store data on a per-thread basis.
- Use mutexes ya dummy.


## PThread Mutexes

| Birrell's Abstractions | PThreads API                                 |
| ---------------------- | -------------------------------------------- |
| Mutex                  | `pthread_mutex_t`                            |
| `Lock(mutex) {  }`     | `int pthread_mutex_lock(mutex)`              |
| (implicit unlock)      | `int pthread_mutex_unlock(mutex)` (explicit) |

```C
// Birrell
list<int> mylist;
Mutex m;
void safe_insert(int i) {
	Lock(m) {
		mylist.insert(i);
	} // unlock
}

// PThreads
list<int> mylist;
pthread_mutex_t m;
void safe_insert(int i) {
	pthread_mutex_lock(m);
	mylist.insert(i);
	pthread_mutex_unlock(m);
}
```

### Other Mutex Operations
- `int pthread_mutex_init(mutex, attr)`
	- Allows the dev to pass mutex attributes.
	- Permits mutexes to be shared among processes
	- Default is private to a process
- `int pthread_mutex_trylock(mutex)`
	- Notifies the calling thread if the mutex is currently locked (return value)
	- Otherwise gives the calling thread the mutex
- `int pthread_mutex_destroy(mutex)`
	- Adios Muchaha

### Safety Tips
- shared data should be access through a single mutex
- mutex scope should be visible to all threads
- globally order your locks. for all threads, lock mutexes in order
- always unlock a mutex. Always unlock the _correct_ mutex

## PThread Condition Variables
They allow a thread to wait until some other thread notifies the thread with `signal` or `broadcast`

| Birrell's Abstractions | PThreads API                         |
| ---------------------- | ------------------------------------ |
| Condition              | `pthread_cond_t`                     |
| Wait                   | `int pthread_cond_wait(cond, mutex)` |
| Signal                 | `int pthread_cond_signal(cond)`      |
| Broadcast              | `int pthread_cond_broadcast(cond)`   |

### Other Condition Variable Operations
- `int pthread_cond_init(cond, attr)`
	- Allows setting attributes to non-default values.
	- e.g. is it shared among processes
- `int pthread_cond_destroy(cond)`

### Safety Tips
- Don't forget to notify waiting threads
- Predicate change -> signal/broadcast correct CV
- when in doubt, broadcast, eat the spurious wakeup performance penalty with your wallet
- You don't need a mutex to signal/broadcast. Signal outside the lock if possible, avoid spurious wakeups

## Producer-Consumer Example in PThreads

```C
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define BUFSIZE 3

int buffer[BUFSIZE];
int add = 0; // Buffer index to add next element
int rem = 0; // Buffer index to remove next element
int num = 0; // Number of elements in the buffer

// Mutex lock for buffer
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

// Consumer wait condition
pthread_cond_t c_cons = PTHREAD_COND_INITIALIZER;

// Producer wait condition
pthread_cond_t c_prod = PTHREAD_COND_INITIALIZER;

// Note the void* type on params and return values
// for the producer/consumer functions.
void *producer (void *param);
void *consumer (void *param);

int main() {
	// 2 variables to store thread IDs
	// pthread create producer (default attrs)
	// pthread create consumer (default attrs)
	// pthread join t1 and t2
	// printf("Adios, main thread quitting \n")
	return 0;
}
```

### Producer Code
![[Pasted image 20220929201403.png]]

### Consumer Code
![[Pasted image 20220929201522.png]]
