---
tags: OMSCS, GIOS, Final
---
# GIOS Final Preparation

## 1. Timeslices

### Prompt
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

### Responses
- 10 I/O tasks
	- Issue I/O operation every 1ms
	- I/O operations take 10ms to complete
- 1 CPU task
- Context switching overhead is 0.1ms
- I/O devices have infinite capacity
- No tasks exit
- 20ms timeslices

- CPU util
	- Active CPU time = $10(1ms)+1(20ms) = 30ms$
	- Idle CPU time = $10(0.1ms)+1(0.1ms)=1.1ms$
	- Total runtime = $30ms+1.1ms=31.1ms$
	- Util = $\frac{30}{30+1.1}=0.96463... \approx 96.4\%$
- I/O util
	- Last I/O request issued by I/O operation from I/O process 10. The previous I/O operations overlap. Time not running I/O operations is equal to
		- +context switching time
		- +CPU task runtime
		- +context switching time
		- -I/O operation runtime
		- **+I/O process runtime** because it takes that long for the first I/O process to issue the first I/O operation in the cycle.
	- time not running I/O = $0.1ms+20ms+0.1ms-10ms+1ms=21.2-10=11.2ms$
	- I/O util = $\frac{31.1ms-11.2ms}{31.1ms}=\frac{19.9}{31.1ms}=0.63987...\approx64\%$

## 2. Linux O(1) Scheduler

### Prompt
For the next four questions, consider a Linux system with the following assumptions:

- uses the O(1) scheduling algorithm for time sharing threads
- must assign a time quantum for thread T1 with priority 110
- must assign a time quantum for thread T2 with priority 135

Provide answers to the following: (questions copied below)

### Response
- From prompt
	- thread T1 with priority 110
	- thread T2 with priority 135
- From notes
	- lower priority value means higher priority
	- I/O tasks will see their priorities increased
	- CPU tasks will see their priorities decreased
	- time quantum == timeslice

> Which thread has a **"higher"** priority (will be serviced first)?

T1 has a "lower" priority value, which means it has a higher priority

> Which thread is assigned a **longer time quantum**?

T1 has the higher priority, so it gets a longer time quantum.

> Assume T2 has used its time quantum without blocking. What will happen to the value that represents its priority level when T2 gets scheduled again?

T2 used its entire time slice, so it's assumed to be a CPU bound task. It will be de-prioritized, its timeslice will be shortened, which means the value of its priority should go up (decreased logical priority).

> Assume now that T2 blocks for I/O before its time quantum expired. What will happen to the value that represents its priority level when T2 gets scheduled again?

T2 blocked, so it's assumed to be an I/O bound task. It will be prioritized, its timeslice will be lengthened, which means the "value" of its priority should go down (increased logical priority).

## 3. Hardware Counters

### Prompt
Consider a quad-core machine with a single memory module connected to the CPU's via a shared “bus”. On this machine, a CPU instruction takes 1 cycle, and a memory instruction takes 4 cycles.

The machine has two hardware counters:

- counter that measures IPC
- counter that measures CPI

Answer the following:

1. What does IPC stand for in this context?
2. What does CPI stand for in this context?
3. What is the highest IPC on this machine?
4. What is the highest CPI on this machine?

### Responses
Relevant Notes: [[P3L1 Scheduling]]

- IPC: Instructions per Cycle. The theoretical max IPC of this system is 4 IPC, because there's 4 CPUs that could handle 4 simultaneous CPU instructions.
- CPI: Cycles per Instruction. This is the number of cycles that it takes to perform a specific instruction. ~~The highest CPI in this system is 4 cycles per instruction. That instruction is a memory load/store instruction.~~ The highest CPI in this system is 16 cycles per instruction. If 4 memory instructions are issued simultaneously, then it will take one of them 4 cycles to complete, the next will take 8 cycles, the next will take 12 cycles, and the last will take 16 cycles.

