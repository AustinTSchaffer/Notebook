---
tags: OMSCS, GIOS, 
---
# P3: Anderson Paper Notes
> The Performance of Spin Lock Alternatives for Shared-Memory Multiprocessors.

- This paper came out when shared-memory multiprocessors were new-ish (1990)
	- Each processor can directly access memory that can also be addressed by all other processors
	- How to ensure mutual exclusion?
	- Consistency of the data is guaranteed by serializing operations done on it.
- pure-software mutexes are expensive
- all shared-memory multiprocessors provide a form of mutex access to memory locations
- Instructions are "atomic", and cannot be interrupted
- instructions can be single atomic instructions, if theyre simple enough. Mutex is directly guaranteed in hardware. Multi-processors wait their turn when applying atomic instructions identical memory locations
- Locks are needed when a section has more than one instruction. There's 2 options when the lock is already acquired
	- Block, allow another process to do work
	- spin-lock ("busy wait"), burn cpu cycles and hope the lock will be available soon. Useful if the critical section is small.
	- The trick is balancing the overhead of a context switch with the inefficiency of performing a spin-lock.
- This paper examines a few algorithms for making the block vs spin-lock determination

## Range of MP Archs Considered
- multistage interconnection network without coherent private caches
- multistage interconnection network with invalidation-based cache coherence using remote directories
- bus without coherent private caches
- bus with snoopy write-through invalidation-based cache coherence
- bus with snoopy write-back invalidation-based cache coherence
- bus with snoopy distributed-write cache coherence

## Common Hardware Support
- Archs provide support for mutex by providing atomic read/modify/write instructions
- Archs require four services that might need interprocessor communication
	- read
	- write
	- method for arbitration between simultaneous requests
	- state that prevents further access from being granted while instructions are being executed

### Multistage Networks
- connect multiple processors to multiple memory modules
- requests are forwarded through switches to correct memory module
- When a value is modified, cached copies of the location must be invalidated and subsequent accesses to that location must be delayed while the new value is being computed
- Sometimes an ALU is directly attached to each memory module to reduce that delay

### Single Bus Multiprocessors
- Bus can be used to arbitrate simultaneous atomic instructions
- before starting an instruction, a processor will raise a bit in the bus to signal "hey I'm using the bus to modify a value"
- this prevents simultaneous access

### No Caching of Shared Data
- Some systems do not cache shared data
- bus transactions used to acquire the atomic bus line can be overlapped with the read request for the data

### Write-Back Invalidation-Based Coherence
- avoids extra bus transaction to write the data
- new value is temporarily stored in processor cache
- when another processor needs the value, it simultaneously gets/invalidates the first processor's copy

### Distributed-Write Write-Back Coherence
- initial read is usually not needed
- copies in all caches are updated instead of invalidated when a processor changes a value
- cache block needed by an atomic instruction will often already be in the cache

## Simple Approaches to Spin-Waiting

- spin on test-and-set
- spin on read (test-and-test-and-set)

![[Pasted image 20221105105406.png]]

### Poor Spin on Read Performance
- separation between detecting that the lock has been released and attempting to acquire it. More than one processor may notice that the lock is freed. Hardware equivalent of a spurious wakeup.
- cache copies of the lock value are invalidated by a test-and-set instruction even if the value is not changed
- invalidation-based cache-coherence requires $O(P)$ bus or network cycles to broadcast a value to $P$ waiting processors.

### Results
- Y Axis: The elapsed time for various number of processors to cooperatively execute a critical section one million times.
- X Axis: Number of processors.

![[Pasted image 20221105110032.png]]

Analysis
- performance degrades as processors spin on test and set
- spinning on read is better, but still disappointing

## Other Alternatives
![[Pasted image 20221105111036.png]]

![[Pasted image 20221105111052.png]]

## Full Results
![[Pasted image 20221105111146.png]]

![[Pasted image 20221105111235.png]]

![[Pasted image 20221105111249.png]]

## Conclusions
- simple methods of spin-waiting for mutex access to shared data degrade overall performance as number of waiting processors increases
- software queueing and a variant of Ethernet backoffs have good performance even for large numbers of waiting processors
- backoff has better performance when there's no contention for the lock
- queueing, by parallelizing the lock handoff, performs best when there are waiting processors
