---
tags: OMSCS, AISA
---
# M11B21 - Key-Value Systems

- AKA Key-Value Stores
- AKA NoSQL

![[Pasted image 20230316201554.png]]

![[Pasted image 20230316201731.png]]

![[Pasted image 20230316202025.png]]

![[Pasted image 20230316202118.png]]

## Architecture

Directory-based Architecture
- Recursive
	- Insert/Put with Master Relay
		- Master node will maintain the mapping between keys and the machines (nodes) that store the values associated with the keys
		- The master node will relay the request
	- Read/Get with Master Relay
- Iterative
	- Iterative Put with Master Reduction
	- Iterative Get with Master Reduction

DHT-based Architecture
- Recursive lookup
- Iterative lookup

### Directory Based

#### Recursive
- Master node will maintain the mapping between keys and the machines (nodes) that store the values associated with the keys
- The master node will relay the request
- Advantages
	- Faster
	- Easier to maintain consistency
	- Master node serializes puts/gets
- Disadvantages
	- scalability bottleneck
	- master node doesn't store data, but nonetheless brokers all of it

Put:
![[Pasted image 20230316202458.png]]

Get:
![[Pasted image 20230316202530.png]]

#### Iterative
- Iterative queries: The master node will return the work node to the requester and let the requester contact the node directly.
- Advantages
	- more scalable
	- master node doesn't touch data, only manages a directory
- Disadvantages
	- more hops for the client (slower)
	- harder to enforce data consistency

Put:
![[Pasted image 20230316202638.png]]

Get:
![[Pasted image 20230316202654.png]]

### DHT-Based
- finger tables
- recursive lookup (relay)
- Classic Chord

![[Pasted image 20230316203843.png]]

## Key-Value Model
API
- `put(key, value)`
- `value = get(key)`

Abstraction used to implement
- File Systems: store value content in blocks (data chunks)
- Distributed File Systems (Key: Block ID, Value: Block)
- Simple and yet highly scalable database

By design it can handle large volumes of data
- Distributes data over a cluster
- More easily handles partitioning/sharding compared to SQL databases

![[Pasted image 20230316204120.png]]

![[Pasted image 20230316204139.png]]

## Google Key-Value System
Lots of semi-structured data at Google
- URLs
	- Contents
	- Crawl metadata
	- links/anchors
	- pagerank
- Per-user data
	- User prefs
	- recent queries
- Geographic locations
	- Physical entities (shops, restaurants, etc)
	- roads
	- satellite image data
	- user annotations

Scale is large
- Billions of URLs, many versions per page (20K versions)
- Hundreds of millions of users, thousands of queries per second
- 100TB+ of satellite image data

Why not use commercial DB?
- Scale too large. Most SQL databases don't partition easily
- Cost would be very high
	- building internally (in-house dev) means that the system can be applied across many projects for a low incremental cost
	- a very small incremental cost for new services and expanded computing power
- Low-level storage optimizations help performance significantly
	- much harder to do when running on top of a SQL database layer

MySQL doesn't work at scale
- designed for a single machine
- Large effort required to make it scale
	- major engineering effort
	- solutions are usually ad hoc
	- solutions usually involve horizontal partitioning

## Google Big Table
Design Goal
- seamlessly run on any commodity hardware
- enable google to have a very small incremental cost for new services and expanded computing power

Google Stack
- Google File System (GFS)
- Map-reduce
- Bigtable
	- Very high read/write rates
	- Efficient scans
	- Efficient joins
- Inherently scalable
- Inherently cost-effective

- Distributed multi-level map
- Fault-tolerant, persistent
- Scalable
	- thousands of servers
	- Terabytes of in-memory data
	- Petabyte of disk-based data
	- Millions of reads/writes per second, efficient scans
- Self-managing
	- Servers can be added/removed dynamically
	- Servers adjust to load imbalance

Most of Google's major services are built on top of it

## BigTable Data Structure
- Distributed multi-dimensional sparse map `(row, column, timestamp) -> cell contents`

![[Pasted image 20230316210229.png]]

### Rows
Name is an arbitrary string
- access to data in a row is atomic
- row creation is implicit upon storing data
- transactions within a row

Rows ordered lexicographically
- Rows close together lexicographically usually on one or a small number of machines

Does not support relational model
- No table wise integrity constraints
- No multi-row transactions

### Columns
- Column oriented storage. Focus from reads by columns
- Columns have 2-level name structure
	- Family
	- Optional qualifier
- Column Family
	- Unit of access control
	- Has associated type information
- Qualifier gives unbounded columns
	- Additional level of indexing, if desired

![[Pasted image 20230316210510.png]]

### Timestamps
- Used to store different versions of data in a cell
	- New writes default to current time
	- timestamps for writes can also be set explicitly by clients
- Lookup options
	- "Return most recent K values"
	- "Return all values in timestamp range (or all values)"