## 4. Synchronization

### Prompt
In a multi-processor system, a thread is trying to acquire a locked mutex.

1. Should the thread spin until the mutex is released or block?
2. Why might it be better to spin in some instances?
3. What if this were a uniprocessor system?

### Responses
Relevant Notes: [[P3L4 Synchronization Constructs]]

1. Sometimes it's beneficial to spin until the mutex is released. **For example, if the thread that has the lock is currently running on another CPU, then it may finish the critical section soon and release the lock.**
2. In some instances, the performance penalty of "spinning" to wait for a lock is preferable to blocking, because performing 2 context switches could be more costly than wasting a few cycles waiting for that lock to be freed. This can happen when critical sections are short and the system is multi-threaded AND the current lock holder is running on another CPU.
3. On systems with one processor, spin-locking makes no sense. Wasting cycles for what? There's no other processors. The thread that has the lock is currently idle. The thread that's attempting to acquire the lock should also go idle to hopefully allow the thread that has the lock to become active.

## 5. Spinlocks

### Prompt
For the following question, consider a multi-processor with write-invalidated cache coherence.

Determine whether the use of a [dynamic (exponential backoff) delay](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/notes/ud923-final-dynamic-delay.png) has the **same, better, or worse performance** than a [test-and-test-and-set (“spin on read”) lock](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/notes/ud923-final-test-and-test-and-set.png). Then, explain why.

![[Pasted image 20221206203415.png]]

![[Pasted image 20221206203443.png]]

Make a performance comparison using each of the following metrics:

1. Latency
2. Delay
3. Contention

### Responses
- a multi-processor with write-invalidated cache coherence
- From notes: [[P3L4 Synchronization Constructs]]
- **write-invalidate (WI)**
	- one CPU changes X
	- hardware invalidates cache locations that also contain X
	- pros
		- lower bandwidth, only need to pass an address to fix coherence
		- amortizes coherence costs over multiple changes
		- data only invalidated once

- test-and-test-and-set
	- latency is good, if the lock isn't set, it's acquired almost immediately
	- delay is good, if the lock is set, it tries to acquire it again almost immediately.
	- contention with write-invalidate has terrible performance with this spinlock model. Threads end up spending a lot of time trying to read from an invalidated memory location.
- Test-and-test-and-set with delay
	- doesn't spin constantly
	- contention is improved, because not every thread sees that the lock is free at the same time, so not every thread is fighting to acquire the lock.
	- latency is ok, if the lock isn't acquired when the thread approaches the critical section, then it acquires it nearly immediately.
	- delay is much worse, because this lock acquisition mechanism has an explicit delay.

| Algorithm                     | Latency | Delay | Contention |
| ----------------------------- | ------- | ----- | ---------- |
| Test and Test and Set (TaTaS) | Ok      | Ok    | Terrible   |
| TaTaS w/ Delay                | Ok      | Poor  | Ok         |

## 6. Page Table Size

### Prompt
Consider a 32-bit (x86) platform running Linux that uses a single-level page table. What are the **maximum number of page table entries** when the following page sizes are used?

1. regular (4 kB) pages?
2. large (2 MB) pages?

Relevant Notes: [[P3L2 Memory Management]]

### Response: 4 kB Pages
- 4kB = 2^12
- The last 12 bits of the virtual address is the offset
- That leaves 20 bits to index the page tables
- 2^20 virtual pages.

### Response: 2 MB Pages
- 2MB = 2^21 bytes
- The last 21 bits of each virtual address is the offset
- That leaves (32-21) = 11 bits to index each page table
- 2^11 virtual pages

## 7. PIO

### Prompt
Answer the following questions about PIO:

1. Considering I/O devices, what does PIO stand for?
2. List the steps performed by the OS or process running on the CPU when sending a network packet using PIO.

### Response
Relevant Notes: [[P3L5 IO Management]]

