---
tags: OMSCS, CN
---
# Lesson 03 - Intradomain Routing
> Focuses on the network layer and a specific function of the network layer: routing within a single administrative domain.

This lesson will cover...

- 2 types of intradomain routing algorithms
	- link-state (LS)
	- distance-vector (DV)
- some example protocols
	- Open Shortest Path First (OSPF)
	- Routing Information Protocol (RIP)
- challenges that intradomain routing protocols face (i.e. convergence delay)
- how routing protocols can be used for more than determining "good" paths
	- traffic engineering, avoiding congested links

## Readings and Additional Resources

### Required

[[Experience in Black-box OSPF Measurement.pdf]]

> In this paper, we present black-box methods (i.e., measurements that rely only on external observations) for estimating and trending delays for key internal tasks in OSPF:
> - processing Link State Advertisements (LSAs)
> - performing Shortest Path First calculations
> - updating the Forwarding Information Base
> - flooding LSAs.

### Optional

Hot Potatoes Heat Up BGP Routing
https://www.cs.princeton.edu/~jrex/papers/hotpotato.pdf

Traffic Engineering With Traditional IP Routing Protocols
https://www.cs.princeton.edu/~jrex/teaching/spring2005/reading/fortz02.pdf

Dynamics of Hot-Potato Routing in IP Networks
https://www.cs.princeton.edu/~jrex/papers/sigmetrics04.pdf

OSPF Monitoring: Architecture, Design and Deployment Experience
https://www.cs.princeton.edu/~jrex/teaching/spring2005/reading/shaikh04.pdf

## Routing Algorithms
Assume that 2 hosts have established a connection using some transport layer protocol. Each of the 2 hosts knows the default router (first-hop router). A host will send a packet to the default router, but then what happens?

In this lecture, we will see the algorithms that we need so that when a packet leaves the default router of the sending host, it will travel over a path towards the default router of the destination host.

- Routers have forwarding tables
- Routers send packets over corresponding links
- "forwarding" refers to transferring a packet from an incoming link to an outgoing link within a single router.
- "routing" refers to how routers work together using routing protocols to determine the good paths (or good routes, as we call them)
- When the routers all belong to the same administrative domain, that is known as "intradomain routing"
- When routers belong to different administrative domains, that is called "interdomain routing"

This lesson focuses on "intradomain" routing. This is also known as Interior Gateway Protocols (IGPs)

The link-state and distance-vector algorithms are graph algorithms used in solving challenges in this space.
- Routers are nodes
- Links are edges
- Edges have associated costs

Things that can affect the edge costs in a graph model of a network:
- Physical cable length of the link
- Time delay to traverse the link
- Monetary cost of using the link
- Capacity of the link
- Current load on the link (Note: this means that edge weights are _not_ static)

## Link-State Routing Algorithm
> link-state routing algorithms, specifically Dijkstra's algorithm

In link-state algorithms, the link costs and the network topology are known to all nodes. This can be a static configuration, or determined via node->node broadcasts.

### Definition

Terminology
- $u$ represents the source node
- $v$ represents some other node in the network
- $D(v)$ represents the cost of the current least cost path from $u$ to $v$
- $p(v)$ represents the previous node along the current least cost path from $u$ to $v$
- $c(u, v)$ represents the cost from $u$ to directly attached neighbor $v$
- $N'$ represents the subset of nodes along the current least-cost path from $u$ to $v$

**Initialization**
- The algorithm starts with an init step, where we initialize all of the currently known least-cost paths from $u$ to directly attached neighbors. These are the costs of immediate links, which can be easily determined by each node.
- For nodes in the network that are not directly attached to $u$, we initialize the cost of those paths to $\infty$.

**Iteration**
- After the initialization step, the algorithm follows with a loop that is executed for every destination node **v** in the network.
- At each iteration, we look at the set of nodes that are not included in **N’**, and we identify the node, say **w**, with the least cost path from the previous iteration. We add that node **w** into **N’**.
- For every neighbor **v** of **w**, we update **D(v)** with the new cost, which is either the old cost from **u** to **v** (from the previous iteration) or the known least path cost from source node **u** to **w**, plus the cost from **w** to **v** (whichever between the two quantities is the minimum).

