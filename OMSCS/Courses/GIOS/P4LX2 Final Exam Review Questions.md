# Final Exam Review Questions from Piazza

## P3L1
> [[P3L1 Scheduling]]

1. How does scheduling work? What are the basic steps and datastructures involved in scheduling a thread on the CPU?
	1. There's a main queue, the runqueue, aka the ready queue, holds tasks ready for scheduling. implementation:
		1. standard queue
		2. priority queue
		3. tree structure
	2. pointer to the currently running thread
	3. All of the data associated with a task's "execution context"
		1. stack pointer
		2. virtual page table
		3. etc
	4. There's also loads of algorithms in determining which task to run. Typically predetermined priority numbers are used.
2. What are the overheads associated with scheduling? Do you understand the tradeoffs associated with the frequency of preemption and scheduling/what types of workloads benefit from frequent vs. infrequent intervention of the scheduler (short vs. long timeslices)?
	1. One of the issues with scheduling, from an overhead perspective, is the time it takes for the OS to perform a "context switch". During a context switch, the OS has to copy data from CPU registers into memory, and then copy data from memory into CPU registers, in order to save the current thread's execution state, and prepare a new thread's execution state. All of these operations take time, which is a source of overhead.
	2. I/O-bound tasks benefit from frequent context switching (short timeslices).
	3. CPU-bound tasks benefit from infrequent context switching (long timeslices).
3. Can you work through a scenario describing some workload mix (few threads, their compute and I/O phases) and for a given scheduling discipline compute various metrics like average time to completion, system throughput, wait time of the tasks…
	1. [[P4LX Final Preparation]]
4. Do you understand the motivation behind the multi-level feedback queue, why different queues have different timeslices, how do threads move between these queues… Can you contrast this with the O(1) scheduler? Do you understand what were the problems with the O(1) scheduler which led to the CFS?
	1. MLFQ
		1. Multiple different queues which are linked together in fancy ways.
		2. Each queue has a different timeslice value, with shorter timeslice queues for I/O-bound tasks, and longer timeslice queues for CPU-bound tasks.
		3. If a task uses its entire timeslice, its determined to be a CPU-bound task, so it is moved into the queue with the next highest timeslice.
		4. If a task yields voluntarily (blocks) before its timeslice expires, then it's determined to be an I/O bound task, so it is moved into the queue with the next lowest timeslice.
	2. O(1) scheduler
		1. Each task has a priority value
		2. The priority value is used to determine the timeslice value.
		3. tasks with long wait/idle times are determined to be interactive tasks, and see priority boosts
		4. tasks with short wait/idle times are determined to be compute intensive tasks, and will have their priority lowered
		5. 2 runqueues. Tasks are pulled from the active runqueue and placed into the expired runqueue once their timeslice has expired. Once there's no more tasks, the active/expired runqueue pointers are swapped, and it starts over.
	3. CFS uses a red-black tree for its data structure
		1. Nodes are ordered by their virtual runtime, tracked by the nanosecond
		2. The tree self-balances when nodes are added/removed
	4. O(1) issues
		1. poor performance of interactive tasks, I/O tasks spend unpredictable amounts of time waiting to be scheduled
		2. hard to make fairness guarantees
5. Thinking about Fedorova’s paper on scheduling for chip multi processors, what’s the goal of the scheduler she’s arguing for? What are some performance counters that can be useful in identifying the workload properties (compute vs. memory bound) and the ability of the scheduler to maximize the system throughput.
	1. idk

## P3L2
> [[P3L2 Memory Management]]

1. How does the OS map the memory allocated to a process to the underlying physical memory? What happens when a process tries to access a page not present in physical memory? What happens when a process tries to access a page that hasn’t been allocated to it? What happens when a process tries to modify a page that’s write protected/how does COW work?
	1. Each process has their own virtual page table, which maps a process's virtual addresses to the hardware physical addresses 
	2. If the memory page is on the disk, not in main memory, the OS will trap instructions trying to read from the page and will take the opportunity to swap that page.
	3. The OS "allocates pages on first touch", lazy-loading pages when required.
	4. COW: Copy on Write. If a process tries to write to a page that's read-only, the OS will trap the instruction, copy the page, adjust the VA->PA mapping.
