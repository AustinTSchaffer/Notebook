---
tags: OMSCS, AISA
---
# Module 3 - Block 5 - P2P Computing

- Arpanet
- Usenet
- DNS is a distributed system

Napster was the first P2P music sharing application.

Other P2P applications: Gnutella, eDonkey, Kazaa, eMule, BitTorrent, Skype

Bitcoin. Decentralized virtual currency. P2P transaction processing.

## Types of P2P Networks

### P2P with Centralized Coordination
- Napster
- Search Engine Crawlers
- YouTube, Uber, AirBnb, Lending Club

### P2P with Decentralized Coordination
- Gnutella, eDonkey
- Kazaa
- BitTorrent, eMule
- Skype

### P2P Cryptocurrencies
- Bitcoin
- Ethereum

### Centralized Flow
1. User sends out request to centralized broker
2. Central server sends a response with URIs to resources controlled by other users
3. User retrieves the resources from other users

### Decentralized P2P Computing Architecture
![[Pasted image 20230124200449.png]]

## P2P Overlay
Logical network where nodes are the computers in a network, which are connected with a TCP IP underlay network

![[Pasted image 20230124200629.png]]

## P2P Cooperative Content Distribution Network
![[Pasted image 20230124200805.png]]

![[Pasted image 20230124200945.png]]

## P2P Lending: Banking without Banks
- match borrowers and lenders directly, usually via online auctions
- Lending Club
- Prosper

## Unstructured Overlay Network
- constructed randomly
- peers are organized in a random graph topology
- build p2p-services based on the graph

Several well-known P2P systems

Decentralized P2P Overlay
- build graph at application layer and forward packets at the application layer
- virtual graph
- underlying physical graph is transparent to the user
- edges are TCP connections or simply an entry of a neighboring node's IP address
- Graph must be continuously maintained
	- Ex: each node must have 5 neighbors

Broadcast messages
- ping: "I'm here"
- query: search pattern and TTL

Back-Propagated Messages
- pint: reply to ping
- query response: contains info about the computer that has the needed file

Node-to-Node messages
- GET: return the requested file
- PUSH: push the file to me

P2P membership
- Join with a ping to announce self
	- bootstrap with system-supplied root nodes
	- receivers forward the ping to neighbors
	- receivers bak-propagate a pong to announce self: IP address, number/size of shared files
- Periodic refresher of network state
	- ping again
	- well-known root nodes if starting from scratch

## Gnutella

![[Pasted image 20230124212903.png]]

- non-deterministic: available info may be outside search radius
- flooding can be expensive

