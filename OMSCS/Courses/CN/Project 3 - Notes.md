---
tags:
  - OMSCS
  - CN
---
# Project 3 - Notes

## Resources
- IP Header Format - https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-packet.html
- TCP Packet Header Format - https://en.wikipedia.org/wiki/Transmission_Control_Protocol
- UDP Packet Header Format - https://en.wikipedia.org/wiki/User_Datagram_Protocol
- The ICMP Protocol - https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
- IP Protocols - https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers    
- TCP and UDP Service and Port References - https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
- Wireshark - https://www.wireshark.org/docs/wsug_html/
- CIDR Calculator - https://account.arin.net/public/cidrCalculator
- CIDR - https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing

## Warmup Questions
> What is the IP (Internet Protocol)? What are the different types of Network Layer protocols?

The Internet Protocol (IP) exists in the network layer (aka the "internet layer") of the layered OSI model of the internet. IP's job is to deliver packets from source hosts to destination hosts based solely on IP addresses, which are located in the IP packet headers.

A IP packet is called a "datagram".

> Review TCP and UDP? How does TCP or UDP differ from IP?  

TCP and UDP are transport layer protocols. They depend on IP in order to work. The only thing that TCP and UDP have in common is that they allow hosts to "multiplex" multiple connections simultaneously.

Effectively, TCP adds many flow control options on top of IP. TCP also guarantees that all data reaches the intended destination, and guarantees that received packets are passed to the application layer in their proper order (not necessarily in the order they were received).

UDP just sends raw packets and doesn't concern itself with whether the network is overloaded nor does it concern itself with silly things like "packets actually reaching their destination" and "packets arriving in the order they were sent". Believe it or not, many applications prefer this behavior over TCP.

> Examine the packet header for a generic IP protocol entry. Contrast that with the packet header for a TCP packet, and for a UDP packet. What are the differences? What does each field mean?

![[Pasted image 20231021200508.png]]

- **Version** (always set to the value 4 in the current version of IP)
- **IP Header Length** (number of 32-bit words forming the header, usually five)
- **[Differentiated Services Code Point (DSCP)](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/dscp.html)**(6 bit field, sometimes set to 0, but can indicate a particular treatment, sometimes refelecting the Quality of Service needs of an application to the network. The DSCP informs a router how to queue packets while they are waiting to be forwarded).
- **Explicit Congestion Notification (ECN) Field** (2 bits)
    - 00 indicates the packet does not use ECN.
    - 01 indicates the packet is a part of an ECN-capable transport flow.
    - 10 indicates the packet is a part of an experimental ECN-capable transport flow.
    - 11 indicates the packet has experienced congestion.
- **Size of Datagram** (in bytes, this is the combined length of the header and the data)
- **Identification** (16-bit number which together with the source address uniquely identifies this packet - used during reassembly of [fragmented](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/intro-pages/segmentation.html) datagrams)
- **Flags** (a sequence of three flags (one of the 4 bits is unused) used to control whether [routers](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/router.html) are allowed to [fragment](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/intro-pages/segmentation.html) a packet (i.e. the [Don't Fragment, DF](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/mtu.html), flag), and to indicate the parts of a packet to the receiver)
- **Fragmentation Offset** (a byte count from the start of the original sent packet, set by any router which performs [IP router fragmentation](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/intro-pages/segmentation.html))
- **Time To Live** (Number of hops /links which the packet may be routed over, decremented by most [routers](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/router.html) - used to prevent accidental routing loops)
- **Protocol** ([Service Access Point (SAP)](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/intro-pages/sap.html) which indicates the type of transport packet being carried (e.g. 1 = [ICMP](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/icmp.html); 2= IGMP; 6 = [TCP](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/tcp.html); 17= [UDP](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/udp.html)).
- **Header Checksum** (A [1's complement checksum](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-cksum.html) inserted by the sender and updated whenever the packet header is modified by a [router](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/router.html) - Used to detect processing errors introduced into the packet inside a [router](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/router.html) or [bridge](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/lan-pages/bridge.html) where the packet is not protected by a link layer [cyclic redundancy check](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/dl-pages/crc.html). Packets with an invalid checksum are discarded by all nodes in an IP network)
- **Source Address** (the [IP address](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-address.html) of the original sender of the packet)
- **Destination Address** (the [IP address](https://web.archive.org/web/20221206011422/https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-address.html) of the final destination of the packet)
- **Options** (not normally used, but, when used, the IP header length will be greater than five 32-bit words to indicate the size of the options field)

> What constitutes a TCP Connection? How does this contrast with a UDP connection?

A TCP connection is formed when 2 hosts perform a 3-way TCP handshake. The connection is then used whenever each end of the connection wants to send segments to the other. The connection lives as long as the 2 hosts desire, and can be closed/terminated with a 4-segment termination procedure.

UDP is a "connectionless" protocol. UDP just sends segments to the network. The end host may receive them or not.

> A special IP protocol is ICMP. Why is ICMP important?

ICMP stands for "Internet Control Message Protocol". This is the protocol that is used when you run the `ping` CLI program. This protocol is used by network devices to send error messages and operational information to specific IP addresses.

These messages can be used to inform specific hosts of problems on the network. Most commonly, these messages are used when a packet is dropped due to its TTL hitting 0. The router which decides to drop the message will send an ICMP message back to the origin host.

This protocol is not typically used to exchange data. It's also not typically used by end-user applications, except for the ones that are specifically used for sending ICMP packets (`ping` and `traceroute`).

Traceroute is implemented by sending a packet to a destination host, incrementally increasing the TTL of the packet. Hosts along the most efficient route to the destination host will send ICMP messages back to the origin host (the end user's host) upon dropping the packet.

There are IPv4 and IPv6 variants of ICMP.

> What behavior happens when you do an ICMP Ping?

An ICMP ping is implemented by using "echo request" and "echo reply" messages. These messages are denoted via the "type" and "code" ICMP message headers.

One host will send an ICMP message to another host. The receiving host will respond with a separate ICMP message.

Hosts can choose not to respond to ICMP pings.

> If you block an ICMP response, what would you expect to see?



> If you block a host from ICMP, will you be able to send TCP/UDP traffic to it?

Yes. Blocking/disabling ICMP on a host, so that pings do not work, is pretty common. The internet continues to work without it.

> Can you explain what happens if you get a ICMP Destination Unreachable response?

A host will receive an "ICMP Destination Unreachable" when a packet is dropped due to its TTL expiring. The router which dropped the packet will send the ICMP DU packet.

> What is CIDR notation?

CIDR uses "slash" notation. The IP address before the slash denotes the base address. The number after the slash is the "mask" which denotes the number of bits which are the "prefix".

> How do you subnet a network?

Buddy, this is probably most of the reason why I decided to take the class in the first place. You tell me.

(Inhale. Exhale.)

You can divide a network into blocks using IP address ranges. These can be denoted using one of many different IP address range formats. The whole point of doing so is to segment a network into partitions of either equal or unequal blocks of IP addresses. This allows network administrators to group hosts by type/department/whatever, where each device within that group will have IP addresses which are "close" to one another.

 > What IP Protocols use Source or Destination Ports?

Mostly transport protocols, so TCP and UDP.
