---
tags: OMSCS, AISA
---
# Module 3 - Block 6 - P2P Overlay Networks

![[Pasted image 20230129191453.png]]

Common p2p overlay issues
- organize network
- maintain the overlay
	- new nodes
	- nodes left
	- failures
- resource alloc / load balancing
- resource location / lookup
- locality (network proximity)

| Unstructured P2P                                      | Structured P2P                             |
| ----------------------------------------------------- | ------------------------------------------ |
| Peers are organized in a random graph topology        | Organize peers using a structured topology |
| Data placement is local                               | global data placement                      |
| Flooding-based lookups over the randomly skewed graph | controlled lookups                         |
| Search is opportunistic (hop-based)                   | search is deterministic                    |

Structured P2P organization
- uni-dimensional vs multi-dimensional
- controlled neighborhood

P2P Goal
- harness storage and computation across nodes
- can create a large-scale, self-organizing system?
- scale to the large network sizes
- robust to faults and malice
- node arrival and departure
- freeloading participants
- malicious participants
- understanding bounds of what systems and cannot be built on top of a P2P framework

## Distributed Hash Table
- stores values at nodes
- hash function
	- lookup(key) -> node ID
	- lookup(key) -> data
- name -> hash key
- peer -> hash ID + search terms -> hash values

Example systems
- uni-dimensional
	- Chord
	- Pastry
- multi-dimensional
	- CAN

### How to design a DHT?
- State assignment: What (key, value) tables does a node store?
- Network topology: How does a node select its neighbors?
- Routing Algorithm: Which neighbor to pick while routing to a destination?

Various DHT algs make different choices
- CAN, Chord, Pastry, Tapestry, many others

## Chord
Design Goal: Better Peer-to-Peer Storage with deterministic search

Chord lookup provides
- good naming semantics and efficiency
	- global naming and placement protocol
- Deterministic lookup

### Chord IDs
Key ID = SHA-1 (URL)
- Cannot use HTTP Connection Alive feature

Key ID = SHA-1 (URL's domain name)

Node ID = SHA-1 (IP addr)

SHA-1: 128-bit

Chord-ID and Consistent Hashing
- Assigns a $m$-bit iID to each of the $N$ nodes and each of the search keys using a base hash function (SHA-1)
	- `Key = SHA-1("LetItBe")`
	- `NodeID = SHA-1(ip addr)`
- Identifiers are ordered in an ID circle
	- files with hash ID values between N14 and N21 are stored with N21

![[Pasted image 20230129193222.png]]

- A key is stored at its successor, the node with the next higher ID

![[Pasted image 20230129193251.png]]

### Efficient Key Search
- Naive search is to pass searches around perimeter of the ring
- Every node knows $m$ other nodes in the ring
- distance increases exponentially, modulus by keyspace

![[Pasted image 20230129193517.png]]

- Lookup is $O(log N)$ as opposed to $O(N)$ in naive case

![[Pasted image 20230129195100.png]]

### Chord Architecture
- interface
	- lookup(DocumentID) -> NodeID, IP Address
- Chord consists of
	- Consistent hashing
	- small routing tables: log(n) for a network of n peers
	- fast join/leave protocol
- Since file names are hashed, which is a pseudo-random operation, keys should be balanced evenly across key space
- Load balancing
	- consistent hashing
	- virtual servers: larger, more powerful servers can be assigned multiple node IDs by having multiple IPs registered in the node ID space
	- Caching: nodes can cache files that they see but don't own

![[Pasted image 20230129195834.png]]

### Chord Summary
![[Pasted image 20230129201135.png]]

## Content Addressable Network (CAN)
- Multi-dimensional structured P2P
	- One of the original four distributed hash table proposals, intriduced concurrently with Chord, Pastry, and Tapestry
- CANs overlay routing
	- Easy to understand
	- Scalable indexing system for large-scale decentralized storage apps
	- Has good performance
- Overview
	- Distributed decentralized P2P infra system that maps keys onto values
	- keys hashed into a $d$-dimensional Cartesian space
	- Associate to each node and item a unique coordinate in the cartesian space
- Interface
	- Insert(key, value)
	- Retrieve(key)
- Entire space is partitioned among all nodes
- Each node "owns" a zone in the overall space
- Can store data at "points" in the space
- Can route from one "point" to another point
- Node that owns the enclosing zone

![[Pasted image 20230129202546.png]]

![[Pasted image 20230129202659.png]]

![[Pasted image 20230129202807.png]]

![[Pasted image 20230129202754.png]]

![[Pasted image 20230129202647.png]]

![[Pasted image 20230129202856.png]]

### CAN Routing
- Data stored in CAN is addressed by name (i.e. key) not location (i.e. IP Addr)
- Have some routing mechanism
- A node only maintains state for its immediate neighbors

![[Pasted image 20230129203011.png]]

### CAN Maintenance
- Use zone takeover in case of failure or leaving of a node
- Send your neighbor table update to neighbors to inform that you are alive at discrete time interval t
- If neighbor does not send alive in time t, takeover its zone
- Zone reassignment is needed

## DHT Overview
- Compare along 2 axes
	- How many neighbors can you choose from when forwarding requests?
	- How many nodes can you choose from when selecting neighbors?
- Failure resilience: Forwarding choices. Pick low-latency neighbors.

## Overview

![[Pasted image 20230129203314.png]]

## P2P Web Crawler
- unique mapping of URL to a peer
	- each peer responsible for a distinct set of URLs
- URL duplicate detection
	- only the responsible peer needs to check for URL duplication
- Page content duplication
	- independent hash of the page contents (bloom filter)
	- unique mapping of the content-hash to a peer
- Answers membership queries efficiently
- URLs partitioned across nodes by
	- domain hash
	- hash table with domain as hash key
	- URLs belonging to that domain as corresponding values

![[Pasted image 20230129204307.png]]

