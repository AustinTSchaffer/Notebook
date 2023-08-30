---
tags: OMSCS, CN
---
# Lesson 02 - Transport and Application Layers

This lesson mainly focuses on the TCP protocol.

Reading: [[CUBIC - A new TCP-Friendly High-Speed TCP Variant.pdf]]

Optional Readings

Congestion Avoidance and Control  
[https://ee.lbl.gov/papers/congavoid.pdf](https://ee.lbl.gov/papers/congavoid.pdf)

A Protocol for Packet Network Intercommunication  
[https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf)
End-to-End Internet Packet Dynamics  
[https://people.eecs.berkeley.edu/~sylvia/cs268-2019/papers//pktdynamics.pdf](https://people.eecs.berkeley.edu/~sylvia/cs268-2019/papers//pktdynamics.pdf)
Data Center TCP (DCTCP)  
[https://people.csail.mit.edu/alizadeh/papers/dctcp-sigcomm10.pdf](https://people.csail.mit.edu/alizadeh/papers/dctcp-sigcomm10.pdf "Link")

TIMELY: RTT-based Congestion Control for the Datacenter  
[https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p537.pdf](https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p537.pdf "Link")

Design, implementation and evaluation of congestion control for multipath TCP  
[https://www.usenix.org/legacy/events/nsdi11/tech/full_papers/Wischik.pdf](https://www.usenix.org/legacy/events/nsdi11/tech/full_papers/Wischik.pdf)

Sizing Router Buffers  [https://web.archive.org/web/20210120232627/http://yuba.stanford.edu/techreports/TR04-HPNG-060800.pdf](https://web.archive.org/web/20210120232627/http://yuba.stanford.edu/techreports/TR04-HPNG-060800.pdf)

## Introduction

The transport layer provides end-to-end connection between 2 applications running on different hosts.

Reminders from [[Lesson 01 - Introduction, History, and Internet Architecture]]
- Transport layer packets are known as "segments"
	- Transport layer header
	- Application layer payload
- 2 most common protocols in this space are TCP (verify delivery) and UDP (fire and forget)

## Multiplexing

This is what allows the transport layer to support the host running multiple applications that are using the network simultaneously.
- Network layer only uses IP addresses
- IP address alone does not have any information about the source/destination application

Transport layer uses ports as an additional identifier. Each application binds itself to a unique port number by opening sockets and listening for any data from a remote application. These ports are what the transport layer uses to guarantee delivery to the correct application.

2 methods for multiplexing
- Connectionless
- Connection-oriented

Note from course instructors:

> Q: Why don’t UDP and TCP just use process IDs rather than define port numbers?
> 
> A: Process IDs are specific to operating systems and therefore using process IDs rather than a specially defined port would make the protocol operating system dependent. Also, a single process can set up multiple channels of communications and so using the process ID as the destination identifier wouldn’t be able to properly demultiplex, Finally, having processes listen on well-known ports (like 80 for http) is an important convention.

Socket metadata
![[Pasted image 20230829195651.png]]

### Connection Oriented Multiplexing

TCP uses these conventions

![[Pasted image 20230829195959.png]]

![[Pasted image 20230829200048.png]]

![[Pasted image 20230829200115.png]]

![[Pasted image 20230829200226.png]]

Note the images above has a typo. One of the packets should have "Source IP: A"

HTTP uses TCP. HTTP uses persistent connections (aka keep-alive conventions) which instructs the server-side clients to keep a single TCP connection open for multiple HTTP requests/responses. This allows the server to reuse a connection and a socket.

### Connectionless Multiplexing

UDP uses these conventions

![[Pasted image 20230829195752.png]]

## More Notes on UDP
> UDP is an unreliable protocol.

Used for
- gaming
- VPNs

Advantages
- no congestion control or similar mechanisms
	- TCP "intervenes" with congestion control mechanisms
	- TCP retransmits packets when they are not acknowledged
- No connection management overhead
	- TCP uses a 3-way handshake before transferring data
	- UDP forgoes the connection and starts sending data immediately

![[Pasted image 20230829201736.png]]

UDP packets have a 63-bit header consisting of
- source port number
- destination port number
- length of the UDP segment (header + data)
- checksum

## TCP 3-way Handshake
Before 2 hosts can exchange data over TCP, they need to establish a connection.

- Step 1 (Connection Request)
	- TCP client sends a special segment (containing no data) with the `SYN` bit set to 1.
	- The client also generates an initial sequence number (`client_isn`) and includes it in this special TCP SYN segment
- Step 2 (Connection Granted)
	- The server allocates the required resources for the connection and sends back the special "connection granted" segment (`SYNACK`)
		- `SYN` bit is set to one
		- The acknowledgement field of the TCP segment header is set to `client_isn + 1`
		- The server adds a randomly chosen initial sequence number (`server_isn`)
- Step 3 (ACK)
	- When the client receives the SYNACK segment, it also allocates buffer and resources for the connection and sends an acknowledgement with the SYN bit set to 0.

![[Pasted image 20230829211112.png]]

## TCP Connection Teardown

- Step 1
	- When the client wants to end the connection, it sends a segment with the `FIN` bit set to 1
- Step 2
	- The server acknowledges that it received the connection close request and is now working on closing the connection
- Step 3
	- The server then sends a segment with the `FIN` bit set to 1, indicating that the connection is closed
- Step 4
	- The client sends an ACK to the server.
	- It also waits for sometimes to resend this acknowledgement in case the first ACK segment is lost.

![[Pasted image 20230829211418.png]]

## Reliable Transmission