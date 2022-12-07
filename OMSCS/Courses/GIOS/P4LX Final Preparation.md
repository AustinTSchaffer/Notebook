---
tags: OMSCS, GIOS, Final
---
# GIOS Final Preparation

## 1. Timeslices

On a single CPU system, consider the following workload and conditions:

- 10 I/O-bound tasks and 1 CPU-bound task
- I/O-bound tasks issue an I/O operation once every 1 ms of CPU computing
- I/O operations always take 10 ms to complete
- Context switching overhead is 0.1 ms
- I/O device(s) have infinite capacity to handle concurrent I/O requests
- All tasks are long-running

Now, answer the following questions (for each question, round to the nearest percent):

1. What is the **CPU utilization** (%) for a round-robin scheduler where the timeslice is 20 ms?
2. What is the **I/O utilization** (%) for a round-robin scheduler where the timeslice is 20 ms?

## 2. Linux O(1) Scheduler

For the next four questions, consider a Linux system with the following assumptions:

- uses the O(1) scheduling algorithm for time sharing threads
- must assign a time quantum for thread T1 with priority 110
- must assign a time quantum for thread T2 with priority 135

Provide answers to the following:

1. Which thread has a **"higher"** priority (will be serviced first)?
2. Which thread is assigned a **longer time quantum**?
3. Assume T2 has used its time quantum without blocking. What will happen to the value that represents its priority level when T2 gets scheduled again?
    - lower/decrease
    - higher/increase
    - same
4. Assume now that T2 blocks for I/O before its time quantum expired. What will happen to the value that represents its priority level when T2 gets scheduled again?
    - lower/decrease
    - higher/increase
    - same

## 3. Hardware Counters

Consider a quad-core machine with a single memory module connected to the CPU's via a shared “bus”. On this machine, a CPU instruction takes 1 cycle, and a memory instruction takes 4 cycles.

The machine has two hardware counters:

- counter that measures IPC
- counter that measures CPI

Answer the following:

1. What does IPC stand for in this context?
2. What does CPI stand for in this context?
3. What is the highest IPC on this machine?
4. What is the highest CPI on this machine?

## 4. Synchronization

In a multi-processor system, a thread is trying to acquire a locked mutex.

1. Should the thread spin until the mutex is released or block?
2. Why might it be better to spin in some instances?
3. What if this were a uniprocessor system?

## 5. Spinlocks

For the following question, consider a multi-processor with write-invalidated cache coherence.

Determine whether the use of a [dynamic (exponential backoff) delay](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/notes/ud923-final-dynamic-delay.png) has the **same, better, or worse performance** than a [test-and-test-and-set (“spin on read”) lock](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/notes/ud923-final-test-and-test-and-set.png). Then, explain why.

![[Pasted image 20221206203415.png]]

![[Pasted image 20221206203443.png]]

Make a performance comparison using each of the following metrics:

1. Latency
2. Delay
3. Contention

## 6. Page Table Size

Consider a 32-bit (x86) platform running Linux that uses a single-level page table. What are the **maximum number of page table entries** when the following page sizes are used?

1. regular (4 kB) pages?
2. large (2 MB) pages?

## 7. PIO

Answer the following questions about PIO:

1. Considering I/O devices, what does PIO stand for?
2. List the steps performed by the OS or process running on the CPU when sending a network packet using PIO.

## 8. inode Structure

Assume an inode has the following structure:

![[Pasted image 20221206203533.png]]

Also assume that **each block pointer element is 4 bytes**.

If a block on the disk is 4 kB, then what is the **maximum file size** that can be supported by this inode structure?

## 9. RPC Data Types

A RPC routine `get_coordinates()` returns the N-dimensional coordinates of a data point, where each coordinate is an integer.

Write the elements of the C data structure that corresponds to the 3D coordinates of a data point.

## 10. DFS Semantics

Consider the following timeline where ‘f’ is distributed shared file and P1 and P2 are processes:

![[Pasted image 20221206203632.png]]

Other Assumptions:

- 't' represents the time intervals in which functions execute
- the ‘w’ flag means write/append
- the ‘r’ flag means read
- the original content of 'f' was “a”
- the `read()` function returns the entire contents of the file

For each of the following DFS semantics, what will be read -- **the contents of 'f'** -- by P2 when t = 4s?

1. UNIX semantics
2. NFS semantics
3. Sprite semantics

## 11. Consistency Models

Consider the following sequence of operations by processors P1, P2, and P3 which occurred in a distributed shared memory system:

![[Pasted image 20221206203750.png]]

Notation

- `R_m1(X) => X` was read from memory location m1 **(does not indicate where it was stored)**
- `W_m1(Y) => Y` was written to memory location m1
- Initially all memory is set to 0

Answer the following questions:

1. Name all processors (P1, P2, or P3) that observe causally consistent reads.
2. Is this execution causally consistent?

## 12. Distributed Applications

You are designing the new image datastore for an application that stores users’ images (like [Picasa](http://picasa.google.com/)). The new design must consider the following scale:

- The current application has 30 million users
- Each user has on average 2,000 photos
- Each photo is on average 500 kB
- Requests are evenly distributed across all images

Answer the following:

1. Would you use replication or partitioning as a mechanism to ensure high responsiveness of the image store?
2. If you have 10 server machines at your disposal, and one of them crashes, what’s the percentage of requests that the image store will not be able to respond to, if any?

## Solutions
> https://docs.google.com/document/d/1XBsgT9eKtqxnQfW9iTN-cDZdo0nKgZSiYh1pKAc-Hfc/edit

