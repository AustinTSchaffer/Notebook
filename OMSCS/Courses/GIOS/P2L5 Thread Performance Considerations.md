---
tags: OMSCS, GIOS, Threads
---
# P2L5: Thread Performance Considerations
- [[#Overview|Overview]]
- [[#Which Threading Model is Better?|Which Threading Model is Better?]]
- [[#Are Threads Useful?|Are Threads Useful?]]
- [[#Performance Metrics|Performance Metrics]]
- [[#Are threads useful (redux)?|Are threads useful (redux)?]]
- [[#Multi-Process Concurrency vs Multi-Threaded Concurrency|Multi-Process Concurrency vs Multi-Threaded Concurrency]]
	- [[#Multi-Process Concurrency vs Multi-Threaded Concurrency#Multi-Process Web Server|Multi-Process Web Server]]
	- [[#Multi-Process Concurrency vs Multi-Threaded Concurrency#Multi-Threaded Web Server (MT)|Multi-Threaded Web Server (MT)]]
- [[#Event-Driven Model|Event-Driven Model]]
	- [[#Event-Driven Model#Concurrency|Concurrency]]
	- [[#Event-Driven Model#Why?|Why?]]
	- [[#Event-Driven Model#How?|How?]]
	- [[#Event-Driven Model#Problems with Event-Driven Model|Problems with Event-Driven Model]]
	- [[#Event-Driven Model#Helper Threads|Helper Threads]]
- [[#Flash: Event-Driven Web Server|Flash: Event-Driven Web Server]]
- [[#Apache Web Server|Apache Web Server]]
- [[#Experimental Methodology|Experimental Methodology]]
	- [[#Experimental Methodology#Comparison Applications|Comparison Applications]]
	- [[#Experimental Methodology#Workload|Workload]]
	- [[#Experimental Methodology#Metrics Measured|Metrics Measured]]
	- [[#Experimental Methodology#Results|Results]]
		- [[#Results#Synthetic Load (Best Case)|Synthetic Load (Best Case)]]
		- [[#Results#Traces|Traces]]
		- [[#Results#Impact of Optimizations|Impact of Optimizations]]
		- [[#Results#Summary|Summary]]
- [[#Quiz: Performance Observation|Quiz: Performance Observation]]
- [[#Designing and Running Experiments|Designing and Running Experiments]]
	- [[#Designing and Running Experiments#Example: Web Server Experiment|Example: Web Server Experiment]]
	- [[#Designing and Running Experiments#Picking the Right Metrics|Picking the Right Metrics]]
	- [[#Designing and Running Experiments#Picking the Right Configuration Space|Picking the Right Configuration Space]]
	- [[#Designing and Running Experiments#What about the competition? The baseline?|What about the competition? The baseline?]]
	- [[#Designing and Running Experiments#Running Experiments|Running Experiments]]
- [[#Quiz: Experimental Design|Quiz: Experimental Design]]

## Overview
In this lecture
- Performance comparisons
	- multi-process vs
	- multi-threaded vs
	- event-driven
- Event-driven architectures
- Designing experiments

Supplemental Materials
- "Flash: An Efficient and Portable Web Server" [[P2 Pai Paper.pdf]] (vs Apache)

## Which Threading Model is Better?
- 6 workers total
- 11 toy orders
- Boss-Worker vs Pipeline
	- Boss-Worker
		- 120ms per order, 6 worker threads
		- Execution time for 11 toy orders = **360ms**
		- Average order completion time = **196ms**
	- Pipeline:
		- 20ms per stage, 6 stages
		- Execution time for 11 toy orders = **320ms**
		- Average order completion time = **220ms**

For this example, if we consider execution time as being the important consideration, we should pick the pipeline model. If we consider average order completion time, the boss-worker model is better.

There is no one true solution, what we care about is generating the metrics for each model.

## Are Threads Useful?
Threads are useful because they enable
- parallelization
- specialization (locality = hot cache)
- efficiency (lower mem requirements and cheaper synch)
- latency hiding of I/O operations (also useful on a single CPU platform)

What metrics are useful?
- Matrix multiply app?
	- execution time for a given matrix
- Web service?
	- Rate of number of client requests handled over time.
	- Per-request response time.
- For hardware?
	- higher utilization (e.g. percentage of the CPU being used over time)
- For each metric, useful operations:
	- average
	- max
	- min
	- 95%
	- 99%

To evaluate any solution, picking useful and relevant metrics is important.

## Performance Metrics
Metrics are a measurement standard. They should be measurable and/or quantifiable property of the system we're interested in that can be used to evaluate the system behavior.

These can be used to evaluate the implementation of a piece of software, and compare it to some other proposed implementation.

- execution time
- throughput
- request rate
- CPU utilization
- wait time
- platform efficiency (how well resources are utilized to deliver throughput)
- performance per $ spent on hardware
- performance per Watt
- uptime
- percentage of SLA violations
- client perception
- aggregate performance
- Average resource usage
	- RAM
	- disk usage
	- CPU usage

These measurable quantities could be obtained from
- experiments with real software deployment, real machines, real workloads, or
- toy experiments representative of realistic settings (simulations)

These experimental settings are referred to as a "testbed".

## Are threads useful (redux)?
- Depends on metrics!
- Depends on workload!
- (Enter JS apps running in a single-CPU environment)

It Depends!™

By itself, I.D. is always a correct answer, but never a complete answer.

## Multi-Process Concurrency vs Multi-Threaded Concurrency
Steps in a simple web server
1. client/browser send request
2. web server accepts request
3. server processing steps
	- accept conn
	- read request
	- parse request
	- find file
	- compute header
	- send header
	- read file, send data (loop)
4. respond by sending file

### Multi-Process Web Server
Just deploy multiple instances/replicas of the web server. Each instance handles requests synchronously as they come in. Deploy more replicas as request times increase.

- Simple
- More memory usage
- Costly to context switch
- Hard to maintain shared state
- Tricky port setup (need a load balancer, or need to understand how multiple processes can share a single socket port)

### Multi-Threaded Web Server (MT)
Multiple execution contexts, multiple threads, within the same address space. Every thread executes all of the steps, or implemented as a boss-worker pattern.

- Shared address space
- shared state (lower memory footprint)
- cheaper to context switch between threads (compared to processes)
- Not simple to implement
- Requires synchronization
- OS/hardware need to support threads. Usually not an issue, but everyone makes hardware these days.

## Event-Driven Model
- Single address space
- single process
- single thread of control

Main thread contains an event dispatcher, which operates like a state machine.

![[Pasted image 20221002173501.png]]

Call handler means jump to the code relevant to each event.

Each handler
- runs to completion
- if they need to block, they initiate the blocking operation and pass an event back to the dispatcher

### Concurrency
In other models, concurrency is achieved by ensuring that multiple requests are being processed at any given time.

This the Event-Driven model, may requests are processed at any given time by interleaving the blocking operations of each request. A single thread switches among processing of different requests.

### Why?
> Why does this work?

On 1 CPU, we can use threads to hide latency. If the time that a thread will idle on an operation is more than 2 times the amount of time that it takes the OS to context switch between threads within the same application, then you can use context switching to hide the latency. Otherwise you're just wasting time context switching.

In this model, you avoid OS context switching and/or ULT context switching, and replace it with your own request context switching.

If you have multiple CPUs, you can still use this model. Just run multiple instances of your event-driven application.

### How?
> How does this work? How is it implemented?

The OS uses abstractions to represent I/O operations. Loads of I/O operations happen against a single abstraction known as a "file descriptor". Any event in the event-driven model can be categorized as "an input on a file descriptor".

Useful system calls for determining "which file descriptor"
- `select()`
- `poll()`
- `epoll()` <- Pretty important one

Benefits
- Single address space
- Single flow of control
- Smaller memory requirement
- No OS-level, ULT-library-level context switching
- No synchronization required.

### Problems with Event-Driven Model
If any handler issues a blocking request/handler, this will block the entire process from being to begin working on a different task while the operation completes.

You need to ensure that all of the I/O operations performed by the process are using asynchronous I/O operations. Async calls happen by:
- Process/thread makes system call
- OS obtains all relevant info from stack, and either learns where to return results, or tells caller where to get results later.
- process/thread can then continue

Requires support from kernel (e.g. threads) and/or device (e.g. DMA)

### Helper Threads
- If a blocking I/O operation doesn't have an `async` variant, we can return to using threads for hiding I/O latency.
- The event dispatcher communicates with these helper threads using pipe/socket based communication.
	- `select()` and `poll()` can be used here
- The helper thread will be blocked, but the main event loop (i.e. the process) will not be blocked.

If the OS doesn't support threads, we can use helper processes instead. This is referred to as "Asymmetric Multi-Process Event-Driven Model (AMPED)".

If the helpers are threads, it can be referred to as "Asymmetric Multi-Threaded Event-Driven Model (AMTED)"

Pros:
- resolves portability limitations of basic event-driven model
- smaller footprint than regular worker thread.
- Only as many threads/processes as there are concurrent blocking I/O operations. Compare this to MT/MP models where there are as many threads/processes as there are requests being handled.

Cons:
- Not as applicable to all classes of applications
- Event routing on multi-CPU systems can be complicated, and often requires a load balancer and/or message broker.

## Flash: Event-Driven Web Server
- An event-driven webserver (AMPED)
- Has asymmetric helper processes
- Uses processes for blocking I/O operations
- Uses handlers for async I/O operations
- Helpers are mainly used for disk reads
- Pipes are used for communication with dispatcher
- Helper reads file in memory via `mmap`
- Dispatcher checks (via `mincore`) if pages of the file are in memory, to decide whether it should call a "local" handler or via a helper.
- Possibility for big savings.

Additional optimizations
- Performs application level caching at multiple levels
	- caches file data (uses helper process on cache misses)
	- caches response headers
	- caches path-name transformation (uses helper process on cache misses)
- Alignment for DMA
- Use of DMA w/ scatter-gather => vector I/O operations

These are now fairly common optimizations, but were fairly novel back when the paper was introduced.

## Apache Web Server
- Apache has a "core" which accepts and responds to requests.
- Apache has different modules, which are per-functionality blocks
- Flow of control: similar to event driven model
- Implementation is a combination of MP+MT
	- Each process is a boss/worker with a dynamic thread pool
	- Total # of processes can also be dynamically adjusted

## Experimental Methodology
_Performance comparison methodology comparing Flash and Apache._

### Comparison Applications
The researchers compared Flash to the following alternate web server implementations, all with the same optimizations that Flash uses (except Apache).

- MP web server, where each process was a single threaded application
- MT web server, using the boss-worker pattern
- Single Process Event-Driven (SPED) (basic event-driven model)
- Zeus (SPED w/ 2 processes)
- Apache (v1.3.1 MP config)
- Flash (AMPED)

### Workload
Realistic request workload
- distribution of web page access over time.
- Controlled, reproducible workloads
- trace-based (from real web servers)
	- CS Web Server trace (Rice University) (large dataset)
	- Owlnet trace (Rice University) (small dataset)
	- Synthetic Workload

### Metrics Measured
- bandwidth (bytes/second)
- connection rate (request rate)

Evaluates both as a function of file size. A larger file size:
- ammortizes the per-connection cost => higher bandwidth
- more work per connection => lower connection rate

### Results
#### Synthetic Load (Best Case)
- N requests for the same file, more likely to encounter a cached file
- Measure Bandwidth
	- $BW = N\frac{bytes(file)}{time}$
	- File sizes 0 - 200kB, varying the work per request
- Observations
	- All exhibit similar results
	- SPED had best performance
	- Flash AMPED had an extra check for memory presence
	- Zeus has an anomaly. Buggy implementation
	- MP/MT extra sync and context switching
	- Apache had no optimizations

![[Pasted image 20221002192633.png]]

#### Traces
![[Pasted image 20221002192622.png]]

- Owlnet Trace Observations
	- trends similar to "best" case
	- small trace, mostly fits in cache
	- sometimes blocking I/O is required
		- SPED will occasionally block
		- Flash's helpers resolve that problem
- CS Trace Observations 
	- larger trace, mostly required I/O
	- SPED is the worst, lacks async I/O
	- MT is better than MP
		- memory footprint
		- faster synchronization
	- Flash best
		- smallest memory footprint
		- more memory available for caching
		- fewer requests lead to a blocking I/O operation
		- one address space, no threads, no sync required

#### Impact of Optimizations
![[Pasted image 20221002192651.png]]

Flash w/ optimizations:
- Path: directory lookup caching
- Path & `mmap`: directory lookup plus file data caching
- All: directory lookup, file data, response header caching

Apache would also have benefited from all of these optimizations.

#### Summary
- When data is in cache
	- SPED > AMPED Flash
		- unnecessary test for memory presence
	- SPEC and AMPED Flash > MT/MP
		- sync and context switching imparts overhead
- With disk-bound workload
	- AMPED Flash > SPED
		- SPED blocks because there's no async I/O
	- AMPED Flash > MT/MP
		- more memory efficient and less context switching

## Quiz: Performance Observation
![[Pasted image 20221002193244.png]]

Comparing SPED and Flash (assuming identical workloads)
- Flash can handle I/O operations w/o blocking
- Workload becomes I/O bound after 100 MB
- SPED has the smallest memory footprint, so it can cache the most files, though that advantage diminishes as soon as disk-access is required

## Designing and Running Experiments
### Example: Web Server Experiment
- Clients: care about response time
- Operators: care about throughput
- Are these metrics at odds with each other?
- Possible goals
	- Improve both metrics? (great!)
	- Improve response time?
	- Improve response time at the expense of throughput? Looks impressive, but not a great way to ensure scalability.
	- Maintain response time when request rate increases
- Goals: metrics and configuration of experiments

### Picking the Right Metrics
- "rule of thumb" for picking metrics
	- "standard" metrics
	- appeals to a broader audience
	- trying to be persuasive at the end of the day
- metrics answers the "Why? What? Who?" questions
	- client performance: response time, # of timeouts on requests
	- operator costs: throughput, cost

### Picking the Right Configuration Space
- System resources
	- hardware: CPU/RAM config
	- software: # threads, queue sies
- Workload
	- web server
		- request rate
		- concurrent requests
		- file size
		- access pattern
- Pick!
	- choose subset of config params that are most impactful to metrics under observation
	- pick ranges for each variable factor. Line charts better than bar charts.
	- pick a relevant workload
	- include best/worst case scenarios (SWOT analysis)

Guidelines
- Pick useful combinations of factors. May just reiterate the same point. Including too many dilutes your point.
- Compare apples to apples. AKA Change one variable at a time.

### What about the competition? The baseline?
- Compare the proposed system to the state-of-the-art system
- OR most common practice
- OR ideal best/worst case scenario

### Running Experiments
Now it's easy
- run test cases N times
- compute metrics
- represent results

**Don't forget about making a conclusion!** Summarize the data and provide recommendations on what system designers aught to do with their systems.

## Quiz: Experimental Design
Prompt: Toy shop. How many workers should be hired to handle the worst case scenario?
- Orders range in difficulty, from blocks, to teddy bears, to trains.
- Toy shop has 3 working areas, all capable of making any of the 3 options.
- Possible experiments:
	- E1 Different Configurations
		- order of trains, 3 workers
		- order of trains, 4 workers
		- order of trains, 5 workers
		- changing the number of workers to see how that affects the system
	- E2 Different Configurations
		- mixed order, 3 workers
		- mixed order, 6 workers
		- mixed order, 9 workers
	- E3 Different Configurations (best experiment)
		- trains, 3 workers
		- trains, 6 workers
		- trains, 9 workers
- Rejected experiments include trials where more than one variable is changing at a time.
