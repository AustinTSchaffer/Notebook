---
tags: GIOS, OMSCS
---

# Introduction to OSes

## Simplest OS Definition

An OS is a piece of software that
- **abstracts** the use of a computer system
- **arbitrates** the use of that computer system

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

[(Continue on P1L2: video 11)](https://gatech.instructure.com/courses/270294/pages/11-os-protection-boundary?module_item_id=2665738)
