---
tags:
  - OMSCS
  - CN
---
# Exam 1 Study Guide

> Exam 1 covers Lessons 1 through Lesson 6. It will be open during the end of Week 7 (Oct 9 – Oct 15 AOE).

> The following questions and prompts are intended to check your understanding of the content. The exam may cover ANY content from the modules. The only exception is those pages marked “optional.” You can find the study guide for all lessons on Canvas. This post serves as a location where you can receive clarification and have discussions concerning the exam.

Note that all exams in this course are CLOSED NOTE.
## Lesson 1: Introduction, History, and Internet Architecture
[[Lesson 01 - Introduction, History, and Internet Architecture]]

> What are the advantages and disadvantages of a layered architecture?

advantages
- modularity
- scalability
- flexibility
disadvantages
- some layers depend on information from other layers, breaking the goal of layer separation
- duplication of functionality
- additional overhead required for encapsulation and de-encapsulation at the transition points between each layer

> What are the differences and similarities between the OSI model and the five-layered Internet model?

- The OSI model has 7 layers, while the 5-layer model is called the "IP-stack" model. These models have 5 layers in common, but the OSI model describes 2 additional discrete layers which are not in the IP stack model.
- Layers
	- Application layer
	- presentation layer (OSI Only)
	- Session layer (OSI Only)
	- Transport layer
	- network layer
	- data link layer
	- physical link layer
- The 2 OSI Only layers can be considered part of the "application layer" in the IP-stack model.

> What are sockets?

A socket is the interface between the application layer and the transport layer.

> Describe each layer of the OSI model.

- application layer
	- you can design any network application. This is currently where the most innovation is happening.
- presentation layer
	- define data formats
	- apply transformation rules
	- no examples
- session layer
	- managing tokens
	- chekpointing
	- no examples
- transport layer
	- Makes guarantees about reliable / in-order packet delivery (or not, in the case of UDP)
	- multiplexing / demultiplexing
- network layer
	- "Routing" and "Forwarding"
	- Deliver packets from one end of a network to another
	- Handle fragmentation and reassembly
	- Scheduling
	- Buffering
- data link layer
	- Data framing (boundaries between packets)
	- Media access control (MAC)
	- Per-hop reliability and flow control
- physical link layer
	- move information between systems connected by a physical link
	- voltages, frequencies, baud rate, etc

> Provide examples of popular protocols at each layer of the five-layered Internet model.

- application layer
	- http, mqtt, smtp, ftp, dns
- transport layer
	- tcp, udp
- network layer
	- IPv4, IPv6, routing
- data link layer
	- Ethernet, wifi
- physical link layer
	- coaxial cable, fiber optics, radio frequencies

> What is encapsulation, and how is it used in a layered model?

Encapsulation is the process of packaging up a packet of information, adding the header of the next layer of the IP-stack model, so that the data can continue across the network.

> What is the end-to-end (e2e) principle?

The idea of the E2E principle is to make the network layer as simple as possible. The network layer (and lower) should not concern itself too much with adding support for specific application/transport layer protocols. This will give applications the flexibility to innovate their own protocols.

> What are the examples of a violation of e2e principle?

- Firewalls. Capable of dropping communication between 2 hosts based on source/destination/application/etc
- Network Address Translation (NAT) boxes. "hides" devices behind a private network. Devices on the private network are not globally addressable.

> What is the EvoArch model?

The EvoArch model suggests that the IP-stack was not trying to compete with telephone networks, and therefore increased its value without being threatened by competition. Over time, different protocols were added to the IP-stack. Each protocol uses technologies in the layer below, and can be used by protocols in the layer above.

The EvoArch model suggests that the internet protocols form an "hourglass" shape, because it's harder to create alternatives for technologies in the middle of the stack than it is to create alternatives for technologies on the top/bottom of the stack.

> Explain a round in the EvoArch model.

A round in the EvoArch model is the process of adding a new protocol into the TCP/IP stack, then calculating the value of that new protocol, recalculating the value of all other protocols, then pruning the model, dropping protocols that have the lowest value.

> What are the ramifications of the hourglass shape of the internet?

- It's hard to create replacements for middle-layer protocols
- IPv4 is being used well past its effectiveness date. It's been hard to transition to IPv6 because so many technologies depend on IPv4.
- Existing technologies were adapted to use the internet (Radio/Voice over IP)

