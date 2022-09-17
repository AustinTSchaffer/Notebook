---
tags: GIOS, OMSCS, C, Threads, PThreads
---

# The PThreads API

The original Pthreads API was defined in the ANSI/IEEE POSIX 1003.1 - 1995 standard. The POSIX standard has continued to evolve and undergo revisions, including the Pthreads specification.

The subroutines which comprise the Pthreads API can be informally grouped into four major groups:

- **Thread management**
	- Routines that work directly on threads - creating, detaching, joining, etc.
	- They also include functions to set/query thread attributes (joinable, scheduling etc.)
- **Mutexes**
	- Routines that deal with synchronization, called a "mutex", which is an abbreviation for "mutual exclusion"
	- Mutex functions provide for creating, destroying, locking and unlocking mutexes.
	- These are supplemented by mutex attribute functions that set or modify attributes associated with mutexes
- **Condition variables**
	- Routines that address communications between threads that share a mutex.
	- Based upon programmer specified conditions.
	- This group includes functions to create, destroy, wait and signal based upon specified variable values.
	- Functions to set/query condition variable attributes are also included.
- **Synchronization**
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