```
Initialization:
	N' = {u}
	for all nodes v
		if v is a neighbor of u
			D(v) = c(u,v)
		else
			D(v) = infinity

Loop until N' = N
	find w not in N' such that (w) is a minimum
	N' += {w}
	for each neighbor v of w
		if v not in N'
			D(v) = min(D(v), D(w) + c(w,v))
```

The algorithm exits by returning the shortest paths and their costs from the source node $u$ to every other node $v$ in the network.

**Complexity**
- The first iteration, we need to search all nodes to find the node with the minimum path cost. This needs to be repeated for each subsequent iteration, but the number of nodes that needs to be searched decreases by one each time.
- Note that the number of iterations is independent of the number of nodes that are connected to the root node.
- $\sum_{x=0}^{n}{n-x}=\frac{n(n+1)}{2}$
- This complexity is proportional to $O(n^2)$
### Example
![[Pasted image 20230906134712.png]]

![[Pasted image 20230906135848.png]]

## Distance Vector Routing
The DV routing algorithm is
- **iterative**: the algorithm iterates until the neighbors do not have new updates to send to each other
- **asynchronous**: the algorithm does not require the nodes to be synchronized with each other
- **distributed**: direct nodes send information to one another, and then they resend their results back after performing their own calculations, so the calculations are not happening in a centralized manner

The DV algorithm is based on the **Bellman Ford Algorithm**.
- Each node maintains its own distance vector, with the costs to reach every other node in the network.
- From time to time, each node sends its own distance vector to its neighbor nodes.
- The neighbor nodes in turn, receive that distance vector and they use it to update their own distance vectors.
- Neighboring nodes exchange their distance vectors to update their own view of the network.

Each node $x$ updates its own distance vector using the Bellman Ford equation: $D_{x}(y)=min_{v}(c(x,v), D_{v}(y))$ for each destination node $y$ in the network. A node $x$ computes the least cost to reach destination node $y$ by considering the options that it has to reach $y$ through each of its neighbors $v$. So node $x$ considers the cost to reach neighbor $v$ and then it adds the least cost from the neighbor $v$ to the final destination $y$. It calculates that quantity over all neighbors $v$ and takes the minimum.

![[Pasted image 20230906160812.png]]

### Formal Definition

Each node $x$ updates its own distance vector using the Bellman Ford equation: $D_{x}(y)=min_{v}(c(x,v), D_{v}(y))$

![[Pasted image 20230906160840.png]]

### Example
![[Pasted image 20230906161010.png]]

![[Pasted image 20230906161018.png]]

![[Pasted image 20230906161026.png]]

### Link Cost Changes and Failures in DV
> The "Count to Infinity" Problem

![[Pasted image 20230906161600.png]]

If the `x<->y` link changes to cost 1.
- At time t=0, y detects that the const to x has changed from 4 to 1, so it updates its distance vector and sends it to its neighbors.
- At time t=1, z receives the update from y. Now z thinks it can reach x through y with a cost of 2, so it sends its new distance vector to its neighbors.
- At time t=2, y receives the update from z. Y does not change its distance vector, so it does not send any updates.

In this scenario, we note that there was a decrease in the link cost which propagated quickly among the nodes in one a few iterations.

In the second case, imagine that the link cost changes to 60.

![[Pasted image 20230906161838.png]]

- At t=0, y detects that cost has changed, and it will update its DV thinking that it can still reach x through z with a total cost of 6 (5 + 1).
- At t=1, we have a routing loop, where z thinks it can reach x through y and y thinks it can reach x through z. This will cause packets to bounce back and forth forever between y and z until their tables change.
- z and y keep updating each other about their new cost to reach x. y computes  its new cost to be 6 then informs z. z computes the new cost to be 7 and informs y.

This will go back and forth until z computes the cost to be larger then 50, and will then prefer to reach x directly rather than through y.

This link cost change took a long time to propagate among the nodes of the network. This is known as the "count to infinity" problem.

(The above was typed verbatim from the course materials, for effective absorption. My synthesis below:)

This issue seems to arise because each node doesn't really know the most efficient path from itself to other nodes. Each node only stores the cost of the most efficient path from itself to each other node, but does not know the costs of the links between adjacent nodes. Each node also does not know when the most efficient path from one node to another node passes through itself. For example, in this case:

![[Pasted image 20230906161026.png]]