> Repeaters, hubs, bridges, and routers operate on which layers?

- Repeaters operate on the physical layer (L1)
- Hubs operate on the physical layer (L1)
- Bridges operate on the data link layer (L2)
- Routers operate on the data link layer (L2) and/or the network layer (L3). Like L3 is what the professor wants to see.

> What is a bridge, and how does it “learn”?

A learning bridge populates and maintains a forwarding table. These bridges can learn to forward packets only to specific ports, rather than all ports.

> What is a distributed algorithm?

A distributed algorithm is an algorithm which runs on multiple hosts connected simultaneously. These algorithms rely on asynchronous communication between the different hosts to propagate information across all connected hosts. Each host is responsible for combining all of the information it receives and deciding whether to (and when to) send information to the hosts that it is connected to.

> Explain the Spanning Tree Algorithm.

The spanning tree algorithm is a distributed algorithm which bridges follow to build a "spanning tree" of the network. Bridges can use the resulting spanning tree to exclude links which lead to loops. The links will still be physically connected, but bridges will not use them.

A "spanning tree" is a tree which connects all nodes in a network using a subset of the network's existing links.

> What is the purpose of the Spanning Tree Algorithm?

The Spanning Tree Alg is important because it allows a network of bridges to build out a tree which connects all nodes in the network but contains no loops. This ensures that no traffic will be endlessly routed in a circle.
## Lesson 2: Transport and Application Layers
[[Lesson 02 - Transport and Application Layers]]

> What does the transport layer provide?

- **Multiplexing**. Multiple different communication streams can happen from the same host to the same network
- TCP also provides
	- Delivery guarantees
	- Retransmission
	- Transmission control
		- Flow control
		- Congestion control
- UDP doesn't really provide any extra functionality other than multiplexing

> What is a packet for the transport layer called?

A segment.

> What are the two main protocols within the transport layer?

TCP and UDP.

> What is multiplexing, and why is it necessary?

Multiplexing is what allows the transport layer to support hosts running multiple applications that are using the network simultaneously. Even if the same host is using multiple instances of the same application to make requests to the same IP address, the transport layer protocol will guarantee that the connections will not interfere with each other.

> Describe the two types of multiplexing/demultiplexing.

- **Connection** Oriented
	- Used by TCP
- **Connectionless** Multiplexing
	- Used by UDP

> What are the differences between UDP and TCP?

UDP is a fire and forget protocol. The application layer is responsible for doing everything.

TCP provides many different variants, guarantees, and settings. TCP also has various flow and congestion control mechanisms.

> When would an application layer protocol choose UDP over TCP?

- VPNs use UDP, since it wraps existing communication streams which are probably already using TCP. Using TCP in this situation would be redundant and can lead to a phenomenon known as "TCP Meltdown"
- Applications would also use UDP if they don't necessarily need to guarantee that the information they're sending to another host needs to arrive in order, or at all. 

> Explain the TCP Three-way Handshake.

1. Connection Request. Host 1 generates an initial sequence number `client_isn`. Host 1 sends a 0 data segment to host 2 with the `client_isn` and the `SYN` bit set to 1.
2. Connection Granted. The server allocates the resources required for the connection.
3. ACK. Host 1 acknowledges the response from host 2 with an ACK.

> Explain the TCP connection tear down.

4 segments are required to tear down a TCP connection.

1. Client sends a segment with `FIN` set to 1
2. Server ACKs
3. Server sends a segment with `FIN` set to 1
4. Client ACKs

> What is Automatic Repeat Request or ARQ?

In TCP, if the sender does not receive an ACK for a given segment within a given period of time, the sender will assume the packet was lost and will resend it.

> What is Stop and Wait ARQ?

The sender will send a packet then wait for an ACK before sending the next packet. The sender can also define a window size, where the sender will have at most N packets unACKed packets sent out to the network.

> What is Go-back-N?

- The receiver will send an ACK for the most recently received "in-order" packet
	- ACKs the packet with the highest packet number that has no missing preceding packets.
	- Receiver ignores packets that came in after a missing packet.
- Sender resends packets starting with the next packet after the one the receiver ACKed.
- Receiver can discard duplicates.

