# GIOS Readiness Survey
Tags: #OMSCS, #GIOS, #CS6200

> Have you taken an undergraduate operating systems course, or at least a computer system course that surveys basic computer hardware and systems software components?

Yes.

> Have you taken a course that covers computer architecture topics? Do you understand the basics of how computer systems work?

I do.

> Do you at least conceptually understand the definition and purpose of some of the key OS mechanisms and abstractions: process, thread, address space, page table, device driver, scheduling, virtual memory management, file system...?

- A process is a unit that describes a running "instance" of a piece of software, usually identified with a process ID or "PID"
- Threads
	- From Wikipedia: "In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), a **thread** of [execution](https://en.wikipedia.org/wiki/Execution_(computing) "Execution (computing)") is the smallest sequence of programmed instructions that can be managed independently by a [scheduler](https://en.wikipedia.org/wiki/Scheduling_(computing) "Scheduling (computing)"), which is typically a part of the [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system"). The implementation of threads and [processes](https://en.wikipedia.org/wiki/Process_(computing) "Process (computing)") differs between operating systems, but in most cases a thread is a component of a process. The multiple threads of a given process may be executed [concurrently](https://en.wikipedia.org/wiki/Concurrent_computation "Concurrent computation") (via multithreading capabilities), sharing resources such as [memory](https://en.wikipedia.org/wiki/Shared_memory_(interprocess_communication) "Shared memory (interprocess communication)"), while different processes do not share these resources. In particular, the threads of a process share its executable code and the values of its [dynamically allocated](https://en.wikipedia.org/wiki/Memory_management#HEAP "Memory management") variables and non-[thread-local](https://en.wikipedia.org/wiki/Thread-local_storage "Thread-local storage") [global variables](https://en.wikipedia.org/wiki/Global_variable "Global variable") at any given time."
	- Processes typically only use one thread at a time, which can be moved from core-to-core on the processor.
	- I've written multithreaded code before, but it's hard to describe exactly what a thread _is_ without tying that understanding to a specific programming language's interface for running tasks on multiple threads.
- Threads differ from traditional [multitasking](https://en.wikipedia.org/wiki/Computer_multitasking "Computer multitasking") operating-system [processes](https://en.wikipedia.org/wiki/Process_(computing) "Process (computing)") in several ways:
	- processes are typically independent, while threads exist as subsets of a process
	- processes carry considerably more [state](https://en.wikipedia.org/wiki/State_(computer_science) "State (computer science)") information than threads, whereas multiple threads within a process share process state as well as [memory](https://en.wikipedia.org/wiki/Computer_storage "Computer storage") and other [resources](https://en.wikipedia.org/wiki/Resource_(computer_science) "Resource (computer science)")
	- processes have separate [address spaces](https://en.wikipedia.org/wiki/Address_space "Address space"), whereas threads share their address space
	- processes interact only through system-provided [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication "Inter-process communication") mechanisms
	- [context switching](https://en.wikipedia.org/wiki/Context_switch "Context switch") between threads in the same process typically occurs faster than context switching between processes
- Address Space
	- From wikipedia, "In [computing](https://en.wikipedia.org/wiki/Computing "Computing"), an **address space** defines a range of discrete addresses, each of which may correspond to a [network host](https://en.wikipedia.org/wiki/Network_host "Network host"), [peripheral device](https://en.wikipedia.org/wiki/Peripheral_device "Peripheral device"), [disk sector](https://en.wikipedia.org/wiki/Disk_sector "Disk sector"), a [memory](https://en.wikipedia.org/wiki/Computer_data_storage "Computer data storage") cell or other logical or physical entity."
	- It's basically just a collection of addresses. I'm sure that an address space can be non-continuous.
- page table
	- A **page table** is the [data structure](https://en.wikipedia.org/wiki/Data_structure "Data structure") used by a [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory "Virtual memory") system in a [computer](https://en.wikipedia.org/wiki/Computer "Computer") [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") to store the mapping between [virtual addresses](https://en.wikipedia.org/wiki/Virtual_address "Virtual address") and [physical addresses](https://en.wikipedia.org/wiki/Physical_address "Physical address"). Virtual addresses are used by the program executed by the accessing [process](https://en.wikipedia.org/wiki/Process_(computing) "Process (computing)"), while physical addresses are used by the hardware, or more specifically, by the [random-access memory](https://en.wikipedia.org/wiki/Random-access_memory "Random-access memory") (RAM) subsystem.
- device driver
	- I use Linux. I understand device drivers pretty well.
- scheduling
	- 
- virtual memory management
	- Virtual memory is a combination of hardware and software that maps memory address used by a program, called "virtual addresses", to the physical addresses in a computer's memory/storage systems. This is completely opaque to the process. The process thinks it has a contiguous address space or a collection of contiguous memory segments. This is useful for process isolation, and to make use of the OS's page file, which is when memory is mapped to a storage drive due to low memory.
	- From Wikipedia: "Virtual memory makes application programming easier by hiding [fragmentation](https://en.wikipedia.org/wiki/Fragmentation_(computer) "Fragmentation (computer)") of physical memory; by delegating to the kernel the burden of managing the [memory hierarchy](https://en.wikipedia.org/wiki/Computer_data_storage#Hierarchy_of_storage "Computer data storage") (eliminating the need for the program to handle [overlays](https://en.wikipedia.org/wiki/Overlay_(programming) "Overlay (programming)") explicitly); and, when each process is run in its own dedicated address space, by obviating the need [to relocate](https://en.wikipedia.org/wiki/Relocation_(computer_science) "Relocation (computer science)") program code or to access memory with [relative addressing](https://en.wikipedia.org/wiki/Addressing_mode#PC-relative "Addressing mode")."
	- ![[Pasted image 20220817185045.png]]
- file system
	- It's where the files go. ZFS, EXT4, etc.

> Are you familiar with C and C++? Have you programmed in a Linux environment? This introductory lesson should give you a better idea of the practical skills you will need for this course.

I took one or two courses in undergrad that required C and C++ for course assignments. It's been a few years. I also used to play around with Arduinos, which use a variant of C. I need to do a refresher.

> Are you interested in understanding the internals of how computing systems work, and how to get them to work “better” (as opposed to being interested in upper-level software and building cool applications)?

To be honest, I am *mostly* interested in using computers as a platform for building "cool applications", aka systems that provide value for the people that use them and rely on them. However, I do really love operating systems, and I'm interested in seeing what else that will qualify me fore in this program.