- Column families can be marked w/ "attributes"
	- "Only retain most recent K values in a cell"
	- "Keep values until they are older than K seconds"

### API
- Metadata operations
	- create/delete tables
	- create/delete column families
	- change metadata
- Writes (atomic)
	- `set()`: write cells in a row
	- `deletecells()`: delete cells in a row
	- `deleterow()`: delete all cells in a row
- Reads
	- Scanner: read arbitrary cells in a bigtable
	- Each row read is atomic
	- Can restrict returned rows to a particular range
	- Can ask for just data from 1 row, all rows, etc.
	- Can ask for all columns, just certain column families, or specific columns.

### Storage Design
- Data Structure
	- Table
	- Tablets
	- SSTable
	- Chunk

Tablets
- Assignment
- Locating
- Serving

![[Pasted image 20230316211603.png]]

- Multiple tablets make up the table
- SSTables can be shared among tablets
- Tablets do not overlap, SSTables can overlap

![[Pasted image 20230316211720.png]]

- Large tables broken into _tablets_ at row boundaries
	- Tablet holds contiguous range of rows
	- Clients can often choose row keys to achieve locality
	- Tablets are each around ~100MB to ~200MB
- Serving machine responsible for ~100 tablets (stored in GFS)
	- Fast recovery
		- 100 machines each pick up 1 tablet from failed machine
	- Fine-grained load balancing
		- Migrate tablets away from overloaded machine
		- Master make load-balancing decisions

![[Pasted image 20230316212326.png]]

![[Pasted image 20230316212350.png]]

![[Pasted image 20230316212411.png]]

![[Pasted image 20230316212456.png]]

## BigTable Implementations

### Editing a Table
- Mutations are logged, then applied to an in-memory version (write optimized)
- Logfile stored in GFS

![[Pasted image 20230316212605.png]]

### Locating Tablets
- Maintain a multi-level index of tables and tablets
- Maintain a local index in each tablet and each sstable
	- to locate ss-tables with each tablet
	- to locate chunks with each ss-table

![[Pasted image 20230316212711.png]]

### Servers
**tablet servers manage tablets, multiple tablets per server**
- each tablet is 100-200 MB
- each tablet lives on only one server
- tablet server splits tablets that get too big

Master responsible for load balancing and fault tolerance
- Use Chubby to monitor the health of table servers, restart failed servers
- GFS replicates data. Prefer to start tablet server on the same machine where the data is already located

### Building Blocks
- Google File System (GFS)
	- Raw storage
	- Stores persistent state
- Scheduler
	- schedules jobs onto machines
- Lock service
	- distributed lock manager
	- can reliably hold tiny files (100s of bytes) with high availability
	- master election
	- location bootstrapping
- MapReduce
	- simplified large-scaling data processing
	- often used to read/write BigTable data

### System Structure
![[Pasted image 20230316213230.png]]

![[Pasted image 20230316213246.png]]

![[Pasted image 20230316213302.png]]

### Compaction
- Tablet state represented as a set of immutable compacted base SSTable files, update SStable files, plus a tail of log (buffered in memory)
- Minor compaction
	- When in-memory state fills up, pick tablet with most data and write contents to SStables stored in GFS
	- Separate file for each locality group for each tablet
- Major compaction
	- Periodically compact all SStables for tablet into new base SStable on GFS
	- Storage reclaimed from deletions at this point

### Compression
Many opportunities for compression
- similar values in the same row/column at different timestamps
- similar values in different columns
- similar values across adjacent rows

Within each sstable for a locality group
- keep blocks small for random access (~64KB compressed data)
- Exploit fact that many values very similar
- Needs to be low CPU cost for encoding/decoding

Keys
- sorted strings of (row, column, timestamp): prefix compression

Values
- Group together values by "type" (e.g. column family name)
- BMDiff across all values in one family
- BMDiff output for values `1..N` is the dictionary for value N+1

Zippy as final pass of whole block
- Catches more localized repetitions
- Also catches cross-column-family repetition, compresses keys

![[Pasted image 20230316214738.png]]

![[Pasted image 20230316214750.png]]

![[Pasted image 20230316214825.png]]

## Other Key-Value Stores

### BigTable Family
- BigTable (Google)
- HBase (Hadoop)
- Dynamo (Amazon)
	- Gossip protocol (discovery and error detection)
	- Distributed key-value data store
	- eventual consistency

![[Pasted image 20230316215003.png]]

![[Pasted image 20230316215028.png]]

## Amazon Dynamo
- There are many Amazon services that only need primary-key access to a data store
- Using relations database would lead to inefficiencies and limit scale availability

![[Pasted image 20230316215215.png]]

![[Pasted image 20230316215244.png]]

![[Pasted image 20230316215258.png]]

![[Pasted image 20230316215310.png]]

![[Pasted image 20230316215554.png]]

![[Pasted image 20230316215601.png]]

