---
tags: OMSCS, GIOS, Scheduling
---
# P3L1: Scheduling

## Overview
- Scheduling mechanisms, algorithms, data structures
- Linux O(1) and FCFS schedulers
- Scheduling on multi-CPU platforms
	- Assign tasks immediately? (FIFO / FCFS)
	- Assign simple or complex tasks first?
		- simple: maximize throughput (Shortest Job First (SJF))
		- complex: maximize CPU utilization, devices, memory

Supplemental materials
- [[P3 Fedorova Paper.pdf]]

## CPU Scheduling
The CPU scheduler
- chooses one of the tasks in the "ready queue" and moves it to running on the CPU
- decides how and when processes (and their threads) should access shared CPUs
- schedules tasks running user-level processes/threads as well as kernel-level threads
- runs when
	- the CPU becomes idle
	- a new task becomes **ready**
		- interrupt/signal occurs against a waiting thread
		- new process/thread/task created
		- a task's "time slice expired"
		- an I/O request is completed
- Dispatches threads onto the CPU
	- context switch
	- enter user mode
	- set the program counter

![[Pasted image 20221009162249.png]]

Scheduling is choosing which **task** should be moved from **ready** to **running**. Advanced mode is also selecting which CPU core the task should run on. Both are selected via a scheduling policy/algorithm, and the data structure used for the **ready queue (runqueue)**. Usually the **runqueue** data structure format and the scheduling policy/alg are tightly coupled.

## "Run-to-Completion" Scheduling
Initial assumptions
- group of tasks/jobs
- known execution times
- no preemption, once a task starts, it will run to completion (RtC)
- Only one CPU

useful metrics
- throughput (tasks per unit of time)
- avg. job completion time (time)
- avg. job wait time (time)
- CPU utilization (percentage)

Downside is task run time has to be known
- how long did it run last time?
- how long did the task run the last n times it ran? (windowed average)

First-Come First-Serve (FCFS)
- schedules tasks in order of arrival
- runqueue = linked list / queue / FIFO

Shortest Job First (SJF)
- schedules tasks in order of their execution time
- runqueue = ordered linked list / ordered queue ($O(n)$ complexity insertions, $O(1)$ lookup)
- OR the runqueue could be a tree ($O(ln(n))$ insertions, $O(ln(n))$ lookup, requires periodic rebalancing (optional))

## Preemptive Scheduling
### SJF + Preempt
As new jobs show up in the run queue, the scheduler should preempt the currently running task and then dispatch the new task, IF the new task is a shorter task.

### Priority + Preempt
Same as "SJF + Preempt", but tasks will only be preempted if the new task has a higher priority.

runqueue
- structured the same way as an SJF runqueue, except tasks will be ordered in the queue or tree based on priority, not execution time.
- alternative is to make a map of "priority level" to "FIFO queue"

biggest downside, low priority tasks may never run. #starvation

**priority aging** helps prevent starvation
- $priority = f(priority_{actual}, time_{waiting})$

#### Example
![[Pasted image 20221009165215.png]]

![[20221009_165658.jpg]]

### Priority Inversion
This happens when
- a lower priority task acquires a lock that a higher priority task also wants to acquire
- the higher priority task arrives at the runqueue after the lower priority task acquired the lock

![[Pasted image 20221009170610.png]]

Solution:
- temporarily boost priority of mutex owners
- lower task priority after lock is released

### Round-Robin Scheduling
- pick first task from queue (like FCFS)
- tasks may yield, to wait on I/O or other events (unlike FCFS)
- Round Robin w/ Priorities is also possible, requires preemption
- Round Robin w/ interleaving is possible. Each task is given a "time slice", called **timeslicing**, after which it will be preempted

## Timesharing and Timesclices
- A **timeslice** is a max amount of uninterrupted time that can be given to a single task (a.k.a. a time quantum)
- task may run less than the timeslice time
	- waiting on I/O or sync or other events
	- higher priority task becomes runnable
- using timeslicing, tasks are interleaved, timesharing the CPU
- CPU bound tasks -> preempted after timeslice.

