---
tags: OMSCS, CN
---
# Lesson 01 - Introduction, History, and Internet Architecture

## Introduction
- Major milestones
- Design choices and principles
- The internet has an hourglass figure
- How would we redesign the internet if we could start over?
	- network control
	- management
	- accountability
- Learning how 2 hosts exchange data
	- protocols
	- infrastructure
- First lecture: devices (bridges, switches, etc)

## Why Study Networks?

- Internet growth
	- IoT
	- vehicles
	- sensors
	- home devices
	- the number of Internet users keeps increasing
- Networks are fundamental infrastructure for 21st-century living
	- business
	- communication
- Networks are prime targets
	- cyber attacks
	- fake news
	- censorship
- Legal implications
- "Networking is a playground for interdisciplinary research innovations"
	- technologies
	- systems
	- algorithms
	- applications
	- innovations
		- distributed systems
		- operating systems
		- computer architecture
		- software engineering
		- algorithms and data structures
		- graph theory
		- queuing theory
		- game theory
		- AI
		- cryptography
		- programming languages
		- formal methods
- "Networking offers multidisciplinary research opportunities with potential for impact"
	- how to incentivize internet providers to keep their networks clean from infected hosts
	- security, economics, social sciences

## A Brief History

- J.C.R. Licklider proposed the "Galactic Network" (1962)
- ARPANET (1969)
- Network Control Protocol (NCP), an initial ARPANET host-to-host protocol (1970)
- Internetworking and TCP/IP (1973)
- The Domain Name System (DNS) (1983) and the World Wide Web (WWW) (1990)

## Internet Architecture Introduction
> The internet architecture is what enables us to connect hosts running the same applications but located in different types of networks. 

![[Pasted image 20230826142914.png]]

> **Layered architecture advantages: scalability, modularity, and flexibility.** Some of the advantages of having a layered network stack include scalability, modularity and the flexibility to add or delete components which make for cost-effective implementations.

## OSI Model
> The Internet architecture follows a layered model, where every layer provides some service to the layer above.

ISO proposed a 7-layered OSI model. Consists of the following layers
- application layer
- **presentation layer (not in 5-layer model)**
- **session layer (not in 5-layer model)**
- transport layer
- network layer
- data link layer
- physical link layer

There's also the 5-layer IP-Stack model
- application layer
- transport layer
- network layer
- data link layer
- physical link layer

To get from the 7-layer model to the 5-layer model, the application/presentation/session layers are all combined into a single "application" layer. **The interface between the application layer and the transport layer are sockets.**

The app dev designs the functionality of the overall application.

Separating the functionalities into layers offers multiple advantages. But, there are also disadvantages of the layered protocol stack model. Some of the disadvantages include:

1. Some layers functionality depends on the information from other layers, which can violate the goal of layer separation.
2. One layer may duplicate lower layer functionalities. For example, the functionality of error recovery can occur in lower layers, but also on upper layers as well. 
3. Some additional overhead that is caused by the abstraction between layers.

### Application Layer

![[Pasted image 20230826143609.png]]

includes the HTTP, FTP, DNS protocols

### Presentation Layer

![[Pasted image 20230826143640.png]]

### Session Layer

![[Pasted image 20230826143707.png]]

> in the case of teleconference application, it is responsible to tie together the audio stream and the video stream.

### Transport Layer

![[Pasted image 20230826143752.png]]

This layer includes the TCP and UDP transport protocols. Many proprietary protocols exist within data centers.

"Packets are segments"

### Network Layer

![[Pasted image 20230826143856.png]]

Protocols in this layer include IPv4, IPv6, routing.

"packets are datagrams"

The IP protocol defines
- the fields in each datagram
- how the source/destination hosts and the intermediate routers use these fields.

This layer includes routing protocols which determine the routes that datagrams can take between sources and destinations.

### Data Link Layer

![[Pasted image 20230826144128.png]]

Some example protocols in this layer include Ethernet, PPP, WiFi.

