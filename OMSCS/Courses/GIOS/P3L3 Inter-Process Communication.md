---
tags: OMSCS, GIOS, IPC
---
# P3L3: Inter-Process Communication

## Overview
- Inter-process Communication (IPC)
- Shared Memory IPC

- Processes can share memory
	- data is placed in shared memory
- processes can exchange messages
	- messages can be passed via sockets
- IPC often requires synchronization
	- mutexes, waiting

IPC is a set of OS-supported mechanisms for interaction among processes. There's mechanisms for both coordination and communication.

- **Message passing:** sockets, pipes, message queues
- **Memory-based IPC:** shared memory, memory mapped files
- **Higher-level semantics:** files, RPC
- **Synchronization primitives:** mutexes

## Message-Based IPC (Message-Passing)

![[Pasted image 20221017201524.png]]

- `send`ing and `recv`ing of messages
	- send: system call + data copy
	- recv: system call + data copy
- OS creates and maintains a **channel**
	- buffer
	- FIFO queue
- OS provides interface to processes, a port
	- processes send/write messages to a port
	- processes recv/read messages from a port
- kernel required to...
	- establish communication
	- perform each IPC operation
- Request->response requires...
	- 4 user/kernel crossings
	- 4 data copies

- Cons
	- overheads
- Pros
	- simplicity: kernel does channel management and synchronization

### Pipes
- Pipes carry byte steams between 2 processes
- often used to connect output from one process to the input of another process

### Queues
- carry "messages" among processes
- OS management includes priorities, scheduling of message delivery
- APIs: SysV and POSIX

### Sockets
- most familiar among web devs
- `send()` and `recv()` pass message buffers
- `socket()` creates a kernel-level socket buffer
- associates necessary kernel-level processing (TCP/IP, ...)
	- If processes are on different machines, OS manages a channel between the process and network device(s).
	- If processes are on the same machine, the OS bypasses the full protocol stack.
	- OS is smart enough to find the most efficient route between processes.

## Shared Memory IPC
![[Pasted image 20221017202330.png]]
- processes `read` and `write` to a shared memory region
- OS establishes shared channel between the processes
	- physical pages are mapped into the virtual address spaces of 2 different processes
	- `VA(P1)` and `VA(P2)`, map to the same physical address
	- `VA(P1)` and `VA(P2)` WILL BE DIFFERENT
	- physical memory doesn't need to be contiguous. That never was guaranteed.

- Pros
	- system calls are only used for the setup phase
	- data copies potentially reduced (but not eliminated)
- Cons
	- explicit synchronization for shared memory operations
	- developer has more responsibility
		- communication protocol?
		- shared buffer management?

**APIs:** SysV, POSIC, memory mapped files, Android `ashmem`

## Copy vs Map
- Goal: Transfer data from one into target address space.

- Copy
	- CPU cycles to copy data to/from port
- Map
	- CPU cycles to map memory into address space
	- CPU to copy data to channel
	- set up once and use many times? good payoff
	- can perform well for 1-time use, and when there's a lot of data

Tradeoff exercised in Windows: "Local" procedure calls (LPC)

## Shared Memory Lifecycle

![[Pasted image 20221017203246.png]]

1. Create
	1. OS assigns unique key to the segment
	2. Processes can request access to the shared memory segment using the key.
2. Attach
	1. Map virtual->physical addresses
	2. Changes made to segment will be visible to all processes that have mapped the memory segment.
3. Detach
	1. invalidate addr. mappings
	2. Doesn't destroy the shared segment
	3. Processes can attach/detach the same segment multiple times
4. Destroy
	1. Only removed when explicitly deleted (or on system reboot)

### SysV Shared Memory API
> "System Five"

- segments of shared memory, not necessarily contiguous physical pages
- **shared memory** is system-wide. System limits on number of segments and total size.

- `shmget(shmid, size, flag)`
	- create or open
- `ftok(pathname, prg_id)`
	- same args? same key
	- One way for processes to receive the same key is to agree on shared memory configuration
- `shmat(shmid, addr, flags)`
	- `addr` can be `NULL` if it doesn't care
	- cast addr to arbitrary type
