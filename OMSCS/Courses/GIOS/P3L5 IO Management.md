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
- What if files are one more than one device?
- What if device(s) work better with different FS implementations?
- What if files are not even on a disk? (Network or RAMDISK)
	- RAMDISK is so silly anyway.
	- The OS caches files when it has free memory.
	- Configuring your own ramdisk is reinventing the wheel

![[Pasted image 20221106112720.png]]

### VFS Abstractions
- file: elements on which the VFS operates
- file descriptors: OS representation of file
	- open, read, write, sendfile, lock, close
- inode: persistent representation of file "index"
	- "inode" == "index node"
	- list of all data blocks belonging to file
	- device, permissions, size
- dentry: "directory entry"
	- corresponds to single path component
	- Ex: `/users/austin`
		- `/`
		- `/users`
		- `/users/data`
		- All 3 of these are a "dentry"
	- OS/FS maintains a dentry cache
	- This is fully in memory, the disk doesn't maintain a list of dentrys. It's inferred from the files
- superblock: filesystem-specific information regarding the FS layout
	- filesystem metadata store
	- size & structure differ from FS implementation to FS implementation

### VFS on Disk
- file: data blocks on disk
- inode: tracks blocks belonging to the file
- superblock: overall map of disk blocks
	- inode blocks
	- data blocks
	- free blocks

## ext2: Second Extended Filesystem
- 2nd iteration of the `ext` file system.
- We're up to `ext4` these days
- partitioned into "block groups"
- The first block group (preceding block group 0) often contains the "boot" block, code that runs on computer startup
- Each block group contains
	- superblock
		- number of inodes
		- number of disk blocks
		- start of free blocks
	- group descriptor
		- bitmaps
		- number of free nodes
		- number of directories
	- bitmaps
		- track free blocks and inodes
	- inodes
		- indexed starting with 1
		- 1 per file
	- data blocks
		- contain the file data

![[Pasted image 20221106114818.png]]

## inodes
> index of all blocks corresponding to a single file

- files are identifed by an inode
- inode, lists all blocks plus other metadata
- file can be fragmented, not a problem on modern storage devices
- file is stitched together from each block
- last block doesn't contain an EOF. That's not necessary, the inode knows how long the file is.
- file system allocates free blocks to the file as it grows
- pros of this implementation
	- easy to perform sequential/random access
- cons
	- limits file size
	- Ex: 128B inode, 4B block pointer
		- 32 addressable blocks
		- 1kB block size
		- 32kB max file size

![[Pasted image 20221106114934.png]]

### Indirect inode pointers
- inodes with indirect pointers are an index of all disk blocks corresponding to a file
- inodes contain
	- metadata
	- pointers to blocks
		- direct block pointers, each pointer points to a block of data
		- indirect pointers, each pointer points to a block of pointers
		- double indirect pointers, each pointer points to a block of pointers to blocks
		- triple indirect, etc.
- example
	- 4B block pointer
	- 1kB blocks
	- Direct pointers
		- each entry can encode 1kB of file data.
	- Indirect pointers
		- each entry points to a 1kB block of block pointers
		- each block of block pointers encodes 1kB of 4B block pointers
		- each block contains 256 block pointers
		- $256*1kB=256kB$
		- each indirect block pointer points to 256kB of file data
	- Double indirect pointers
		- each entry points to a 1kB block of pointers to block pointers
		- 256 block pointers per block, means we just multiply the "indirect pointers" by the same amount
		- 256 pointers per dip block, 256 pointers per ip block, 1kB per data block
		- $256*256*1kB=64MB$

![[Pasted image 20221106132408.png]]

- Advantage of indirect pointers, small inodes can encode large file sizes
- Disadvantage, file access slowdown
	- assembling the entirety of a file results in multiple file reads
	- direct pointers, 2 disk accesses to retrieve a file block
	- indirect pointers, 3 disk accesses to retrieve a file block
	- double indirect pointers, 4 disk accesses to retrieve a file block
	- triple? 5 disk accesses

### Inode Quiz A
- block pointers are 4B
- disk block size is 1kB (1024 bytes)
- inode has following structure
	- 12 direct pointers
	- 1 single indirect pointer
	- 1 double indirect pointer
	- 1 triple indirect pointer
- pointers block per block = $\frac{1\frac{kB}{block}}{4\frac{B}{pointer}}=\frac{1024\frac{B}{block}}{4\frac{B}{pointer}}=256$ pointers per block
- 12 direct pointers
	- $12*1kB=12kB$ of file data referenced
- 1 single indirect pointer
	- $256*1kB=256kB$ of file data referenced
- 1 double indirect pointer
	- $256*256*1kB=64MB$ of file data referenced
- 1 triple indirect pointer
	- $256*64MB=16GB$ of file data referenced
- Total: $16GB+64MB+256kB+12kB\approx16GB$

**Note:** the units used here are actually in terms of $iB$, not $B$. Each scale change is in terms of 1024, not 1000.

### Inode Quiz B
- block pointers are 4B
- disk block size is 8kB (8192 bytes)
- inode has following structure
	- 12 direct pointers
	- 1 single indirect pointer
	- 1 double indirect pointer
	- 1 triple indirect pointer
- pointers block per block = $\frac{8\frac{kB}{block}}{4\frac{B}{pointer}}=\frac{8192\frac{B}{block}}{4\frac{B}{pointer}}=2048$ pointers per block
- 12 direct pointers
	- $12*8kB=96kB$ of file data referenced
- 1 single indirect pointer
	- $2048*8192B=16777216B=16384kB=16MB$ of file data referenced
- 1 double indirect pointer
	- $2048*16MB=32GB$ of file data referenced
- 1 triple indirect pointer
	- $2048*32GB=64TB$ of file data referenced
- Total: $\approx64TB$

**Note:** the units used here are actually in terms of $iB$, not $B$. Each scale change is in terms of 1024, not 1000.

## Disk Access Optimizations
- **caching/buffering**
	- used to reduce the number of disk accesses
	- files are cached in main memory
	- read/write are targeted against the cache
	- OS periodically flushes the file to the disk using `fsync()`
- **I/O scheduling**
	- reduces disk head movement
	- maximizes sequential vs random access
	- example: write block 25, write block 17, OS reorders instructions to write 17 first.
	- Not 
- **prefetching**
	- increases cache hits
	- leverages locality
	- example: read block 17 => also reads 18 and 19
- **journaling/logging**
	- reduce random access
	- "describe" write to I/O log: block, offset, value, etc
	- periodically applies updates to proper disk locations
	- `ext3` and `ext4` use journaling
