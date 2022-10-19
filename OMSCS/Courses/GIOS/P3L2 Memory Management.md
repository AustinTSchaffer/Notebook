---
tags: OMSCS, GIOS, Memory
---
# P3L2: Memory Management

## Overview
- How an OS manages virtual and physical memory
- What are the mechanisms?
- OSes use intelligently sized containers for memory
	- AKA pages, AKA segments
	- OS allocates memory to processes using units of equal size
	- page/segment size can be tweaked
- Not all memory is needed at once
	- tasks operate on a subset of system memory
- Memory mechanisms are optimized for performance.
	- Reducing the time it takes to access state in memory improves performance for all processes.

## Memory Management
- reminder: OS manages physical resources (i.e. RAM) on behalf of processes
	- Physical memory locations have physical addresses
	- processes use virtual memory addresses, which the OS translates to physical memory addresses
	- virtual memory address spaces can be much larger than physical address spaces, thanks to swap
- OS must Allocate physical memory, and Arbitrate access to that memory
	- allocation involves allocation, replacement
		- OS has to track which memory is being used and which memory addresses are "free/available"
		- OS has to determine when to swap memory and which memory to swap
	- arbitration involves
		- address translation and validation

### Page-based memory management
- Virtual address space is page-based
- Physical address space uses page frames, which are the same size as virtual address pages
- Allocation involves mapping a virtual memory pages to physical page frames
- Arbitration involves keeping track of those pages via a page table

This is the dominant method for memory management.

### Segment-based memory management
- Allocation process doesn't use fixed size pages. Segments can vary in size
- Arbitration uses segment registers, supported by the hardware.

## Hardware Support for Memory Management
Hardware integrates memory mgmt mechanisms

![[Pasted image 20221016153549.png]]

CPU package has a **Memory Management Unit (MMU)**.
- translates virtual to physical addresses
- reports faults
	- illegal access
	- inadequate/insufficient permissions. Some memory can be designated as "write protected"
- page not found in memory? fetch it from the disk

**Registers**
- pointers to active page table
- base address of segments, size limits on segments, number of segments

**Cache:** Translation Lookaside Buffer (TLB) contains valid VA->PA translations

**Translation:** actual PA generation is done in hardware

Hardware dictates whether paging is supported, or if segmentation is supported, or if both are supported.

Actual allocation of memory is performed in software by the OS, i.e. determining which PAs are allocated to which processes. Replacement (aka swapping) policies are determined and controlled by the OS.

## Page Tables
- more popular method for memory management
- virtual memory pages and physical memory page frames are the same size
- page tables translate VAs to PAs, and are per-process data structures
- page tables are implemented as a "map" that tells the OS/hardware where to find a VA in Physical memory
- page tables translate the first address of a VA page to the first address of a PA page frame. The other addresses in the page are contiguous

![[Pasted image 20221016160259.png]]

Virtual address anatomy
- Contain a Virtual Page Number (VPN), and an offset
- The VPN is the index in the page table
- the offset is added to the result to get the physical address

Physical address anatomy
- contain a Physical Frame Number (PFN), and an offset
- the PFN is used to find the physical memory page frame. The rest of the addresses in the frame are contiguous.
- Used to locate a physical address in main memory

"allocation on first touch": Data is allocated semi-lazily, to make sure that page frames are only allocated the first time they're used.

Unused memory pages are "reclaimed". These are pushed onto the disk.

Page tables also contain a "valid bit", which determines whether the page frame is in main memory.
- If a process tries to access this memory, the hardware will fault and trap the instruction, and will pass control to the OS, so it can fetch the memory page frame from the disk.
- The memory page will likely be stored in a different page frame than the one that's recorded in the page table, so that will need to be updated too.

Note that they're per-process
- on ctx switch, OS needs to switch to the valid page table
- there's a hardware register that stores the address of the current page table, which the OS needs to update on ctx switch

### Page Table Entry
- Page Frame Number (PFN)
- Flags
	- Present (valid/invalid)
	- Dirty (written to)
	- Accessed (for read/write)
	- Protection bits (Read, Write, eXecute)

