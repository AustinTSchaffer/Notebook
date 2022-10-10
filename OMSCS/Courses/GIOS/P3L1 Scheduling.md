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