Node x knows that it can send traffic to node `z` with a cost of 3. It also knows that it has a direct link to `z`, but that the cost of that link is 7. `x` also knows that node `y` has a more efficient route to `z`, so it forwards packets to `z` through `y`. If the `y-z` link explodes in cost, `y` will think that `x` still has an efficient path to `z`.

Essentially it seems like the only way to prevent this using the DV algorithm would be to ensure there's low variability in link costs.

## Poison Reverse
> A solution to the previous problem is the following idea, called a "poison reverse".

![[Pasted image 20230906163230.png]]

Since `z` reaches `x` through `y`, `z` will advertise to `y` that the distance to `x` is infinity: $D_z(x)=\infty$. `z` tell this lie to `y` as long as it knows that it can reach `x` via `y`. Since `y` assumes that `z` has no path to `x` except via `y`, it will never send packets to `x` via `z`.

So `z` poisons the path from `z` to `y`.

*In a way this feels similar to the spanning tree algorithm.*

Things change when the cost from `x` to `y` changes to 60. `y` will update its table and send packets to `x` directly with cost $D_z(x)=60$. `y` will inform `z` about its new cost to `x`. `z` will immediately shift its route to `x` to be be via the direct link `x-z` at cost 50. `z` will inform `y` that $D_z(x)=50$.

When `y` receives this update from `z`, `y` will update $D_y(x)=51=c(y,z)+D_z(x)$.

Since `z` is now on least cost path of `y` to reach `x`, `y` poisons the reverse path from `z` to `x`. `y` tells `z` that $D_y(x)=\infty$ even though $y$ knows that it has a direct link to `x` at cost 60.

*This method helps nodes communicate to other nodes when their most-efficient route to a host routes back through those other nodes.*

Note: This technique will solve the problem with 2 nodes. However, poisoned reverse will not solve a general count to infinity problem involving 3 or more nodes that are not directly connected.

## Distance Vector Routing Protocol Example: RIP
> The routing information protocol (RIP) is based on the Distance Vector (DV) protocol.

> The first version, released as a part of the BSD version of Unix, uses hop count as a metric (i.e. assumes link cost as 1). The metric for choosing a path could be shortest distance, lowest cost, or a load-balanced path. In RIP, routing updates are exchanged between neighbors periodically, using a RIP response message, as opposed to distance vectors in the DV Protocols. These messages, called RIP advertisements, contain information about sender’s distances to destination subnets.

> The figure below shows a portion of the network. Here, A, B, C and D denote the routers and w, x, y and z denote the subnet masks.

![[Pasted image 20230906164718.png]]

> Each router maintains a **routing table**, which contains its own distance vector as well as the router's forwarding table. If we have a look at the routing table of Router D, we will see that it has three columns: destination subnet, identification of the next router along the shortest path to the destination, and the number of hops to get to the destination along the shortest path. A routing table will have one row for each subnet in the AS (AS = Autonomous Systems, which will be discussed in more detail in Lesson 4).

![[Pasted image 20230906164727.png]]

> For this example, the table in the above figure indicates that to send a datagram from router D to destination subnet w, the datagram should first be forwarded to neighboring router A; the table also indicates that destination subnet w is two hops away along the shortest path. Now if router D receives from router A the advertisement (the routing table information of router A) shown in the figure below it merges the advertisement with the old routing table.

![[Pasted image 20230906165727.png]]

> In particular, router D learns that there is now a path through router A to subnet z that is shorter than the path through router B. Therefore, router D updates its table to account for the new shortest path. The updated routing table is shown in the figure below. As the Distance Vector algorithm is in the process of converging or as new links or routers are getting added to the AS, the shortest path is changing.

![[Pasted image 20230906170638.png]]

> Each node maintains a RIP Table (Routing Table), which will have one row for each subnet in the AS. RIP version 2 allows subnet entries to be aggregated using route aggregation techniques.

> If a router does not hear from its neighbor at least once every 180 seconds, that neighbor is considered to be no longer reachable (broken link). In this case, the local routing table is modified, and changes are propagated. Routers send request and response messages over UDP, using port number 520, which is layered on top of network-layer IP protocol. RIP is actually implemented as an application-level process. 

> Some of the challenges with RIP include updating routes, reducing convergence time, and avoiding loops/count-to-infinity problems.

## Linkstate Routing Protocol Example (OSPF)
> OSPF: Open Shortest Path First