> The data link layer is responsible to move the frames from one node (host or router) to the next node. At each node across this path, the network layer passes the datagram to the data link layer, which in turn delivers the datagram to the next node. Then, at that node, the link layer passes the datagram up to the network layer.

> The data link layer offers services that depend on the data link layer protocol that is used over the link. Some example services include reliable delivery, that covers the transmission of the data from one transmitting node, across one link, and finally to the receiving node. We note that this specific type of reliable delivery service is different from the reliable delivery service that is offered by the TCP protocol which offers reliability from the source host to the destination end host.

### Physical Layer

![[Pasted image 20230826144338.png]]

> The physical layer facilitates the interaction with the actual hardware. It is responsible to transfer bits within a frame between two nodes that are connected through a physical link. The protocols in this layer again depend on the link and on the actual transmission medium of the link. One of the main protocols in the data link layer, Ethernet, has different physical layer protocols for twisted-pair copper wire, coaxial cable, and single-mode fiber optics.

## Encapsulation
> The process of taking data from one protocol and translating it into data that are used by another protocol, so the data can continue across a network.

![[Pasted image 20230826144514.png]]

![[Pasted image 20230826144541.png]]

- M: message (aka "the payload")
- HT: transport layer header (aka "a segment")
- HN: network header information (aka "a datagram")
- HL: link layer header information (aka "a frame")

Adding an additional header is called "encapsulation". Removing/decoding a header is called "de-encapsulation".

At each handoff point, each protocol adds an additional layer of header information. The application/firmware/hardware at the receiving end has to strip off the header information and determine what to do with the contents.

> **A design choice.** We note again that end-hosts implement all five layers while the intermediate devices don’t. This design choice ensures that the Internet architecture puts much of its complexity and intelligence at the edges of the network while keeping the core simple. Next, we will look deeper into the so-called end-to-end principle.

The path that connects the sending and the receiving hosts may include
- intermediate layer-3 devices, such as routers
- layer-2 devices, such as switches.

> We will see later how switches and routers work, but for now we note that both routers and layer-2 switches implement protocol stacks similarly to end-hosts. The difference is that routers and layer-2 switches do not implement all the layers in the protocol stack; routers implement layers 1 to 3, and layer-2 switches implement layers 1 to 2.

## The End-to-End (e2e) Principle

![[Pasted image 20230826145131.png]]

![[Pasted image 20230826145204.png]]

Building specialized functions into the network core to support specific applications is not necessary and should be avoided.

![[Pasted image 20230826145335.png]]

TLDR: The E2E principle is to keep the network infrastructure as simple as possible, and to give application designers the flexibility to think about their protocol.

Pop Quiz

> Q: Some data link layer protocols, such 802.11 (WiFi), implement some basic error correction as the physical medium used is easily prone to interference and noise (such as a nearby running microwave). Is this a violation of the end-to-end principle?

> A: No, because violations of the e2e principle typically refer to scenarios where it is not possible to implement a functionality entirely at the end hosts, such as NAT and firewalls.

## Violations of the E2E Principle

### Firewalls
- operate on the periphery of a network
- capable of dropping the communication between end 2 hosts

### Network Address Translation (NAT) Boxes
![[Pasted image 20230826145903.png]]

- Devices on a private network
- Outgoing traffic all has the same public-facing IP address, regardless of source device
- Incoming traffic has the same public-facing IP address, and the NAT box must then route the packets to the intended destination
- Violation because...
	- The hosts behind NAT boxes are not globally addressable or routable.
	- As a result, it is not possible for other hosts on the public Internet to initiate connections to these devices.
	- So, if we have a host behind a NAT and a host on the public Internet, they cannot communicate by default without the intervention of a NAT box.

![[Pasted image 20230826150119.png]]

![[Pasted image 20230826150230.png]]

Some workarounds allow hosts to initiate connections to hosts that exist behind NATs.
- For example, STUN is a tool that enables hosts to discover NATs and the public IP address and port number that the NAT has allocated for the applications for which the host wants to communicate.
- Also, UDP hole punching establishes bidirectional UDP connections between hosts behind NATs.
- Port-forwarding on the NAT.

