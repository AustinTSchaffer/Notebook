---
tags: Linux, OMSCS, CS6200, GIOS
---

# The Linux Programming Interface
> Notes taken while working through the book: "The Linux Programming Interface"

A lot of the people that have taken this class highly recommend using this book as a study guide for this course.

## OS vs Kernel
The term _operating system_ is commonly used with two different meanings:
- To denote the entire package consisting of 
	- the central software managing a computer’s resources
	- all of the accompanying standard software tools, such as command-line interpreters, graphical user interfaces, file utilities, and editors
- More narrowly, to refer to the central software that manages and allocates computer resources (i.e., the CPU, RAM, and devices).

The term _kernel_ is often used as a synonym for the second meaning.

It is possible to run programs on a computer without a kernel, but the kernel makes it way easier. Since the kernel manages the limited resources of the computer, programs don't need to do that individually, nor coordinate among themselves.

## The Kernel's Role
The Kernel handles:
- **Process Scheduling:**
	- A computer has one or more central processing units (CPUs), which execute the instructions of programs.
	- Linux is a _preemptive multitasking_ operating system, _Multitasking_ means that multiple processes can simultaneously reside in memory and each may receive use of the CPU(s).
- **Memory Management**
	- Linux employs virtual memory management. Advantages:
		- Processes are isolated from one another and from the kernel, so that one process can’t read or modify the memory of another process or the kernel.
		- Only part of a process needs to be kept in memory, optimizing memory usage. More processes loaded means better CPU utilization, due to an increased likelihood that there is usually at least one process the CPU(s) can execute.
- **Provision the File System**
- **Creation and termination of processes**: The kernel can load a new program into memory and provide it with resources. This is called a _process_. Once a process has completed execution, the kernel ensures that the resources it uses are "freed" for reuse.
- **Access to devices**: `/dev` and drivers and arbitrating multiple programs and their access to devices
- **Networking**: The kernel transmits and receives network messages (packets) on behalf of user processes. This task includes routing of network packets to the target system.
- **Provision of a system call application programming interface (API)**: Processes can request the kernel to perform various tasks using kernel entry points known as _system calls_.

In addition to the other features that provide process isolation, multiuser operating systems such as Linux generally provide users with the abstraction of a _virtual private computer_. Each user can log on to the system and operate largely independently. Each user can have resource allocations on a per-user basis.

## Kernel vs User modes
The Kernel has privileged access to memory. User programs can only access memory in the "user space", while the kernel can access memory in the "user space" as well as in a special "kernel space". This can be (is) referred to as "supervisor mode". Hardware instructions allow the processor to switch between these 2 different modes.

Examples of kernel-mode-only operations:
- executing the halt instruction to stop the system
- accessing memory-management hardware
- initiating device I/O operations

## Process versus kernel views of the system
Processes generally don't concern themselves with other processes. They also don't know when they'll be scheduled, timed out, and resumed.

The delivery of signals and other interprocess communication is mediated by the kernel. The process doesn't know the timing on that either, generally speaking.

Processes don't know the physical addresses that map to their virtual addresses. They also don't know if a virtual address is mapped to the swapspace. They also don't know where in RAM the _process itself_ is stored.