2. How do we deal with the fact that processes address more memory than physically available? What’s demand paging? How does page replacement work?
	1. By using multi-level page tables, the OS saves memory when keeping track of a process's virtual addresses
	2. demand paging is what the "swap space" is for. "virtual memory pages are not always in physical memory"
	3. Page replacement happens when the OS starts running out of space in main memory. It will determine an old page, move it to the storage device, and set a flag on the VA->PA mappings that refer to that page, so it can trap instructions that try to access it later.
3. How does address translation work? What’s the role of the TLB?
	1. Virtual Addresses contain a virtual frame number (VFN) + an offset
	2. Physical address are calculated by looking up the value in the VFN and then adding the offset
	3. multi-level page tables work the same way, except the VFN is broken up into multiple components
	4. The Translation Lookaside Buffer is a hardware component that assists in VA->PA translations.
4. Do you understand the relationships between the size of an address, the size of the address space, the size of a page, the size of the page table…
	1. Size of an address, the number of bits required to index a "word" (byte) of memory. 64-bits on most modern hardware
	2. Size of an address space, the total number of addressable words. Can be virtual and/or physical
	3. Size of a page. This is configurable in the OS, and determines how many continuous addresses are grouped in a single page.
	4. Size of the page table. The actual size of the data structure that the OS uses to track VA->PA mappings.
5. Do you understand the benefits of hierarchical page tables? For a given address format, can you workout the sizes of the page table structures in different layers?
	1. Hierarchical page tables are useful because they prevent the OS from allocating a single contiguous data structure that maps all of the addresses for a process. Using a multi-level allows the OS to "skip" allocating inner page tables until they're useful.
	2. Notes
		1. Page size can be used to calculate the number of bits used for the VA page offset
		2. The rest of the bits are allocated to the "page frame number" (PFN)

## P3L3
> [[P3L3 Inter-Process Communication]]

1. For processes to share memory, what does the OS need to do? Do they use the same virtual addresses to access the same memory?
	1. The physical address of a shared memory page will still just be one physical address. Each process has a reference to that PA in their page tables. Each process will likely have a different virtual address for that page.
2. For processes to communicate using a shared memory-based communication channel, do they still have to copy data from one location to another? What are the costs associated with copying vs. (re-/m)mapping? What are the tradeoffs between message-based vs. shared-memory-based communication?
	1. message-based allows the OS to broker communication, which is less error-prone compared to mapping memory.
	2. mapping memory is way faster. They may need to copy data into and out of the shared memory pages, but that's more efficient that performing context switches with the OS.
3. What are different ways you can implement synchronization between different processes (think what kids of options you had in Project 3).
	1. semaphores
	2. IPC queues
	3. Shared mutexes

## P3L4
> [[P3L4 Synchronization Constructs]]

1. To implement a synchronization mechanism, at the lowest level you need to rely on a hardware atomic instruction. Why? What are some examples?
	1. Without hardware atomic instructions, you have race conditions when acquiring locks. 2 threads could check `if lock free?` at the same time, and then continue to acquire the lock at the same time
2. Why are spinlocks useful? Would you use a spinlock in every place where you’re currently using a mutex?
	1. spinlocks can be more effienct than context switching
	2. I don't see why a threading library couldn't implement a mutex lock operation as a spinlock when appropriate.
	3. Spinlocks are worthless on single-processor architectures.
3. Do you understand why is it useful to have more powerful synchronization constructs, like reader-writer locks or monitors? What about them makes them more powerful than using spinlocks, or mutexes and condition variables?
	1. Reader/writer locks and monitors are more expressive than attempting to roll your own for accomplishing the same thing.
	2. Reader/writer locks are just great.
4. Can you work through the evolution of the spinlock implementations described in the Anderson paper, from basic test-and-set to the queuing lock? Do you understand what issue with an earlier implementation is addressed with a subsequent spinlock implementation?
	1. idk, maybe?

## P3L5
> [[P3L5 IO Management]]

