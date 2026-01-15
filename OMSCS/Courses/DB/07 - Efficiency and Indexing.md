---
tags:
  - OMSCS
  - DB
---
# 07 - Efficiency and Indexing (Physical Database Design)

## Computer Architecture
- Main memory (RAM)
	- volatile
	- fast
	- small
	- expensive
- secondary memory (Disk)
	- permanent
	- slow
	- big
	- cheap

![[Pasted image 20251126224224.png]]

- applications run by the CPU can only query and update data in main memory
- data must be written back to secondary memory after it is updated
- only a tiny fraction of a real database fits in main memory

## Why should you care?
### Time
- main memory access time is 30ns
- disk access time is about 10ms
### Phonebook
- read a page in 1 minute
- open a page in 200 days
### Cost computation
- only I/O cost counts
- CPU cost is ignored

## Disk
Typical high-end pack capacity
- 4 platters
- 8 heads
- 150k tracks/surface
- 1000kB/track
- 1200 GB
- 512 bytes/sector
- 4kB, 8kB, or 16kB per block (configurable in OS)
- 600MB/s transfer rate
- 10,000 RPMs
- 3-4ms latency

## Records, Blocks, and Files
```sql
RegularUser(
	Email varchar(50),
	Sex char(1),
	Birthdate datetime,
	CurrentCity varchar(50),
	HomeTown varchar(50)
)
```

- Record
	- record size: 159 bytes
- Block
	- 4K + metadata (block size)
	- filled: ~80%
	- records/block: ~20
	- spanned vs unspanned
		- whether a single record can span multiple blocks
		- if a record is larger than your configured block size, it will always span multiple blocks
- Files
	- Blocks linked by pointers
	- block pointer: 4 bytes
	- number of records: 4 million
	- number of blocks: ~200,000
	- file size: ~800MB

## Assumptions
- Page fault:
	- Seek time: 3-8 ms
	- Rotational delay: 2-3 ms
	- Transfer time: 0.5 - 1.0 ms
	- Total: 5-12ms
- Extent transfers (e.g. 250 blocks) save seek time and rotational delay, but require more buffer space
- with a page fault of 10ms, each costs 2.5 seconds
- as an extent costs 0.260 seconds
- buffer management
	- LRU strategies are excellent for merge joins
	- LRU strategies kill nested loop joins

## Heap-Unsorted File
- A heap is an unsorted set of data
- block pointer: 4 bytes
- len(data) = 4,000,000
- len(blocks) = 200,000
- file size: ~800 MB
- Lookup time
	- N/2 where N = len(data blocks)
	- 200,000 / 2 x 0.01 seconds = 16.6 minutes

## Heap
![[Pasted image 20251126225620.png]]

> Sometimes you get lucky when you're searching for something that you're looking for.

## Sorted File
Lookup time
- $O(N)$ for linear search ($200000/2 * 0.01s = 16.6\space minutes$)
- $O(log_2(N))$ for binary search ($18 * 0.01s = 0.18s$)

## Primary Index
point and range queries

- Primary indexes store the values and a pointer to the block which contains the value.
- Primary indexes assume that the records they point to are sorted by the indexed value on the disk.
- How many index blocks do we need?
	- block pointer: 4 bytes
	- filled: ~80%
	- fanout: 60
	- records: 4 million
	- data blocks: ~200,000
	- sparse:
		- only contains values which occurred in the first record of a block
		- in this example, requires 3334 blocks
	- dense:
		- contains all values with pointers to the block(s) which contain(s) the value
		- Can be used to perform statistics on the values contained within the index (min (easy), max (easy), median (easy), average)
		- in this example, requires 66,666 blocks
- Lookup time
	- $O(log_2(N)+1)$ where $n$ is the number of index blocks
	- Sparse: $(log_2(200,000/60)+1) * 0.01s=0.13s$
	- Dense: $(log_2(400,000/60)+1) * 0.01s=0.13s$
- Trading time for space

![[Pasted image 20251126231737.png]]

## Secondary Index
point queries only

- Secondary indexes store the values and a pointer to the block which contains the value.
- Secondary indexes **cannot** assume that the records they point to are sorted by the indexed value on the disk.
- Indexes must be dense, cannot be sparse.
- Tricky for non-key fields. An indexed value can appear on multiple data blocks.

![[Pasted image 20251126231726.png]]

## Multi-level index
- Build an index on your index
- Can speed up access time if your index is large enough (fewer block accesses to find data page)

![[Pasted image 20251126231838.png]]

## Multi-level index - $B^+$-Tree
- The "B" stands for "balanced"
- most popular multi-level index implementation
- insertion, deletion, and update operations are implemented to keep the tree balanced
- only rarely does an overflow at a lower level of the tree propagate more than 1-2 levels up

## Static Hashing
- large space of key values
- hash key space must be much larger than the address space
- good hash function
	- distribute values uniformly over the address space
	- full buckets as much as possible
	- avoid collisions

![[Pasted image 20251126232445.png]]

![[Pasted image 20251126232807.png]]

