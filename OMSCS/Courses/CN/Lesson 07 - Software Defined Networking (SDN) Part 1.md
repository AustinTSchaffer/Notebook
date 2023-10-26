---
tags:
  - OMSCS
  - CN
---
# Lesson 07 - Software Defined Networking (SDN) Part 1

- SDN exists to separate the data plane from the control plane
- This lesson will cover the architecture of SDN controllers, along with some example controllers.
- This lesson will also touch on OpenDaylight, a popular and open source project for network programmability

## Readings and Activities

- Important
	- [[The Road to SDN - An Intellectual History of Programmable Networks.pdf]]
- Optional
	- SDN Controllers: Benchmarking & Performance Evaluation: [https://arxiv.org/pdf/1902.04491.pdf](https://arxiv.org/pdf/1902.04491.pdf)
	- SDN Architecture: [https://www.opennetworking.org/wp-content/uploads/2013/02/TR_SDN_ARCH_1.0_06062014.pdf](https://www.opennetworking.org/wp-content/uploads/2013/02/TR_SDN_ARCH_1.0_06062014.pdf)
	- OpenDaylight Application Developer's Tutorial

## What led us to SDN?
- Arose to make computer networks more programmable
- Computer networks are complex
	- diversity of equipment
	- proprietary technologies for the equipment
- Offers new ways to redesign networks to make them more manageable
- simple idea - separation of tasks
- SDN divides a network into 2 planes
	- control plane
	- data plane
### Equipment Diversity
- routers
- switches
- middleboxes
	- firewalls
	- NATs
	- load balancers (LBs)
	- intrusion detection systems (IDSs)
- the network has to handle different software adhering to different protocols for each component of the network
- network management tools
	- provide a central access point
	- need to speak the individual languages/protocols of each piece of equipment on the network
### Proprietary Technology
- routers and switches tend to run closed/proprietary software
- configuration interfaces vary between vendors
- interfaces can differ between products offered by the same vendor as well
- makes it harder to centrally manage a network

## Brief History of SDN (Milestones)

history of SDNs can be divided into 3 phases
1. Active networks
2. Control and data plane separation
3. OpenFlow API and network operating systems

### 1. Active Networks
- mid-1990s to early 2000s
- network nodes began exposing APIs and supporting customization of functionalities for subsets of packets
- 2 types of programming models in active networking
	- Capsule model - carried in-band in data packets
	- programmable router/switch model - established by out-of-band mechanisms
- The pushes that encouraged active networking were
	- reduction in computation cost
	- advancement in programming languages
	- advances in rapid code compilation and formal methods
	- funding from agencies such as DARPA for a collection promoted interoperability among projects.
- The use pulls for active networking were
	- network service provider frustration concerning the long timeline of developing/deploying new network services
	- 3rd party interests to add value by implementing control at a more individualistic nature.
	- Researcher interest in having a network that would support large-scale experiments.
	- Unified control over middleboxes
- Active networks made 3 major contributions to SDN
	- programmable functions in the network to lower the barrier to innovation
	- network virtualization, and the ability to demultiplex to software programs based on packet headers
	- The vision of a unified architecture for middlebox orchestration

Biggest downfall? Too ambitious.
- Required end users to write Java
- Not as much emphasis was given to performance and security
- There were no specific short-term problems that active networks solved

### 2. Control and Data Plane Separation
- Lasted from 2001 to 2007
- network operators were looking for better network-management functions such as control over paths to deliver traffic (traffic engineering)
- researchers explored short-term approaches that were deployable using existing protocols. They identified the challenge in network management lay in the way existing routers and switches tightly integrated the control and data planes
- efforts to separate the two began
- technology push
	- higher link speeds in the backbone networks led to vendors implementing packet forwarding directly in hardware, separating the data plane from the control plane by necessity
	- ISPs found it hard to meet the increasing demand for greater reliability and new services (such as VPNs), and struggled to manage the increased size/scope of their networks
	- Servers had substantially more memory and processing resources. A single server could store all routing states and compute all routing decisions for a large ISP. Also enabled simple backup replication strategies, ensuring controller reliability
	- Open source routing software lowered the barrier to creating prototype implementations of centralized routing controllers
- These pushes inspired 2 main innovations
	- open interface between control/data planes
	- logically centralized control of the network
- different from active network in 2 ways
	- focused on spurring innovation by and for network admins rather than end users/researchers
	- emphasized programmability in the control domain rather than the data domain
	- worked towards network-wide visibility and control rather than device-level configurations
- use pulls
	- Selecting between network paths based on the current traffic load
	- Minimizing disruptions during planned routing changes
	- Redirecting/dropping suspected attack traffic
	-  Allowing customer networks more control over traffic flow
	- Offering value-added services for virtual private network customers

most work during this phase tried to manage routing within a single ISP, but there were proposals about ways to enable flexible route control across many administrative domains.

Resulted in a couple concepts which were used in further SDN design
- logically centralized control using an open interface to the data plane
- distributed state management

### 3. OpenFlow API and Network Operating Systems
https://github.com/mininet/openflow

- Took place from 2007 to 2010
- OpenFlow was born out of the interest in the idea of network experimentation at scale.
- Balances the vision of fully programmable networks and the practicality of ensuring real world deployment.
- OpenFlow built on existing hardware and enabled more functions than earlier route controllers.
- Dependency on hardware limited its flexibility, but enabled immediate deployment.
- Basic working of an OpenFlow switch
	- each switch contains a table of packet-handling rules
	- each rule has a pattern, list of actions, set of counters, and a priority
	- when an OpenFlow switch receives a packet, it determines the highest priority matching rule, performs the action, then increments the counter
- Technology push
	- Before OpenFlow, switch chipset vendors had already started to allow programmers to control some forwarding behaviors.
	- This allowed more companies to build switches without having to design and fabricate their own data plane.
	- Early OpenFlow versions built on technology that the switches already supported. This meant that enabling OpenFlow initially was as simple as performing a firmware upgrade!
- Use pulls
	- OpenFlow came up to meet the need of conducting large scale experimentation on network architectures. In the late 2000s, OpenFlow testbeds were deployed across many college campuses to show its capability on single-campus networks and wide area backbone networks over multiple campuses.
	- OpenFlow was useful in data-center networks – there was a need to manage network traffic at large scales.
	- Companies started investing more in programmers to write control programs, and less in proprietary switches that could not support new features easily.  This allowed many smaller players to become competitive in the market by supporting capabilities like OpenFlow.

Some key effects that OpenFlow had were
- generalizing network devices and functions
- the vision of a network operating system
- distributed state management techniques

### SDN History Key Takeaways
- Active Networks consists mainly of creating a programming interface that exposed resources/network nodes and supported customization of functionalities for subsets of packets passing through the network
- The control and data plane phase was focused on separating the concerns of a switch
- Open Flow is just good software

## Why Separate the Data Plane from the Control Plane?
- control plane contains the logic that controls the forwarding behavior of routers such as routing protocols and network middlebox configurations.
- The data plane performs the actual forwarding as dictated by the control plane.

> We are not the same.

IP forwarding and Layer 2 switching are functions of the data plane.

Reasons for separating the 2 include
1. Independent evolution and development
2. Control from high-level software program(s)

In addition, this separation leads to opportunities in different areas.
1. Data Centers - Easier network management.
2. Routing - It's easier to update router states across a network. SDN can provide more control over path selection.
3. Enterprise networks - SDN can improve the security applications for enterprise networks. SDN can make it easier to protect a network from volumetric attacks such as DDoS if the network drops the attack traffic at strategic locations.
4. Research networks - SDN allows research networks to coexist with production networks.

## Control Plane and Data Plane Separation
Two important functions of the network layer include forwarding and routing.
1. Forwarding
	- most common yet important functions of the network layer
	- forwarding is when a router sends a packet on an outgoing link.
	- Forwarding could also entail a router blocking a packet from exiting a router.
	- Forwarding is a local function for routers, and usually takes place in nanoseconds, as its is implemented in the hardware itself.
	- Forwarding is a function of the data plane.
2. Routing
	- Routing involves determining the path from sender to receiver across a network.
	- Routers rely on routing algorithms
	- Routing is a function of the control plane.

**In the traditional approach**, the routing algorithms (control plane) and forwarding function (data plane) are closely coupled. The router runs and participates in the routing algorithms. From there it is able to construct the forwarding table which consults it for the forwarding function.

![[Pasted image 20231018162914.png]]

**In the SDN approach**, there is a remote controller that computes and distributes the forwarding tables to be used by every router. This controller is physically separate from the router. It could be located in some remote data center, managed by the ISP or some other third party.

![[Pasted image 20231018162937.png]]

## SDN Architecture
The main components of an SDN are
- SDN-controlled network elements
	- the SDN-controlled network elements, sometimes called the infrastructure layer, is responsible for the forwarding of traffic in a network based on the rules computed by the SDN control plane
- SDN controller
	- the SDN controller is a logically centralized entity that acs as an interface between the network elements and the network-control applications
- Network control applications
	- The network-control applications are programs that manage the underlying network by collecting information about the network elements with the help of SDN controller

![[Pasted image 20231018163742.png]]

The 4 defining features in an SDN architecture are:
1. Flow-based forwarding
	- The rules for forwarding packets in SDN-controlled switches can be computed based on any number of header values in various layers such as
		- the transport layer
		- the network layer
		- the link layer
	- This differs from the traditional approach where only the destination IP address determines the forwarding of a packet.
	- OpenFlow allows up to 11 header fields to be considered
2. Separation of data plane and control plane
	- The SDN-controlled switches operate on the data plane and the only execute the rules in flow tables
	- Those rules are computed, installed, and managed by software that runs on separate servers.
3. Network control functions
	- The SDN control plane, running on multiple servers, consists of 2 components
		- The controller
		- Network applications
	- The controller maintains up to date network state information about the network devices and elements. Elements includes
		- hosts
		- switches
		- links
	- The controller provides the information to the network-control applications
	- This information is used by the applications to monitor and control the network devices.
4. A programmable network
	- The network control applications act as the "Brain" of the SDN control plane by managing the network
	- Example applications include
		- network management
		- traffic engineering
		- security
		- automation
		- analytics
		- etc
	- We can have an application that determines the E2E path between sources and destinations in the network using Dijkstra's algorithm.

## SDN Controller Architecture

The SDN controller is part of the SDN control plane and acts as an interface between the network elements and the network control applications

An SDN controller can be broadly split into 3 layers
- **Communication layer:** communicating between the controller and the network elements
- **Network-wide state-management layer:** stores information of network-state
- **Interface to the network-control application layer:**  communicating between controller and applications

The SDN controller, although viewed as a monolithic service by external devices and applications, is implemented by distributed servers to achieve fault tolerance, high availability and efficiency. Despite the issues of synchronization across servers, many modern controllers such as OpenDayLight and ONOS have solved it and prefer distributed controllers to provide highly scalable services.
### 1. Communication Layer
> This layer consists of a protocol through which the SDN controller and the network controlled elements communicate. Using this protocol, the devices send locally observed events to the SDN controller providing the controller with a current view of the network state. For example, these events can be a new device joining the network, heartbeat indicating the device is up, etc. The communication between SDN controller and the controlled devices is known as the “southbound” interface. OpenFlow is an example of this protocol, which is broadly used by SDN controllers today.

![[Pasted image 20231018180801.png]]

### 2. Network-wide state-management layer
> This layer is about the network-state that is maintained by the controller. The network-state includes any information about the state of the hosts, links, switches and other controlled elements in the network. It also includes copies of the flow tables of the switches. Network-state information is needed by the SDN control plane to configure the flow tables.
### 3. The interface to the network-control application layer
> This layer is also known as the controller’s “northbound” interface using which the SDN controller interacts with network-control applications. Network-control applications can read/write network state and flow tables in controller’s state-management layer. The SDN controller can notify applications of changes in the network state, based on the event notifications sent by the SDN-controlled devices. The applications can then take appropriate actions based on the event. A REST interface is an example of a northbound API.

