---
tags:
  - OMSCS
  - CN
---
# Lesson 06 - Router Design and Algorithms (Part 2)

## Why do we need packet classification?

Some examples of packet classification include:
1. Firewalls
	1. Routers implement firewalls at the entry/exit points of the network
	2. filter out unwanted traffic
	3. enforces security policies
2. Resource preservation protocols
	1. DiffServ has been used to reserve bandwidth between a source and destination
3. Routing based on traffic type
	1. Helps avoid delays for time-sensitive applications

![[Pasted image 20230929183340.png]]

> The above figure shows an example topology where networks are connected through router R. Destinations are shown as S1, S2, X, Y, and D. L1 and L2 denote specific connection points for router R. The table shows some examples of packet classification rules. The first rule is for routing video traffic from S1 to D via L1. The second rule drops all traffic from S2, for example, in the scenario that S2 was an experimental site. Finally, the third rule reserves 50 Mbps of traffic from prefix X to prefix Y, which is an example of a rule for resource reservation.

## Simple Solutions for Packet Classification
### Linear Search
- Firewall implementations perform a linear search of the rules DB and keep track of the best-match rule
- The solution can be reasonable for a few rules.
- Large DBs result in high latency

### Caching
- Cache results so that future searches can run faster
- 2 issues
	- Need to perform the search for missed cache hits
	- Even with a high cache hit rate, a slow search can dominate the search time complexity

### Passing Labels
> The Multiprotocol Label Switching (MPLS) and DiffServ use this technology. MPLS is useful for traffic engineering. First, a label-switched path is set up between sites A and B. Then, before traffic leaves site A, a router does packet classification and maps the web traffic into an MPLS header. Then the intermediate routers between A and B apply the label without having to redo packet classification. DiffServ follows a similar approach, applying packet classification at the edges to mark packets for special quality-of-service.

## Fast Searching Using Set-Pruning Tries
A two-dimensional rule is a packet classification scheme where you want to classify packets based on their source and destination IP addresses.

![[Pasted image 20231002105235.png]]

Simplest approach is to build a trie based on destination IPs then "hang" tries based on the source IPs

![[Pasted image 20231002105649.png]]

> By S1, we denote the source prefix of rule R1, S2 of rule R2, etc. Thus for every destination prefix _D_ in the destination trie, we "_prune"_ the set of rules to those compatible with _D_. 

> We first match the destination IP address in a packet in the destination trie. Then we traverse the corresponding source trie to find the longest prefix match for the source IP. The algorithm keeps track of the lowest-cost matching rule. Finally, the algorithm concludes with the least-cost rule.

> The problem that we need to solve now is which source prefixes to store at the sources tries

> For example, let's consider the destination D = 00*. Both rules R4 and R5 have D as the destination prefix. So the source tries for D will need to include the source prefixes 1* and 11*. But if we restrict to 1* and 11*, this is not sufficient. Because the prefix 0*, also matches 00*,  and it is found in rules R1, R2, R3, R7. So we will need to include all the corresponding source prefixes. 

> Moving forward, the problem with the set pruning tries is memory explosion. Because a source prefix can occur in multiple destination tries.

## Reducing Memory using Backtracking
- The set pruning approach has a high cost in memory to reduce time. 
- The opposite approach is to pay in time to reduce memory. 

> Let's assume a destination prefix D. The backtracking approach has each destination prefix D point to a source trie that stores the rules whose destination field is exactly D. The search algorithm then performs a "backtracking" search on the source tries associated with all ancestors of D.

> So first, the algorithm goes through the destination trie and finds the longest destination prefix D matching the header. Then it works its way back up the destination trie and searches the source trie associated with every ancestor prefix of D that points to a nonempty source trie. 

> Since each rule is stored exactly once, the memory requirements are lower than the previous scheme. But, the lookup cost for backtracking is worse than for set-pruning tries.

## Grid of Tries
- Set pruning method has high algorithmic memory complexity
- Backtracking method has high algorithmic time complexity

We can optimize the backtracking approach by making "switch pointers". Switch pointers precompute backtracking by pointing to the next possible source trie containing the matching rule at relevant failure points.

![[Pasted image 20231002105235.png]]

> Consider searching for the packet with a destination address 001 and source address 001. We start the search with the destination trie, which gives us _D_ = 00 as the best match. The search at that point for the source trie fails. Instead of backtracking, the grid of tries has a switch pointer (labeled 0) that points to x. At which point it fails again. We follow another switch pointer to node y. At that point, the algorithm terminates.