> - CPU "programs" the device
>	- via command registers
>	- data movement
> - NIC device as an example, handling for network packets
>	- write command to command register(s) to request packet transmission
>	- copy packet to data registers
>	- repeat until packet is sent, data register size may be smaller than packet size
>	- Example: 1.5kB packet; 8B registers or bus
>		- 1 CPU store instruction for bus command
>		- 188 CPU store instructions for copying data to register
>		- 189 total CPU store instructions to send the packet
> - This option is better when the data size and/or data transfer frequency is lower.

1. PIO stands for "Programmed IO".
2. Steps required
	1. Write a command to the command registers on the I/O device.
	2. Copy data to I/O device's data registers.
	3. Read status register on the I/O device to confirm that the data was successfully received by the I/O device.
	4. Repeat steps 2 and 3 until the I/O device has all the data.

## 8. inode Structure

Assume an inode has the following structure:

![[Pasted image 20221206203533.png]]

Also assume that **each block pointer element is 4 bytes**.

If a block on the disk is 4 kB, then what is the **maximum file size** that can be supported by this inode structure?

### Response
- Block pointers are 4 bytes
- block size is 4kB (4096 bytes)
- 1 block holds 1024 block pointers (4096/4)
- inode structure
	- 12 direct pointers
	- 1 single indirect pointer
	- 1 double indirect pointer
	- 1 triple indirect pointer
- 12 direct block pointers: $12*4kB=48kB$
- 1 single indirect block pointer
	- $1024*4kB=4MB$
- 1 double indirect block pointer
	- $1024*1024*4kB=4GB$
- 1 triple indirect block pointer
	- $1024*1024*1024*4kB=4TB$
- Max file size $\approx4TB$

## 9. RPC Data Types

A RPC routine `get_coordinates()` returns the N-dimensional coordinates of a data point, where each coordinate is an integer.

Write the elements of the C data structure that corresponds to the 3D coordinates of a data point.

### Response
- well in C, we don't have generics, so we need an integer length, and a pointer to define the array of coordinates.

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

### Response
Relevant: [[P4L2 Distributed File Systems (DFS)]]

1. UNIX Semantics
	1. Every write is immediately visible
	2. P2 will see "ab"
2. NFS Semantics
	1. Depends on whether P1 is the server, or if there's a third component which is the server. Also depends on whether it's using session-based semantics or periodic updates. Also note that sync period for periodic updates is 3 sec.
	2. Session-based
		1. changes flushed to server on close
		2. client checks the server for updated file data on open
		3. If P1 is the server? P2 sees "ab". Otherwise P2 sees "a".
	3. Periodic updates
		1. P2 sees "a" because not enough time has passed.
3. Sprite semantics
	1. P2 sees "ab". Server will check with current writer P1, to see what the most recent value is, before returning the value to P2.

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

### Response
- P1 and P2 see causally consistent reads
- P3 does not. The change to M1 appears to go backwards in time.

## 12. Distributed Applications

You are designing the new image datastore for an application that stores users’ images (like [Picasa](http://picasa.google.com/)). The new design must consider the following scale:

- The current application has 30 million users
- Each user has on average 2,000 photos
- Each photo is on average 500 kB
- Requests are evenly distributed across all images

Answer the following:

1. Would you use replication or partitioning as a mechanism to ensure high responsiveness of the image store?
2. If you have 10 server machines at your disposal, and one of them crashes, what’s the percentage of requests that the image store will not be able to respond to, if any?

### Response
- $500kB*2000=1GB$ per user
- $(3*10^7)*1GB=3*10^{7}GB=30PB$ total storage
- Pure replication isn't feasible at this scale. The data needs to be partitioned.
- 90% of the data is still accessible if one of 10 machines goes offline.

## Solutions
> https://docs.google.com/document/d/1XBsgT9eKtqxnQfW9iTN-cDZdo0nKgZSiYh1pKAc-Hfc/edit