> What is selective ACKing?

- Sender retransmits only packets that it suspects were lost.
- Receiver buffers as many out-of-order packets as space allows, with the hope that the sender correctly guesses the number of packets that were missing.
- Receiver ACKs correctly received packets even when it's not in-order.

> What is fast retransmit?

When the sender receives 3 ACKs for the same packet, it considers the packet to be lost, and will retransmit it instead of waiting for the timeout.

> What is transmission control, and why do we need to control it?

Transmission control is used by TCP to adjust the rate that the sender sends data to the receiver. This is to
- Account for network congestion.
- Account for network bandwidth.
- Account for the receiver's available resources (buffer space).

> What is flow control, and why do we need to control it?

Flow control is transmission control which protects the receiver's buffer.
- This is based on a "receive window" variable maintained by the receiver.
- TCP ensures that the last byte received, minus the last byte read, is less than or equal to the receiver's buffer. `rwnd` is equal to `Rcv Buffer Size - [Last Byte Rcvd - Last Byte Read]`
- The receiver advertises the `rwnd` variable's value in every ACK it sends back to the sender.

The sender uses this variable to ensure that `Last Byte Sent - Last Byte Acked` is less than or equal to `rwnd`.

> What is congestion control?

Congestion control is transmission control that protects the network from too much traffic.

> What are the goals of congestion control?

The goal of congestion control is to ensure that the network is used optimally, while also being protected from too much traffic overwhelming. At a high level, TCP congestion control attempts to promote
- Efficiency
- Fairness
- Low Delay
- Fast Convergence

> What is network-assisted congestion control?

This is when the network layer provides feedback to senders about the overall congestion level in the network.

> What is end-to-end congestion control?

The network layer provides no assistance, the transport layer must probe the network for indications that the network is congested all on its own.

> How does a host infer congestion?

- packet delays (changes/variability wrt RTT)
- packet loss

> How does a TCP sender limit the sending rate?

The number of packets that TCP senders will send to the network is maintained on the sending side using a "congestion window" variable.

> Explain Additive Increase/Multiplicative Decrease (AIMD) in the context of TCP.

- TCP will "probe" the network by gradually increasing the number of packets it sends at any given time. It does this by adding a constant value to the "congestion window" variable (additive increase).
- In the event of packet loss, TCP will decrease the number of packets by dividing the congestion window by a constant vale (multiplicative decrease)

> What is a slow start in TCP?

"slow start" in TCP is the period of time immediately following the start of a TCP connection. The sender will increase the "congestion window" variable exponentially up to a preset threshold (or until packet loss is detected).

"slow start" is a bit of a misnomer because it's much faster than using "additive increase" all the way to the same threshold.

![[Pasted image 20231006200549.png]]

> Is TCP fair in the case where connections have the same RTT? Explain.

Yes. Even if 2 flows start at different times, the AIMD algorithm will eventually cause both flows to converge at the same throughput.

> Is TCP fair in the case where two connections have different RTTs? Explain.

It depends on the TCP variant. TCP Reno uses ACK-based adaptation of the congestion window. Therefore, connections with smaller RTTs will increase their congestion window faster than connection with higher RTTs.

TCP CUBIC addresses this issue.

> Explain how TCP CUBIC works.

TCP Cubic has a lot of different improvements over standard TCP and TCP Reno.
- the congestion window is increased based on absolute time, so its fair to streams with different RTTs
- following a packet loss, the congestion window is increased according to a cubic function, so that the congestion window
	- quickly increases back to the level it was at prior to dividing the congestion window by 2
	- plateaus at that value for a while
	- exponentially increases again to probe the network

![[Pasted image 20230903130312.png]]

> Explain TCP throughput calculation.

Integrating (finding the area under) the plot of the congestion window is a good way to measure the throughput of TCP based only on the historical values of the congestion window value.

![[Pasted image 20230903131348.png]]

## Lesson 3: Intradomain Routing
[[Lesson 03 - Intradomain Routing]]

> What is the difference between forwarding and routing?

- Forwarding is what a router does when it moves a packet from an input link to an output link.
- Routing is what a collection of routers do. Each individual router forwards packets to each other. The process of moving one packet across a network from its source to its destination is called routing. Routing also refers to collections of routers working together to find the "good routes" through the network.