![[Pasted image 20231003155058.png]]

![[Pasted image 20231003155107.png]]

## Scheduling and Head-of-Line Blocking
### Scheduling
> Let’s assume that we have an N-by-N crossbar switch with N input lines, N output lines, and N2 crosspoints. Each crosspoint needs to be controlled (on/off), and we need to make sure that each input link is connected with at most one output link. Also, we want to maximize the number of input/output links pairs that communicate in parallel for better performance.

## Take-a-Ticket Algorithm
> A simple scheduling algorithm is the “take-the-ticket algorithm”. Each output line maintains a distributed queue for all input lines that want to send packets to it. When an input line intends to send a packet to a specific output line, it requests a ticket. Then, the input line waits for the ticket to be served. At that point, the input line connects to the output line, the crosspoint is turned on, and the input line sends the packet.

> For example, let’s consider the figure below that shows three input lines that want to connect to four output lines. Next to each input line, we see the queue of the output lines it wants to connect with. For example, input lines A and B want to connect with output lines 1, 2, and 3.

![[Pasted image 20231003161036.png]]

> In the first round, the input lines make ticket requests. For example, line A requests a ticket for output link 1. The same for B and C. So output link 1 grants three tickets, and it will process them in order. First, the ticket for A, then for B, and then for C. Input A observes that its ticket is served, so it connects to output link 1 and sends the packet.    

> In the second round, A repeats the process to request a ticket and connect with link 2. Also, B requests a ticket and connects with output link 2.

> In the third round, A and B move forward, repeating the steps for their next connection. C gets the chance to make its first request and connect with output link 1. All this time, C was blocked, waiting for A and B.    

> The following figure shows how the entire process progresses. We can see the timeline for each output link as it connects with input links. The empty spots mean there was no packet sent at the corresponding time.

![[Pasted image 20231003161140.png]]

> As we see, while A sends its packet in the first iteration, the entire queue for B and C is waiting. We refer to this problem as **head-of-line (HOL) blocking** because the entire queue is blocked by the progress of the head of the queue.

## Avoiding Head-of-Line Blocking
### Output Queuing
> Suppose that we have an N-by-N crossbar switch. Can we send the packet to an output link without queueing? If we could, then assuming that a packet arrives at an output link, it can only block packets sent to the same output link. We could achieve that if we have the fabric running N times faster than the input links. 

> A practical implementation of this approach is the **Knockout scheme**. It relies on breaking up packets into fixed sizes (cell). In practice, we suppose that the same output rarely receives N cells, and the expected number is k (smaller than N). Then we can have the fabric running k times as fast as an input link instead of N. We may still have scenarios where the expected case is violated. To accommodate these scenarios, we have one or more of a primitive switching element that randomly picks the chosen output:

- k = 1 and N = 2. Randomly pick the output that is chosen. The switching element, in this case, is called a _concentrator._ 
- k = 1 and N > 2. One output is chosen out of N possible outputs. We can use the same strategy of multiple 2-by-2 concentrators in this case.
- k needs to be chosen out of N possible cells, with k and N arbitrary values. We create k knockout trees to calculate the first k winners. 

> The drawback with this approach is that is it is complex to implement.
### Parallel Iterative Matching
> The main idea is that we can still allow queueing for the input lines, but in a way that avoids the head-of-line blocking. With this approach, we schedule both the head of the queue and more packets so that the queue makes progress in case the head is blocked. 

> How can we do that? Let's suppose that we have a single queue at an input line. We break down the single queue into virtual queues, with one virtual queue per output link. 

> Let's consider the following graph that shows A, B, C input links and 1, 2, 3, 4 output links. 

> The algorithm runs in three rounds. 

> In the first round, the scheme works by having all inputs send requests in _parallel_ to all outputs they want to connect with. This is the request phase of the algorithm. 

> In the grant phase, the outputs that receive multiple requests pick a random input, so the output link 1 randomly chooses B. Similarly, the output link 2 randomly chooses A (between A and B).

![[Pasted image 20231003164424.png]]

![[Pasted image 20231003164435.png]]

![[Pasted image 20231003164451.png]]

> Finally, in the accept phase, inputs that receive multiple grants randomly pick an output to send to. 

> We have two output ports (2 and 3) that have chosen the same input (A). A randomly chooses port 2. B and C choose 1 and 4, respectively. 