Scheduler doesn't have to know how long tasks run to be effective. There is no RtC component required.

- Good
	- shorter tasks finish sooner
	- more responsive
	- lengthy I/O ops initiated sooner
- Not Great
	- overheads with interrupts, schedules, and context switches
	- need to keep timesclice time much larger than context switching time

### How Long should TimeSlices Be?
balance benefits and overheads
- ... for I/O-bound tasks?
- ... for CPU-bound tasks?

#### Summary
- CPU-bound tasks prefer longer timeslices
	- limits context switching overheads
	- keeps CPU util. and throughput high
- I/O bound tasks prefer shorter timeslices
	- I/O bound tasks can issue I/O ops earlier
	- keeps CPU and device utilization high
	- better user-perceived performance (lower average wait time)

#### CPU bound tasks
better off picking a **higher** timeslice value

![[Pasted image 20221009173809.png]]

- Timeslice = 1 second
	- throughput = 2 / (10 + 10 + 19*0.1) = 0.091 tasks/second
	- avg. wait time = (0 + (1+0.1)) / 2 = 0.55 seconds
	- avg. comp. time = 21.35 seconds
- Timeslice = 5 seconds
	- throughput = 2 / (10 + 10 + 3*0.1) = 0.098 tasks/second
	- avg. wait time = (0 + (5+0.1)) / 2 = 3.05 seconds
	- avg. comp. time = 17.75 seconds
- Timeslice = ♾
	- throughput = 2 / (10 + 10) = 0.1 tasks/second
	- avg. wait time = (0 + (10)) / 2 = 5 seconds
	- avg. comp. time = (10 + 20)/2 = 15 seconds

#### I/O-bound tasks

When tasks are purely I/O bound, tasks will end up preempting themselves, so timeslice duration doesn't really matter that much.

![[Pasted image 20221009174324.png]]

When you have a mix of I/O and CPU -bound tasks, longer timeslicing can appear better for average completion time, but **shorter** timeslicing is better for throughput and average wait time.

![[Pasted image 20221010095630.png]]

- for Timeslice = 1sec
	- avg. comp. time = (21.9 + 20.8) / 2 = 21.35
- Timeslice = 5 second*
	- throughput = 2 / 24.3 = 0.082 tasks/second
	- avg. wait time = 5.1 / 2 = 2.55 seconds
	- avg. comp. time = (11.2 + 24.3) / 2 = 17.75 seconds

#### Quiz
![[Pasted image 20221010122458.png]]

> **Helpful Steps to Solve:**
> 1. Determine a consistent, recurring interval
> 2. In the interval, each task should be given an opportunity to run
> 3. During that interval, how much time is spent computing? This is the **cpu_running_time**
> 4. During that interval, how much time is spent context switching? This is the **context_switching_overheads**

- 10 I/O bound tasks
	- Every 1ms, each issues a 10ms blocking instruction, forcing a context switch.
	- If the timeslice interval is greater than 1ms, it's essentially ignored for these tasks.

##### 1ms timeslice

Recurring Interval would be:
- multiply by 10
	- 1ms of running time for an I/O bound-task
	- 0.1ms context switch
- 1ms running time for the CPU-bound task
- 0.1ms context switch

- $t_{running} = 10(1ms) + 1ms = 11ms$
- $t_{overhead} = 10(0.1ms) + 0.1ms = 1.1ms$
- $util = \frac{t_{running}}{t_{running} + t_{overhead}} = \frac{11}{12.1} \approx 0.91 = 91\%$

##### 10ms timeslice

Recurring Interval would be:
- multiply by 10
	- 1ms of running time for an I/O bound-task
	- 0.1ms context switch
- 10ms running time for the CPU-bound task
- 0.1ms context switch

- $t_{running} = 10(1ms) + 10ms = 20ms$
- $t_{overhead} = 10(0.1ms) + 0.1ms = 1.1ms$
- $util = \frac{t_{running}}{t_{running} + t_{overhead}} = \frac{20}{21.1} \approx 0.95 = 95\%$