> What is the main idea behind a link-state routing algorithm?

- global algorithm
- all nodes understand the entire network topology
- each node determines the shortest path and the cost of each path from itself to every other node in the network

> What is an example of a link-state routing algorithm? Walk through an example of the link-state routing algorithm.

$u$ is the node currently executing the algorithm.

![[Pasted image 20230906135848.png]]

- Start by calculating the distance from node U to each of its neighbors. Store those distances.
	- Store the letter U as the "node that we need to pass through to reach the node for the lowest distance". 
	- If a node is not adjacent to U, the distance to that node is infinity.
- Create a set of nodes. Add node U.
- For each node not in the set of nodes we just defined, we're going to reassess all of the nodes that are adjacent to that node, for its distance to U.
	- Pick the node that U has the lowest cost to reach which is not in the set of nodes we defined.
	- Check the distance from U to each neighbor of the selected node, passing through the neighbor.
	- If the distance to that neighbor is lower than the currently stored distance from U, update the table.

> What is the computational complexity of the link-state routing algorithm?

$O(n^2)$

> What is the main idea behind the distance vector routing algorithm?

the DV routing algorithm is a distributed, iterative, and asynchronous algorithm, in which each node
- maintains its own distance vector (the costs required to reach each other node in the network)
- periodically sends its distance vector to its neighbors
- updates its distance vector based on information received from other nodes in the network

The core of this algorithm is the bellman ford algorithm.

> Walk through an example of the distance vector algorithm.

The core of this algorithm is the bellman ford algorithm. Each node sends their own personal distance vector to each other. Receiving nodes check received messages to see if they need to update their own distance vector. If they changed their distance vector, they need to rebroadcast their own distance vector.

Walking through this one on a midterm would be hell.

> When does the count-to-infinity problem occur in the distance vector algorithm?

The count-to-infinity problem happens when a link in a network suddenly increases in value. Typically this results in a 2+ nodes believing that the shortest route to some third node is through each other. The nodes will keep sending incremental increases in their DVs back and forth until they settle on the actual cost of navigating the network.

> How does poison reverse solve the count-to-infinity problem?

Essentially, using an example
- Nodes A, B, and C form a fully connected graph.
- Node A's shortest path to C is through B.
- Node A will "lie" to node B and say that its path to C is $\approx \infty$.

i.e. some nodes will "lie" to other nodes about the cost to reach another node.

> What is the Routing Information Protocol (RIP)?

- Based on the Distance Vector protocol
- Routers periodically send RIP advertisements to other routers containing information about the sender's distance to destination subnets.
- Routers maintain routing tables, which contain a forwarding table and distance vector.

> What is the Open Shortest Path First (OSPF) protocol?

- Uses the link-state routing algorithm to find the best path between source and destination routers
- Improvement to RIP
- Uses flooding of link-state info
- Uses Dijkstra's least-cost path algorithm

> How does a router process advertisements?

Like this.

![[Pasted image 20230913111212.png]]

> What is hot potato routing?

Hot potato routing is the practice of choosing a path within the network by choosing the closest egress point based on intradomain path cost.

The idea is to get traffic out of the network as soon as possible to reduce the resource utilization of the traffic existing in the network.
## Lesson 4: AS Relationships and Interdomain Routing
[[Lesson 04 - Autonomous Systems]]

> Describe the relationships between ISPs, IXPs, and CDNs.

- ISP: Internet service provider
- IXP: Internet exchange point
- CDN: Content delivery network

Each type of network has its own business goals which result in different business relationships and interconnection strategies.

These relationships used to be hierarchical, but these days the internet is pretty flat.

> What is an AS?

An AS is an autonomous system, and is defined as a group of routers (and other network hardware) that are all under the same administrative domain. Each of the types of network described above (ISP, IXP, CDN) can be operated as one or multiple ASes.

> What kind of relationship does AS have with other parties?

An AS can have the following relationships with other parties
- provider-customer relationship (aka "transit")
- peering relationship

> What is BGP?

- BGP: Border gateway protocol.
- BGP outlines ASes deciding to import and export routes through the relationships they have with other ASes. Route importing/exporting generally follows business decisions to maximize profit / reduce cost of routing traffic.

