---
tags:
  - OMSCS
  - CN
---
# Lesson 05 - Router Design and Algorithms (Part 1)

> When a packet arrives at the input link, the router’s job is to look at the destination IP address of the packet and determine the output link by consulting the forwarding table.

- Lesson 5 focuses on longest-prefix-match algorithms
- Lesson 6 focuses on packet classification and scheduling

- packets require different quality of service or security guarantees
- routers need to handle packets based on multiple criteria (flags, quality of service)

## Readings
[[Survey and Taxonomy of IP Address Lookup Algorithms.pdf]]

## What in a Router?
> The main job of a router is to implement the forwarding plane functions and the control plane functions

### Forwarding / Switching Function
- transfer a packet from an input link interface to the appropriate output link interface
- Forwarding occurs at very short timescales (typically a few nanoseconds)
- typically implemented in hardware.

![[Pasted image 20230924185414.png]]

![[Pasted image 20230924185455.png]]

### Input Ports
- Physically terminates incoming links to the router
- Decapsulates the packets
- Performs the lookup function
	- input port consults the forwarding table
	- forwards to the appropriate output port through the switching fabric

### Switching Fabric
- the switching fabric moves the packets from input to output ports
- makes the connections between the input and the output ports
- There are three types of switching fabrics:
	- memory
	- bus
	- crossbar

### Output Ports
- receives and queues the packets from the switching fabric
- sends them over to the outgoing link

![[Pasted image 20230924190753.png]]

### Control Plane Functions
- implements routing protocols
- maintains routing tables
- computes forwarding tables
- implemented in software in the routing processor
- can be implemented as a remote controller

![[Pasted image 20230924190815.png]]

## Routing Architecture
![[Pasted image 20230924192837.png]]

Routers involve
- input links
- output links
- I/O links are typically not differentiated. Links do both I and O.
- packet switching to appropriate links

Packets traverse a few processing stages inside a router

### Lookup
> When a packet arrives at the input link, the router looks at the destination IP address and determines the output link by looking at the forwarding table (or Forwarding Information Base or FIB). The FIB provides a mapping between destination prefixes and output links. 

> The routers use the longest prefix matching algorithms to resolve any disambiguities. We will see these algorithms soon. Also, some routers offer a more specific and complex type of lookup, called packet classification, where the lookup is based on destination or source IP addresses, port, and other criteria.

### Switching
> After lookup, the switching system takes over to transfer the packet from the input link to the output link. Modern fast routers use crossbar switches for this task. Although scheduling the switch (matching available inputs with outputs) is difficult because multiple inputs may want to send packets to the same output.

### Queuing 
> After the packet has been switched to a specific output, it will need to be queued (if the link is congested). The queue may be as simple as First-In-First-Out (FIFO), or it may be more complex (e.g., weighted fair queuing) to provide delay guarantees or fair bandwidth allocation.

### Header Validation and Checksum
> The router checks the packet's version number, decrements the time-to-live (TTL) field, and recalculates the header checksum.

### Route Processing
> The routers build their forwarding tables using routing protocols such as RIP, OSPF, and BGP. These protocols are implemented in the routing processors.

### Protocol Processing
> The routers need to implement the following protocols to implement their functions:
> 
> Simple Network Management Protocol (SNMP) for a set of counters for remote inspection
> 
> TCP and UDP for remote communication with the router
> 
> Internet Control Message Protocol (ICMP) for sending error messages, e.g., when time-to-live (TTL) time is exceeded

## Different Types of Switching
> The switching fabric is the brain of the router, as it performs the main task to switch (or forward) the packets from an input port to an outport port.

### Switching via Memory
> Input/Output ports operate as I/O devices in an operating system, controlled by the routing processor. When an input port receives a packet, it sends an interrupt to the routing processor, and the packet is copied to the processor's memory. Then the processor extracts the destination address and looks into the forward table to find the output port, and finally, the packet is copied into that output's port buffer.

![[Pasted image 20230924194048.png]]

### Switching via bus
>vIn this case, the routing processor does not intervene as we saw the switching via memory. When an input port receives a new packet, it puts an internal header that designates the output port, and it sends the packet to the shared bus. Then all the output ports will receive the packet, but only the designated one will keep it. When the packet arrives at the designated output port, the internal header is removed from the packet. Only one packet can cross the bus at a given time, so the speed of the bus limits the speed of the router.

