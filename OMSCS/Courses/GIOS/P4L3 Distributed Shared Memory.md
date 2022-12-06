---
tags: OMSCS, GIOS, Distributed
---
# P4L3: Distributed Shared Memory

## Overview
- Distributed State Management (DSM) and design alternatives
- consistency models

> Managing distributed shared memory is like managing tools/parts across all workspaces in a toy shop.

- must decide placement
	- place resources close to relevant workers
	- place memory pages close to relevant processes
- must decide migration
	- must move resources as soon as possible to relevant workers
	- when to copy memory pages from remote to local
- must decide sharing rules
	- how long can resources be kept?
	- when are they ready?
	- how to store?
	- ensure memory operations are properly ordered

## Reviewing DFS Systems
> mfw "ATM Machine". DFSs looked weird too.

Callback to distributed file systems
- clients
	- send requests to service to interact with data/state (files)
- servers
	- own and manage data/state (files)
	- provide service (file access)
- caching
	- improve performance (seen by clients) and scalability (supported by servers)

The previous lesson didn't talk about situations where...
- there's multiple servers
- peer-to-peer distributed file systems (client == server)

This lesson will talk about some of these concepts

## "Peer" Distributed Applications
> This is not Peer-to-peer. Some nodes may perform management tasks for the entire system.

In current distributed computing applications, state is distributed across the compute nodes. Each node...
- ... "owns" some portion of the state
- ... runs some subset of the service
- ... is a peer of all other nodes

![[Pasted image 20221204190722.png]]

Examples:
- big data analytics
- web searches
- content sharing
- distributed shared memory (DSM)

## Distributed Shared Memory (DSM)
Each node...
- "owns" state (memory)
- provides service
	- memory reads/writes from any node
	- consistency protocols

- permits scaling beyond one single machine's memory limits
- more "shared" memory at lower cost
	- pricing for memory capacity can be non linear 📈
	- if you can shard/partition your memory across multiple nodes, you can optimize your VM sizes for cost
- slower overall memory access
- **commodity interconnect technologies** support this architecture
	- helps ensure low latency between nodes in the system
	- example: remote direct memory access (RDMA)
	- https://en.wikipedia.org/wiki/Remote_direct_memory_access

## Hardware vs Software DSM
### Hardware-Supported
![[Pasted image 20221204192025.png]]

- relies on interconnect
- OS manages larger virtual->physical memory mappings
- NICs translate remote memory accesses to messages
- NICs involved in all aspects of memory management, including some atomic operations
- this type of hardware is expensive. super computing platforms mostly.

### Software-Supported
- everything done by software
- supported by OS, or the language runtime

### Hybrid
Supplemental material:
- [[P4L3 DSM Concepts and Systems.pdf]]
- [[P4L3 DSM Concepts and Systems]]

## DSM Design: Sharing Granularity
- cache line granularity?
	- overheads too high for DSM
- variable granularity
	- programmer can define which variables should be shared
	- still potentially too high overhead
- page granularity
	- OS-level, OS manages sharing pages with the rest of the nodes
- object granularity
	- software-level, language runtime
	- OS doesn't require modification
	- less-general solution

Picking a higher level granularity amortizes costs of sharing changes with other nodes.

Important problem: beware of false sharing.
- Process A on Node A only writes to `x`
- Process B on Node B only writes to `y`
- if `x` and `y` are on the same page, and page-level granularity is used, the OS will share copies of `x` from A to B and copies of `y` from B to A, when no transfers are needed.
- Big question, what is actually "shared state"? How does the system avoid unnecessary transfers between nodes?
	- compilers might help, but we're already relying on compilers maybe too much
	- programmers need to better isolate shared state and unique state.

## DSM Design: Access Algorithms
Application access algorithm
- single reader / single writer (SRSW)
- multiple readers / single writer (MRSW)
- multiple readers / multiple writers (MRMW)

Most DSMs focus on MRMW, since it's the most general case.

## DSM Design: Migration vs Replication
Important DSM performance metrics: access latency

Achieving low latency through...
- Migration: Move data from one node to another when the other node need access to the data.
	- makes sense for SRSW
	- requires data movement
- Replication: state is copied across multiple/all nodes (caching)
	- more general
	- requires consistency management
		- overhead of maintaining consistency is proportional to the number of copies that need to be managed
		- limiting the number of replicas should help reduce overhead
	- for many concurrent writes, overheads may be too high

## DSM Design: Consistency Management
> DSMs ~ shared memory in Shared Memory Processors (SMPs)

In SMP
- write-invalidate
- write-update

coherence operations are triggered on each write
- overheads of supporting that in a DSM would be too high

- push invalidations when data is written to...
	- proactive approach
	- eager
	- pessimistic
	- nodes rush to alert other nodes of changes
- pull modification info periodically or on-demand...
	- periodically: (proactive-ish)
	- on-demand (reactive)
	- lazy
	- optimistic
	- nodes don't 

when methods get triggered depends on the consistency model for the shared state.

## DSM Architecture
### Page-based DSM Arch
- distributed nodes, each w/ own local memory contribution
- pool of pages from all nodes
- each page has ID, page frame number
- ID referred to as the "home node"
- if MRMW
	- need local caches for performance (latency)
	- home (or manager) node drives coherence ops
	- all nodes responsible for part of distributed memory (state) management
