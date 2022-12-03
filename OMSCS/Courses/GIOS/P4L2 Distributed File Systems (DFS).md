---
tags: OMSCS, GIOS, DFS
---
# P4L2 Distributed File Systems (DFS)

## Overview
- DFS design and implementations
- Networked File System (NFS)
- Sprite File System

Supplemental materials
- [[P4L2 Caching in the Sprite File System.pdf]]

Distributed file systems are like distributed storage facilities
- They need to have a well-defined interface, i.e. access via VFS
- The need to focus on maintaining a consistent state
	- tracking state
	- file updates
	- cache coherence
- Should support mixed distribution models
	- replication
	- partitioning
	- peer-like systems

Modern operating systems hide the fact that a file system can store files in more than one storage device. They can also hide the fact that some of the files don't even exist on a local storage device. This is exposed via a file-system interface, which can has an abstracted VFS interface.

![[Pasted image 20221203120800.png]]

From the client machine's perspective, there's still only one file system, where some files have higher latency than others. From a systems design perspective, this is a distributed system.

## DFS Models
- client and server on different machines
- file server is distributed on multiple machines
	- replicated? (each server has all files)
	- partitioned? (each server has a partition i.e. subset of the files)
	- both? (files are partitioned, the partitions are replicated)
- files are stored on and served from all machines (peers)
- blurred distinction between clients and servers

## Remote File Service: Extremes
### Extreme 1: Upload/Download model
- File moved to the client
- Accesses are done on the client
- Client uploads the file back to the server
- local reads/writes on client are more performant
- entire file download/upload even for small accesses/changes
- server gives up control of the files
- Examples: FTP, SVN

![[Pasted image 20221203121611.png]]

### Extreme 2: True Remote File Access
- server performs file I/O on behalf of the client
- nothing is done locally
- file stays on the server
- file accesses are centralized, easy to maintain consistency
- every file operation pays network costs
- poor performance on readonly files
- limits server scalability

## Compromise
> A more practical remote file access, with caching

1. Allow clients to store parts of files locally (blocks)
	- low latency on file operations
	- server load reduced
	- more scalable
2. Force clients to interact with the server (frequently)
	- Clients need to notify server of file modifications
	- Clients need to listen the server for information about modifications made by other clients
	- Server has insights into what clients are doing
	- Server has control over which accesses can be permitted
	- Easier to maintain consistency
	- Server more complex, requires different file sharing semantics
	- Clients more complex

## Stateless v. Stateful File Server
### Stateless
- cannot support the "practical" model
- keeps no state about clients
- every request has to be self described and self contained
- cannot support caching and consistency management
- every request has to be self-contained, meaning more bits are transferred per request
- no resources are used on the server side to maintain state (CPU/RAM)
- on failure? just restart.

### Stateful
- needed for "practical" model to track what is cached/accessed
- can support locking, caching, incremental operations
- on failure, need checkpointing and recovery mechanisms
	- rebuild state?
	- keep on-disk state?
- overheads to maintain state and consistency
- depends on caching mechanism and consistency protocol

## Caching State in a DFS
- locally
	- clients maintain a portion of the state (e.g. file blocks)
	- clients perform operations on cached state (e.g. open/read/write)
	- requires coherence mechanisms

![[Pasted image 20221203123846.png]]

How/when does client1 find out that client2 changed `F`?
- SMP
	- How: write-update/write-invalidate
	- When: on write
- DFS
	- client/server -driven
	- on demand, periodically, on open

In a DFS, files can be cached
- in the client's memory
- in the client's file system (HDD/SSD/...)
- in a buffer cache in memory on the server
	- the OS should be doing this anyway
	- usefulness will depend on client load, request interleaving, access patterns

## File Sharing Semantics on a DFS
Whenever a file is modified by a process, the changed file is immediately available to other processes on that machine, even if the OS hasn't flushed the buffer cache back out to the disk, since all processes have access to that buffer cache.

![[Pasted image 20221203125459.png]]

In a DFS, that's not the case.

![[Pasted image 20221203125549.png]]

This is a classic distributed computing problem.
- Consistency
- Availability
- Partitionability

- UNIX semantics
	- every write visible immediately
	- ⬆C ⬆A ⬇P
- Session semantics
	- client writes-back file changes to server on `close()`
	- updates its cached file on `open()`
	- `open()` ... currently in a "session" ... `close()`
	- easy to reason, may not be sufficient
	- leads to long periods of inconsistency in the file system
	- server maintains, for each file:
		- current readers
		- current writers (possible to have concurrent writers)
		- version number, allows server/clients to reconcile conflicts when there's concurrent writers
