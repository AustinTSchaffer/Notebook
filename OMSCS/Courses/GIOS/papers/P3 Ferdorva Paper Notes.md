---
tags: OMSCS, GIOS, Scheduling
---
# P3: Notes on the "Ferdorva Paper"
The full title of the paper is "Chip Multithreading Systems Need a New Operating System Scheduler".


## Key Takeaways
- The unpredictable nature of modern workloads can result in processor utilization as low as 19%, when using a naive OS scheduler.
	- Frequent branches and control transfers
	- Terrible locality and cache performance
- Making a process scheduler that is aware of CPUs that have multiple processing cores on a single chip can improve performance
	- A naive scheduler may actually reduce application performance on such a system, compared to single-threaded processors
	- Schedulers designed for single-core CPUs are not equipped to handle scheduling processes against CPUs that have tens of cores/threads.
- Scheduling algorithms designed for single-processor MT systems would run combinations of threads that could be co-scheduled, and picked a combination that performed well. This strategy does not scale well as both hardware and applications increase in complexity.
- Better schedulers necessarily need to model "resource contention", which is a hard problem.
- An MT processing core has multiple hardware contexts (usually 1, 2, 4, or 8). Each context consists of a set of registers and other thread state. The processor interleaves execution of instructions for multiple threads, switching contexts on each cycle. If a thread becomes blocked, the processor will skip it's context in the cycle.
- On a CMT system, each execution context appears to the OS as a logical processor. Threads are assigned to execution contexts. The scheduler necessarily has to decide which threads should run on the same processor.
- Processor pipeline contention depends on the lantencies of the instructions being executed. If a thread has instructions with long delay latencies, then it's not using the ALU. One thread can use the ALU while another thread is waiting for a latent operation. If a thread is running an instruction mix that's entirely ALU operations, it can starve all other threads by keeping the pipeline busy. (Hint: Processors can and should have multiple ALUs per CPU core). ![[Pasted image 20221009153328.png]]
- Schedulers can use "average instruction delay latency" as a heuristic for approximating processor pipeline requirements for a workload. The OS should group threads with differing requirements together (i.e. one thread that mostly performs ALU operations and another that mostly performs memory operations).
	- This does not model contention for other resources, not a perfect predictor of performance.
	- Example, does not take cache contention into consideration.
- ![[Pasted image 20221009155117.png]]
- ![[Pasted image 20221009155134.png]]
- 

## Key Terms
- Chip multithreading (CMT)
- Instruction-level parallelism (ILP)
- Chip multiprocessing (CMP)
- hardware multi-threading (MT)
- Thread-level parallelism (TLP)
- ??? (TLB)
- ??? (OLTP)
- Simultaneous multithreaded (SMT) system
- Arithmetic Logic Unit (ALU)
- "instruction delay latency": When a thread performs a long-latency operation, it is blocked. Different instructions have different delays (ALU operation vs loading memory).
- mean/average "cycles-per-instruction" (CPI)
