---
tags:
  - OMSCS
  - CN
---
# Lesson 04 - Autonomous Systems
> AS Relationships and Interdomain Routing

- We know that the Internet is an ecosystem that consists of thousands of independently operated networks.
- Each network operates in its own interest, and they have independent economic and traffic engineering objectives.
- They must interconnect to provide global connectivity.
- In this lesson, we learn about
	- the BGP protocol that provides the glue for this connectivity. 
	- the different interconnections types based on business relationships between networks.
	- increasingly popular infrastructures called Internet Exchange Points, which primarily provide interconnection services so that the participant networks can directly exchange traffic.

## Key Acronyms
- AS: Autonomous System
- ASN: autonomous system number
- BGP: Border Gateway Protocol
	- eBGP: External BGP Session
	- iBGP: Internal BGP Session
- CDN: Content Delivery Network
- I-GIRP: ???
- IGP: Interior Gateway Protocol
- IS-IS: Intermediate System - Intermediate System
- ISP: Internet Service Provider
- IXP: Internet Exchange Point
- MED: Multi-Exit Discriminator
- OSPF: Open Shortest Path First
- PI: Private Interconnects
- POP: Point of Presence
- RCC: Router Configuration Checker
- RIP: Routing Information Protocol
- RIB: Routing Information Base
- RP: Remote Peering
- RS: Route Server
- SDN: Software Defined Network / Networking

