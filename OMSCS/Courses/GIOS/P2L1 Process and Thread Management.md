---
tags: OMSCS, GIOS, Processes
---
# P2L1: Process and Thread Management

## Overview
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

### Process Execution State
> How does the OS know what a process is doing?

Before applications can execute, their source code must be compiled.

At any given point in time, the CPU must know where in the list of instructions a process is currently executing. This address is supplied to the **Program Counter**. The Program Counter is maintained on the CPU in a register. There are other registers maintained on the CPU for status info, etc. This is part of the state of the process.

The top of a process's stack is defined by the stack pointer. We need to know the topic of the stack because of its LIFO behavior. The stack pointer ensures that the CPU can find the data that is relevant to the process's current execution.

There's other information that help the OS know what a process is doing.

The OS maintains a **Process Control Block** (PCB) to keep track of this information across all of the processes that it is scheduling and running.

### Process Control Block (PCB)
A PCB is a data structure that the OS maintains for each process under it's purview.

![[Pasted image 20220924215842.png]]

- This structure is created when a process is created. When a process requests more memory, it will be reflected in the PCB.
- The Program Counter (PC) is stored in the PCB, but changes on every single instruction. It would be unworkable if the OS had to update the PC every time a process executes a single instruction.
	- The CPU has a dedicated register that keeps track of the PC, along with other registers that keep track of other items that change quickly, and automatically updates them at the hardware level.
	- It's up to the OS to collect and save that information to the PCB whenever the processes is no longer being actively executed on the CPU.

### Context Switching
- When an OS decides to make one process idle, it must gather data from a CPU's registers and store it in the process's PCB.
- When an OS decides to restore another process, it has to load values from the process's PCB into the CPU's registers, so the CPU can begin/resume executing that process's instructions.

![[Pasted image 20220924220952.png]]

**Context Switching** is the mechanism that the OS uses to switch the CPU from the context of running one process to the context of running another process.

This operation is expensive!
- **direct costs**: number of cycles required to store and load instructions
- **indirect consts**: COLD cache! cache misses. Accessing a CPU's cache is way faster than accessing main memory. Pretty much 0% chance that 2 processes share data that would live in the same memory pages that are loaded into the cache.

The OS needs to limit how frequently it's context switching in order to keep the cache HOT. When the cache is HOT, the CPU is performing at its best. Context Switching effectively kills that momentum.

Sometimes the OS has to context switch anyway. P.S. a "hot cache" actually is hot temperature-wise. The OS/hardware have to manage that too, but that's beyond the scope of this document.

### Process Lifecycle
Processes can be **running** or **idle**, but also any of these other states:

![[Pasted image 20220924222025.png]]

- **new** processes, resource/PCB initialization and allocation
- processes have to be **admitted** into the ready state
- they have to wait in a **ready** state until the OS's scheduler decides to dispatch the process to the **running** state
- **running** processes can be **interrupted** back to **ready** or **exited**/**terminated**
- **running** processes could also enter a state where they need to **wait** on I/O or some other event, this puts them into the **waiting** state until the event is completed. This will put them back in the **ready** state.

### Process Creation
Processes can create child processes, resulting in a process tree structure. Most OSes have a "root" process, which is the parent of all other processes.

| OS             | Root Process |
| -------------- | ------------ |
| Android        | `zygote`     |
| Linux (Kernel) | `kthreadd`   |
| Linux          | `init`       |

There's two basic mechanisms for creating processes

- **fork**
	- copies the parent PCB into a new child PCB
	- parent and child both continue their execution after the `fork()` call
	- when writing `fork()` code, you need to keep in mind that your code is now managing 2 identical processes, and needs to distinguish between them.
- **exec**
	- replaces the child image
	- loads a new program and starts that program from its first instruction

### Length of a Process
How long should a process run? How frequently should we run the scheduler?

The longer we run a process, the less frequently we're wasting time running the scheduler. Always remember that the OS is enabling real work to be done. The OS operating its services is self-serving and isn't "real work".

Useful CPU work = total processing time ($T_p$) / total time ($T$)

$T = T_p + T_{scheduler}$ 

If scheduler time approaches processing time, then only 50% of the CPU time is doing useful work.

However if we don't run the scheduler, the OS can only run as many processes as there are CPU cores ($N$), and the first $N$ ones are the only ones that get to run.

### I/O Considerations
How does I/O factor into scheduling?

![[Pasted image 20220924224605.png]]

The OS manages how processes access resources on the hardware platform. When a process makes an I/O request, it will have to enter the I/O queue for I/O resources, then it has to enter the **waiting** state while the I/O request is processed by the hardware. Once the I/O request is met, the process can enter the ready queue. If there's no other processes in the ready queue, we can move the process directly to **running**.

### Process Ready Queue
There's a lot of cases where a running process can enter the ready state.

![[Pasted image 20220924224921.png]]

### The Scheduler's Job
The scheduler is responsible for
- maintaining the process ready queue
- deciding when to context switch and move processes into and out of the running state.

The scheduler is _not_ responsible for
- maintaining the I/O queue
- deciding when to generate an event that a process is waiting on

### Inter-Process Communication
Processes can interact with each other. The OS must support this interaction and mediate those communications between processes. Most modern applications are structured as multi-process applications.

The OS has Inter Process Communication (IPC) mechanisms. #IPC mechanisms can
- transfer data/info between address spaces
- maintain protection and isolation that OSes enforce
- provide flexibility and performance to those IPC

#### Message-Passing IPC
- OS provides communication channels, like shared buffers
- processes interact with these channels by:
	- write (`send`)
	- read (`recv`)
- Pro: OS managed
- Con: Overhead

#### Shared-Memory IPC
- OS establishes a shared channel and maps it into each process address space
- processes directly read/write those memory addresses
- OS is out of the way!
- Pro: Performance
- Con: Obviously this would be insane for a number of application-development reasons, unless it's used in the context of a multi-threaded application.
	- Error prone
	- devs have to re-implement memory sharing code that could already be handled fairly efficiently via network I/O or system calls.

