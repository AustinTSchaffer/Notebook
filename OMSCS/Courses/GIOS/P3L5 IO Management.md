---
tags: OMSCS, GIOS, I/O
---
# P3L5: I/O Management

## Overview
- Lesson covers OS support for I/O devices
- the "block device" stack
- "file system" architecture

There is no supplemental paper for this module.

> I/O is like the shipping department in a toy shop.

- has protocols
	- how/what "parts" come in
	- how/what "toys" come out
- have dedicated handlers
	- device drivers
	- interrupt handlers
- decouples I/O details from core processing

## I/O Devices
- USB
- Ethernet/Wifi (network)
- Disk
- human interfaces
	- keyboard
	- screen
	- mouse
	- microphone
	- camera

- input
	- keyboard
	- microphone
- output
	- speaker
	- display
- both
	- network interface card (NIC)
	- flash card
	- hard disk drive

### Basic I/O Features
Any device can be abstracted to have the following core features

![[Pasted image 20221106100703.png]]

- control registers
	- command registers
	- data transfer registers
	- status registers
- internals
	- microcontroller (device CPU)
	- on-device memory
	- other logic
		- example: analog to digital converters

## CPU-Device Interconnect
> Devices interface with the rest of the system with a controller.

- Platforms have a Peripheral Component Interconnect (PCI)
- Modern platforms have PCI Express (PCIe)
	- Previous iteration: PCI-X (PCI Extended)
	- Previous iteration: PCI
- Other types of interconnects
	- SCSI bus
	- peripheral bus
	- bridges handle differences

![[Pasted image 20221106100858.png]]

## Device Drivers
- The modules that plug in to OSes to handle/control devices
- There is a driver per each device type
- responsible for device access, management, and control
- provided by device manufacturers per OS/version
	- printers for example
- each OS standardizes interfaces for driver developers
	- some hardware can share drivers, depends on manufacturer
	- device independence
	- device diversity

![[Pasted image 20221106101236.png]]

## Types of Devices
**block/disk**
- read/write blocks of data
- direct access to arbitrary blocks

**character/keyboard**
- get/put character

**network devices**
- stream of data

Drivers should abstract the details of different devices within the category.

## Linux Device Directory

OS represents devices using special "device" file abstractions
- `/dev` on Linux
- Also `tmpfs`
- Also `devfs`
- not actually files
- support read/write operations

## Device Examples

- `/dev/null`: Where data goes to die
- `/dev/zero`: Infinite stream of zeros
- `/dev/random` and `/dev/urandom`: Infinite stream of random bytes. They have different blocking behavior, and different behavior on OS startup, but are otherwise equivalent. `/dev/random` is considered "legacy" by the man pages.

`/dev/zero` example usage:

```python
z = open('/dev/zero', 'rb'); z
# OUT: <_io.BufferedReader name='/dev/zero'>
z.read1(12)
# OUT: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

- `/dev/hda*` and `/dev/sda*`: Storage devices
- `/dev/tty*`: "talk to you" (Terminals)
- `/dev/lp*`: Line printer

## CPU Device Interactions
- access device registers, memory load/store
- memory-mapped I/O
	- part of "host" physical memory dedicated for device interactions
	- Base Address Registers (BAR)
	- callback to Jeff Geerling series on trying to get a graphics card running on a Raspberry Pi
- I/O port
	- dedicated in/out instructions for device access
	- target device (I/O port) and value in register
- Interrupt
	- device sends an interrupt to 
	- interrupt handling steps
	- can be generated as soon as possible
	- used when performance is a requirement
- Polling
	- CPU polls device, reading its status register
	- I/O occurs when convenient for OS
	- incurs delays and CPU overhead, resulting from checking statuses when no data is available
	- This is how USB works, it's a "host-initiated" communication protocol

## Device Access Options
- 

### Programmed I/O (PIO)
- no additional hardware support required
- CPU "programs" the device
	- via command registers
	- data movement
- NIC device as an example, handling for network packets
	- write command to command register(s) to request packet transmission
	- copy packet to data registers
	- repeat until packet is sent, data register size may be smaller than packet size
	- Example: 1.5kB packet; 8B registers or bus
		- 1 CPU store instruction for bus command
		- 188 CPU store instructions for copying data to register
		- 189 total CPU store instructions to send the packet
- This option is better when the data size and/or data transfer frequency is lower.

### Direct Memory Access (DMA)
![[Pasted image 20221106104251.png]]

- relies on DMA controller, specialized hardware
- CPU "programs" the device
	- via command registers
	- via DMA controller to communicate where the data is stored (pointers/length)
	- data can move in the opposite direction.
- NIC device as an example, handling for a network packet
	- write command to command register(s) to request packet transmission
	- configure DMA controller with physical memory address and the size of the packet buffer
	- Example: 1.5kB packet, 8B registers or bus
		- 1 store instruction
		- 1 DMA configure operation
	- fewer steps, but DMA config is more complicated
- For DMAs
	- data buffer must be in physical memory until transfer completes
	- Need to "pin" regions to mark them as "non-swappable"
- This option is better when the data size and/or data transfer frequency is higher.

## Typical Device Access
This is the typical flow of control whenever a process performs an I/O request via a system call.

- user process
	- sends data
	- reads file
- in-kernel stack
	- form packet
	- determine disk block
	- invokes device driver
- device-driver
	- write Tx request record
	- issue disk head move/read
- device
	- performs the request
- results propagate back up the stack

![[Pasted image 20221106104943.png]]

## OS Bypass
![[Pasted image 20221106105436.png]]

- It's not necessary to go through the kernel
- device regs/data are directly accessible by user process
- OS can grant/configure access to the process then stay out of the way
- This typically happens via "user-level drivers" aka "user-level driver libraries"
- OS retains coarse-grain control to prevent privilege escalation 
- relies on device features / sufficient registers, to grant/deny specific functionality
	- need to share user-level driver/library among multiple processes
	- Device needs to de-multiplex the request so it can determine the recipient of the results.

## Sync vs Async Access
> What happens to a calling thread?

![[Pasted image 20221106105911.png]]

### Synchronous I/O Operations
- process blocks, will be context switched off
- thread will become runnable when the response is available

### Asynchronous I/O Operations
- process is allowed to continue
- later
	- process checks and retrieves result (poll)
	- process is notified that the operation is completed and that the results are ready (interrupt)
- generally considered a better model for handling I/O

## Block Device Stack
- processes use files, which are a "logical storage unit"
- processes think about "files" in a "file system", not about disks/sectors
- Kernel file system (fs)
	- where are files 
	- how to find them
	- how to access them
	- OS specifies the FS interface
- generic block layer
	- OS standardized block device interface
	- sits between device drivers and the kernel
- device drivers
	- implements block device interface
	- controls hardware to store/receive file info
- devices
	- protocol specific APIs
- Block devices are the typical storage backend for file systems

![[Pasted image 20221106111041.png]]

## Block Device System Call
```c
int ioctl(int fd, unsigned long request, ...);
```

- programs can get block device info using the `ioctl` system call
- options for `request` are defined in the `linux/fs.h` header file
- typical 3rd argument is a pointer to define where the call should place results

## Virtual File System
> RAMDISK!!!!!!!!!!!!!!!
> People like \[ramdisk\].

- What if files are one more than one device?
- What if device(s) work better with different FS implementations?
- What if files are not even on a disk? (Network or RAMDISK)
- RAMDISK is so silly anyway.

![[Pasted image 20221106112720.png]]