> How does an AS determine what rules to import/export?

- import
	 - Customer routes > peer routes > transit provider routes
	- ASes will try to import routes from peered ASes that the AS would otherwise have to pay to use alternative routes.
	- ASes will avoid importing routes from other ASes if the AS profits from using alternative routes.
	- ASes will import routes if it has no other alternative route for getting data to the destination.
- export
	- An AS will advertise routes that it learned from its customers to its peers. If more traffic goes to a customer of an AS, the AS will profit more from that customer.
	- An AS will not advertise routes that it learned from its providers to its peers, as there is no business incentive for doing so. An AS will however advertise those routes to its customers.
	- An AS will not advertise routes learned from its peers to other peers. That only increases the traffic through the AS at additional cost with no additional revenue coming in. The AS will however advertise those routes to its customers.

> What were the original design goals of BGP? What was considered later?

- Scalability
- Express routing policies
- allow cooperation among ASes
- Security (added later)

> What are the basics of BGP?

- BGP peers (2 peered routers) exchange routing information over a TCP connection known as a "BGP session"
- the 2 routers will then begin to exchange messages with each other
- The main message is an `UPDATE` message, which can be used to announce new routes, alter previously advertised routes, and withdraw previously advertised routes.

> What is the difference between iBGP and eBGP?

- i = internal
- e = external
- eBGP is used to advertise / revoke routes between 2 different ASes.
- iBGP is used within an AS to broadcast route changes to all of the routers within the AS.

> What is the difference between iBGP and IGP-like protocols (RIP or OSPF)?

- iBGP is only used to share routes that were learned through BGP with other ASes.
- IGP protocols are used for finding efficient paths within an AS.

> How does a router use the BGP decision process to choose which routes to import?

- LocalPref is used for assigning a hierarchy of routes.
- Routers use LocalPref when deciding which routes to use.

> What are the 2 main challenges with BGP? Why?

- Scalability (when routes are too granular)
- Misconfiguration (when an AS is managed poorly or maliciously)

> What is an IXP?

An IXP is an "internet exchange point". IXPs connect multiple different ASes/networks together, charge membership fees, and provide a range of services to their members, not limited to just routing packets between different ASes.

> What are four reasons for IXP's increased popularity?

- Higher bandwidth.
- Lower costs.
- Lower latency.
- Incentives imparted by other ASes connected to the IXP.

> Which services do IXPs provide?

- public peering
- private peering
- route servers
- SLAs
- Remote peering
- Mobile peering
- DDoS blackholing
- Internet Routing Registries (IRRs)
- consumer broadband speed tests
- DNS root name servers
- country-code top-level domain (ccTLD) nameservers
- NTP

> How does a route server work?

A route server (RS) is infrastructure that exists at an IXP to manage/broker BGP session / advertisements among member ASes (multilateral peering sessions). This is to cut down on the amount of cross traffic (bilateral peering sessions).

![[Pasted image 20230919132742.png]]

## Lesson 5: Router Design and Algorithms (Part 1)
[[Lesson 05 - Router Design and Algorithms (Part 1)]]

> What are the basic components of a router?

- Forwarding / switching function
- input / output ports
- switching fabric
- control plane

> Explain the forwarding (or switching) function of a router.

- Moves packets from input ports to output ports
- Makes physical connection between input and output ports
- There are 3 types of switching fabrics
	- memory
	- crossbar
	- bus

> The switching fabric moves the packets from input to output ports. What are the functionalities performed by the input and output ports?

- input ports
	- physically terminate incoming links to the router
	- decapsulates packets
	- performs lookup function against the router's forwarding table
	- sends the packet to the appropriate output port through the switching fabric
- output ports
	- receives packets from the switching fabric
	- sends them out over the outgoing link

> What is the purpose of the router’s control plane?

The control plane is software running on the router which can adjust the operation of the router (i.e. changes to the forwarding/forwarding tables). Routers can have a locally running control plane or can be managed remotely.

> What tasks occur in a router?

see above

> List and briefly describe each type of switching. Which, if any, can send multiple packets across the fabric in parallel?

- memory
	- input links copy packets to router's memory
	- output links copy packets from router's memory
	- Copies are slow, but can theoretically be done in parallel
