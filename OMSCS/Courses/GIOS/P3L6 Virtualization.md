---
tags: OMSCS, GIOS, Virtualization
---
# P3L6: Virtualization

## Overview
- Overview of virtualization
- main technical approaches in virtualization solutions
- virtualization-related hardware advances

Supplemental papers
- [[P3L6 Rosenblum and Garfinkel.pdf]]
- [[P3L6 Popek and Goldberg Paper.pdf]]

## Defining Virtualization
![[Pasted image 20221108190608.png]]

- A **virtual machine** is an efficient, isolated duplicate of the real machine
- VMs are supported by a **virtual machine monitor** (VMM)
	- VMM Goal: fidelity. virtualized hardware matches real hardware
	- VMM Goal: performance
	- VMM Goal: safety & isolation
- 3 main characteristics
	1. provides an environment that is essentially identical to the original machines
	2. programs show, at worst, only a minor decrease in speed. Virtualized resources should perform close to bare metal resources.
	3. VMM is in complete control of system resources. It determines if a VM should be given hardware access. The VM then shouldn't be able to control policies

## Examples
- Virtual Box is virtualization software
- The Java Virtual Machine is _not_ virtualization software. Despite the name, it's just a program runtime.
- Virtual GameBoy is not virtualization software. It's primarily emulation software.
- Containerization (Docker) is not virtualization. Containerization is isolation.

## Why Virtualization?
- Consolidation
	- run multiple VMs on one host
	- decreased cost
	- improve manageability
	- improve hardware utilization
- Migration
	- availability
	- reliability
	- VMs can be easily moved/cloned
- Security
- Debugging
- Support for legacy OSes

## History Lesson
Virtualization has been around since the 60's, but wasn't dominant. However
- mainframes weren't ubiquitous
- buying more machines was just cheaper

What changed?
- Servers were underutilized
- data centers were becoming too large since every new OS meant another piece of physical hardware. As a result
	- companies had loads of system admins
	- electrical bills were sky high (refrigeration mostly)

## Virtualization Models
### Bare-metal
> a.k.a. Hypervisor-based
>
> a.k.a. Type 1

- VMM (hypervisor) manages all hardware resources and supports execution of VMs
- privileged, secure VM deals with devices and other configuration/management tasks
- The privileged VM runs the device drivers
- Implementations
	- Xen (opensource or Citrix XenServer)
		- dom0 (privileged VM) and domU (Guest VM)
		- drivers run in dom0
	- ESX (VMware)
		- many open APIs
		- drivers in VMM
		- used to have Linux control core, now uses remote APIs

![[Pasted image 20221108202435.png]]

### Hosted
> a.k.a. Type 2

- Host OS owns all hardware and runs the drivers
- special VMM module provides hardware interfaces to VMs and deals with VM context switching
- Example: Kernel-based VM (KVM)
	- based on Linux
	- Linux host provides all hardware management
	- KVM kernel module + QEMU for hardware virtualization
	- QEMU virtualizer
	- leverages Linux's open-source community

![[Pasted image 20221108203255.png]]

### Implementations Summary
- Bare Metal / HyperVisor-Based implementations
	- VMware ESX
	- Citrix XenServer
	- Microsoft Hyper-V
- Host OS implementations
	- KVM
	- VMware Fusion
	- VirtualBox
	- VMware Player

## Virtualization Requirements
- Present virtual platform interface to VMs
	- virtualize CPU
	- virtualize memory
	- ... devices
	- etc
- Provide isolation across VMs
	- preemption
	- MMU for address translation and validation
- Protect guest OS from apps
	- cannot run guest OS and apps at same protection level
	- need separate protection levels for the guest OS and the apps running in that guest OS
- Protect VMM from guest OS
	- similar to isolation
	- prevent privilege escalation
	- cannot run guest OS and VMM at same protection level

## Hardware Protection Levels
- commodity hardware has more than 2 protection levels
- x86 has 4 protection levels (rings)
	- ring 3: lowest privilege (apps)
	- ring 0: highest privilege (OS)
	- Example usage of rings
		- ring 3: apps
		- ring 1: OS
		- ring 0: Hypervisor
	- x86 also has 2 protection modes
		- root
		- non-root
	- Example usage of rings+modes
		- non-root: VMs
			- ring 3: apps
			- ring 0: OS
		- root
			- ring 0: hypervisor
	- non-root modes have traps
		- `VMexit`
		- `VMentry`
		- These instructions switch between modes

![[Pasted image 20221108204550.png]]

## Processor Virtualization
### Trap-and-Emulate Model
- Guest instructions are executed directly by the hardware
- for non privileged operations: hardware speeds lead to efficiency
- privileged operations are trapped by highest privilege level (hypervisor)
- The hypervisor validates/authorizes privileged operations
	- **Illegal operation?** Terminate VM
	- **Legal operation?** emulate the behavior the guest OS was expecting from the hardware
- This is called "Trap-and-Emulate"

