# Midterm Exam Prep
> This is not an exclusive list of questions, just a guideline so you keep in mind the main takeaways from the lessons.
>
> Feel free to create a shared document in a Piazza post and to collaborate on answering the questions.
> 
> -Ada

## Part 1
1. What are the key roles of an operating system?
	- An OS is a layer of systems software that
		- has privileged access to the underlying hardware
		- hides the hardware complexity
		- manages hardware on behalf of one of more applications, according to predefined policies
		- ensures that applications are isolated and protected from each other
	- The **key roles** of an OS are
		- **abstraction**. abstract the use of a computer system
		- **arbitration**. arbitrate the use of the computer system
		- **policies**. have policies which govern how the OS abstracts and arbitrates
		- **system calls**. exposes system calls that applications can use to access the hardware of a computer
2. Can you make distinction between OS abstractions, mechanisms, policies?
	- **Abstractions**: Provides a functional interface against computer hardware, in order to make developing applications for the platform easier. An example of this would be providing "files and directories" in a "file system", so that processes don't have to worry about how each physical device represents the contents of a file, nor the protocols used to interact with those physical devices.
		- Files, sockets, memory pages, processes, threads
	- Mechanisms are the methods that an OS uses to interact with a hardware platform.
		- Create, schedule, open, read, write, allocate
	- Policies are interchangeable components of mechanisms, allowing the system to be tweaked/customized without rewriting core functionality.
		- least recently used, least frequently used, earliest deadline
3. What does the principle of separation of mechanism and policy mean?
	- The separation means that each mechanism that an OS supports should be flexible enough to support multiple policies.
	- One example of a mechanism is swapping memory. When a computer gets close to running out of memory, the OS must "swap" memory pages, meaning pages of memory must be copied/moved between memory and the file system.
	- The component of that process which decides which memory pages to swap could be implemented using a "policy". Least Recently Used (LRU) or Least Frequently Used (LFU) would be 2 examples of such policies.
4. What does the principle optimize for the common case mean?
	- Optimizing for the common case means that, when designing a system, you want to make sure that you're thinking about the workload requirements of that system that will occur the most frequently. Ensuring those requirements are fulfilled and optimized should be top priority. This ideally leads to the best performance outcomes of that system.
5. What happens during a user-kernel mode crossing?
	- User-kernel crossings are typically what happens when a process makes a system call. When this happens, the underlying hardware "traps" instructions that applications are not allowed to execute. The hardware then passes control to the Kernel/OS, which will validate/reject the process's request.
6. What are some of the reasons why user-kernel mode crossing happens?
	- Crossings typically happen whenever a process makes a system call, or attempts to execute a privileged instruction that can only be executed by the kernel. Examples include
		- Asking the OS to allocate memory (`malloc`)
		- Asking the OS to open a file so the program can read its contents
		- Asking the OS to make a network request on behalf of the process
8. What is a kernel trap? Why does it happen? What are the steps that take place during a kernel trap?
	- A kernel trap happens when a process attempts to perform privileged instructions. The "mode bit" on the processor will be set appropriately, and then the kernel will steal the execution context from the application. The kernel will then complete or reject the operation, set the "mode bit" on the processor back to its original value, then will pass control back to the process.
9. What is a system call? How does it happen? What are the steps that take place during a system call?
	- A system call is effectively what happens when a process asks the kernel to perform an operation that it is not privileged enough to perform. To perform a system call, an application must
		- Write arguments
		- save relevant data to a well-defined location, so the kernel knows where to retrieve sys call arguments
		- make the system call using the specific system call number
		- applications pass args to the system call by passing the args directly to the OS (pass by value) and/or setting args in registers and passing the addresses to the system call (pass by reference (pointers)).
10. Contrast the design decisions and performance tradeoffs among monolithic, modular and microkernel-based OS designs.
	- Monolithic
		- One giant codebase to rule them all. All services that the OS supports is included in the OS.
		- Batteries-included OS design.
		- Limited customization, portability, manageability, and maintainability.
	- Modular
		- The OS has basic services/APIs, and specifies module interfaces, allowing implementers to install new modules to support additional functionality.
		- Better maintainability, smaller core OS code size, fewer resources used by the OS itself
		- "indirection impacts performance", OS offloads work onto separate modules (implying overhead on providing OS services) maintenance is still an issue.
	- Microkernel
		- The kernel does at little as possible in order to support system calls, process/thread management, and address space management.
		- All other OS services are run as applications on top of the kernel and communicate via IPC
		- Super small code size, least resources used by all kernel models.
		- questionable portability, limited code sharing among different OS services, increased frequency of user/kernel crossings, not a great model for a general purpose OS

Part 2:

1. Process vs. thread, describe the distinctions. What happens on a process vs. thread context switch.
	- Processes can be single threaded or multithreaded. Separate processes do not share an address space, while separate threads within a single process do share an address space. Each thread in a process has its own execution context.
	- When the OS context switches between 2 processes
		- it must first make one of the processes idle. When this happens, it stops the execution of that process, and gathers information about the process from CPU registers, and records all of the information in various data structures that describe the process.
		- The OS is then able to set those CPU registers from the data structures that describe a different process, and allow the CPU to begin/resume executing that other process's instructions.
		- Historically, the state that the OS manages about a process was contained by a single structure known the Process Control Block (PCB). These days, processes are incredibly complicated, so the data structures required to keep track of a process's current state are not as easily described.
	- When the OS context switches between 2 threads within the same process, similar steps happen. However, there is less information that the OS needs to swap into CPU registers, since 2 threads can share the same address space. Only the threads' execution contexts need to be swapped out.
2. Describe the states in a lifetime of a process?
	- New: The process has been created, but has not yet been "admitted" to the "ready" state.
	- Ready: The process is ready to be scheduled.
	- Running: The process's instructions are currently being executed by the CPU.
	- Waiting: The process made a request for a mutex lock, made an I/O request, or is waiting for a condition, and is now blocked.
	- Terminated: A process has been exited and can no longer execute instructions.
3. Describe the lifetime of a thread?
	- Threads share a similar life-cycle to processes. When threads are created, the don't immediately run. They must be placed into some kind of ready queue before they can be associated with a kernel thread and begin execution.
4. Describe all the steps which take place for a process to transition form a waiting (blocked) state to a running (executing on the CPU) state.
	- When a process is waiting/blocked on some kind of condition or event, it's moved to the "waiting" state. Once the event completes, the process moves to the "ready" state. The process is then free to be moved to the "running" state only once the scheduler dispatches the process, so that its instructions can be executed by the CPU.
5. What are the pros-and-cons of message-based vs. shared-memory-based IPC.
	- Message-based
		- Pro: The OS manages and brokers the communication
		- Con: There's overhead on performing those system calls
	- shared memory
		- Pro: Unmatched performance.
		- Cons: 2 code bases accessing the same memory addresses is error prone, requiring the code that accesses that memory to be duplicated and/or shared between different applications. Maintaining synchronization is very difficult. 
6. What are benefits of multithreading? When is it useful to add more threads, when does adding threads lead to pure overhead? What are the possible sources of overhead associated with multithreading?
	- Multithreading allows a process to more efficiently utilize the entirety of a platform's CPU resources. This means that, if a CPU has multiple cores, and the OS supports multiple concurrent threads running on that CPU, the process can perform computations in parallel on that CPU.
	- Threads can also be used to hide the latency that is the result of I/O. This allows I/O to block a child thread, allowing other threads to continue executing. This benefit is especially useful even when there's only one CPU core.
	- Threads add unnecessary overhead when a process's has more threads attempting to execute instructions than there are CPUs available. Threads also add overhead if the instructions being executed by the threads cannot run in parallel. If the entirety of a thread's instructions are guarded by a mutex, adding more threads to execute.
	- Threads overhead includes
		- the memory required to store information about that thread
		- the memory required to store the thread in the ready queue
		- the fact that threads must be scheduled to execute on the CPU, so having more threads than CPU cores means its more likely that a thread will be context switched off the CPU before it's completed something.
		- the fact that context switches makes it more likely that threads will be accessing a cold cache, due to threads requiring different memory addresses.
7. Describe the boss-worked multithreading pattern. If you need to improve a performance metric like throughput or response time, what could you do in a boss-worker model? What are the limiting factors in improving performance with this pattern?
	- One main thread, multiple peered worker threads. The main thread enqueues jobs onto a shared queue, the worker threads pull jobs from that shared queue.
	- Apart from performance considerations that are applicable to all multithreaded process models, the biggest change you can make to a boss worker pattern is to increase the number of worker threads that are available to process requests. This number of threads should be somewhere around the number of cores on CPU, unless the threads are performing a lot of I/O requests, in which case it might make sense to have more threads than there are CPU cores. You could also create a separate thread pool for handling I/O requests, though that could be seen as transitioning to a pipelined or layered threading model.
8. Describe the pipelined multithreading pattern. If you need to improve a performance metric like throughput or response time, what could you do in a pipelined model? What are the limiting factors in improving performance with this pattern?
	- In the pipelined multithreading model, each stage of a pipeline is defined as a single thread pool, with multiple threads executing one component of a process. Each stage of the pipeline shares a shared buffer with the stage after. If one state takes longer than other stages, you can increase the number of threads made available to that stage. This model has better specialization and locality compared to the boss-worker model, but maintaining balance is challenging, and there's significant overheads on maintaining synchronization between stages.