## Runqueue Data Structure
- Runqueues are only logically a queue
- They could be a list of queues or even a tree.
- If we want I/O and CPU bound tasks to have different timeslices, then
	- same runqueue, check type
	- separate runqueue into different runqueues with differing timeslicing values
	- store timeslice as part of runqueue task struct

### Multi-Level Feedback Queue (MLFQ)
- Put most I/O intensive tasks into a $ts=8ms$ queue, with tasks in that queue assumed to have the highest priority.
- Put medium I/O intensive tasks (mix of I/O and CPU processing) into a $ts=16ms$ queue, with tasks in that queue having lower priority.
- Put CPU intensive tasks into the lowest priority queue, with $ts\rightarrow\infty$ (FCFS). These tasks will be preempted when I/O tasks enter the runqueue
- Pros
	- shorter timeslicing provides benefits for I/O bound tasks
	- longer timeslicing avoids overheads for CPU bound tasks

#### Considerations
- How do we know if a task is CPU or I/O intensive?
- How do we know how I/O intensive a task is?
- Have to use history-based statistics
	- What about new tasks?
	- what about tasks that dynamically change behavior during different execution phases?

#### Dealing with different timeslice values
![[Pasted image 20221010195444.png]]

1. tasks enter topmost queue
2. if task yields voluntarily before 8ms timeslice expires
	- good choice! Keep task at this level
3. If task uses entire timeslice
	- push the task down to a more CPU intensive queue
4. Task in lower queue are pushed upward when they release the CPU due to I/O waits

MLFQ != Priority Queues
- different treatment of threads at each level
- feedback mechanism

Solaris used a variant of this mechanism that incorporates 60 levels.

#### Linux O(1) Scheduler
> Oh of one.

- O(1) means "constant time" to add and select tasks
- Preemptive, priority-based
	- real time priority levels (0-99)
	- timesharing priority levels (100-129)

User processes
- default 120
- nice value (-20 to 19)

Timeslice value
- depends on priority
- smallest for low priority
- highest for high priority

Feedback
- sleep time: waiting/idling
- longer sleep times imply that the task is interactive
	- priority -= 5 (boost)
- shorter sleep times imply that the task is compute intensive
	- priority += 5 (lowered)

Runqueue is 2 arrays of tasks
- **Active**
	- used to pick next task to run
	- constant time to add/select
	- Uses a bit mask to determine the lowest priority level that contains tasks that are available to run
	- Takes a constant time to index the specific run queue and select the first task from the list.
	- tasks remain in queue in active array until timeslice expires
	- once expired, tasks will be moved to "expired" task queue array
- **Expired**
	- inactive list
	- when no more tasks in active array, active and expired arrays are swapped.

Introduced in 2.5 by Ingo Molnar, but workloads changed. Introduced jitter in realtime streaming applications.

Problems
- poor performance of interactive tasks, due to unpredictable amounts of time waiting to be scheduled.
- hard to make claims of fairness guarantees.

Eventually replaced by the Completely Fair Scheduler (CFS) in 2.6.23 by Ingo Molnar.