Search protocol
- Gnutella request by peer $A$ creates
	- search string $S$
	- Unique Request ID $N$
	- Time to Live (TTL) $T$ (# hops passed)
- Check local system, if not found
	- Sends **(A, S, N, T)** to all Gnutella neighbors
	- Controlled flooding with pre-defined number of hops

![[Pasted image 20230124213454.png]]

![[Pasted image 20230124213509.png]]

### Propagation (forwarding/response) Protocol
- **B** receives gnutella request **(A, S, N, T)**
- If B has already received request N or T=0, B drops the request and does nothing
- B looks up S locally, and if results found, node B sends (N, Result) to A
- B sends **(B, S, N, T-1)** to all of its neighbors, and it records the fact that A has made the request N
- When B receives a response of the form (N, Result) from one of its neighbors, it forwards this response to A

### Flooding Protocol Overview
If B doesn't have the requested file
- Query all neighbors
- If they don't have it, they contact all their neighbors, for a max hop count of a given TTL, say 10 hops
- Anonymity: You only know that the file request comes from your neighbor, but you don't know the request's origin.

Stop flooding by checking
- Unique ID (stop when seen twice, avoid duplicate)
- Hop count exceeded

### Gnutella Network Stats
- Grew from 2K nodes to 48K nodes in 7 months
- About 40% of nodes live less than 4 hours
- About 25% of nodes live more than 24 hours
- Message breakdown in June 2001
	- 91% queries
	- 8% pings
- ~95% of node pairs were within 7 hops
- Node to node distance maintains similar distribution
- Average node-to-node distance grew 25% while the network grew 50x over 6 months

Node connectivity
- power law networks: number of links per node follows a power-law distribution
- Implications
	- high tolerance to random node failures, but low reliability when facing an intelligent adversary
	- 3.4 links per node on average
- Had a small-world phenomenon
	- Few nodes were "hubs"
	- most nodes had a few connections
- Mismatch problem: node peering connections did not necessarily take physical network connections into account

## Two Popular Solutions: Improving Unstructured P2P
- Network proximity-based optimization
	- SuperPeers.
		- Similar to the electrical grid. SuperPeers are substations
	- FrieldList, Shortcut list, etc
- Deterministic overlay
	- distributed hash table (DHT)

![[Pasted image 20230124215356.png]]

![[Pasted image 20230124215423.png]]

- trading of copyright music and videos without paying royalties to the authors
- March 2001, Kazaa

![[Pasted image 20230124220259.png]]

![[Pasted image 20230124220411.png]]

## What makes P2P Successful?
- Cheap, no infra needed
- Everybody can bring own content
	- Homemade
	- Ethnic
	- Legal
	- Illegal <- Most common reason
- High availability
	- Content accessible most of the time

## Common Issues
- Organize an overlay network
- Maintain the overlay
	- node arrivals
	- node departures
	- node failures
- Resource allocation / load balancing
- Resource location / lookup
- Locality (network proximity)
- **Idea:** generic P2P substrate

## Web Crawling Problems
- Traversing the WWW by following hyperlinks
- Two primary components
	- Duplicate URLs: Same URL may be reached through many hyperlinks (normalized URL `btree`?)
	- Duplicate page content: some web pages are mirrored (content hashes?)
- Not avoiding duplicate URLs: 100x time to crawl the WWW
- Not avoiding duplicate page contents: 10x time to crawl the WWW

## P2P Web Crawling Design Decisions
- Choice of P2P Topology
	- Structured or unstructured?
- Choice of data structures
	- Arrays, linked lists, hash tables, directed graphs
- Order of crawl
	- DFS? BFS? mixture of DFS and BFS?
- Robustness
	- Illegal URLs, cannot be parsed
	- web site is down
	- recoverable and restartable
- Modularity
	- Upgradeability

## PeerCrawl
- Improve on P2P crawling ideas by Apoidea for improving speed and efficiency
- Reduce overhead during information exchange, storing out performance issues, make it faster than Apoidea
- Uses Gnutella protocol for formation over the network layer
- Gnutella File Sharing
	- Nodes serve as client, server, and router in P2P network
	- Each node will
		- Store files
		- Route queries (file searches) from and to neighboring peers
		- Serve files if has file

Unstructured P2P
- Overlay links are established arbitrarily
- Flooding queries, queries are non-deterministic
- Maintains anonymity

Phex open-source P2P file sharing client

Local hist caching and web caching

Division of labor - URL distribution function
- $upperbound(\pi) = min(h(\pi)+2^{128-x}-1, 2^{128}-1)$
- $lowerbound(\pi) = max(0, h(\pi)+2^{128-x})$
- $crawlrange(\pi) = upperbound(\pi) - lowerbound(\pi)$

Peers broadcast URLs not in their crawl range

![[Pasted image 20230124223147.png]]

### Partition-By-Document
- Divide documents (URLs) among hosts by hash values
	- Each peer maintains a range of URL hash values
	- Each peer maintains local inverted index of documents it is responsible for
	- Query approach: flooding, return highly ranked doc(s)

### Partition-By-Terms
Responsibility for words divided among peers. Each peer stores the posting list for word(s) it is responsible for.

Query for one or more terms implies postings be sent over the network

Two-term queries. Smaller postings sent to holder of larger postings. Perform intersections and return highly ranked doc(s)

## Retrieval and Ranking
- Directing queries to appropriate peers
- How to decide which results should be returned by each peer?
- Combining results from different peers
	- Different top-k query processing algorithms
- Link-based ranking for distributed web graph

### Architecture
![[Pasted image 20230124223629.png]]