Routing protocol which uses a link-state routing algorithm to find the best path between the source and destination router.

- OSPF is an improvement to the RIP, operating in upper-tier ISPs.
- Link-state protocol that uses flooding of link-state information and a Dijkstra least-cost path algorithm.
- Advances include
	- authentication of messages exchanged between routers
	- the option to use multiple same-cost paths
	- support for hierarchy within a single routing domain

> A link-state routing algorithm is a dynamic routing algorithm in which each router shares knowledge of its neighbors with every other router in the network

### Hierarchy
- An OSPF autonomous system (AS) can be configured hierarchically into areas
- Each area runs its own OSPF link-state routing alg, with each router in an area broadcasting its link-state to all other routers in that area
- Within each area, one or more area border routers are responsible for routing packets outside the area
- Exactly one OSPF area in the AS is configured to be the **backbone area**.
	- Routes traffic between the other areas in the AS
	- Contains all area border routers in the AS
	- may contain non-border routers as well
	- All inter-area traffic crosses this area

### Operation
> First, a graph (topological map) of the entire AS is constructed. Then, considering itself as the root node, each router computes the shortest-path tree to all subnets by running Djikstra's algorithm locally. The link costs have been pre-configured by a network administrator. The administrator has a variety of choices while configuring the link costs. For instance, the administrator may choose to set them to be inversely proportional to link capacity, or set them all to one. Given a set of link weights, OSPF provides the mechanisms for determining least-cost path routing. 

> Whenever there is a change in a link's state, the router broadcasts routing information to all other routers in the AS, not just to its neighboring routers. It also periodically broadcasts a link's state even if its state hasn't changed.

### Link State Advertisements (LSAs)
> Every router within a domain that operates on OSPF uses Link State Advertisements (LSAs). LSA communicates the router's local routing topology to all other local routers in the same OSPF area. In practice, LSA is used for building a database (called the link state database) containing all the link states. LSAs are typically flooded to every router in the domain. This helps form a consistent network topology view. Any change in the topology requires corresponding changes in LSAs.

### LSA Refresh Rate
> OSPF typically has a refresh rate for LSAs, which has a default period of 30 minutes. If a link comes alive before this refresh period is reached, the routers connected to that link ensure LSA flooding. Since the flooding process can happen multiple times, every router receives multiple copies of refreshes or changes - and stores the first received LSA change as new and the subsequent ones as duplicates.

## Processing OSPF Messages in the Router

Terminology refresher
- OSPF = Open Shortest Path First
- LSA = Link State Advertisement
- LS = Link State

![[Pasted image 20230913111212.png]]

Above is a simple model of a router
- consists of a route processor (main processing unit)
- interface cards that receive data packets
- packets are forwarded via a switching fabric

1. Initially, the LS update packets which contain LSAs from a neighboring router reach the current router's OSPF
	- This is the first trigger for the route processor
	- As the LS updates reach the router, a consistent view of the topology is being formed and this information is stored in the LS database
	- Entries of LSAs correspond to the topology which is actually visible from the current router.
2. Using this information from the LS DB
	- The current router calculates the shortest path using the shortest path first (SPF) algorithm.
	- The result of this step is fed to the Forwarding Information Base (FIB)
3. The information in the FIB is used when a data packet arrives at an interface card on the router. The next hop for the packet is decided and it's forwarded to the outgoing interface card.

![[Pasted image 20230913111819.png]]

1. The processing tasks begin at the receipt of an LS update packet **(T1)**.
	- For every LSA unpacked from the update packet, the OSPF protocol checks whether it is a new or a duplicate LSA.
	- This is done by referring to the link-state database, and checking for the sequence number of the LSA to a matching LSA instance in the database.
2. For every new LSA, the database is updated, an SPF calculation is scheduled **(T2)** and it’s determined which interface the LSA needs to be flooded out of.  In modern routers, the _when_ of LSA flooding can be based on a timer.
3. When all the LSAs from an LS update packet have been processed **(T3)**, the LSAs are prepared and flooded out as an LS Update packet to the next router **(T4).**
5. After this, we move on to the actual execution of SPF calculation within the router **(T5 and T6)**. Since a SPF calculation is a CPU-intensive task, SPF calculations are scheduled and carried out over a period of time (usually when LSA’s are changed) so as to offset the CPU costs.
6. After the SPF calculation is completed, the FIB is updated **(T7).**