### Linux's Completely Fair Scheduler (CFS)
- Addresses problems of O(1) scheduler.
- Default scheduler for all non-realtime tasks. Realtime tasks are scheduled by a realtime scheduler.
- Uses a [Red-Black tree](https://algs4.cs.princeton.edu/33balanced/) for its data structure
	- As nodes are added/removed, the tree self-balances
	- Ordered by virtual runtime (`vruntime`), tracked by nanosecond
	- `vruntime` is the time spent on the CPU

CFS scheduling alg
- Always picks the left-most node (least amount of time on the CPU)
- periodically adjusts `vruntime` 
- compares the runtime of the task to the leftmost `vruntime`
	- if smaller, continues running
	- if larger, task is preempted and placed accordingly in the tree
- `vruntime` process rate depends on priority and niceness
	- rate progresses faster for low-priority tasks
	- rate progresses slower for high-priority tasks
- Uses one runqueue tree for tasks of all priorities
- Performance
	- $O(1)$ for task selection
	- $O(\log{n})$ for adding tasks

## Scheduling on Multi-CPU Systems

### Shared memory multiprocessors (SMP)
![[Pasted image 20221010203053.png]]

- CPUs each have private on-chip caches (L1, L2, ...)
- Shared last-level cache (LLC)
- Shared memory (DRAM)

### Multicore CPUs
![[Pasted image 20221010203207.png]]

- CPUs contain multiple cores
- cores have private caches (L1, L2, ...)
- Shared LLC
- Shared memory

### Scheduling on Multi-CPU Systems
**cache-affinity**: Something we want to achieve is to schedule threads on CPUs on which the thread had been scheduled previously. This is to increase the likelihood that a thread is working with a cache that is populated with data that it needs (HOT! cache)

- keep tasks on same CPU as much as possible
- **hierarchical** scheduler architecture

![[Pasted image 20221010203838.png]]

**per-CPU run queues**
- load balance tasks across CPUs
- based on queue length
- or when CPU is idle

**Non-Uniform Memory Access (NUMA)**: Possible to have multiple memory nodes where one memory node is closer to one processor than another. Processor nodes can access memory that is further away, but with higher latency.

- Access to local memory node is faster than access to a remote memory node.
- Keep tasks on CPU closer to memory node where their data is stored
- Referred to as "NUMA-aware" scheduling.

## Hyperthreading (aka SMT or CMT)
- CPUs have a set of registers to keep track of the execution state of a program, including the stack pointer and the program counter.
- Over time, hardware added more sets of registers for storing multiple execution contexts simultaneously.
- Still one CPU, but with ultra-fast context switching.

Referred to by many names
- hardware multithreading
- hyperthreading
- chip multithreading (CMT)
- simultaneous multithreading (SMT)

- hardware known to have up to 8 sets of registers per CPU
- Exposed to OS as additional CPUs
- Can typically be enabled/disabled at boot time.

- SMT context switch (`0`-ish cycles)
- compared to a memory load (100+ cycles)

What kinds of threads should we co-schedule on hardware threads?

### Scheduling for Hyperthreaded Platforms
Refer to [[P3 Fedorova Paper.pdf]] and [[P3 Ferdorva Paper Notes]].

TLDR: Schedule a mix of memory-bound and CPU-bound tasks on different hyper-threads on the same CPU.
- avoid/limit contention on processor pipeine
- all components (CPU and memory) have good utilization
- still leads to interference and degradation, but minimal compared to alternatives.

## Is a thread CPU-bound or memory-bound?
- use historic information
- "sleep time" won't work. memory-bound =/= I/O bound
- need hardware information

Execution context registers includes hardware counters
- L1, L2, ... LLC misses
- IPC (Instructions per Cycle)
- power and energy data

Software interface and tools
- e.g. `oprofile`, Linux `perf` tool
- `oprofile` website lists available hardware counters on different architectures

From hardware counters, a scheduler can...
- estimate (guesstimate) what kind of resources a thread needs.
- determine if/when something changed in the execution of a thread
- make informed decisions
	- typically make use of multiple counters
	- models with per-architecture thresholds
	- based on well-understood workloads

Advanced research problem. Out of scope of this course.

## Scheduling with Hardware Counters
> Is cycles-per-instruction (CPI) useful?

- 1 cycle per instruction (low CPI) means CPU-bound
- high CPI implies a memory-bound instruction
- Is CPI a good metric?

This section also refers to the Ferdorva paper.

- In theory, using CPI is a great metric for making scheduling decisions.
- In practice, CPI is between 2 and 5 for most applications, meaning real workloads don't vary a lot in terms of CPI.

Takeaways
- resource contention on SMTs is important
- hardware counters can be used to characterize workloads
- schedulers should be aware of resource contention, not just load balancing tasks onto different CPUs
- The best optimization that can be made in this space is making sure that threads don't compete for space in the last-level cache (LLC).