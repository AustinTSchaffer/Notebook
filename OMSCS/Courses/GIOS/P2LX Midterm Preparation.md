# Midterm Preparation
## 1. Process Creation
> How is a new process created? Select all that apply.

- **Via fork**
- ~~Via exec~~
- **Via fork followed by exec**
- ~~Via exec followed by fork~~
- ~~Via exec or fork followed by exec~~
- **Via fork or fork followed by exec**
- ~~None of the above~~
- ~~All of the above~~

**exec** **_replaces_** the currently running process.

## 2. Multithreading when you only have 1 CPU

> Is there a benefit to multi-threading on 1 CPU? Y/N. Give 1 reason to support your answer.

Yes. Even if you only have 1 CPU, you can use multithreading to hide the latency associated with I/O requests. Having multiple threads in a thread pool handling I/O requests allows you to maintain at least one thread that isn't blocked waiting on the completion of an I/O request.

## 3. Issues with Multithreaded Code

>In the (pseudo) code segments for the **producer code** and **consumer code**, mark and explain all the lines where there are errors.

- In the global section, the mutex and cond vars need to be initialized with the default initialization constants that are provided with the pthread module. This is pseudo code, so that's probably fine.
- The consumer code needs to use a while `out == in`, instead of `if (out == in)`. The producer code probably should also use a while condition surrounding the condition wait.
- **Condition waits need to specify a mutex**
- The producer should signal, instead of broadcasting. It doesn't need to broadcast to all threads since it's only adding one item per loop iteration.
- The producer never unlocks the mutex
- The consumer never unlocks the mutex
- The consumer is signaling to the wrong condition variable.

## 4. Multithreaded Calendar App

> A shared calendar supports three types of operations for reservations:
> 1. read
> 2. cancel
> 3. enter
> 
> Requests for cancellations should have priority above reads, who in turn have priority over new updates.
> In pseudocode, write the critical section enter/exit code for the **read** operation.

There is no "accepted solution".

The relevant "read" critical section needs to
- wait if there's any in-progress "cancel" operations. Integer to track number of cancel operations.
- lock out any potential updaters. Integer to track number of readers.
- decrement integer and signal to updaters when reading is done.
- 2 mutexes, 2 condition variables
	- mutex for locking cancellations
	- mutex for locking updates
	- CV for signalling cancellation completions
	- CV for signalling updates
- Drawbacks when system is under sufficient load
- Review the 1 writer multiple readers pseudocode

## 5. ULT Signal Masks

> If the kernel cannot see user-level signal masks, then how is a signal delivered to a user-level thread (where the signal can be handled)?

- The OS kernel maintains a per-process table that correlates signal IDs to the memory address that contains the starting instruction for the handler that should handle signals of that type.
- When a signal is handled, the instructions for that signal's handler runs in the execution context of a particular thread.
- Threads can independently set their per-thread signal mask, which enables/disables signal handling for specific signal types for the particular thread.
- If a signal is disabled by a ULT, the ULT library can check to see if there's another ULT that has the signal enabled. In that case, the ULT library will route the signal to another thread or another CPU, so it can be handled on other thread.
- If no ULTs have the mask set to 1, the threading library will make a system call to set the kernel-level mask to 0. The ULT library will then reissue the signal to another thread, which will cascade and cause all of the LWP masks to be set 0.
- Once a thread enables the mask, the ULT library will make a system call to enable the mask on one of the KLTs/LWPs.
- When a process cannot process a signal, the OS will keep track of pending signals, so they can be issued once the process allows signals again.

## 6. Multithreading Data Structures

> The implementation of Solaris threads described in the paper ["Beyond Multiprocessing: Multithreading the Sun OS Kernel" (Links to an external site.)](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-eykholt-paper.pdf), describes four key data structures used by the OS to support threads.
> 
> For each of these data structures, **list at least two elements** they must contain:
> 
> 1. Process
> 2. LWP
> 3. Kernel-threads
> 4. CPU

- The process data structure must contain
	- A list of kernel-level threads
	- The virtual address space
	- User credentials
	- Signal handlers
- A light-weigh process (LWP) data structure must contain
	- user-level registers
	- system call arguments
	- resource usage info
	- a signal mask
- The data structure for a Kernel Level Thread (KLT) must contain
	- kernel-level registers
	- stack pointers
	- scheduling information
	- pointers to associated LWP, process, and CPU data structures
	- Essentially it must contain information that is needed even when a process is not running.
- The in-memory data structure that models the CPU must contain
	- A pointer to the currently running thread
	- A list of kernel-level threads
	- information for dispatching and interrupt handling.

## 7. Multithreading Pipeline Model

> An image web server has three stages with average execution times as follows:
>
> - Stage 1: read and parse request (10ms)
> - Stage 2: read and process image (30ms)
> - Stage 3: send image (20ms)
> 
> You have been asked to build a multi-threaded implementation of this server using the **pipeline model**. Using a **pipeline model**, answer the following questions:
> 
> 1.  How many threads will you allocate to each pipeline stage?
> 2.  What is the expected execution time for 100 requests (in sec)?
> 3.  What is the average throughput of the system in Question 2 (in req/sec)? Assume there are infinite processing resources (CPU's, memory, etc.).

1. I would allocate the following thread counts for each stage, or some multiple of these thread counts. This would be the base, the next increment would be "2, 6, and 4".
	- 1 thread for stage 1
	- 3 threads for stage 2
	- 2 threads for stage 3
2. For my thread counts, listed above, It would take 1000ms to run stage 1 for all of the requests. Presuming that all of these threads have highest priority, etc etc, the final request would finish 50ms after all of the stage 1 iterations have completed. The total runtime would be 1050ms or 1.05 seconds.
3. The average throughput of the system in question 2 would be 100requests/1.05seconds, `95.23 req/s`

## 8. Performance of Web Servers

> Here is a graph from the paper "Flash: An Efficient and Portable Web Server" ([[P2 Pai Paper.pdf]]), that compares the performance of Flash with other web servers.
> 
> For data sets **where the data set size is less than 100 MB** why does...
> 
> 1. Flash perform worse than SPED?
> 2. Flash perform better than MP?

![[Pasted image 20221001154159.png]]

TODO: Read the paper, understand what any of this means. Answer from instructor:

> 1.  In both cases the dataset will likely fit in cache, but **Flash incurs an overhead on each request because Flash must first check for cache residency**. In the SPED model, this check is not performed.    
> 2.  When data is present in the cache, there is no need for slow disk I/O operations. Adding threads or processes just adds context switching overheads, but there is no benefit of “hiding I/O latency”.

## Answers
**DON'T LOOK AT THE ANSWERS to questions that you don't already understand.**

https://docs.google.com/document/d/1WM4j-u--ZYf-vZvHiq526LSTB7ssZ-CRxwgv75m3IIs/edit#heading=h.kdyyditnvk4v