## Hot Potato Routing
> In large networks, routers rely both on interdomain and intradomain routing protocols to route the traffic.

- Routers within a network use intradomain routing protocols to find the best path to route traffic within the network
- traffic will travel towards network exits (egress points) before leaving
- In some cases there are multiple egress points that the routers can choose from
- These egress points (routers themselves) can be equally good in the sense that the offer similarly good external paths to the final destination

> hot potato routing is a technique/practice of choosing a path within the network, by choosing the closest egress point based on intradomain path cost (Interior Gateway Protocol/IGP cost).

![[Pasted image 20230913112516.png]]

> In the figure above, we have a network, and specifically we are looking at the a router located in Dallas and the router needs to forward traffic towards a  destination. It could do so via New York or San Francisco. We assume that both egress points offer BGP (Border Gateway Protocol) path costs, so they are equally good egress points. In this case, the router has multiple egress points. We see that the IGP path cost for SF is 9 while the path cost for NY is 10. Thus, the router uses hot potato routing to choose to send the traffic to the destination via SF.

> Hot potato routing simplifies computations for the routers as they are already aware of the IGP path costs. It makes sure that the path remains consistent, since the next router in the path will also choose to send the packet to the same egress point. 

> Hot potato routing also effectively reduces the network’s resource consumption by getting the traffic out as soon as possible.

> Hot potato routing is a technique/practice of choosing a path within the network, by choosing the closest egress point based on intradomain path cost (Interior Gateway Protocol/IGP cost).

## Optional Reading: An Example Traffic Engineering Framework

[[Traffic Engineering with Traditional IP Routing Protocols.pdf]]

Traffic engineering frameworks have 3 main components
- measure
- model
- control

![[Pasted image 20230913132149.png]]

- The network operator measures the topology of the network and traffic demands
- The network operator predicts the effect of change in IGP parameters on the traffic flow to evaluate different link weights
- Once the weights are decided, the new values are updated on the routers.

### Measure
> The efficient assignment of link weights depends on the real time view of the network state which includes the operational routers and links, and the link capacity and IGP parameters configuration.

> The status of the network elements can be obtained using Simple Network Management Protocol (SNMP) polling or via SNMP traps. The link capacity and the IGP parameters can be gathered from the configuration data of the routers or external databases that enable the provisioning of the network elements. Furthermore, a software router could act as an IGP route monitor by participating in OSPF/IS-IS with operational routers and reporting real time topology information. 

> In addition to the current network state, the network operator also requires an estimate of the traffic in the network that can be acquired either by prior history or by using the following measurement techniques: 

1. Directly from the SNMP Management Information Bases (MIBs) 
2. By combining packet-level measurements at the network edge using the information in routing tables 
3. Network tomography which involves observing the aggregate load on the links along with the routing data 
4. Direct observation of the traffic using new packet sampling techniques

### Model
> This involves predicting the traffic flow through the network based on the IGP configuration. The best path between two routers is selected by calculating the shortest path between them when all the links belong to the same OSPF/IS-IS area. In case of large networks consisting of multiple OSPF/IS-IS areas, the path selection among routers in different areas is dependent on the summary information passed across the area boundaries. If there are multiple shortest paths between two routers, it is leveraged for load balancing by splitting the traffic almost evenly over these paths. 

> The routing model thus aims to compute a set of paths between each pair of routers, with each path representing the fraction of traffic that passes through each link. The volume of traffic on a link can now be estimated by combining the output of the routing model and the estimated traffic demands.

### Control
> The new link weights are applied on the affected routers by connecting to the router using telnet or ssh. The exact commands are dependent on the operating systems of the router. These updates may be automated or done manually depending on the size of the network. 

> Once a router receives a weight change, it updates its link-state database and floods the newly updated value to the entire network. On receiving the updated value, each router in turn updates its link-state database, recomputes the shortest paths and updates affected entries in its forwarding table.  Similar to when there is a topology change or a failure, this involves a transition period where there is a slightly inconsistent view of the shortest path for few destinations. Although the convergence after a weight change is faster than a failure scenario (as there is delay in detecting a failure), it still involves a transient period in the network. Hence, understandably, changing the link weights is not done frequently and only done in scenarios where there is new hardware, equipment failures or changes in traffic demands.