## Hourglass Shape

![[Pasted image 20230826150352.png]]

[[The Evolution of Layered Protocol Stacks Leads to an Hourglass-Shaped Architecture.pdf]]

## Evolutionary Architecture Model

![[Pasted image 20230826150643.png]]

> The EvoArch model suggests that the TCP/IP stack was not trying to compete with the telephone network services. The TCP/IP was mostly used for applications such as FTP, E-mail, and Telnet, so it managed to grow and increase its value without competing or being threatened by the telephone network, at that time that it first appeared. Later it gained even more traction, with numerous and powerful applications relying on it.

> IPv4, TCP, and UDP provide a stable framework through which there is an ever-expanding set of protocols at the lower layers (physical and data-link layers), as well as new applications and services at the higher layers.

> A large birth rate at the layer above the waist can cause death for the protocols at the waist if these are not chosen as substrates by the new nodes at the higher layers.

> the transport layer acts as an “evolutionary shield” for IPv4, because any new protocols that might appear at the transport layer are unlikely to survive the competition with TCP and UDP which already have multiple products.

> In other words, the stability of the two transport protocols adds to the stability of IPv4, by eliminating any potential new transport protocols, that could select a new network layer protocol instead of IPv4.

Ramifications of the hourglass shape
- Many technologies that were not originally designed for the internet have been modified so they have versions which can communicate over "the internet" (network hardware)
	- Radio over IP
	- VoIP
- It has been difficult to transition from IPv4 to IPv6, despite the shortage of public IPv4 addresses.

## Interconnecting Hosts and Networks

### Repeaters and Hubs
- Operate on the Physical Layer (L1)
- receive and forward signals to connect different Ethernet segments
- Provide connectivity between hosts that are directly connected (in the same network)
- Advantage is that they are simple and inexpensive, and can be arranged in a hierarchy
- Unfortunately, hosts that are connected through these devices belong to the same collision domain, meaning they compete for access to the same link

### Bridges and Layer-2 Switches
- Enable communication between hosts that are not directly connected
- The operate on the data link (L2) layer based on MAC addresses
- The receive packets and forward them to reach the appropriate destination
- Limitation is the finite bandwidth of the outputs
	- If the arrival rate of the traffic is higher than the capacity of the outputs, then packets are temporarily stored in buffers
	- If the buffer fills up, this can (will) lead to packet drops

A bridge is a device with multiple inputs/outputs. A bridge transfers frames from an input to one (or multiple) outputs. Though it doesn’t need to forward all the frames it receives.

A **learning bridge** learns, populates and maintains, a forwarding table. The bridge consults its forwarding table so that it only forwards frames on specific ports, rather than all ports.

Consider the topology in the diagram below. When the bridge receives a frame on port 1, with source Host A and destination Host B, the bridge does not have to forward it to port 2.

![[Pasted image 20230826152136.png]]

When the bridge receives any frame this is a "learning opportunity" to know which hosts are reachable through which ports. This is because the bridge can view the port over which a frame arrives and the source host. Going back to our example topology, eventually the bridge builds the following forwarding table.

| Host | Port |
| ---- | ---- |
| A    | 1    |
| B    | 1    |
| C    | 1    |
| X    | 2    |
| Y    | 2    |
| Z    | 2     |

### Routers and Layer-3 Switches
- These are devices which operation on Layer 3

## Looping Problem in Bridges and the Spanning Tree Algorithm

Using bridges to connect LANs fails if the network topology results in loops (cycles). In that case, the bridges loop through packets forever!

![[Pasted image 20230826152358.png]]

Example Topology

![[Pasted image 20230826152426.png]]

Resulting spanning tree:

![[Pasted image 20230826152436.png]]

- Bridges B3 and B6 are removed from the network. Traffic can still reach these nodes.
- The link from B7 to node "B" was removed.
- Note that this spanning tree is only guaranteed to be comprehensive and acyclic, not optimal. There are no guarantees made about E2E connection performance.