![[Pasted image 20221016163032.png]]

The MMU uses page table entries to validate access to pages
- PFN is used to generate PA and access it
- flags are used to generate error codes on kernel stack
- traps into the kernel

page fault handlers
- determine actions based on error codes and faulting address
- bring page from disk to memory?
- protection error? (SIGSEGV)

### Page Table Size
Page table has a known number of entries based on the number of virtual page numbers.

32-bit arch example
- Page Table Entry (PTE)
	- 4 bytes (32 bits) per PTE, including PFN and flags
- Virtual Page Number (VPN)
	- $2^{32}$ total addresses
- Page Size
	- 4kB ($2^{12}$ bits) (can be any size, 8kB, 2MB, 4MB, 1GB, etc.)
- Page Table Size = $\frac{2^{32}addresses}{2^{12}\frac{addresses}{PTE}} * 32\frac{bits}{PTE} = 4MB$
- 4MB PER PROCESS

64-bit arch example
- 8 bytes per Page Table Entry (PTE) (64 bits)
- $2^{64}$ total virtual addresses
- 4kB page size (configurable), means $2^{12}$ words are encoded per PTE. This assumes that each 8bit word is addressable.
- $\frac{2^{64}addresses}{2^{12}\frac{addresses}{PTE}} * 64\frac{bits}{PTE} = 32PB$
- 32PB PER PROCESS

A process likely will not use an entire address space. Even on 32-bit architectures, a process will likely not use all of the 4GBs of memory that can be referred to by their page table.

Page tables assumes an entry per VPN, regardless of whether the corresponding virtual memory is needed or not.

## Multi-Level Page Tables
Page tables have evolved from a "flat" page table map to a hierarchical page table map.

![[Pasted image 20221016165629.png]]

The **outer page table** or **top page table** is the **page table directory**. Instead of pointing to memory pages, the table points to smaller page tables.

The internal page table is only for **valid** virtual memory regions. If a region of memory is not being used by a process, the OS will not allocate a page table for that region of memory. On `malloc`, the OS _may_ allocate a new internal page table.

To account for this, the OS splits virtual addresses into 3 components
- $p_1$ the entry in the outer page table
- $p_2$ the PTE in the inner page table. This table is identified by the outer page table as $p_1$
- $d$ the page offset

![[Pasted image 20221016170148.png]]

This scheme can be extended to add additional layers. Each additional layer adds another directory that points to page table directories. This technique is important on 64-bit architectures. Page table requirements are larger, but address space of processes are more sparse, meaning larger gaps between allocated memory pages. Could samve more internal page table components.

### Multi-level PT tradeoffs
- Pros
	- smaller internal tables/directories
	- better granularity of coverage
	- reduced size of coverage
- Cons
	- more memory accesses are required for address translation
	- increased translation latency, increased memory access latency

### Quiz
![[Pasted image 20221016171658.png]]

#### Address Format 1
The full Page Table is initialized, always. The VPN is 6 bits. This means the table can hold $2^6$ PTEs. This means the OS always initializes 64 PTEs.

#### Address Format 2
- The outer page table takes a 2-bit indexer, meaning it can point to 4 different inner page tables.
- The inner page tables take 4-bit indexer, meaning each points to 16 different PTEs. When one of the inner page tables is initialized, the OS initializes 16 PTEs.
- Note that 12-bit addresses means that the OS can only support $2^{12}$ addresses per process. With 8-bit words, that means each process can access 4kB of memory, total, regardless of table structure.
- Each inner PTE encodes $2^{10}$ addresses, 1kB.
- With the proposed usage pattern, the OS can omit initializing the 3rd inner page table (Page Table $10_2$)

## Speeding Up Address Translation: TLB
Translating addresses introduces overhead. For each memory reference
- single level page table
	- 1 access to page table entry
	- 1 access to memory
- four-level page table
	- 4 access to page table entries
	- 1 access to memory

