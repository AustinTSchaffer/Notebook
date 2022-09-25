# Midterm Preparation
## Prompts and Responses
> How is a new process created? Select all that apply.

-   Via fork
-   Via exec
-   Via fork followed by exec
-   Via exec followed by fork
-   Via exec or fork followed by exec
-   Via fork or fork followed by exec
-   None of the above
-   All of the above

> Is there a benefit to multi-threading on 1 CPU? Y/N. Give 1 reason to support your answer.

TODO:

>In the (pseudo) code segments for the **producer code** and **consumer code**, mark and explain all the lines where there are errors.

- In the global section, the mutex and cond vars need to be initialized with the default initialization constants that are provided with the pthread module. This is pseudo code
- The consumer code needs to use a while `out == in`, instead of `if (out == in)`. The producer code probably should also use a while condition surrounding the condition wait.
- **Condition waits need to specify a mutex**
- The producer should signal, instead of broadcasting. It doesn't need to broadcast to all threads since it's only adding one item per loop iteration.
- The producer never unlocks the mutex
- The consumer never unlocks the mutex
- The consumer is signaling to the wrong condition variable.

> A shared calendar supports three types of operations for reservations:
> 1. read
> 2. cancel
> 3. enter
> 
> Requests for cancellations should have priority above reads, who in turn have priority over new updates.
> In pseudocode, write the critical section enter/exit code for the **read** operation.

TODO:

> If the kernel cannot see user-level signal masks, then how is a signal delivered to a user-level thread (where the signal can be handled)?

TODO:

> The implementation of Solaris threads described in the paper ["Beyond Multiprocessing: Multithreading the Sun OS Kernel" (Links to an external site.)](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-eykholt-paper.pdf), describes four key data structures used by the OS to support threads.
> 
> For each of these data structures, **list at least two elements** they must contain:
> 
> 1. Process
> 2. LWP
> 3. Kernel-threads
> 4. CPU

TODO: 

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

TODO: Look up the multithreaded pipeline model more in depth.

1. I would allocate the following thread counts for each stage, or some multiple of these thread counts. This would be the base, the next increment would be "2, 6, and 4".
	- 1 thread for stage 1
	- 3 threads for stage 2
	- 2 threads for stage 3
2. For my thread counts, listed above, It would take 1000ms to run stage 1 for all of the requests. Presuming that all of these threads have highest priority, etc etc, the final request would finish 50ms after all of the stage 1 iterations have completed. The total runtime would be 1050ms or 1.05 seconds.
3. The average throughput of the system in question 2 would be 100requests/1.05seconds, `95.23 req/s`

> Here is a graph from the paper ["Flash: An Efficient and Portable Web Server" (Links to an external site.)](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-pai-paper.pdf), that compares the performance of Flash with other web servers.
> 
> For data sets **where the data set size is less than 100 MB** why does...
> 
> 1. Flash perform worse than SPED?
> 2. Flash perform better than MP?

TODO: Read the paper, understand what any of this means.

## Answers
**DON'T LOOK AT THE ANSWERS to questions that you don't already understand.**

https://docs.google.com/document/d/1WM4j-u--ZYf-vZvHiq526LSTB7ssZ-CRxwgv75m3IIs/edit#heading=h.kdyyditnvk4v