![[Pasted image 20230924194134.png]]

### Switching via Interconnection Network (Crossbar)
> A crossbar switch is an interconnection network that connects N input ports to N output ports using 2N buses. Horizontal buses meet the vertical buses at crosspoints controlled by the switching fabric.
> 
> For example, let's suppose that a packet arrives at port A that will need to be forwarded to output port Y, the switching fabric closes the crosspoint where the two buses intersect so that port A can send the packets onto the bus, and then the packet can only be picked up by output port Y. Crossbar network can carry multiple packets at the same time, as long as they are using different input and output ports. For example, packets can go from A-to-Y and B-to-X simultaneously.

![[Pasted image 20230924194257.png]]

## Routing Challenges
### Bandwidth and internet population scaling.
Caused by
1. increasing number of internet-connected devices
2. increasing volumes of network traffic due to new applications
3. new technologies (e.g. optical links) that can accommodate higher volumes of traffic

### Services at high speeds.
New applications require services such as
- protection against delays in the presence of congestion
- protection during attacks or failures

offering these services at high speed can be difficult due to a variety of processing bottlenecks

![[Pasted image 20230924194843.png]]

### Longest Prefix Matching
- routers need to look up a packet’s destination address to forward it.
- The increasing number of Internet hosts and networks has made it impossible for routers to have explicit entries for all possible destinations.
- routers group destinations into prefixes.
- Routers require more complex algorithms for efficient longest prefix matching.

### Service Differentiation
- Routers can also offer service differentiation which means different quality-of-service (QoS) or security guarantees to different packets
- This requires the routers to classify packets based on more complex criteria beyond destination. This can include
	- packet source
	- packet application
	- packet service

### Switching Limitations
- switches can process packets in parallel using crossbar switching
- at high speeds, this comes with problems and limitations (e.g. "head of line blocking")

### Bottlenecks about Services
- Providing service guarantees (QoS) at high speeds is non-trivial
- Also non-trivial, providing support for new services such as measurements or security guarantees

## Prefix-Match Lookups

One way to help with the internet's scalability problem is to "group" multiple IP addresses by the same prefix.

### Prefix Notation
There are a few different ways to denote prefixes.
#### Dot decimal
- Example of the 16-bit prefix: `132.234`
- The binary form of the first octet: `10000100`
- Binary of the second octet: `11101010`
- The binary prefix of `132.234`: `1000010011101010*`
- The * indicates wildcard character to say that the remaining bits do not matter.
#### Slash Notation
- Standard notation: A/L
	- A denotes the base address
	- L denotes the number of relevant bits
- Example: `132.238.0.0/16`
	- The starting address is `132.238.0.0`
	- The `16` denotes that only the first 16 bits are relevant
#### Masking
- We can use a bit mask to denote prefix as opposed to a length
- Example, the prefix `123.234.0.0/16` can be written as
	- Address: `123.234.0.0`
	- Mask: `255.255.0.0`
- The `255.255.0.0` mask denotes that only the first 16 bits (the first 2 octets) are important.
- The octets in the mask don't need to all be 1s or all 0s, though typically there will not be any gaps in the string of 1s.

### What is the need for variable-length prefixes?
> In the earlier days of the Internet, we used an IP addressing model based on classes (fixed-length prefixes). With the rapid exhaustion of IP addresses, in 1993, the Classless Internet Domain Routing (CIDR) came into effect. CIDR essentially assigns IP addresses using arbitrary-length prefixes. CIDR has helped to decrease the router table size, but at the same time, it introduced us to a new problem: longest-matching-prefix lookup.

### Why do we need (better) lookup algorithms?
> To forward an incoming packet, a router first checks the forwarding table to determine the port and then does switching to send the packet. There are various challenges that the router needs to overcome when performing a lookup to determine the output port. These challenges revolve around lookup speed, memory, and update time.

> The table below mentions some basic observations around network traffic characteristics. The table shows the consequence (inference) that motivates and impacts the design of prefix lookup algorithms for every observation. The four takeaway observations are:

