---
tags: OMSCS, GIOS, Threads, PThreads
---
# P2L4: Thread Design Considerations
- [[#Kernel vs User Level Threads|Kernel vs User Level Threads]]
- [[#Thread-related Data Structures|Thread-related Data Structures]]
- [[#Rationale for Multiple Datastructures|Rationale for Multiple Datastructures]]
- [[#Quiz: Linux KThread Structures|Quiz: Linux KThread Structures]]
- [[#User Level Structures in Solaris 2.0|User Level Structures in Solaris 2.0]]
- [[#Kernel Level Structures in Solaris 2.0|Kernel Level Structures in Solaris 2.0]]
- [[#Basic Thread Management Interactions|Basic Thread Management Interactions]]
- [[#Quiz: PThread Concurrency|Quiz: PThread Concurrency]]
- [[#Thread Management Visibility and Design|Thread Management Visibility and Design]]
- [[#How/When does the UL Library run?|How/When does the UL Library run?]]
- [[#Issues on Multiple CPUs|Issues on Multiple CPUs]]
	- [[#Issues on Multiple CPUs#Thread Mutexes and Priority|Thread Mutexes and Priority]]
	- [[#Issues on Multiple CPUs#Synchronization-Related Issues|Synchronization-Related Issues]]
	- [[#Issues on Multiple CPUs#Destroying Threads|Destroying Threads]]
- [[#Quiz: Number of Threads|Quiz: Number of Threads]]
- [[#Interrupts and Signals|Interrupts and Signals]]
	- [[#Interrupts and Signals#Interrupt Handling|Interrupt Handling]]
	- [[#Interrupts and Signals#Signal Handling|Signal Handling]]
	- [[#Interrupts and Signals#Why Disable Interrupts or Signals?|Why Disable Interrupts or Signals?]]
	- [[#Interrupts and Signals#More on Signal Masks|More on Signal Masks]]
	- [[#Interrupts and Signals#Interrupts in Multicore Systems|Interrupts in Multicore Systems]]
	- [[#Interrupts and Signals#Types of Signals|Types of Signals]]
	- [[#Interrupts and Signals#Quiz: Signal Names|Quiz: Signal Names]]
	- [[#Interrupts and Signals#Handling Interrupts as Threads|Handling Interrupts as Threads]]
	- [[#Interrupts and Signals#Interrupts: Top vs Bottom Half|Interrupts: Top vs Bottom Half]]
	- [[#Interrupts and Signals#Performance of Threads as Interrupts|Performance of Threads as Interrupts]]
	- [[#Interrupts and Signals#Threads and Signal Handling|Threads and Signal Handling]]
		- [[#Threads and Signal Handling#Case 1|Case 1]]
		- [[#Threads and Signal Handling#Case 2|Case 2]]
		- [[#Threads and Signal Handling#Case 3|Case 3]]
		- [[#Threads and Signal Handling#Case 4|Case 4]]
- [[#Tasks in Linux|Tasks in Linux]]
	- [[#Tasks in Linux#Linux Task Creation|Linux Task Creation]]
	- [[#Tasks in Linux#Linux Threads Model|Linux Threads Model]]

## Overview
- Threads can be implemented at the Kernel level and at the user level.
- Threads and interrupts
- Threads and signal handling

Supplemental Materials
- [[P2 Eykholt Paper.pdf]] "Beyond Multiprocessing: Multithreading the Sun OS Kernel"
- [[P2 Stein Shah Paper.pdf]] "Implementing Lightweight Threads"

## Kernel vs User Level Threads
OS kernel maintains
- thread abstraction
- scheduling, sync, etc

User-level threading library provides
- thread abstraction, scheduling, sync, etc
- Different processes may even use different user-level threading libraries

User-level threads can be mapped onto kernel-level threads
- one-to-one (user-level thread per kernel-level thread)
- many-to-one
- many-to-many

## Thread-related Data Structures
Remember: whenever a process makes a system call, the process is interrupted and the kernel validates the request, then the operation runs in the context of a kernel-level thread.

- The user-level thread (ULT) library needs some kind of data structure
	- UL thread ID
	- UL registers
	- thread stack
- The Kernel needs to store the PCB
	- virtual address mapping
- Kernel Level Thread (KLT) thread management
	- stack
	- registers

![[Pasted image 20220930191651.png]]

For each process
- We need to maintain the relation ship between the ULT data structures and the PCB (virtual address mapping)
- We need to maintain a relationship between each PCB and the KLT data structures
- We need a pointers to current and other threads, and need to maintain relationships between the KLT data structures and a model of the CPU

![[Pasted image 20220930192014.png]]

When the kernel is multithreaded, we can have multiple kernel level threads supporting a single process.

When the kernel is supporting different processes, it can easily decide that it needs to invalidate address mappings when swapping one kernel thread to execute a thread for a different process.

When 2 kernel level threads belong to the same address space, there's info in the PCB that corresponds to each individual thread
- signals
- system call args

Context switching between different KLTs has implications for what PCB info is currently relevant. Virtual address mappings are preserved, but other things arent.

**Hard Process State**: Relevant to all KLTs
- Virtual address mapping

**Light Process State:** Relevant to a single KLT
- signal mask
- system call args

In a previous model where we only allowed single threads, all data about a process could be encapsulated by a single PCB. Now, we have to split up the PCB across all of these different components, in order to support multiple multithreaded applications running on a platform with a multi-core CPU.

![[Pasted image 20220930192633.png]]

## Rationale for Multiple Datastructures

Single PCB
- large continuous data structure
- private for each thread
- saved and restored on context switches
- update for any changes
- limitations
	- high overhead
	- low scalability
	- low performance
	- limited flexibility

Multiple data structures
- smaller data structures
- easier to share
- on context switching, only need to save and restore necessary changes
- user-level library need only update portion of the state
- limitations
	- more complicated
- benefits
	- opposite of all of the single PCB limitations

## Quiz: Linux KThread Structures
1. What is the name of the kernel thread structure?
	1. `kthread_worker`
2. What is the name of the data structure, contained in the above structure, that describes the process the kernel thread is running?
	1. `task_struct`
	2. NOT `kthread_work`

## User Level Structures in Solaris 2.0
![[Pasted image 20220930193928.png]]

This example is important because Sun 5 (aka Solaris 2?) had really good threading support in their kernel. This diagram shows the threading model supported in that version of the operating system.

- The OS is intended for a multiple processor system, supporting multiple kernel-level threads
- Process can be single threaded or multithreaded
- both one-to-one and many-to-many are supported for mapping user-level threads to kernel-level threads.
- Each kernel level thread that's executing a user-level thread has a lightweight data structure associated with that interaction.
- From the user-level process perspective, each user-level thread has "virtual CPUs" that it schedules the process threads to run on.
- At the kernel level, there's a kernel-level scheduler

UserLevel Thread Structure
- not POSIX threads, but similar
- thread creation returns a thread ID
- Thread ID is used as an index, correlated with a table of pointers
- The pointers point to the thread-specific data structure, containing
	- execution context
	- registers
	- signal mask
	- priority
	- stack pointer
	- thread local storage
		- includes variables defined in thread functions which are known at compile time.
	- stack. Can be user-provided.
	- most of this info is known at compile time. Helps achieve locality
- Problems
	- stack growth can be dangerous. possible that one thread will overwrite the data structure of another thread. Debugging this is hard. Solution was to pad the ending of each thread data structure with a "red zone". Refers to unallocated portion of address space. This will cause a fault if a thread tries to write to this region, which makes debugging easier.

## Kernel Level Structures in Solaris 2.0
- A Process 
	- list of kernel-level threads
	- virtual address space
	- user credentials
	- signal handlers
- Light-Weight Process (LWP)
	- user level registers
	- system call args
	- resource usage info
	- signal mask
	- similar to ULT, but visible to kernel. Not needed when process is not running.
	- **This information can be swapped.**
- Kernel-Level Threads
	- kernel-level registers
	- stack pointers
	- scheduling info
	- pointers to associated LWP, process, CPU structures
	- contains information that's needed even when a process is not running.
	- **This information is not swappable**.
- CPU (in-memory model of CPU)
	- current running thread
	- list of kernel-level threads
	- dispatching and interrupt handling information
	- on SPARC dedicated registers for storing the current thread.

Here's the relationships between all of these different data structures.

![[Pasted image 20220930195454.png]]

## Basic Thread Management Interactions
What happens when process starts?
- Kernel gives default number of KLTs.
- Process requests additional KLTs (`set_concurrency` system call)
- Kernel responds by creating additional threads.

When a ULT blocks on an I/O operation, this also blocks the KLT.

User-level library doesn't know what is happening in the kernel. The KLT library needs to notify the ULT library that it's about to block, so the ULT library can request more LWPs/KKTs. The KLT library will make more KLTs, allowing execution to continue.

Once the blocking I/O operations are complete, the KLT library will eventually notice that the ULT library is not using one of the KLTs, since the process is bounded by the predefined amount of concurrency. The KLT library will eventually destroy one of the KLTs and notify the ULT library that the KLT is no longer available.

The Kernel also doesn't know what's happening in the ULT library.

System calls and special signals allow kernel and ULT library to interact and coordinate.

## Quiz: PThread Concurrency
```bash
man pthread_setconcurrency
```

In the pthreads library, which function sets the concurrency level?

`pthread_setconcurrency`

For the above function, which concurrency value instructs the implementation to manage the concurrency level as it deeps appropriate?

> Specifying _new_level_ as 0 instructs the implementation to manage the concurrency level as it deems appropriate.


## Thread Management Visibility and Design
Kernel sees
- KLTs
- CPUs
- Kernel Level Scheduler

ULT library sees
- ULTs
- available KLTs

ULT library can "bind" a thread to a kernel level thread (ULT is "bound").

PROBLEM: Visibility of state and decisions between kernel and UL library. This is an issue if you only have one CPU and the code being executed has a mutex lock. Mutexes and wait queues are invisible to the kernel.

1-1 models help address some of these issues.

## How/When does the UL Library run?
- Thread lib is part of the process address space
- Process jumps to UL library scheduler when:
	- ULTs explicitly yield
	- timer set by UL library expires 
	- ULTs call library functions like lock/unlock/wait/signal/broadcast/etc
	- blocked threads become runnable
- UL library scheduler runs
	- on ULT operations
	- on signals from timer or kernel

## Issues on Multiple CPUs
- In a multiCPU system, KLTs may be running concurrently

### Thread Mutexes and Priority
Scenario
- Thread Priority: T3 > T2 > T1
- T2 is running a critical section on CPU A, T3 is waiting for the mutex, T1 is running on CPU B.
- T2 unlocks, makes T3 runnable
- OS/ULT lib want to preempt T1 on CPU B. We need to context switch T1. Somehow need to notify the other CPU to update its registers and program counters.
- Need to send signal to other thread, on other CPU B, to run library code locally.

Basically when we add multiple CPUs, the interactions between management and user levels become more complicated.

### Synchronization-Related Issues
Scenario
- T1 and T2 are running simultaneously on 2 different CPUs
- T1 is running a critical section
- T2 would like to acquire the mutex
- In normal operation
	- mutex queue
- In multi CPU system
	- owner of mutex is running on one cpu
	- it's possible by the time we context switch T2 and put it on the queue, in that amount of cycles, maybe T1 will complete the critical section
	- instead, T2 might just spin on the cpu, waste a few cycles, until T1 completes the critical section. This is wasteful usually, but in this case, it might waste fewer resources compared to all of the context switching and queueing operations on the mutex queue
- **Adaptive mutexes**
	- short critical section? don't block, spin
	- for long critical section, default blocking behavior involving altering the thread state and adding the thread to the mutex queue.
	- The mutex stores information about the thread that currently has the lock. Threading libraries can use this information to determine if the thread is running on a different CPU, and can use that info to determine if the waiting thread should spin.
	- Program needs some info about how long these kinds of critical sections are. Maybe handled by the compiler.

In a single CPU system, there's no need for adaptive mutexes.

### Destroying Threads
- Instead of destroying thread data structures, reuse them.
- when a thread exists
	- put it on death row
	- periodically destroy these data structures by reaper threads
	- otherwise, thread structures/stacks can be reused, which leads to performance gains, due to not needing to perform memory reallocation.

## Quiz: Number of Threads
In the Linux Kernel's code base, minimum number of threads required to allow system to boot?

- In the latest version of the kernel: `#define MIN_THREADS 20`
- In 3.17 though, it's in `fork.c` in the `init_fork` function. Also 20.

What is the name of the variable used to set this limit?

- in the latest version: `MIN_THREADS`
- in 3.17: `max_threads` in the `init_fork` function

## Interrupts and Signals
- Interrupts
	- **events** generated externally by components other than the CPU
		- I/O devices
		- timers
		- other CPUs
	- determined based on the physical platform
	- they appear asynchronously
- Signals
	- events generated/triggered by software running on the CPU
	- events triggered by the CPU
	- determined based on the OS
	- appear both synchronously and/or asynchronously
- Both Interrupts and Signals
	- have a unique ID depending on the hardware or OS
	- can be **masked**, disabled/suspended via corresponding mask
		- per-CPU interrupt mask
		- per-process signal mask
	- if enabled, trigger corresponding handler
		- **interrupt** handler **set for entire system** by OS
		- **signal** handlers are **set per process**

An interrupt is like a weather warning. Applies to the whole environment.

A signal is like a "low battery" warning. Applies to one thing.

### Interrupt Handling
- Interrupts are generated by an entity that is external to the CPU, such as a hard drive.
- Each interrupt has an interrupt type code (`INT#`), and an interrupt ID (`MSI#`)
- The interrupt type code is correlated with the "interrupt handler table". 
	- This table stores the start addresses of the routines that handle interrupts of type `INT#`.
	- PC is set to that starting address.
	- Each handler implementation is specific to that operating system
- All of this happens in the context of the thread that the interrupt targeted

### Signal Handling
- Signals are not generated by an external hardware device
- The OS defines a "signal handler table" for each process. Similarly to interrupts, the table maps `SIGNAL#` to handler code routine starting addresses.
- The OS defines default actions for each signal. Each process can specify how those signals should be handled. This is called "installing a handler".
- Synchronous signals
	- SIGSEGV (access to protected memory)
	- SIGFPE (divide by zero)
	- SIGKILL (kill, id). Can be directed to a specific thread.
- Asynchronous signals
	- SIGKILL (kill)
	- SIGALARM

### Why Disable Interrupts or Signals?
In some point, an interrupt or signal appears. The stack pointer stays the same, and the PC becomes set to a handler routine. If the handler routine attempts to acquire a mutex that's locked by the thread that received the event, that's a deadlock situation!

Resolutions
1. keep handler code simple. Maybe don't use mutexes in handlers. This is too restrictive.
2. Control interruptions by handler code
	- Use interrupt/signal masks
	- A bit mask is used to enable/disable individual events
	- threads can disable/enable interrupts and signals with `clear_field_in_mask` and `reset_field_in_mask`.
	- OS maintains a queue of pending interrupts

### More on Signal Masks
> moron

- Interrupt masks are per-CPU
- if mask disables interrupts, hardware interrupt routing mechanism will not deliver interrupt to CPU
- Signal masks are per execution context (ULT on top of KLT)
- if mask disables signal, kernel sees mask and will not interrupt corresponding thread

### Interrupts in Multicore Systems
- interrupts can be directed to any CPU that has them enabled
- may set interrupt on just a single core, meaning one core is designated as the CPU core that handles **all** of the system's interrupts. this avoids overheads and perturbations on all other cores. This improves application performance on all other cores.

### Types of Signals
- One-Shot Signals
	- "n signals pending == 1 signal pending": only one of the signals will be handled if there's a queue of unprocessed signals of that type.
	- The handler must be explicitly re-enabled after being invoked.
- Real-Time Signals
	- "if n signals are raised, then the handler will be called n times"

### Quiz: Signal Names
Reference `signal.h` (online reference: https://pubs.opengroup.org/onlinepubs/9699919799/)

- terminal interrupt signal: `SIGINT`
- high bandwidth data is available on a socket: `SIGURG`
- background process attempting write: `SIGTTOU`
- file size limit exceeded: `SIGXFSZ`

### Handling Interrupts as Threads
One possible way to implement interrupts to avoid deadlock situations is to allow interrupt code to be run as a completely new thread.

![[Pasted image 20221001141619.png]]

One major concern is that dynamic thread creation is expensive. You don't want the process creating and deleting threads whenever an interrupt occurs.

Dynamic Decision
- if handler doesn't attempt to acquire any mutexes, execute the handler on interrupted thread's stack
- if handler can block, turn the handler into a real thread

Optimization
- It's possible to pre-create and pre-init thread structures for interrupt routines on application startup
- This optimization can be performed by sufficiently feature-rich compilers

### Interrupts: Top vs Bottom Half
The "on thread" portion of an interrupt handler is considered the "top half" of the interrupt handler, and should only contain fast, non-blocking instructions, with a minimum amount of processing.

The "new thread" portion of an interrupt handler is considered the "bottom half" of the interrupt handler, and can have arbitrary complexity.

![[Pasted image 20221001143734.png]]

### Performance of Threads as Interrupts
On Solaris
- Overhead of this interrupt scheme is 40 SPARC instructions per interrupt
- This also saves 12 instructions per mutex, since there's no changes in interrupt masks being performed
- Fewer interrupts than mutex lock/unlock operations means that this is a win for performance.

Optimize for the common case! The common case is usually the mutex lock/unlock process.

### Threads and Signal Handling
- When a thread disables a signal, it clears a signal in its per-thread signal mask
- The OS still might have that signal mask bit set to `1`, meaning it will attempt to send signals of that type to the thread.
- What to do?

#### Case 1
- ULT mask = 1
- KLT mask = 1
- Thread will handle the interrupt.

#### Case 2
- KLT mask = 1
- ULT mask = 0
- Another ULT mask = 1
- If another ULT has the mask enabled, that other thread will handle the interrupt. This is brokered by the ULT library.
- The signal handlers table can point to routines that are managed by the ULT library, which can wrap each signal handling routine.

#### Case 3
- KLT mask = 1
- ULT mask = 0
- Another ULT mask = 1
- The other ULT is not on the run queue, it's actively running on another KLT on another CPU
- The other KLT mask = 1
- Library handling routing will kick in, it knows that there's another thread that can handle the signal
- It sees that the thread is associated with a LWP managed by the library
- The library will generate a **directed signal** to the other LWP.
- When the OS delivers the signal, it will see that the signal mask is enabled, and the OS will route the signal, and the library handling routine will re-process the signal.

![[Pasted image 20221001145646.png]]

#### Case 4
- All ULT masks = 0
- KLT mask = 1
- The kernel still thinks the process can handle the signal.
- The library handling routine will pick up the signal. It sees that the current thread has the mask set to 0. It also sees that all of the other ULTs have the mask set to 0.
- The ULT library will perform a system call to request that the KLT mask be set 0 on the specific KLT/LWP associated with the current thread.
- The ULT library will reissue the signal to other CPUs/LWPs/KLTs, which will cascade and cause the masks across all of the LWPs to be set 0.

**Optimize for the common case**
- signals less frequent than signal mask updates
- system calls avoided, cheaper to update the ULT mask
- signal handling is more expensive

## Tasks in Linux
- A task is the main execution abstraction.
- Single threaded processes have one task.
- Multithreaded processes have multiple tasks.

Linux defines a `struct task_struct` in `sched.h`, with a few properties:

```C
struct task_struct {
	// ...

	/* -1 unrunnable, 0 runnable, >0 stopped */
	volatile long state; 

	void *stack;
	atomic_t usage;

	/* per process flags */
	unsigned int flags;

	unsigned int ptrace;
	unsigned int policy;
	int nr_cpus_allowed;
	cpumask_t cpus_allowed;

	int exit_state;
	int exit_code, exit_signal;

	/*  The signal sent when the parent dies  */
	int pdeath_signal;

	/* JOBCTL_*, siglock protected */
	unsigned int jobctl;

	/* Revert to default priority/policy when forking */
	unsigned sched_reset_on_fork:1;
	unsigned sched_contributes_to_load:1;

	/* Flags needing atomic access. */
	unsigned long atomic_flags;

	pid_t pid;
	pid_t tgid;
	
	// ...
}
```

- In a single threaded process, `pid` and `tgid` will have the same value
- In a multithreaded process, `pid` is the task ID. `tgid` is the ID of the task group ID.

![[Pasted image 20221001151413.png]]

- Linux never had one contiguous PCB
- The task struct contains a ton of pointers to other structs.

### Linux Task Creation
`clone(function, stack_ptr, sharing_flags, args)`

![[Pasted image 20221001151535.png]]

### Linux Threads Model
- Native POSIX Threads Library (NPTL) "1:1 model"
	- Kernel sees each ULT info
	- kernel traps are cheaper
	- more resources: memory, large range of IDs, no need to constrain the number of Kernel level threads
- Older Linux Threads "M:M model"
	- similar issues to those described in Solaris papers.

For most practical purposes, the "1:1 model" for associating ULTs and KLTs is sufficient. For more exotic computing setups, such as platforms with multiple CPUs that might even have different architectures, the ULT library may need to support more complex policies for associating ULTs and KLTs.