MMU uses a Translation Lookaside Buffer (TLB)
- MMU-level address translation cache
- on TLB miss, page table access from memory
- TLB contains protection/validity bits
- Even a small number of cached addresses can lead to a high TLB hit rate, when coupled with temporal and spatial locality

On an x86 Core i7
- per core
	- 64-entry data TLB
	- 128-entry instruction TLB
- 512-entry shared second-level TLB

## Inverted Page Tables
- Highest-end machines currently may have 10s of TBs of physical memory, when virtual memory systems can index PBs or even EBs.
- We can save space if virtual memory address spaces mirror the size of memory actually available on the machine.

Adding process ID (pid) to the logical address.

![[Pasted image 20221016173750.png]]

Problem, no clever search technique for finding a PID/p combo in the page table. Getting an entry from the page table is an `O(n)` operation, where `n` is the number of pages. The TLB will help, but not every time.

A hashing page table
- First component of the logical address is fed to a hash function
- The hash is used to lookup the PFN
- The hashes point to a linked list of PFNs, possible matches for the VPN.

![[Pasted image 20221016174442.png]]

## Segmentation
Using segments instead of pages for memory management

![[Pasted image 20221016174532.png]]

- segments have arbitrary granularity
- typically correspond to similar data components
	- e.g. code, heap, data, stack
- Addresses are a combination of a segment selector and an offset.
- segment is a contiguous physical memory location
- segment size = segment base + limit registers
- segmentation + paging
	- IA x86_32
		- segmentation + paging are supported
		- linux: allows up to 8k per process and 8k global segments
	- IA x86_64
		- segmentation is supported for backwards compatibility
		- paging is supported and recommended

![[Pasted image 20221016174724.png]]

## Page Size
- 10-bit offset? -> 1kB page size
- 12-bit offset? -> 4kB page size

On Linux/x86: 4kB is a common/default page size

| Common Name | Page Size | Offset Bits | Reduction Factor |
| ----------- | --------- | ----------- | ---------------- |
| Default     | 4kB       | 12 bits     | x1               |
| "large"     | 2MB       | 21 bits     | x512             |
| "huge"      | 1GB       | 30 bits     | x1024            |


Fewer bits are used to represent VPNs, which means you end up with a smaller page table when your page sizes are larger (benefit).

- Pros of larger page sizes:
	- few page table entries
	- smaller page tables
	- more TLB cache hits
- cons
	- internal fragmentation
	- wasted memory

Sometimes database servers make use of larger page sizes. I believe LTT's footage storage server makes use of non-default page sizes as well.

### Quiz
On a 12-bit arch, what are the number of entries in a single-level page table when the page size is 32 bytes? 512 bytes?

12-bit arch means $2^{12}$ bytes of addressable memory.

32-byte ($2^5$) page size? Pages required $\frac{2^{12}}{2^5}=2^7$ pages = 128 pages (and by extension, 128 PTEs)

512-byte ($2^9$) page size? Pages required $\frac{2^{12}}{2^9}=2^3$ pages = 8 pages (and by extension, 8 PTEs)

## Memory Allocation
OS has a memory allocator, subsystem of memory management system
- determines VA to PA mapping
- address translation, page tables
- simply determine PA from VA and check validity and permissions

Kernel-level allocators
- allocate kernel state
- allocate static process state (call stack, data, program instructions)

User-level allocators
- dynamic process state (heap)
- `malloc` and `free`
- Once the kernel allocates a memory page, and the page table that points to that page or page(s), the OS is no longer in the loop for managing data in those pages
- e.g. dlmalloc, jemalloc, Hoard, tcmalloc

## Memory Allocation Challenges
**External fragmentation:** This can occur when successive alloc and free calls cause the system to be unable to alloc a new contiguous block, even when there's enough total free memory, due to the free memory not being contiguous.

![[Pasted image 20221016182723.png]]

If the allocator has information about upcoming requests, it could add gaps in between different contiguous blocks. This permits coalescing/aggregation of free areas.

