---
tags: OMSCS, GIOS, Processes
---
# P2L1: Process and Thread Management
The process is a key abstraction in OSes. This lesson covers
- what a process is
- how processes are represented by an OS
- how multiple concurrent processes are managed by an OS

## Simple process definition
A process is an instance of an executing program. Synonymous with "task" or "job". Using the toy shop visual metaphor, a process is like an "order of toys"
- There's a **state of execution**
- There's parts an a temporary holding area. Data, register state, etc
- May require special hardware, a la I/O devices

## What is a Process
The OS manages hardware on behalf of **applications**. An **application** is a program on disk, memory. An application is a **static entity**.

A **process** is a state of a program when executing loaded into memory. It's an **active entity**. Represents the execution state of an application. Processes don't have to be running, they could be in a state of waiting, or scheduled, but not actively running on a processor due to being de-prioritized.

A process encapsulates all of this data

| Process Data | Note                                         |
|:------------:| -------------------------------------------- |
|    stack     | Top of the program stack starts at $V_{max}$ |
|      🔽      |                                              |
|      🔼      | Depicted at contiguous, in reality is not    |
|     heap     |                                              |
|     data     |                                              |
|  text, code  | Bottom of program text starts at $V_0$       |

Every single element of a process's state needs to has to be uniquely identified by an address. The OS uses an address space to keep track of these address identifiers.

### Types of state
- text and data
	- static state when process first loads
- #heap
	- dynamically created during execution
	- in reality, this data may not be contiguous in memory
- #stack
	- grows and shrinks based on a Last In First Out (LIFO) queue.
	- dynamic
	- This component of process memory is used to keep track of the context for functions, so that when a function A makes a call to function B, the state of function A's execution can be restored when the control returns from function B.

### Process Address Space
- As a whole, the in-memory representation of a process is the "**address space**".
- A process refers to its memory addresses from 0 to MAX, which are the **virtual addresses**.
- The **physical addresses**, the actual locations of data in physical memory, are not exposed to the process.
- A **page table** is the mapping of virtual addresses to physical addresses. The OS manages this page table. Note that memory is allocated in chunks known as "pages". More on this later.

Processes are allowed a maximum amount of memory, represented by $V_{max}$ in our diagrams. Note that $V_{max}$ may even be greater than the total amount of memory and disk space available on the machine. This is a feature of the virtual address space growing the **stack** from the "top down" and the **heap** from the "bottom up". The process will not be able to access the data in between the "bottom of the stack" and the "top of the heap", because the OS has not yet allocated that memory to the process.

The OS dynamically decides where each physical address space resides in physical memory, and will translate that address into a process's page table, which defines the process's virtual address space. Those memory pages could even live on the disk, in the swapspace.