- `shmdt(shmid)`
	- Detach shared memory
- `shmctl(shmid, cmd, buf)`
	- Destroy shared memory segment with `IPC_RMID`

### POSIX Shared Memory API
https://man7.org/linux/man-pages/man7/shm_overview.7.html

- It's the "standard", but not as widely supported.
- Uses the "file" abstraction, instead of "segment", but doesn't actually use files.
- Uses a "file descriptor" instead of a "key"

- `shm_open()`
	- returns file descriptor
	- in "tmpfs"
- `mmap()` and `unmmap()`
	- mapping virtual to physical addresses
- `shm_close()` removes the file descriptor
- `shm_unlink()` deletes the data

## Shared Memory and Synchronization
> like threads accessing shared state in a single address space... but for processes.

Synchronization methods
- mechanisms supported by process threading libraries (pthreads)
- OS-supported IPC for synchronization

Either method most coordinate...
- number of concurrent access to shared segment
- when data is available and ready for consumption

### Pthreads for IPC Sync

- Must set `PTHREAD_PROCESS_SHARED` on the attr structs
	- `pthread_mutexattr_t`
	- `pthread_condattr_t`
- Synchronization data structs must be shared between processes.

```c
// shm data struct
typedef struct {
	pthread_mutex_t mutex;
	char *data;
} shm_data_struct, *shm_data_struct_t;

// create shm segment
//   - arg[0] is the process name
//   - 120 is "some integer parameter"
//   - 1024 means 1kB
seg = shmget(ftok(arg[0], 120), 1024, IPC_CREATE | IPC_EXCL);

// shm_address is the address.
shm_address = shmat(seg, (void *)0, 0);

// 
shm_ptr = (shm_data_strct_t)shm_address;

// create and init mutex
pthread_mutexattr_t(&m_attr);
pthread_mutexattr_set_pshared(&m_attr, PTHREAD_PROCESS_SHARED);
pthread_mutex_init(&shm_ptr.mutex, &m_attr);
```

**MAKE SURE MUTEX IS ALLOCATED IN THE SHARED MEMORY REGION.**

## Other IPC Sync
pthreads aren't necessarily always supported on every platform for managing access to shared memory.

### Message Queues
- implement "mutual exclusion" via send/recv
- P1 writes data to shmem, send "ready" to queue
- P2 receives msg, reads data, and sends "ok" message back

### Semaphores
- binary semaphores are essentially a mutex. They can be 0 or 1.
- if value is 0, stop/blocked
- if value is 1, decrement (lock) and proceed

### External Resources
- http://www.tldp.org/LDP/lpg/node21.html
	- SysV IPC Tutorials
	- has example source for SysV IPC
- http://man7.org/linux/man-pages/man3/mq_notify.3.html
	- `mq_notify()` man page
	- registers for notification when a message is available
- http://man7.org/linux/man-pages/man3/sem_wait.3.html
	- `sem_wait()` man page
	- locking a semaphore
- http://man7.org/linux/man-pages/man7/shm_overview.7.html
	- `shm_overview` man page
	- overview of POSIX shared memory

## IPC CLI Tools
- `ipcs`
	- list all IPC facilities
	- `-m` displays info on shared memory IPC only
- `ipcrm`
	- delete IPC facility
	- `-m [shmid]` deletes shm segment with given ID.

## Shared Mem Design Considerations
- different APIs/mechanisms for sync. Not the only decisions
- OS provides shared memory, and is out of the way
- data passing/sync protocols are up to the programmer
- "with great power comes great responsibility"

![[Pasted image 20221017211555.png]]

### How Many Segments?
- 1 large segment?
	- manager for allocating/freeing memory from shared segment
- many small segments?
	- use a pool of segments
	- maybe a queue with segment IDs
	- communicate segment IDs among processes

### What size segments?
What if data doesn't fit?

- segment size = data size?
	- works for well-known static sizes
	- NOTE: OS limits max segment size, which might be less than the data you want to send
- segment size < message size?
	- transfer data in rounds
	- include protocol to track progress
	- sync, data, flags

## Summary
- IPC using pipes, messages (ports), and shared memory.
- Memory-based vs message-based IPC