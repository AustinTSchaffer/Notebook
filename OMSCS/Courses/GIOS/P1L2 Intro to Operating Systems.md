---
tags: GIOS, OMSCS
---

# P1L2: Introduction to OSes
- [[#Overview|Overview]]
- [[#Visual Metaphor|Visual Metaphor]]
- [[#What is an Operating System|What is an Operating System]]
- [[#Examples of Operating Systems|Examples of Operating Systems]]
- [[#OS Elements|OS Elements]]
- [[#OS Design Principles|OS Design Principles]]
- [[#OS Protection Boundary|OS Protection Boundary]]
- [[#System Calls are Pretty Complicated|System Calls are Pretty Complicated]]
- [[#Crossing the User/Kernel Protection Boundary|Crossing the User/Kernel Protection Boundary]]
- [[#OS Services|OS Services]]
- [[#Linux System Calls|Linux System Calls]]
- [[#OS Design|OS Design]]
	- [[#OS Design#Monolithic OS|Monolithic OS]]
	- [[#OS Design#Modular OS|Modular OS]]
	- [[#OS Design#Microkernel|Microkernel]]
- [[#Linux Architecture|Linux Architecture]]
- [[#MacOS Architecture|MacOS Architecture]]

## Overview
An OS is a piece of software that
- **abstracts** the use of a computer system
- **arbitrates** the use of that computer system
- has **policies** which governs how the OS performs those 2 things
- exposes **system calls** that applications can use to access the hardware of a computer

## Visual Metaphor

- The OS is a toy shop manager
	- Directs operational resources
		- Employee time, scheduling, parts, tools
	- Enforces policies
		- fair resource access, safety, security, cleanup, limits resource usage
	- Mitigates difficulty of complex tasks
		- simplifies operation
		- optimizes performance
		- "system calls"

## What is an Operating System

Computing systems contain
- One CPU or multiple CPUs, each with multiple cores
- Memory
- Network devices
- GPU
- Storage devices
- USB devices

All of these components will be shared by all of the processes running on the computer. The OS sits between those processes/application, and the physical components of the computing system. The OS will also abstract these components, aka "hide the complexity of the hardware" from the programs, so the programs don't have to manage that complexity.

For example, the OS abstracts away all of the different types of storage devices that you could buy (tape, HDD, SSD, flash, RAM, etc) and exposes a single concept of a "file" that you can read and write.

Another example, the OS abstracts away networking hardware and exposes "sockets" that programs can send packets to or receive packets from.

The OS also manages the underlying hardware, for example allocating memory for applications, and schedules the applications on the CPU, and brokers communication for other external devices. As part of this, the OS also isolates applications/processes from each other, so they can't step on each other's toes, or access each other's resources.

In short, an OS is a layer of systems software that
- has privileged access to the underlying hardware
- hides the hardware complexity
- manages hardware on behalf of one of more applications, according to predefined policies
- ensures that applications are isolated and protected from each other

An OS is NOT
- A user-facing application
- A component of the computing system, aka "the hardware"

Abstraction v Arbitration
- Abstraction
	- distributing memory between processors
	- supporting multiple types of speakers
	- interchangeable access of storage devices (i.e. if there's a driver, you can read/write files)
- Arbitration
	- distributing memory between processes
	- controlling access to storage devices

## Examples of Operating Systems

Platforms
- Desktop
- Embedded
- Mobile
- Server

Families
- Windows
- Unix-based
	- Mac OSX (BSD)
	- Linux
		- Ubuntu
		- CentOS
		- Debian
		- 1000 more
- Android
- iOS
- Symbian

This course particularly focuses on Linux.

## OS Elements
> Not to be confused with ElementaryOS

- Abstractions
	- Process, Thread
	- File
	- Socket
	- Memory page
- Mechanisms
	- Create, Schedule
	- Open
	- Read / Write
	- Allocate
- Policies
	- least-recently used (LRU)
	- earliest deadline first (EDF)

Memory Management Example
- The OS uses a memory page as an abstraction. The OS specifies a size for each memory page, such as 4KB.
- The OS has mechanisms to allocate those memory pages in DRAM and map them to processes. The process can now access those memory addresses, exposed to them via virtual memory addresses. These memory addresses could also be in a storage device (aka "swap memory")
- The OS incorporates policies, such as least recently used (LRU) to decide whether the contents of a page should be stored in RAM or stored in a storage device. This is referred to as "swapping". The LRU page are assumed to be less important, and it would be more efficient to free up space in RAM for other more frequently accessed, "more important", memory pages.

## OS Design Principles

Separation of mechanisms and policy
- OSes need to implement flexible mechanisms to support multiple policies
- e.g. memory page management, swap policy examples:
	- Least Recently Used (LRU)
	- Least Frequently Used (LFU)
	- random selection
- Optimize for the common case
	- How will the OS be used?
	- What will the user want to execute on that machine?
	- What are the workload requirements?

## OS Protection Boundary

Generally, OSes have 2 different execution modes, "user-level" and "kernel-level". These may also be called "unprivileged" and "privileged" modes.

- user-level
	- applications
- kernel-level
	- OS
	- access to hardware

The hardware should support user-kernel permissions switching.
- There typically will be a "bit" that the Kernel can use to switch between these modes. This is called a "user-kernel switch".
- If an unprivileged application (i.e. a non-Kernel application) attempts to use a privileged kernel-mode instruction, the CPU should "**trap**" the instruction and interrupt the program. The Kernel will then have to essentially approve or deny that application's request to execute that instruction.
- The "**system call**" interface allows applications to allow the Kernel to execute privileged instructions on their behalf.
	- open (file)
	- send (socket)
	- malloc (memory)
- "**signals**" allow the OS to pass notifications into applications

## System Calls are Pretty Complicated

- Application running along when suddenly it needs a file, network resource, new memory, etc
- The application makes a system call for one of these resources, passing whatever arguments are relevant.
- This **traps** the application, the "**mode bit**" is set to `0`.
- The Kernel then steals the execution context from the application and performs the necessary operations
- Then the Kernel returns the result back to the application, setting "mode bit" to `1`.
- Control is returned to the application, which accepts the result from the operating system.
- To make a system call, an application must
	- Write arguments
	- save relevant data at a well-defined location. This is so the OS knows where to retrieve the system call arguments from.
	- make the system call using the specific sys call number
- The application can pass args to the system call by
	- passing the args to the OS (directly)
	- Setting the args in registers and passing the addresses to the system call (indirectly)
	- Combinations of these 2 are allowed
- System call modes
	- synchronous mode, where the application/process waits until the system call completes.
	- There's also an asynchronous mode, covered later.

## Crossing the User/Kernel Protection Boundary

**User/Kernel Transitions** are a necessary step during application execution. There is basically no point to applications without system calls. Don't forget that even just creating a C `struct` REQUIRES a `malloc`, which is a system call.

The underlying system hardware must support these **User/Kernel Transitions**. The hardware should **trap** instructions that applications are not allowed to execute, and trap requests to access memory that the applications don't own. The hardware should pass control to the Kernel/OS, who will then validate and approve/deny those requests.

This involves a number of instructions, which can take 50-100 nanoseconds on a 2GHz Linux machine. This also affects the hardware's ability to use the CPU cache, because the operations "switch the locality" of the instructions being executed.

These operations are _not cheap_.

> Instructor Note:
>
> Because context switches will swap the data/addresses currently in **cache**, the performance of applications can benefit or suffer based on how a context switch changes what is in **cache** at the time they are accessing it.
>
> A **cache** would be considered **hot** (fire) if an application is accessing the **cache** when it contains the data/addresses it needs.
>
> Likewise, a **cache** would be considered **cold** (ice) if an application is accessing the **cache** when it does not contain the data/addresses it needs -- forcing it to retrieve data/addresses from main memory.


## OS Services

An OS provides applications with access to underlying hardware. It does so by exposing services.
- scheduler, controls CPU access
- mem manager, self explanatory, handles memory address translation, isolation
- block device driver, handles storage devices
- file system
- etc

Windows and Unix have very different system call interfaces, but there are parallels between both as far as what functionality is supported.

![[./images/Pasted image 20220827152200.png]]

## Linux System Calls

- Reference: https://man7.org/linux/man-pages/man2/syscalls.2.html
- Also `man syscalls`

## OS Design

### Monolithic OS

- Every service that an OS could provide was part of the OS
- pros
	- everything included
	- compile time optimizations
- cons
	- customization
	- portability
	- manageability
	- maintainability
	- it's just software, all pains apply

### Modular OS

This is the more common/sensible approach today.

- The OS has basic services/APIs included by default.
- The OS specifies module interfaces
- modules then implement those interfaces, and then plug-in to those interfaces.
- You can dynamically install new modules.
- pros
	- maintainability
	- smaller footprint
	- less resource needs
- cons
	- indirection impacts performance
	- the OS has to offload work onto a separate module, which has overhead
	- maintenance is still an issue

### Microkernel

- The kernel does a little as possible
	- basic sys calls
	- address space mgmt
	- thread mgmt
- Other OS services are run as applications on top of the minimal kernel
- The Kernel brokers communication between those applications "inter process communications (IPC)"
- pros
	- super small size
	- easier to verify the OS code
	- useful for embedded
- cons
	- questionably portable
	- limited inherent code sharing between different OS services
	- increased frequency of user/kernel crossings, which impacts performance
	- Not a great model for a general purpose operating system

## Linux Architecture

![[Pasted image 20220827154138.png]]

![[Pasted image 20220827154304.png]]

## MacOS Architecture

MacOS uses more of a microkernel approach, apparently. It runs BSD, but as a user-application.

![[Pasted image 20220827154904.png]]