![[Pasted image 20221016182910.png]]

## Linux Kernel Allocators
### Buddy Allocator
![[Pasted image 20221016205538.png]]
- start with $2^x$ area
- On request, recursively subdivide the area into $2^x$ chunks and find smallest $2^x$ chunk that can satisfy the request.
- On free, check "buddy" to see if the chunk can be aggregated into a larger chunk.

Fragmentation still occurs. Aggregation of free areas is fast.

Areas are powers of 2 to make starting addresses of "buddies" only differ by one bit.

### Slab Allocator
![[Pasted image 20221016205513.png]]

Linux also uses the Slab allocator in the kernel
- caches for common object types/sizes, on top of contiguous memory.
- Avoids internal fragmentation.
- External fragmentation is not an issue since the caches leave gaps perfectly sized for common object types/sizes.

## Demand Paging
virtual memory is much much larger than physical memory
- virtual memory pages are not always in physical memory
- physical page frames are saved and restored to/from secondary storage

demand paging is when pages get swapping in/out of memory and a swap partition (e.g. on the disk)

![[Pasted image 20221016210130.png]]

1. When a page is not in memory, the relevant bit in the page table is set 0.
2. If there's a reference to that page, the CPU will trap the instruction, the OS kernel will then handle the exception.
3. The OS will then issue an I/O operation to retrieve the page from the disk.
4. The OS will store the contents of that page in a free space in physical memory (possibly swapping it into the location of some other page, if there's no room).
5. The OS will update the page table accordingly. The original PA
6. Control is returned to the process.

Pages can be "pinned", which disables swapping. Can be useful when the OS is managing devices that require direct memory access.

## Page Replacement
- **When** should pages be swapped out?
	- page(out) daemon
	- when memory usage is above a threshold (high water mark)
	- when CPU usage is below a threshold (low watermark)
- **Which** pages should be swapped out?
	- pages that likely won't be used
	- history-based prediction
		- least-recently used (LRU). Access bit to track if a page was referenced.
		- least-frequently used (LFU)
	- Pages that don't need to be written out to disk. Dirty bit used to track if the page was modified.
	- Avoid non-swappable pages

**Linux Configurations**
- parameters to tune thresholds: target page count.
- categorize pages into different types
	- claimable
	- swappable
- "second chance" variation of LRU
	- takes 2 scans of pages before determining which page(s) to swap out.

## Copy on Write (COW)
MMU Hardware
- performs translations
- tracks access
- enforces protrection
- useful to build other services and optimization

On process creation
- copy entire parent address space
- many pages are static and don't change
- why make multiple copies of the same data?
	- map new VA to original page frames
	- write protect the original page (read only)
	- if pages are only read, saved memory and time
	- on write
		- page fault, copy the page
		- pay copy cost on demand and only if necessary

![[Pasted image 20221016211432.png]]

## Failure Management
### Checkpointing
- failure and recovery management technique
- periodically save process state
- failure may be unavoidable, but can restart from checkpoint, so recovery is much faster
- Simple approach
	- pause and copy
	- disruptive
- better approach
	- write-protect and copy everything once
	- copy diffs of "dirtied" pages for incremental checkpoints
	- rebuild process state from multiple diffs, or in the background, aggregate diffs

From checkpointing to...
- debugging
	- rewind-replay (RR)
	- rewind: restart from checkpoint
	- gradually go back to older checkpoints until error found
- migration
	- continue process on another machine
	- disaster recovery
	- consolidation: reduce fragmentation of compute resources
	- repeated checkpoints in a fast loop until pause-and-copy becomes acceptable (or unavoidable)

The more frequently you checkpoint
- the more state that will be captured by the checkpoint
- the faster you'll be able to recover from potential faults, if the cost of combining incremental checkpoint diffs is lower than the cost of rerunning the process for X amount of time.
- the higher the overheads of the checkpointing process

## Summary
- Virtual memory abstracts a process' view of physical memory
- page-based and segment-based memory management
- allocation and replacement strategies for memory chunks
- checkpointing