- bus
	- All input/output links are connected by a bus
	- only one packet can cross the bus at a time
	- much better per-packet performance, worse all-packet performance
- interconnection network (aka crossbar)
	- 2N busses connect all N input links to all N output links
	- packets can cross this network in parallel, but specialized algorithms are required for determining which packets can cross the switching fabric simultaneously, and scheduling those transfers.

> What are two fundamental problems involving routers, and what causes these problems?

- bandwidth, as the size of the internet grows, we impart increased demand on routers to move traffic through a network
- services at high speeds, similar to the previous point, routers provide many high-level services, which can be difficult to operate at speed and at scale.
- 

> What are the bottlenecks that routers face, and why do they occur?

All systems have bottlenecks. Routers have many places where bottlenecks can happen
- bandwidth of an outgoing link
- bandwidth of switching fabric
- performance of address lookup in switching/forwarding tables
- QoS guarantees
- security guarantees

> Convert between different prefix notations (dot-decimal, slash, and masking).

- dot-decimal notation is just a collection of octets (a single byte) or a string of binary digits.
	- `123.234`
- slash notation is a base address plus a length denoting the number of relevant bits
	- `123.234.0.0/16`
- masking is specifying a base address, then using a separate mask to denote which bits are important.
	- `123.234.0.0`
	- `255.255.0.0`

> What is CIDR, and why was it introduced?

- Classless Internet Domain Routing (CIDR)
- It was introduced due to the rapid exhaustion of ip addresses.
- Assigns IP addresses using arbitrary-length prefixes.
- Helps decrease routing table size, makes address lookup more difficult (i.e. when some prefixes contain others)

> Name 4 takeaway observations around network traffic characteristics. Explain their consequences.