- Periodic updates
	- client writes-back periodically
	- clients have a "lease" on cached data
		- Not an exclusive lock
	- server invalidates periodically
		- provides bounds on "inconsistency"
	- augmented with `flush()`/`sync()` API
- immutable files
	- never modify
	- new files created
	- files have versions
- transactions
	- all changes are atomic

## File vs Directory Service
> knowing the access patterns
- Too many options?
	- sharing frequency?
	- write frequency?
	- importance of consistent view?
- Optimize for the common case.

- File systems have 2 types of files
	- regular files
	- directories
- Choose different policies for each
	- e.g. session semantics for files, UNIX for directories
	- e.g. less frequent write-back for files than directories

## Replication vs. Partitioning
> Challenges of maintaining consistent state across multiple machines.

Can combine both techniques. 

### Replication
- each machine holds all the files
- load balancing, availability, fault tolerance
- writes become more complex
	- synchronously to all
	- or, write to one, propagate to others
- replicas must be reconciled
	- e.g. voting

### Partitioning
- each machine has a subset of files
- availability vs single server DFS
- scalability w/ file system size
- single file writes are simpler
- on failure
	- lose portion of data
	- load balancing becomes harder
	- if not balanced, some machines will be hotter than others

## Networked File Systems (NFS)
> clients access files over the network

![[Pasted image 20221203134410.png]]

- on open
	- NFS server creates a file handle
	- file handle returned to client machine
	- client tries to access file? internally the file handle is passed with every request
	- file deleted? attempts to use the file handle will result in a "file stale" result
- on write
	- ...
- on read
	- ...

### NFS: Versions
- NFS is from the 80s
- currently NFSv3 and NFSv4
- NFSv3 is stateless
- NFSv4 is stateful

caching semantics
- session-based semantics (non-concurrent)
	- close? changes flushed to server
	- open? client checks server for updated file data
- periodic updates
	- default: 3 sec for files
	- default: 30 sec for dirs
		- they generally don't change as frequently
		- easier to resolve conflicts
- NFSv4
	- delegation to clients for a period of time
	- avoids "update checks"

locking semantics
- lease-based, with an expiration time
- client's responsibility to release the locks when done or extend the lock duration
- NFSv4 also supports "share reservation", for reader/writer locking

## Sprite Distributed File System
> See [[P4L2 Caching in the Sprite File System.pdf]]

- Sprite was a "research DFS"
- People were using it at UCB
- great value in the explanation of the design process
- authors used trace data on usage/file access patterns to analyze DFS design requirements and justify decisions

### Access Pattern (Workload) Analysis
- 33% of all file accesses are writes
- 75% of files are open less than 0.5 seconds
- 90% of files are open less than 10 seconds
- 20-30% of new data deleted within 30 seconds
- 50% of new data deleted within 5 minutes
- file sharing is rare! Rarely do multiple clients read/write the same files.

### Analysis
- caching is ok, but write-through is not sufficient
- session semantics still too high overhead
- write-back on close not really necessary
- no need to optimize for concurrent access, but DFS/NFS must (should) support it.

### Design
- cache with write-back
	- every 30-sec, client will write back blocks that have NOT been modified for the last 30 seconds. Client may still be working on those blocks.
	- when another client opens the file, server will contact the client to retrieve those "dirty" blocks
	- This helps optimize the write operation
- open goes to the server
- **directories are not cached**
- on concurrent write, caching is disabled

### Sharing semantics
- sequential write sharing? caching and sequential semantics
- concurrent write sharing? no caching

### File Access Operations in Sprite
- $R_1$ ... $R_n$ readers
- $W_1$ writer
- all `open()` operations contact the server
- all clients cache blocks
- writer keeps timestamps for each modified block

Client, data per file
- cache? Y/N
- cached blocks
- timer for each dirty block
- version

Server, data per file
- readers
- writer
- version
- cacheable? Y/N

$W_2$ sequential writer shows up? sequential sharing
- server contacts last writer for dirty blocks ($W_1$)
- if $W_1$ has closed, update version
- $W_2$ can now cache the file

$W_3$ shows up while $W_2$ hasn't yet closed the file? concurrent sharing
- server contacts last writer ($W_2$) to retrieve dirty blocks
- since $W_2$ hasn't closed the file, caching is disabled for everybody
- server will now mediate all accesses for that file
- once one of the clients closes the file, the server will mark the file as cacheable again, which will improve performance for everybody. There was much rejoicing