1. What are the steps in sending a command to a device (say packet, or file block)? What are the steps in receiving something from a device? What are the basic differences in using programmed I/O vs. DMA support?
	1. Programmed IO vs Direct Memory Access
	2. PIO is better when you aren't sending data that frequently, nor in high quantities. This is when the CPU sets registers on the I/O device in order to transfer data.
		1. set command on device
		2. write data to register
		3. read register to see when I/O device completed transfer
		4. repeat 2 and 3
	3. DMA is better when you're dealing with high volumes of data. This is when the CPU tells which memory regions the I/O device should read/write to/from.
		1. write data to contiguous memory location
		2. mark the pages as non-swappable (pinned)
		3. configure the device with the info about where to get the data and how much is there
2. For block storage devices, do you understand the basic virtual file system stack, the purpose of the different entities? Do you understand the relationship between the various data structures (block sizes, addressing scheme, etc.) and the total size of the files or the file system that can be supported on a system?
	1. virtual file system stack is used to support network file systems and multiple different storage mediums under the same umbrella.
	2. sure
3. For the virtual file system stack, we mention several optimizations that can reduce the overheads associated with accessing the physical device. Do you understand how each of these optimizations changes how or how much we need to access the device?
	1. caching/buffering
	2. I/O scheduling
	3. prefetching
	4. journaling/logging

## P3L6
> [[P3L6 Virtualization]]

1. What is virtualization? What’s the history behind it? What’s hosted vs. bare-metal virtualization? What’s paravirtualization, why is it useful?
	1. hosted: 
	2. bare-metal: 
	3. paravirtualization: 
2. What were the problems with virtualizing x86? How does protection of x86 used to work and how does it work now? How were/are the virtualization problems on x86 fixed?
3. How does device virtualization work? What a passthrough vs. a split-device model?

## P4L1
> [[P4L1 RPC]]

1. What’s the motivation for RPC? What are the various design points that have to be sorted out in implementing an RPC runtime (e.g., binding process, failure semantics, interface specification… )? What are some of the options and associated tradeoffs?
2. What’s specifically done in Sun RPC for these design points – you should easily understand this from your project?
3. What’s marshalling/unmarschaling? How does an RPC runtime serialize and deserialize complex variable size data structures? What’s specifically done in Sun RPC/XDR?

## P4L2
> [[P4L2 Distributed File Systems (DFS)]]

1. What are some of the design options in implementing a distributed service? What are the tradeoffs associated with a stateless vs. stateful design? What are the tradeoffs (benefits and costs) associated with using techniques such as caching, replication, partitioning, in the implementation of a distributed service (think distributed file service).
2. The Sprite caching paper motivates its design based on empirical data about how users access and share files. Do you understand how the empirical data translated in specific design decisions? Do you understand what type of data structures were needed at the servers’ and at the clients’ side to support the operation of the Sprite system (i.e., what kind of information did they need to keep track of, what kids of fields did they need to include for their per-file/per-client/per-server data structures).

## P4L3
> [[P4L3 Distributed Shared Memory]]

1. When sharing state, what are the tradeoffs associated with the sharing granularity?
2. For distributed state management systems (think distributed shared memory) what are the basic mechanisms needed to maintain consistence – e.g., do you why is it useful to use ‘home nodes’, why do we differentiate between a global index structure to find the home nodes and local index structures used by the home nodes to track information about the portion of the state they are responsible for.
3. Do you have some ideas how would you go about implementing a distributed shared memory system?
4. What’s a consistency model? What are the different guarantees that change in the different models we mentioned – strict, sequential, causal, weak… Can you work through a hypothetical execution example and determine whether the behavior is consistent with respect to a particular consistency model?

## P4L4
> [[P4L4 Datacenter Technologies]]

1. When managing large-scale distributed systems and services, what are the pros and cons with adopting a homogeneous vs. a heterogeneous design?
2. Do you understand the history and motivation behind cloud computing, and basic models of cloud offerings? Do you understand some of the enabling technologies that make cloud offerings broadly useful?
3. Do you understand what about the cloud scales make it practical? Do you understand what about the cloud scales make failures unavoidable?