> In the second round, the algorithm repeats by having each input send to two outputs. And finally, the third row repeats by having each input send to one output. 

> Thus, all the traffic is sent in four cell times (of which the fourth cell time is sparsely used and could have been used to send more traffic). This is more efficient than the take-a-ticket.

## Scheduling Introduction
> Busy routers rely on scheduling to handle routing updates, management queries, and data packets. For example, scheduling enables routers to allow certain types of data packets to get different services from other types. It is important to note that this scheduling is done in real-time. Due to the increasing link speeds (over 40 gigabit), these scheduling decisions need to be made in the minimum inter-packet times!

### FIFO with tail drop
- packets enter router on input links
- lookup via address lookup component. Returns output link number
- The switching system within the router then places the packet in the corresponding output port
- This port is a FIFO (first-in, first-out) queue. If the output link buffer is completely full, incoming packets to the tail of the queue are dropped.

This results in fast scheduling decisions but a potential loss in important data packets.

### Need for Quality of Service (QoS)
> There are other methods of packet scheduling such as priority, round-robin, etc. These methods are useful in providing quality of service (QoS) guarantees to a flow of packets on measures such as delay and bandwidth. A flow of packets refers to a stream of packets that travels the same route from source to destination and requires the same level of service at each intermediate router and gateway. In addition, flows must be identifiable using fields in the packet headers. For example, an internet flow could consist of all packets with either a source or destination port number of 23.

> The reasons to make scheduling decisions more complex than FIFO with tail drop are:

> **Router support for congestion.** Congestion in the internet is increasingly possible as the usage has increased faster than the link speeds. While most traffic is based on TCP (which has its own ways to handle congestion), additional router support can improve the throughput of sources by helping handle congestion.

> **Fair sharing of links among competing flows.** During periods of backup, these packets tend to flood the buffers at an output link. If we use FIFO with tail drop, this blocks other flows, resulting in important connections on the clients’ end freezing. This provides a sub-optimal experience to the user, indicating a change is necessary!

> **Providing QoS guarantees to flows.** One way to enable fair sharing is to guarantee certain bandwidths to a flow. Another way is to guarantee the delay through a router for a flow. This is noticeably important for video flows – without a bound on delays, live video streaming will not work well.

Thus, finding time-efficient scheduling algorithms that provide guarantees for bandwidth and delay are important!

## Deficit Round Robin
> We saw that the FIFO queue with tail drop could drop important flows. We consider round-robin to avoid this and introduce fairness in servicing different flows. If we alternate between packets from different flows, the difference in packets sizes could result in some flows getting serviced more frequently. To avoid this, researchers came up with **bit-by-bit round robin**.

Effectively, this is round robin, but each queue gets a timeslice which is normalized based on average packet size.

It doesn't actually split each packet into bits and round robin the bits from each queue. That would be inefficient. Also you can't transmit half a packet.

> Let $R(t)$ be the current round number at time $t$. If the router can send $µ$ bits per second and the number of active flows is $N$, the rate of increase in round number is given by

$dR / dt = µ / N$

> The rate of increase in round number is inversely proportional to the number of active flows. An important takeaway is that the number of rounds required to transmit a packet does not depend on the number of backlogged queues.

> Consider a flow α. Let a packet of size p bits arrive as the i-th packet in the flow. If it arrives at an empty queue, it reaches the head of the queue at the current round $R(t)$. If not, it reaches the head after the packet in front of it finishes it. Combining both the scenarios, the round number at which the packet reaches the head is given by

$S(i) = max( R(t), F(i−1) )$

> where $R(t)$ is the current round number, and $F(i−1)$ is the round at which the packet ahead of it finishes. The round number at which a packet finishes, which depends only on the size of the packet, is given by

$F(i) = S(i) + p(i)$

> where $p(i)$ is the size of the i-th packet in the flow. Using the above two equations, the finish round of every packet in a queue can be calculated.

### Packet-level Fair Queuing
> This strategy emulates the bit-by-bit fair queueing by sending the packet with the smallest finishing round number. At any round, the packet chosen to be sent out is garnered from the previous round of the algorithm. The packet which had been starved the most while sending out the previous packet from any queue is chosen. Let’s consider the following example:

![[Pasted image 20231003174159.png]]

> The figure above shows the state of the packets along with their finishing numbers (F) in their respective queues, waiting to be scheduled.

![[Pasted image 20231003174212.png]]