- "Home" node
	- keeps state: pages accessed, modifications, caching enabled/disabled, locked...
	- tracks current "owner" (owner may not equal home node)
- Explicit replicas
	- for load balancing, performance, or reliability
	- "home"/manager node controls management

![[Pasted image 20221204201254.png]]

## Indexing Distributed State
Each page (object) has...
- address = node ID + page frame number
- node ID = "home" node

Global map (replicated)
- object (page) ID => manager node ID
- manager map is available on each node in the system
- object ID = index into mapping table => manager node

Metadata for local pages (partitioned)
- per-page metadata is distributed across managers

Possible to change the manager for a particular page
- node down
- system rebalancing

## Implementing DSMs
Problem: DSM must "intercept" accesses to DSM state
- to send remote messages requesting access
- to trigger coherence messages

Overheads should be avoided for local, non-shared state (pages). Dynamically "engage" and "disengage" DSM when necessary.

Solution: Use Hardware MMU support!
- trap in OS if mapping invalid or access not permitted
- remote address mapping => trap and pass to DSM to send message
- cached content => trap and pass to DSM to perform necessary coherence operations
- other MMU information is useful
	- e.g. dirty pages

For object-level granularity
- consider similar types of structure
- you can try to bootstrap it on top of the OS-level services
- try to implement all of those structures in pure software

## What is a Consistency Model?
Consistency model is an agreement between memory/state and upper software layers

> Memory behaves correctly if and only if software follows specific rules.

Memory (state) guarantees to behave correctly...
- access ordering
- propagation / visibility of updates
- mutexes, locking, atomic operations
- software must use specific APIs to avoid subverting the rules

### Notation
- $R_{m1}(x)$: "X was read from memory location $m1$"
- $R_{m1}(y)$: "Y was written to memory location $m1$"
- initially all memory set to 0

### Strict Consistency
> changes visible everywhere immediately

In practice
- even on single SMP, no guarantees on order w/o extra locking and synchronization
- in distributed systems, latency and message reorder/loss make this even harder...
- This is actually impossible. See CAP theorem.

### Sequential Consistency
> Memory updates from different processors may be arbitrarily interleaved. ALL processes will see the same interleaving. Operations from the same processes will always appear in the order they were issued.

![[Pasted image 20221204205355.png]]

- It's ok to let one process see that M2 was updated before M1 was updated.
- ...but it's NOT ok for another process to simultaneously see that M1 was updated before M2 was updated.

![[Pasted image 20221204205953.png]]

### Causal Consistency
> Causally related writes are ordered. There are no guarantees about "concurrent" writes. Writes performed on the same processor are shown to other nodes in the same order they're performed.

![[Pasted image 20221204210647.png]]

This is fine in this mode, because the update to M1 doesn't affect the update to M2.

![[Pasted image 20221204210822.png]]

This is not fine, because there is an implied causal relationship from the value of M1 to the value of M2.

![[Pasted image 20221204213007.png]]

This is now OK. M1 is always shown as updated before M2.

### Weak Consistency
> Consistency guarantees immediately following a synchronize operation. No guarantees otherwise.

![[Pasted image 20221205171357.png]]

**Synchronization points**
- operations that are available (R, W, Sync)
- all updates prior to a sync point will be visible
- no guarantee what happens in between

In the diagram above, there's no guarantee that P2 will see that M1 was set to `x` by P1. P2 has to perform its own synchronization in order to see that value.

![[Pasted image 20221205171924.png]]

**Variations**
- single sync operation (Sync)
- separate sync per subset of state (Sync page)
- separate "entry/acquire" vs "exit/release" operations

This helps prevent unnecessary data movement and coherence operations, but needs to maintain extra state for these additional operations.

### Additional Examples
![[Pasted image 20221205172359.png]]

- This trivial example is sequentially consistent.
- This example is also strictly consistent, which is the ideal case, but not achievable on highly distributed systems.

![[Pasted image 20221205172657.png]]

- Notes
	- M1's value doesn't affect M2's value
	- M2's value affect's M3's value
	- P3/P4 don't require M3's value
- This example is causally consistent
- This example is also sequentially consistent
	- Both processes see that M2's value was updated before M1
	- No processes see M1's value updated before M2.
	- This example would not be sequentially consistent if P4 saw `M1 == x` while P3 sees `M1 == 0`

![[Pasted image 20221205173337.png]]

- Notes
	- M1's value doesn't affect M2's value
	- P1 uses M2's value to affect M3's value. M3 depends on M2.
	- P3 and P4 require both M2 and M3
	- P3 sees that M2 and M3 were updated to `y` and `z`. These changes were performed by P1.
	- P4 sees that M3 is `z`, but sees that M2 is `0`
- This is **not causally consistent**. If it were causally consistent, P4 should be able to see that M2 is set to `y`, since it sees that M3 is set to `z`.
- This is also **not sequentially consistent**. P3 sees that M2 was updated, then checked M3 and also saw that it was updated. At the same time, P4 saw that M3 was updated, but M2 was not updated.

![[Pasted image 20221205174310.png]]

- This is weakly consistent, but isn't any other kind of consistent. P2 and P3 didn't perform a Sync before reading, so there's no guarantees about the consistency of the values M1 and M2 seen by P2 and P3.