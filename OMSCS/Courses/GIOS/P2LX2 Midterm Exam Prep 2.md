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
	- Asking the OS to allocate memory (`malloc`)
	- Asking the OS to open a file so the program can read its contents
	- Asking the OS to make a network request on behalf of the process
7. What is a kernel trap? Why does it happen? What are the steps that take place during a kernel trap?
	- A kernel trap happens when a process attempts to perform privileged instructions. The "mode bit" on the processor will be set appropriately, and then the kernel will steal the execution context from the application. The kernel will then complete or reject the operation, set the "mode bit" on the processor back to its original value, then will pass control back to the process.
8. What is a system call? How does it happen? What are the steps that take place during a system call?
	- A system call is effectively what happens when a process asks the kernel to perform an operation that it is not privileged enough to perform. To perform a system call, an application must
		- Write arguments
		- save relevant data to a well-defined location, so the kernel knows where to retrieve sys call arguments
		- make the system call using the specific system call number
		- applications pass args to the system call by passing the args directly to the OS (pass by value) and/or setting args in registers and passing the addresses to the system call (pass by reference (pointers)).
9. Contrast the design decisions and performance tradeoffs among monolithic, modular and microkernel-based OS designs.
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
	- 
2. Describe the states in a lifetime of a process?
	- 
3. Describe the lifetime of a thread?
	- 
4. Describe all the steps which take place for a process to transition form a waiting (blocked) state to a running (executing on the CPU) state.
	- 
5. What are the pros-and-cons of message-based vs. shared-memory-based IPC.
	- 
6. What are benefits of multithreading? When is it useful to add more threads, when does adding threads lead to pure overhead? What are the possible sources of overhead associated with multithreading?
	- 
7. Describe the boss-worked multithreading pattern. If you need to improve a performance metric like throughput or response time, what could you do in a boss-worker model? What are the limiting factors in improving performance with this pattern?
	- 
8. Describe the pipelined multithreading pattern. If you need to improve a performance metric like throughput or response time, what could you do in a pipelined model? What are the limiting factors in improving performance with this pattern?
	- 
9. What are mutexes? What are condition variables? Can you quickly write the steps/code for entering/existing a critical section for problems such as reader/writer, reader/writer with selective priority (e.g., reader priority vs. writer priority)? What are spurious wake-ups, how do you avoid them, and can you always avoid them? Do you understand the need for using a while() look for the predicate check in the critical section entry code examples in the lessons?
	- 
10. What’s a simple way to prevent deadlocks? Why?
	- 
11. Can you explain the relationship among kernel vs. user-level threads? Think though a general mxn scenario (as described in the Solaris papers), and in the current Linux model. What happens during scheduling, synchronization and signaling in these cases?
	- 
12. Can you explain why some of the mechanisms described in the Solaris papers (for configuring the degree concurrency, for signaling, the use of LWP…) are not used or necessary in the current threads model in Linux?
	- 
13. What’s an interrupt? What’s a signal? What happens during interrupt or signal handling? How does the OS know what to execute in response to a interrupt or signal? Can each process configure their own signal handler? Can each thread have their own signal handler?
	- 
14. What’s the potential issue if a interrupt or signal handler needs to lock a mutex? What’s the workaround described in the Solaris papers?
	- 
15. Contrast the pros-and-cons of a multithreaded (MT) and multiprocess (MP) implementation of a webserver, as described in the Flash paper.
	- 
16. What are the benefits of the event-based model described in the Flash paper over MT and MP? What are the limitations? Would you convert the AMPED model into a AMTED (async multi-threaded event-driven)? How do you think ab AMTED version of Flash would compare to the AMPED version of Flash?
	- 
17. There are several sets of experimental results from the Flash paper discussed in the lesson. Do you understand the purpose of each set of experiments (what was the question they wanted to answer)? Do you understand why the experiment was structured in a particular why (why they chose the variables to be varied, the workload parameters, the measured metric…).
	- 
18. If you ran your server from the class project for two different traces: (i) many requests for a single file, and (ii) many random requests across a very large pool of very large files, what do you think would happen as you add more threads to your server? Can you sketch a hypothetical graph?
	- 