> The packet with the smallest finishing number (F=1002) is transmitted. This represents the packet that was the most starved during the previous round of scheduling.

![[Pasted image 20231003174227.png]]

> Similarly, in the next round (above figure), the packet with F=1007 is transmitted, and in the subsequent round (below figure), the packet with F=1009 is transmitted.

![[Pasted image 20231003174240.png]]

> Although this method provides fairness, it also introduces new complexities. We will need to keep track of the finishing time at which the head packet of each queue would depart and choose the earliest one. This requires a priority queue implementation, which has a time complexity that is logarithmic in the number of flows! Additionally, if a new queue becomes active, all timestamps may have to change – an operation with time complexity linear in the number of flows. Thus, the time complexity of this method makes it hard to implement at gigabit speeds.

### Deficit Round Robin (DRR)
> Although the bit-by-bit round-robin gave us bandwidth and delay guarantees, the time complexity was too high. It is important to note that several applications benefit only by providing bandwidth guarantees. We could use a simple constant-time round-robin algorithm with a modification to ensure fairness.

> We assign a quantum size, $Q_i$, and a deficit counter, $D_i$, for each flow. The quantum size determines the share of bandwidth allocated to that flow. For each turn of round-robin, the algorithm will serve as many packets in the flow i with size less than ($Q_i + D_i$). If packets remain in the queue, it will store the remaining bandwidth in Di for the next run. However, if all packets in the queue are serviced in that turn, it will clear $D_i$ to 0 for the next turn.

![[Pasted image 20231003174406.png]]

![[Pasted image 20231003174413.png]]

> In this router, there are four flows – F1, F2, F3, and F4. The quantum size for all flows is 500. Initially, the deficit counters for all flows are set to 0. Initially, the round-robin pointer points to the first flow. The first packet of size 200 will be sent through. However, the funds are insufficient to send the second packet of size 750. Thus, a deficit of 300 will remain in D1. For F2, the first packet of size 500 will be sent, leaving D2 empty.

> Similarly, the first packets of F3 and F4 will be sent with D3 = 400 and D4 = 320 after the first iteration. For the second iteration, the D1+ Q1 = 800, meaning there are sufficient funds to send the second and third packets through. Since there are no remaining packets, D1 will be set to 0 instead of 30 (the actual remaining amount).

## Traffic Scheduling: Token Bucket
> There are scenarios where we want to set bandwidth guarantees for flows in the same queue without separating them. For example, we can have a scenario where we want to limit a specific type of traffic (e.g., news traffic) in the network to no more than X Mbps without putting this traffic into a separate queue.

> We will start by describing the idea of token bucket shaping. This technique can limit the burstiness of a flow by: a) limiting the average rate (e.g., 100 Kbps), and b) limiting the maximum burst size (e.g., the flow can send a burst of 4KB at a rate of its choice).

![[Pasted image 20231003174700.png]]

> The bucket shaping technique assumes a bucket per flow that fills with tokens with a rate of R per second, and it also can have up to B tokens at any given time. If the bucket is full with B tokens, additional tokens are dropped. When a packet arrives, it can go through if there are enough tokens (equal to the size of the packet in bits). If not, the packet needs to wait until enough tokens are in the bucket. Given the max size of B, a burst is limited to B bits per second.

> In practice, the bucket shaping idea is implemented using a counter (can’t go more than max value B, and gets decremented when a bit arrives) and a timer (to increment the counter at a rate R).

> The problem with this technique is that we have one queue per flow. This is because a flow may have a full token bucket, whereas other flows may have an empty token bucket and, therefore, will need to wait.

> We use a modified version of the token bucket shaper to maintain one queue, called **token bucket policing**. Here, if a packet arrives and there are no tokens in the bucket, it is dropped.

## Traffic Scheduling: Leaky Bucket
> Traffic policing and traffic shaping are mechanisms to limit the output rate of a link. The output rate is controlled by identifying traffic descriptor violations and then responding to them in two different ways.

![[Pasted image 20231004121029.png]]

- Policing
	- When traffic rate reaches the max configured rate, the excess traffic is dropped.
	- Results in sawtooth-like bitrates.
	- Senders must retransmit dropped packets
- Shaping
	- Shaper retains excess packets in a queue or buffer
	- Excess is scheduled for later transmission
	- Excess traffic is delayed rather than dropped

Shaping and policing can work in tandem.

### Leaky Bucket
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

![[Pasted image 20231004122033.png]]