1. Measurement studies on network traffic had shown a large number (in the order of hundreds of thousands (250,000 according to a measurement study in the earlier days of the Internet) of concurrent flows of short duration. This already large number has only been increasing, and as a consequence, caching solutions will not work efficiently. 
2. The important element of any lookup operation is how fast it is done (lookup speed). A large part of the cost of computation for lookup is accessing memory.
3. An unstable routing protocol may adversely impact the update time in the table: add, delete or replace a prefix. Inefficient routing protocols increase this value up to additional milliseconds.
4. A vital trade-off is memory usage. We can use expensive fast memory (cache in software, SRAM in hardware) or cheaper but slower memory (e.g., DRAM, SDRAM).

![[Pasted image 20230924202341.png]]

## Tries
### Unibit Tries
![[Pasted image 20230925114449.png]]
> Example routing prefix database

Simplest technique for prefix lookup is the unibit trie. The database above would produce the unibit trie below

![[Pasted image 20230925114559.png]]

Every node has a nullable 0-pointer and a nullable 1-pointer. Data structure:

```python
@dataclass
class UnibitTrie:
	route: Optional[str]
	zeroBranch: Optional[UnibitTrie]
	oneBranch: Optional[UnibitTrie]
```

- Each pointer points to a subtrie, or nothing
- Each subtrie is labelled with a route, or nothing
- Addresses will be compared against the tree to determine the link
	1. We begin the search for a longest prefix match by tracing the trie path.
	2. We continue the search until we fail (no match or an empty pointer)
	3. When our search fails, the last known successful prefix traced in the path is our match and our returned value.

In theory, the purely abstracted Unibit Trie model works fine. In practice, one-way branches can be compressed for more efficient traversals. For example, the P6 to P7 branch can be compressed if we use this slightly different model.

```python
class UnibitTrie:
	route: Optional[str]
	branches: dict[str, UnibitTrie]
```

Instead of hardcoding prefixes 0 and 1, you can instead encode each prefix in the `branches` property.

### Multibit Tries
Unibit Tries are a simple abstract model for determining how to route packets. Multibit Tries work similar but decrease the number of memory accesses that need to be performed.

- Multibit Tries come in 2 flavors
	- fixed-length stride
	- variable-length stride
- The "stride" is the number of bits checked at each stage.
- For both, each node in the trie has $2^k$ children, as opposed to 2 children. $k$ is the "stride"

### Prefix Expansion
Given a stride length greater than one, it's possible for prefixes whose lengths aren't divisible by the stride length to be not representable by a multibit trie. Those paths can be expanded to the appropriate lengths.

When collisions happen, expanded prefixes are dropped in favor of unexpanded prefixes.

![[Pasted image 20230925170858.png]]

Another example

![[Pasted image 20230925171027.png]]

### Fixed-Stride Multibit Tries
```python
STRIDE_LENGTH: int = ...

class FSMultibitTrie:
	def __init__(self):
		self.stride = STRIDE_LENGTH

		# Populate later. Each element has an optional pointer
		# and an optional prefix value.
		self.prefixes: list[tuple[str, FSMultibitTrie] = [
			[None, None] for _ in
			range(2 ** self.stride)
		]
```

1. Every element in a trie represents two pieces of information: a pointer and a prefix value.
2. The prefix search moves ahead with the preset length in n-bits (3 in this case) 
3. When the path is traced by a pointer, we remember the last matched prefix (if any).  
4. A search ends when an empty pointer is met. At that time, we return the last matched prefix as our final prefix match.

![[Pasted image 20230926160018.png]]

### Variable Stride Multibit Trie
```python
class VSMultibitTrie:
	def __init__(self, stride: int):
		self.stride = stride

		# Populate later. Each element has an optional pointer
		# and an optional prefix value.
		self.prefixes: list[tuple[str, VSMultibitTrie] = [
			[None, None] for _ in
			range(2 ** self.stride)
		]
```

- more flexible
- prefix database does not need as much prefix expansion, so the prefix DB can be smaller
- requires more computations to determine the relevant portion of the prefix when performing searches

![[Pasted image 20230926160257.png]]

1. Every node can have a different number of bits to be explored.
2. The optimizations to the stride length for each node are all done to save trie memory and the least memory accesses.
3. An optimum variable stride is selected by using dynamic programming