1. Measurement studies on network traffic had shown a large number (in the order of hundreds of thousands (250,000 according to a measurement study in the earlier days of the Internet) of concurrent flows of short duration. This already large number has only been increasing, and as a consequence, caching solutions will not work efficiently. 
2. The important element of any lookup operation is how fast it is done (lookup speed). A large part of the cost of computation for lookup is accessing memory.
3. An unstable routing protocol may adversely impact the update time in the table: add, delete or replace a prefix. Inefficient routing protocols increase this value up to additional milliseconds.
4. A vital trade-off is memory usage. We can use expensive fast memory (cache in software, SRAM in hardware) or cheaper but slower memory (e.g., DRAM, SDRAM).

> Why do we need multibit tries?

Multibit tries are useful because they decrease the number of memory access required to perform address lookup compared to unibit tries.

> What is prefix expansion, and why is it needed?

Prefix expansion is necessary for converting prefixes of any length to a format that can be used in a multibit trie with a fixed-length stride. Prefixes in a multibit trie must 

> Perform a prefix lookup given a list of pointers for unibit tries, fixed-length multibit ties, and variable-length multibit tries.



> Perform a prefix expansion. How many prefix lengths do old prefixes have? What about new prefixes?

```
P1 = 101*
P2 = 111*
P3 = 11001*
P5 = 0*
P6 = 1000*
P7 = 100000*
P8 = 100*
P9 = 110*
```

Stride length 3

P1 -> 101*
P2 -> 111*
P7 -> 100000*
P8 -> 100*
P9 -> 110*

P3 -> 110010*
P3 -> 110011*

P5 -> 000*
P5 -> 001*
P5 -> 010*
P5 -> 011*

P6 -> ~~100000*~~ Fails because of P7.
P6 -> 100001*
P6 -> 100010*
P6 -> 100011*

> What are the benefits of variable-stride versus fixed-stride multibit tries?

- fixed stride multibit tries
	- Better efficiency
- variable stride multibit tries
	- more flexible
	- prefix database does not need as much prefix expansion, so the prefix DB can be smaller
	- requires more computations to determine the relevant portion of the prefix when performing searches
## Lesson 6: Router Design and Algorithms (Part 2)
[[Lesson 06 - Router Design and Algorithms (Part 2)]]

> Why is packet classification needed?

1. Firewalls
2. Packet priority (Resource preservation (reservation?) protocols)
3. Routing based on traffic type

> What are three established variants of packet classification?



> What are the simple solutions to the packet classification problem?

- Linear Search
- Caching
- Passing Labels

> How does fast searching using set-pruning tries work?

Set pruning tries are used for 2 dimensional packet classification schemes, where the 2 dimensions are Destination IP and Source IP. In this scenario, you generate a Trie based on one of the IP addresses. At relevant points along the trie, you "hang" tries based on the other IP address, for all rules that are relevant to that point in the trie.

> What’s the main problem with the set pruning tries?

High memory cost

> What is the difference between the pruning approach and the backtracking approach for packet classification with a trie?

- The set pruning approach duplicates rules
- the backtracking approach only stores a single copy of each rule
- The backtracking approach has high time complexity

> What’s the benefit of a grid of tries approach?

- Set pruning method has high algorithmic memory complexity
- Backtracking method has high algorithmic time complexity

The grid of tries approach extends the backtracking method by "precomputing" pointers from failure conditions to the next branch of the trie that would match. These are called "switch pointers".

> Describe the “Take the Ticket” algorithm.

The "take the ticket" algorithm is an algorithm used by switches to determine which input link gets to connect to which output link at any given time. In each round,
1. an input link makes a request to send a packet to an output link.
2. The output links determine which input links get "tickets" i.e. a timeslice for sending a packet across the switching fabric.
3. Then the input links connect to the output links that they were given a ticket for and send their packet across.

> What is the head-of-line problem?

If an input link is using an in-order queue to keep track of the packets that it's trying to send to output links, and the first packet in that queue waits for multiple rounds to send a packet to an output link, then all of the packets in the queue are blocked waiting for the "head-of-line" to move.

> How is the head-of-line problem avoided using the knockout scheme?

The knockout scheme relies on the switching fabric breaking up packets into smaller chunks so that some data from all inputs in each timeslice. The switching fabric runs at some speed faster than the input links.

> How is the head-of-line problem avoided using parallel iterative matching?

Instead of using a queue in the input links, each input link has a bucket of packets that it is trying to push through the switching fabric. In each round, each input link makes a request across the fabric to all of the output links that it would like to send packets to. Each output links grants access to one of the input links.

This allows input queues to send packets across the switching fabric out-of-order.

> Describe FIFO with tail drop.

- packets enter on input links
- packets that arrive earlier get processed earlier
- if the buffer is full, then newly arrived packets are dropped.

> What are the reasons for making scheduling decisions more complex than FIFO?

- QoS guarantees.
- Fairness in sharing bandwidth among all links.
- Router support for congestion.

> Describe Bit-by-bit Round Robin scheduling.

- each queue gets a timeslice which is normalized based on average packet size. If a link sends a packet that is twice as large, then it'll wait twice as long.
- Lot's of complicated math and algorithms for determining which queues get to go next.
- This one never really made it out of the lab.

> Bit-by-bit Round Robin provides fairness; what’s the problem with this method?

High time complexity in determining which queue gets to go next.

> Describe Deficit Round Robin (DRR).

- Input queues are triggered using round robin.
- Input queues get a "budget" (quantum) for how much data they can send during their turn.
- If they don't use their whole budget during their turn, the remainder is added to a "deficit" counter.
- Each round, queues have access to the "quantum" amount plus their deficit.
- If they have a packet that's larger than their current bank account, they can just wait for a future turn to send it.

> What is a token bucket shaping?

- each input has a data buffer
- each input has a buffer of tokens
- if the input is out of tokens, the input buffers packets
- as tokens come in, the input can push data to an output

> In traffic scheduling, what is the difference between policing and shaping?

- policing, if a queue sends too much data, the amount that goes over the limit is dropped.
- shaping, if a queue has too much data to send, it will be coerced into slowing down to only send the right amount

![[Pasted image 20231004121029.png]]

> How is a leaky bucket used for traffic policing and shaping?

- Algorithm which can be used in both policing and shaping
- Bucket has capacity $b$
	- represents a packet buffer
	- water corresponds to incoming packets
- Leak rate $r$
	- represents the rate at which packets are allowed to enter the network
	- This rate is constant irrespective of the bucket's fill rate
- Behavior
	- If an arriving packet does not cause an overflow when added to the bucket, it is said to be conforming. Packets classified as conforming are added to the bucket.
	- Otherwise, it is said to be non-conforming. non-conforming packets are discarded.