### Problems with Trap-and-Emulate
> x86 (Pre-2005)
- 4 rings, no root/non-root modes yet
- hypervisor was in ring 0, guest OS was in ring 1
- **17 privileged instructions did not trap and failed silently**
	- example: interrupt enable/disable bit in flags privileged register
	- POPF/PUSHF instructions that access it from ring 1 fail silently 
- Hypervisor doesn't know, so it doesn't try to change settings
- Guest OS doesn't know, so it assumes the change was successful
	- guest VM could not request interrupts enabled
	- guest VM could not request interrupts disabled
	- guest VM could not find out what is the state of the interrupts enabled/disabled bit

### Binary Translation
- **Main idea:** rewrite the VM binary to never issue those 17 instructions
- This principle was pioneered by Mendel Rosenblum's group at Stanford, and was commercialized as VMware. Rosenblum was awarded ACM Fellow. Credited for "reinventing virtualization".

- **goal:** full virtualization, guest OS is not modified
- **approach:** dynamic binary translation

You can't really statically (up-front), perform the translation before the VM is running.

1. Inspect code blocks to be executed
2. If needed, translate to alternate instruction sequence. Emulate desired behavior, possibly avoiding a trap
3. Otherwise, run the instructions at hardware speeds

Optimizations include
- caching translated blocks to amortize translation costs.
- only attempting to translate Kernel code, since application code doesn't/can't run those instructions.

### Paravirtualization
- **goal:** _performance_. Give up on unmodified guests.
- Approach is to modify guest OSes so they
	- know they're running virtualized
	- makes explicit calls to the hypervisor (hypercalls)
	- hypercalls are similar to system calls
		- package context info
		- specified desired hypercall
		- trap to VMM

Adopted and popularized by Xen. Originally open-source. Commercialized as XenSource. Acquired by Citrix.

## Memory Virtualization
### Full Memory Virtualization
- all guests expect contiguous physical memory, starting at `0`
- distinguish between 3 categories of addresses and page frame numbers
	- virtual (VA)
	- physical (PA)
	- machine (MA)
- This still leverages hardware MMU and TLB to prevent all address translation from happening in software; however,

#### Option 1: Tiered Page Tables
- guest page table maps VAs to PAs
- hypervisor maps PAs to MAs
- guest page table translation will still happen in software.
- **This is too slow! Too expensive!**

#### Option 2: Hypervisor Shadow Page Table
- guest page table maps VAs to PAs
- hypervisor establishes a shadow page table which maps VAs to MAs
- Hardware MMU uses the VA to MA page table
- Hypervisor maintains consistency between the page tables
	- invalidate on context switch
	- write-protect guest page table to track new mappings

### Paravirtualized Memory Virtualization
- guest aware of virtualization
- no longer strict requirement on contiguous physical memory addresses starting at 0
- explicitly registers page tables with hypervisor
- can "batch" page table updates to reduce VM exists\
- other optimizations

Overheads are eliminated (or at least reduced) on newer platforms.

## Device Virtualization
For CPUs and memory, there's less diversity between instruction set architecture (ISA). Interfaces are standardized. Virtualization knows which ISA it needs to support. Hardware manufacturers know which interfaces it needs to support.

For devices
- high diversity
- lack of standard specification of device interfaces and behavior

There's 3 key models for device virtualization.

### Pass-through Model
**Approach:** VMM-level driver configures device access permissions

- VM provided with exlusive access to the device
- VM can directly access the device (bypasses VMM)
- VM gets direct access to control registers or even BAR
- Device sharing is difficult. Too many bosses.
- VMM must have exact type of device as what VM expects. Launching the VM could cause the VM to crash if the device is removed.
- VM migration is trickier because the VM now has a dependency on an external resource.

![[Pasted image 20221108211904.png]]

### Hypervisor-Direct Model
**Approach:** VMM intercepts all device accesses.

The VMM emulates device operations.
- translate to generic I/O operation
- traverse VMM-resident I/O stack
- invoke VMM-resident driver

- VM decoupled from physical device
- Easier sharing, migration, dealing with device specifics
- VMware ESX uses this model
- Adds latency on device operations
- Device driver ecosystem must integrate with complexities in hypervisor

![[Pasted image 20221108213214.png]]

### Split-Device Driver Model
**Approach:** Device access control is split between
- front-end driver in guest VM (device API)
- back-end driver in service VM (or host)
- Guest drivers must be modified. This model is limited to paravirtualization 
- Eliminates emulation overhead.
- Allows for better management of shared devices.

![[Pasted image 20221108213504.png]]

## Key Virtualization-Related Hardware Features
Hardware companies responded to growing popularity of virtualization.

AMD Pacifica and Intel Vanderpool Technology (Intel-VT). Circa 2005.
- Closes holes in x86 ISA
- Modes: root/non-root (or "host" and "guest" modes)
- VM Control Structure (Control Block in AMD)
	- data structure
	- per vCPU. "walked" by hardware
- extended page tables and tagged TLB with VM IDs
- Multiqueue devices: device has multiple logical interfaces
- Better interrupt routing: interrupts can be routed to specific VMs
- Security support
- Management support
- Additional x86 instructions to exercise/perform all features above

## x86 VT Revolution
![[Pasted image 20221108215017.png]]