## Important Readings
Interdomain Internet Routing  
[https://web.mit.edu/6.829/www/currentsemester/papers/AS-bgp-notes.pdf](https://web.mit.edu/6.829/www/currentsemester/papers/AS-bgp-notes.pdf)

BGP routing policies in ISP networks [https://www.cs.princeton.edu/~jrex/papers/policies.pdf](https://www.cs.princeton.edu/~jrex/papers/policies.pdf)

On the importance of Internet eXchange Points for today’s Internet ecosystem  
[https://cryptome.wikileaks.org/2013/07/ixp-importance.pdf](https://cryptome.wikileaks.org/2013/07/ixp-importance.pdf)

Peering at Peerings: On the Role of IXP Route Servers  
[https://people.csail.mit.edu/richterp/imc238-richterA.pdf](https://people.csail.mit.edu/richterp/imc238-richterA.pdf)

## Optional Readings
Investigating Interdomain Routing Policies in the Wild  
[https://people.cs.umass.edu/~phillipa/papers/AnwarIMC15.pdf](https://people.cs.umass.edu/~phillipa/papers/AnwarIMC15.pdf)

BGP Communities: Even more Worms in the Routing Can  
[https://people.mpi-inf.mpg.de/~fstreibelt/preprint/communities-imc2018.pdf](https://people.mpi-inf.mpg.de/~fstreibelt/preprint/communities-imc2018.pdf)

On the scalability of BGP: the roles of topology growth and update rate-limiting  
[https://www.cc.gatech.edu/home/dovrolis/Papers/bgp-scale-conext08.pdf](https://www.cc.gatech.edu/home/dovrolis/Papers/bgp-scale-conext08.pdf)

O Peer, Where Art Thou? Uncovering Remote Peering Interconnections at IXPs  
[https://www.inspire.edu.gr/wp-content/pdfs/uncovering_remote_peering_interconnections_v1.pdf](https://www.inspire.edu.gr/wp-content/pdfs/uncovering_remote_peering_interconnections_v1.pdf)

Detecting BGP Configuration Faults with Static Analysis  
[https://www.usenix.org/legacy/events/nsdi05/tech/feamster/feamster.pdf](https://www.usenix.org/legacy/events/nsdi05/tech/feamster/feamster.pdf)

## AS and Internet Interconnection
- Internet is a network of networks
	- Internet Service Providers (ISPs)
	- Internet Exchange Points (IXPs)
	- Content Delivery Networks (CDNs)
- Each type of network has its own business goals which result in different business relationships and interconnection strategies

### Internet as an Ecosystem
![[Pasted image 20230917180026.png]]

ISPs
- can be categorized into three types (or types)
	- and large global scale ISPs (or Tier-1)
		- There are a dozen of large-scale Tier-1 ISPs that operate at a global scale
		- they form the "backbone" network over which smaller networks can connect
		- Some example Tier-1 ISPs include AT&T, NTT, Level-3, and Sprint
	- regional ISPs (or Tier-2)
	- access ISPs (or Tier-3)
- regional ISPs connect to Tier-1 ISPs, and smaller access ISPs connect to regional ISPs.

IXPs
- interconnection infrastructures that provide the physical infrastructure where multiple networks (e.g., ISPs and CDNs) can interconnect and exchange traffic locally.
- As of 2019, there are approximately 500 IXPs around the world.

CDNs
- networks that content providers create with the goal of having greater control of how the content is delivered to the end-users while reducing connectivity costs
- Examples of CDNs are Google and Netflix
- These networks have multiple data centers, and each one of them may be housing hundreds of servers that are distributed across the world.

### Competition and Cooperation Among Networks
![[Pasted image 20230917180116.png]]

- This ecosystem we described forms a hierarchical structure since smaller networks (e.g., access ISPs) connect to larger networks (e.g., Tier-2 ISPs).
- An access ISP receives Internet connectivity, becoming the customer of a larger ISP.
- The larger ISP becomes the provider of the smaller ISP.
- This leads to competition at every level of the hierarchy. 
	- Tier-1 ISPs compete with each other, and the same is true for regional ISPs that compete with each other.
	- Competing ISPs need to cooperate in providing global connectivity to their respective customer networks.
	- ISPs deploy multiple interconnection strategies depending on the number of customers in their network and the geographical location of these networks.

#### More interconnection options in the Internet ecosystem
> To complete the picture of today's Internet interconnection ecosystem, we note that ISPs may also connect through Points of Presence (PoPs), multi-homing, and peering. PoPs are one (or more) routers in a provider's network, which a customer network can use to connect to that provider. Also, an ISP may choose to multi-home by connecting to one or more provider networks. Finally, two ISPs may choose to connect through a settlement-free agreement where neither network pays the other to directly send traffic to one another.

#### The Internet topology: hierarchical versus flat
> As we said, this ecosystem we just described forms a hierarchical structure, especially in the earlier days of the Internet. But, it's important to note that as the Internet has been evolving, the dominant presence of IXPs and CDNs has caused the structure to begin morphing from hierarchical to flat.

#### Autonomous Systems (ASes)
> Each of the networks we discussed above (e.g., ISPs and CDNs) may operate as an Autonomous System (AS). An AS is a group of routers (including the links among them) that operate under the same administrative authority. An ISP, for example, may operate as a single AS, or it may operate through multiple ASes. Each AS implements its own policies, makes its own traffic engineering decisions and interconnection strategies, and determines how the traffic leaves and enters its network.

#### Protocols for routing traffic between and within ASes
> The border routers of the ASes use the Border Gateway Protocol (BGP) to exchange routing information with one another. In contrast, the Interior Gateway Protocols (IGPs) operate within an AS, and they are focused on "optimizing a path metric" within that network

Example IGPs include
- Open Shortest Paths First (OSPF)
- Intermediate System - Intermediate System (IS-IS)
- Routing Information Protocol (RIP)
- E-IGRP

## AS Business Relationships

![[Pasted image 20230917182936.png]]

### Provider-Customer Relationship (aka "transit")
- based on a financial settlement that determines how much the customer will pay the provider
- The provider forwards the customer's traffic to destinations found in the provider's routing table

### Peering Relationship
- 2 ASes share access to a subset of each other's routing tables
- The routes shared between the 2 peers are often restricted to the respective customers of each one
- The agreement holds as long as the traffic exchanged between the 2 peers is not highly asymmetric
- Generally the 2 peers need to be a similar size and should handle proportional amounts of traffic, otherwise the larger ISP would lack an incentive to enter a peering relationship with another network
- When 2 small ISPs peer, both save money that they would otherwise pay their providers directly forwarding traffic between themselves instead of through their providers.
- This arrangement is primarily beneficial when a significant amount of traffic is destined for each other, or each other's customers.

### How do providers charge customers?
> While peering allows networks to have their traffic forwarded without cost, provider ASes have a financial incentive to forward as much of their customers' traffic as possible. One major factor determining a provider's revenue is the data rate of an interconnection. A provider usually charges in one of two ways:

1. Based on a fixed price, given that the bandwidth used is within a predefined range. 
2. Based on the bandwidth used. The bandwidth usage is calculated based on periodic measurements, e.g., five-minute intervals. The provider then charges by taking the 95th percentile of the distribution of the measurements. 

> We might observe complex routing policies. In some cases, the driving force behind these policies is to increase traffic from a customer to its provider so that the provider gains more revenue.

## BGP Routing Policies
> Importing and Exporting Routes

![[Pasted image 20230917190436.png]]

### Exporting Routes 

> Deciding which routes to export is an important decision with business and financial implications. Advertising a route for a destination to a neighboring AS means that this route may be selected by that AS, and traffic will start to flow through. Therefore, deciding which routes to advertise is a policy decision, which is implemented through route filters. Route filters are rules that determine which routes an AS's router should advertise to the routers of neighboring ASes.

#### Routes learned from customers
> These are the routes X receives as advertisements from its customers. Since provider X is getting paid to provide reachability to a customer AS, it makes sense that X wants to advertise these customer routes to as many neighboring ASes as possible. This will likely cause more traffic toward the customer (through X) and, hence, more revenue for X.   
#### Routes learned from providers
> These are the routes X receives as advertisements from its providers. Advertising these routes does not make sense since X has no financial incentive to carry traffic for its provider's routes. Therefore, these routes are withheld from X's peers and X's other providers, but they are advertised to X's customers.  
#### Routes learned from peers
> These are routes that X receives as advertisements from its peers. As we saw earlier, it does not make sense for X to advertise to provider A the routes it receives from provider B. Because in that case, providers A and B will use X to reach the advertised destinations without X making revenue. The same is true for the routes that X learns from peers.    

### Importing Routes
> Like exporting, ASes are selective about which routes to import. These decisions are primarily based on which neighboring AS advertises them and the type of business relationship established. An AS receives route advertisements from its customers, providers, and peers. 

> When an AS receives multiple route advertisements towards the same destination from multiple ASes, it needs to rank the routes before selecting which one to import. In order of preference, the imported routes are the **customer** routes, then the **peer** routes, and finally, the **provider** routes. The reasoning behind this ranking is as follows:

1. An AS wants to ensure that routes toward its customers do not traverse other ASes, unnecessarily generating costs.
2. An AS uses routes learned from peers since these are usually "free" (under the peering agreement).
3. An AS resorts to importing routes learned from providers only when necessary for connectivity since these will add to costs.

![[Pasted image 20230917190645.png]]

## BGP Design Goals

### Scalability
> As the size of the Internet grows, the same is true for the number of ASes, the number of prefixes in the routing tables, the network churn, and the BGP traffic exchanged between routers. One of the design goals of BGP is to manage the complications of this growth while achieving convergence in reasonable timescales and providing loop-free paths. 

### Express routing policies
> BGP has defined route attributes that allow ASes to implement policies (which routes to import and export) through route filtering and route ranking. Each ASes routing decisions can be kept confidential, and each AS can implement them independently. 

### Allow cooperation among ASes
> Each AS can still make local decisions (which routes to import and export) while keeping these decisions confidential from other ASes. 

### Security
> Originally, the design goals for BGP did not include security. However, the increase in size and complexity of the Internet demands security measures to be implemented. We need protection and early detection for malicious attacks, misconfiguration, and faults. These vulnerabilities still cause routing disruptions and connectivity issues for individual hosts, networks, and even entire countries. There have been several efforts to enhance BGP security ranging from protocols (e.g., S-BGP), additional infrastructure (e.g., registries to maintain up-to-date information about which ASes own which prefixes ASes), public keys for ASes, etc. Also, there has been extensive research to develop machine learning-based approaches and systems. But these solutions have not been widely deployed or adopted for multiple reasons that include difficulties in transitioning to new protocols and a lack of incentives.

## BGP Protocol Basics
![[Pasted image 20230917191655.png]]

- A pair of routers, known as **BGP peers**, exchange routing information over a semi-permanent TCP port connection called a **BGP session**.
- In order to begin a BGP session, a router will send an `OPEN` message to another router.
- The sending and receiving routers will send each other announcements from their routing tables.
- The time it takes to exchange routes varies from a few seconds to several minutes, depending on the number of routes exchanged.

![[Pasted image 20230917191743.png]]

### BGP messages
After BGP peers establish a session, they can exchange BGP messages to provide reachability information and enforce routing policies.

- `UPDATE` messages contain information about the routes that have changed since the previous update.
	- `Announcement`: Advertise new routes and updates to existing routes. They include several standardized attributes. 
	- `Withdrawal`: A previously announced route is no longer available. The removal could be due to some failure or a change in the routing policy.
- `KEEPALIVE` messages are exchanged between peers to keep a current session going.

### BGP Prefix Reachability
- In the BGP protocol, destinations are represented by IP prefixes.
- Each prefix represents a subnet or a collection of subnets that an AS can reach.
- Gateway routers running eBGP advertise the IP prefixes they can reach according to the AS's specific export policy to routers in neighboring ASes. 
- Then, using separate iBGP sessions, the gateway routers disseminate these routes for external destinations to other internal routers according to the AS's import policy.
- Internal routers run iBGP to propagate the external routes to other internal iBGP speaking routers.  

#### Path Attributes and BGP Routes
In addition to the reachable IP prefix field, advertised **BGP routes** consist of several **BGP attributes**. Two notable attributes are AS-PATH and NEXT-HOP.

- `ASPATH`
	- "AS Path"
	- Each AS is identified by its **autonomous system number (ASN)**.
	- As an announcement passes through various ASes, their identifiers are included in the ASPATH attribute.
	- This attribute prevents loops and is used to choose between multiple routes to the same destination, the route with the shortest path.
- `NEXT-HOP`
	- This attribute refers to the next-hop router's IP address (interface) along the path towards the destination.
	- Internal routers use the field to store the IP address of the border router. 
	- Internal BGP routers will forward all traffic bound for external destinations through the border router.
	- If there is more than one such router on the network, and each advertises a path to the same external destination, `NEXT HOP` allows the internal router to store in the forwarding table the best path according to the AS routing policy.

### More on eBGP and iBGP
> The eBGP speaking routers learn routes to external prefixes and disseminate them to all routers within the AS. This dissemination is happening with iBGP sessions. For example, as the figure below shows, the border routers of AS1, AS2, and AS3 establish eBGP sessions to learn external routes. Inside AS2, these routes are disseminated using iBGP sessions.

![[Pasted image 20230917192832.png]]

> The dissemination of routes within the AS is done by establishing a full mesh of iBGP sessions between the internal routers. Each eBGP speaking router has an iBGP session with every other BGP router in the AS to send updates about the routes it learns (over eBGP).

![[Pasted image 20230917192849.png]]

> Both flavors (iBGP and eBGP) take care of disseminating *external* routes. An eBGP session is established between two border routers that belong to different ASes. An iBGP session is established between routers that belong to the same AS. Once a router hears about a route that is learned through eBGP, then it disseminates that route to other internal routers in the same AS, using iBGP.

> Finally, we note that iBGP is not another IGP-like protocol (e.g., RIP or OSPF). IGP-like protocols are used to establish paths between the internal routers of an AS based on specific costs within the AS. In contrast, iBGP is only used to disseminate external routes within the AS.

## BGP Decision Process
> Selecting Routes at a Router

![[Pasted image 20230919120311.png]]

- A router receives incoming BGP messages and processes them.
- When a router receives advertisements, it first applies the import policies to exclude routes from further consideration.
- Then the router implements the decision process to select the best routes that reflect the policy in place.
- Next, the newly selected routes are installed in the forwarding table.
- Finally, the router decides which neighbors to export the route to by applying the export policy.

### Router Decision Process
In the simplest scenario, where there is no policy in place (meaning it does not matter which route will be imported), the router uses the attribute of the path length to select the route with the fewest number of hops.

![[Pasted image 20230919121406.png]]

- LocalPref is used to control outbound traffic.
- MED is used to control inbound traffic.
### Influencing the route decision using the LocalPref
![[Pasted image 20230919121452.png]]

- The LocalPref attribute is used to prefer routes learned through a specific AS over other ASes.
	- Suppose AS B learns of a route to the same destination `x` via A and C.
	- If B prefers to route its traffic through A, due to peering or business, it can assign a higher LocalPref value to routes it learns from A.
	- AS B can control where the traffic exits the AS. It will influence which routers will be selected as exit points for the traffic that leaves the AS (outbound traffic).
- an AS ranks the routes it learns by preferring the routes learned from its customers, then the routes learned from peers, and finally routes learned from its providers.
- Operators can assign value ranges to the LocalPref attribute based on relationship type.
- Assigning different LocalPref ranges will influence which routes are imported.

![[Pasted image 20230919121828.png]]
> Example LocalPref configuration

### Influencing the Route Decision Using the MED Attribute
- The MED (Multi-Exit Discriminator) value is used by ASes connected by multiple links to designate which links are preferred for inbound traffic
	- The network operator of AS B will assign different MED values to its routes advertised to AS A through R1 and different MED values to its routes advertised through R2. 
	- AS A will be influenced to choose R1 to forward traffic to AS B, if R1 has a lower MED value, and if all other attributes are equal.  
- An AS does not have an economic incentive to export routes that it learns from providers or peers to other providers or peers. An AS can reflect this by tagging routes with a MED value to "staple" the type of business relationship. 
- An AS filters routes with specific MED values before exporting them to other ASes.
- Influencing the route exports will also affect how the traffic enters an AS (the routers that are entry points for the traffic that enters the AS).

### So, where/how are the attributes controlled?

The attributes are set either
1. locally by the AS (e.g., LocalPref)
2. by the neighboring AS (e.g., MED)
3. or by the protocol (e.g., if a route is learned through eBGP or iBGP)

### Couple of Scenarios

- The LocalPref attribute is used to prefer routes learned through a specific AS over other ASes for **outbound** traffic. Higher LocalPref values indicate higher preference.
- If AS X learns of a route to the same destination via AS Y and AS Z, and AS X prefers to route its traffic through AS Z, it can assign a **higher** LocalPref value to routes it learns from Z to control how traffic exits the AS.

- The MED (Multi-Exit Discriminator) value is used by ASes connected by multiple links to designate with of those links are preferred for **inbound** traffic. Lower MED values indicate higher preference.
- If AS X has 2 border gateways to AS Y, and AS X prefers routes advertised to AS Y to go through R1 as opposed to R2, AS X can influence AS Y to prefer R1 by setting a **lower** MED value for R1.

## BGP Challenges: Scalability and Misconfigurations
> Unfortunately, the BGP protocol in practice can suffer from two significant limitations: misconfigurations and faults. A possible misconfiguration or an error can result in an excessively large number of updates, resulting in route instability, router processor and memory overloading, outages, and router failures. One way that ASes can help reduce the risk that these events will happen is by limiting the routing table size and limiting the number of route changes. 

> An AS can limit the routing table size using filtering. For example, long, specific prefixes can be filtered to encourage route aggregation. In addition, routers can limit the number of prefixes advertised from a single source on a per-session basis. Some small ASes also have the option to configure **default routes** into their forwarding tables. ASes can likewise protect other ASes by using route aggregation and exporting less specific prefixes where possible. 

> Also, an AS can limit the number of routing changes, explicitly limiting the propagation of unstable routes by using a mechanism known as **flap damping**. To apply this technique, an AS will track the number of updates to a specific prefix over a certain amount of time. If the tracked value reaches a configurable value, the AS can suppress that route until a later time. Because this can affect reachability, an AS can be strategic about how it uses this technique for certain prefixes. For example, more specific prefixes could be more aggressively suppressed (lower thresholds), while routes to known destinations that require high availability could be allowed higher thresholds.

## Peering at IXPs
> Internet Exchange Points
- IXPs are physical infrastructures that provide the means for ASes to interconnect and directly exchange traffic with one another.
- The ASes that interconnect at an IXP are called participant ASes.
- The physical infrastructure of an IXP is usually a network of switches located either in the same physical location or distributed over a region or even at a global scale.
- Typically, the infrastructure has a fully redundant switching fabric that provides fault tolerance.
- The equipment is usually located in facilities such as data centers, which provide reliability, sufficient power, and physical security.

![[Pasted image 20230919131610.png]]
> Example IXP infrastructure called DE-CIX in Frankfurt (2012).

### Why are IXPs so popular?
1. IXPs are interconnection hubs handling large traffic volumes
2. They are important in mitigating DDoS attacks
	- Observe traffic to/from ASes
	- IXPs can act as a shield 
	- In March 2013, a massive DDoS attack took place that involved Spamhaus, Stophaus, and CloudFlare.
3. "Real-world" infrastructures with a plethora of research opportunities
	- BGP black-holing for DDoS mitigation
	- applications for software defined networking
4. IXPs are active marketplaces and technology innovation hubs
	- DDoS protection
	- SDN-based services

### What are the steps for an AS to peer at an IXP?
> Each participating network must have a public Autonomous System Number (ASN). Each participant brings a router to the IXP facility (or one of its locations if the IXP has an infrastructure distributed across multiple data centers) and connects one of its ports to the IXP switch. The router of each participant must be able to run BGP since the exchange of routes across the IXP is via BGP only. In addition, each participant must agree to the IXP’s General Terms and Conditions (GTC).

> Two networks may publicly peer at IXP by using the IXP infrastructure to establish a connection for exchanging traffic according to their own requirements and business relationships. But, first, each network incurs a one-time cost to establish a circuit from the premises to the IXP. Then, there is a monthly charge for using a chosen IXP port, where higher port speeds are more expensive. The entity that owns and operates the IXP might also charge an annual membership fee. In particular, exchanging traffic over an established public peering link at an IXP is in principle “settlement-free” (i.e., involves no form of payment between the two parties) as IXPs typically do not charge for exchanged traffic volume. Moreover, IXPs usually do not interfere with the bilateral relationships between the IXP’s participants unless they violate the GTC. For example, the two parties of an existing IXP peering link are free to use that link in ways that involve paid peering. Other networks may even offer transit across an IXP’s switching fabric. Depending on the IXP, the time it takes to establish a public peering link can range from a few days to a couple of weeks.

### Why do networks choose to peer at IXPs?

- The traffic exchanged between two networks do not need to travel unnecessarily through other networks if both networks are participants in the same IXP facility.  
- Lower costs. Typically peering at an IXP is offered at a lower cost than relying on third parties to transfer the traffic, which is charged based on volume. 
- Network performance is improved due to reduced delay.
- Incentives. Critical players in today’s Internet ecosystem often "incentivize" other networks to connect at IXPs. For example, a prominent content provider may require another network to be present at a specific IXP or IXPS in order to peer with them.

### What services are offered at IXPs?

1. **Public peering**
	1. The most well-known use of IXPs is public peering service, in which two networks use the IXP’s network infrastructure to establish a connection to exchange traffic based on their bilateral relations and traffic requirements.
	2. The costs required to set up this connection are a one-time cost for establishing the connection, the monthly charge for using the chosen IXP port (those with higher speeds are more expensive), and perhaps an annual fee of membership in the entity owning and operating the IXP. 
	3. However, the IXPs do not usually charge based on the amount of exchanged volume. They also do not usually interfere with bilateral relations between the participants unless there is a violation of the GTC. 
	4. Even with the set-up costs, IXPs are generally cheaper than other conventional methods of exchanging traffic (such as relying on third parties which charge based on the volume of exchanged traffic).
	5. IXP participants also often experience better network performance and Quality-of-Service (QoS) because of reduced delays and routing efficiencies.
	6. In addition, many companies that are significant players in the Internet space (such as Google) incentivize other networks to connect at IXPs by making it a requirement to peering with them. 
2. **Private peering**
	1. Most operational IXPs also provide a private peering service (Private Interconnects, or PIs) that allows direct traffic exchange between the two parties, and doesn’t use the IXP’s public peering infrastructure.
	2. This is commonly used when the participants want a well-provisioned, dedicated link capable of handling high-volume, bidirectional, and relatively stable traffic.
3. **Route servers and Service level agreements**
	1. Many IXPs also include service level agreements (SLAs) and free use of the IXP’s route servers for participants.
	2. This allows participants to arrange instant peering with many co-located participant networks using essentially a single agreement/BGP session.
4. **Remote peering through resellers**
	1. Another popular service is IXP reseller/partner programs.
	2. Third parties resell IXP ports wherever they have infrastructure connected to the IXP.
	3. These third parties can offer the IXP’s service remotely, which will enable networks that have little traffic also to use the IXP.
	4. This also enables remote peering, where networks in distant geographic areas can use the IXP.
5. **Mobile peering**
	1. Some IXPs also provide support for mobile peering, which is a scalable solution for the interconnection of mobile GPRS/3G networks.
6. **DDoS blackholing**
	1. A few IXPs support customer-triggered blackholing, which allows users to alleviate the effects of DDoS attacks against their network.
7. **Free value-added services**
	1. In the interest of "good of the Internet", a few IXPs such as Scandinavian IXP Netnod offer free value-added services like
		1. Internet Routing Registry (IRR)
		2. consumer broadband speed tests,
		3. DNS root name servers
		4. country-code top-level domain (ccTLD) nameservers
		5. distribution of the official local time through NTP.

## Peering at IXPs: How does a route server work?
![[Pasted image 20230919132742.png]]

- A two-way BGP session is called a **bilateral** BGP session. This can result in a lot of traffic routing through an IXP.
- some IXPs operate a route server (RS), which helps to make peering more manageable
	- It collects and shares routing information from its peers or participants of the IXP that connect to the RS.
	- It executes its own BGP decision process and re-advertises the resulting information (e.g., best route selection) to all RS's peer routers.

### How does a route server (RS) maintain multi-lateral peering sessions?
- A typical routing daemon maintains a _Routing Information Base (RIB),_ which contains all BGP paths that it receives from its peers
- In addition, the route server also maintains AS-specific RIBs to keep track of the individual BGP sessions they maintain with each participant AS.
- Route servers maintain two types of route filters.
	- **Import filters** are applied to ensure that each member AS only advertises routes that it should advertise.
	- **Export filters** are typically triggered by the IXP members themselves to restrict the set of other IXP member ASes that receive their routes.
- When AS X and AS Z exchange routes through a multi-lateral peering session, the steps are:
	- AS X advertises prefix `p1` to the RS.
	- `p1` is added to the RS's RIB specific to AS X.
	- The RS uses the peer-specific import filter to check whether AS X is allowed to advertise `p1`. If it passes, `p1` is added to the Master RIB.
	- The RS applies the peer-specific export filter to check if AS X allows AS Z to receive `p1`. If it passes, `p1` is added to the RS's RIB specific to AS Z.
	- The RS advertises `p1` to AS Z with AS X as the next hop.

![[Pasted image 20230919133626.png]]

## Optional Reading: Remote Peering
> Remote peering (RP) is peering at the peering point without the necessary physical presence. The **remote peering provider** is an entity that sells access to IXPs through their own infrastructure. RP removes the barrier to connecting to IXPs around the world, which in itself can be a more cost-effective solution for localized or regional network operators.

> An interesting problem is how we can tell if an AS is directly connected to an IXP or connected through remote peering. Researchers have studied this problem and identified methodologies to detect remote peering with high accuracy by performing experiments with many IXPs.

![[Pasted image 20230919133854.png]]

> The primary method of identifying remote peering is to measure the round-trip time (RTT) between a vantage point (VP) inside the IXP and the IXP peering interface of a member. However, this method fails to account for the changing landscape of IXPs today and even misinfers latencies of remote members as local and local members as being remote. Instead, a combination of methods can achieve detection of remote peering in a more tractable way, some of which include:

1. **Information about the port capacity**: One way to find reseller customers is via port capacities. The capacity of the peering port for each IXP member can be obtained through the IXP website or PeeringDB. IXPs offer ASes connectivity to ports with capacity typically between 1 and 100 Gbit/s. But resellers usually offer connectivity through their virtual ports with smaller capacities and lower prices. 
2. **Gathering colocation information:** An AS needs to be physically present (i.e., actually deploy routing equipment) in at least one colocation facility where the IXP has deployed switching equipment. It should be easy to locate the colocation facilities where both AS and IXPs are colocated, though this information is imperfect in practice.  
3. **Multi-IXP router inference:** An AS can operate a multi-IXP router, which is a router connected to multiple IXPs to reduce operational costs. Suppose a router is connected to multiple IXPs, and say, we infer the AS as local or remote to one of these IXPs from a previous step. In that case, we can extend the inference to the rest of the involved IXPs based on whether they share colocation facilities or not.
4. **Private connectivity with multiple existing AS participants:** If an AS has private peers over the same router that connects it to an IXP, and the private peers are physically colocated to the same IXP facilities, it can be inferred that the AS is also local to the IXP.

## Optional Reading: BGP Configuration Verification
> **Control of BGP configuration is complex** and easily misconfigured both at the eBGP configuration level and within an AS, at the iBGP level, where route propagation happens in a full mesh or via “route reflectors”. In addition, configuration languages vary among routing manufacturers and may not be well-designed. Adding to the complexity is the distributed nature of BGP’s implementation.

> Two main aspects of persistent routing define BGP correctness. They are **path visibility and route validity.**

- Path visibility means that route destinations are correctly propagated through the available links in the network.
- Route validity means that the traffic meant for a given destination reaches it.

> **The _router configuration checker_, or _rcc_,** is a tool researchers propose that detects BGP configuration faults. _rcc_ uses static analysis to check for correctness before running the configuration on an operational network before deployment. The _rcc_ analyzes router configuration settings and outputs a list of configuration faults. 

> In order to analyze a single router or a network-wide BGP configuration, the rcc will first “factor” the configuration to a normalized model by focusing on how the configuration is set to handle route dissemination, route filtering, and route ranking.

> Although rcc is designed to be used before running a live BGP configuration, it can be used to analyze the configuration of live systems and potentially detect live faults. While analyzing real-world configurations, it was found that most Path Visibility Faults were the result of:

1. problems with “full mesh” and route reflector configurations in iBGP settings leading to signaling partitions
2. Route reflector cluster problems 
3. Incomplete iBGP sessions where an iBGP session is active on one router but not the other

> Route Validity Faults were determined to stem from filtering and dissemination problems. The specific filtering behaviors included legacy filtering policies not being fully removed when changes occur, inconsistent export to peer behavior, inconsistent import policies, undefined references in policy definitions, or non-existent or inadequate filtering. Dissemination problems included unorthodox AS prepending practices and iBGP sessions with “next-hop self”. These issues suggest that routing might be less prone to faults if there were improvements to iBGP protocols when it comes to making updates and scaling.

> Because _rcc_ is intended to run prior to deployment, it may help network operators detect issues before they become major problems in a live setting, which often go undetected right away. rcc is implemented as static analysis and does not offer either completeness or soundness; it may generate false positives, and it may not detect all faults.