9. What are mutexes? What are condition variables? Can you quickly write the steps/code for entering/existing a critical section for problems such as reader/writer, reader/writer with selective priority (e.g., reader priority vs. writer priority)? What are spurious wake-ups, how do you avoid them, and can you always avoid them? Do you understand the need for using a while() look for the predicate check in the critical section entry code examples in the lessons?
	- Mutexes: These are "mutual exclusions" which allows applications to ensure that protects multiple threads from operating on a shared piece of data.
	- Condition Variables: These allow threads to wait for a condition, so they don't spend excess energy constantly checking the result of a computation, while waiting for a specific condition.
	- **Can you quickly write the steps/code for entering/existing a critical section for problems such as reader/writer, reader/writer with selective priority (e.g., reader priority vs. writer priority)?**
		- Critical sections should be fine. The part I don't have a great grasp of yet is the "one level of indirection" in making sure that one of the services has priority.
	- Spurious wake ups are what happens when a thread wakes up, only to go right back to sleep. This happens when one thread broadcasts to a condition, when it could/should have just signaled. This also happens when a thread sends a signal/broadcast before unlocking the mutex that guards the condition. They can almost always be avoided by adding more complexity to your management of mutexes and conditions, but sometimes its worth it to take the usually minor performance hit and keep application complexity lower. Sometimes you just need to make sure your threads are signalling instead of broadcasting, or unlocking mutexes before signaling/broadcasting.
	- Using `while()` around a condition makes sure that a program both (a) avoids waiting on a condition when the condition is already satisfied and (b) checks the condition after the signal/broadcast occurs to ensure that the condition is still valid, before it proceeds to operating on shared data.
10. What’s a simple way to prevent deadlocks? Why?
	- Order your mutex locks! Globally maintaining the order that threads lock mutexes ensures that you don't create a cycle in which all threads are waiting to acquire a mutex lock, but can't because the holders of those locks are also waiting and will never reach the mutex unlock instruction. Ordering the locks makes sure that your threads never create such a cycle.
11. Can you explain the relationship among kernel vs. user-level threads? Think though a general mxn scenario (as described in the Solaris papers), and in the current Linux model. What happens during scheduling, synchronization and signaling in these cases?
	- In the current linux model, the POSIX Threads API only associates ULTs and KLTs in a single 1-to-1 mapping.
	- In previous models, you could see 1-to-1, 1-to-many, and even many-to-many.
	- [[P2L2 Threads and Concurrency]]
12. Can you explain why some of the mechanisms described in the Solaris papers (for configuring the degree concurrency, for signaling, the use of LWP…) are not used or necessary in the current threads model in Linux?
	- LWPs are no longer needed as a useful abstraction. The Linux Kernel just maintains a 1-to-1 relationship between ULTs and KLTs. Memory is so cheap now that initializing that many threading data structures is considered as much of a penalty.
13. What’s an interrupt? What’s a signal? What happens during interrupt or signal handling? How does the OS know what to execute in response to a interrupt or signal? Can each process configure their own signal handler? Can each thread have their own signal handler?
	- Interrupts are handled by the OS, since they are events generated by components that aren't the CPU. They typically describe the results of an I/O request
	- Signals are handled by the threads of a process, and are events that are generated by the CPU.
	- Each has an ID which correlates with a lookup table, where the values points to the memory address of the starting instruction of the handler routine. The OS has a table for interrupt handlers. Each process has its own table for signal handlers.
	- Each process can define its own signal handlers, but each thread can only set its own signal mask, declaring which signals it will and will not handle.
14. What’s the potential issue if a interrupt or signal handler needs to lock a mutex? What’s the workaround described in the Solaris papers?
	- This could potentially cause a deadlock situation, if the handler is executed in the same execution context as a thread that has already locked the same mutex. The workaround is to run the handler in its own thread, so it doesn't pull the running thread out of the running state.
16. Contrast the pros-and-cons of a multithreaded (MT) and multiprocess (MP) implementation of a webserver, as described in the Flash paper.
	- Threads are cheaper than processes, but a MT implementation requires synchronization.
	- MPs are an easier implementation (just run more replicas of a single threaded service), but requires an intermediary service to broker connections, often called a load balancer.
17. What are the benefits of the event-based model described in the Flash paper over MT and MP? What are the limitations? Would you convert the AMPED model into a AMTED (async multi-threaded event-driven)? How do you think ab AMTED version of Flash would compare to the AMPED version of Flash?
	- I would convert the AMPED model to an AMTED model. The biggest concerns with the AMTED model over the AMPED model would be portability and requiring synchronization. These days, all platforms that I would feel comfortable deploying a web server to would certainly support threads, and synchronization is commonplace in applications these days. An AMTED implementation would certainly outperform an AMPED implementation, for all the same reasons that an MT implementation outperforms an MP implementation.
		- Lower memory usage
		- Faster results sharing due to only having one address space.
1. There are several sets of experimental results from the Flash paper discussed in the lesson. Do you understand the purpose of each set of experiments (what was the question they wanted to answer)? Do you understand why the experiment was structured in a particular why (why they chose the variables to be varied, the workload parameters, the measured metric…).
	- Yes.
2. If you ran your server from the class project for two different traces: (i) many requests for a single file, and (ii) many random requests across a very large pool of very large files, what do you think would happen as you add more threads to your server? Can you sketch a hypothetical graph?
	- Given enough brain power, probably.
