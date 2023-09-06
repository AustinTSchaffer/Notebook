---
tags:
  - OMSCS
  - CN
  - TCP
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
Data Center TCP (DCTCP)  [[Data Center TCP (DCTCP).pdf]]

TIMELY: RTT-based Congestion Control for the Datacenter  [[TIMELY - RTT-based Congestion Control for the Datacenter.pdf]]

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

- In general, the network layer is considered unreliable for the majority of the connected web
	- Can lead to lost packets
	- can lead to out-of-order delivery
- UDP forces applications to account for network unreliability
- TCP guarantees in-order delivery of application-layer data without loss or corruption

- To have reliable communication, the sender should be able to know which segments were received, and which need to be retransmitted.
	- If the sender does not receive an acknowledgment within a given period of time, the sender can assume the packet is lost and resend it. 
	- This method of using acknowledgments and timeouts is also known as **Automatic Repeat Request or ARQ.**

- Simplest method is **Stop and Wait ARQ**
	- Send / Wait for ACK / Resend or Send
	- Typically the timeout value is a function of the estimated round trip time (RTT) of the connection.
	- Obviously performs terribly.

- To solve the performance issues of Stop and Wait, sender can send at most N un-acked packets, typically referred to as a "window size"
	- Each packet is tagged with a unique ID, an incrementing "byte sequence number"
	- Both the sender and receiver need to buffer more than one packet.
		- Sender: Packets sent and not acked
		- Receiver: Packets which are out of order, cases where consuming the packets is slower than network transmission rate

### Method A: "Go-back-N"
- Receiver sends an ACK for the most recently received in-order packet.
- Sender would then send all packets from the most recently received in order packet, even if some of them had already been sent and successfully received.
- Receiver can discard duplicates.

![[Pasted image 20230830211507.png]]

Major downside: If many messages are sent at a time, one error can result in many being retransmitted.

### Selective ACKing

- sender retransmits only those packets that it suspects were lost.
- Receiver would ACK a correctly received packet even if it's not in order
- The out of order packets are buffered until any missing packets have been received.
- Receiver keeps packets in a buffer until it has enough in-order segments to send to the application layer.
- When the sender receives 3 duplicate ACKs for a packet, it considers the packet to be lost and will retransmit it instead of waiting for the timeout This is known as **fast retransmit.**

## Transmission Control
> Consider a scenario when user A needs to send a 1 Gb file to a remote host B on a 100 Mbps link. What rate should it send the file? One could say that it should be 100 Mbps. But how does user A determine that since it does not know the link capacity? Also, what about other users that also would be using the same link? What happens to the sending rate if receiver B is also receiving files from other users? Finally, which layer in the network decides the data transmission rate? In this section, we will try to answer all these questions.

- UDP: Let the application layer figure it out
- TCP: Figure it out so the application layer doesn't have to

## Flow Control
> Controlling the Transmission Rate to Protect the Receiver buffer

- Protect the receiver buffer from overflowing
- TCP uses "flow control" to help match the sender's rate against the receiver's rate of reading the data
- The sender maintains a variable named "receive window" (`rwnd`), which provides the sender an idea of how much data the receiver can handle at the moment

The receiving host maintains two variables:
- **`LastByteRead`**: the number of the last bytes in the data stream read from the buffer by the application process in the receiver
- **`LastByteRcvd`**: the number of the last bytes in the data stream that has arrived from the network and has been placed in the receive buffer at the receiver
- to not overflow the buffer, TCP needs to make sure that: `LastByteRcvd - LastByteRead <= RcvBuffer`
- The extra space that the receive buffer has is specified using a parameter termed as receive window. `rwnd = RcvBuffer - [LastByteRcvd - LastByteRead]`
- The receiver advertises the value `rwnd` in every segment/ACK it sends back to the sender.

The sender
- also keeps track of two variables, **`LastByteSent`** and **`LastByteAcked`**.
- To not overflow the receiver’s buffer, the sender must ensure that the maximum number of unacknowledged bytes it sends is no more than the `rwnd`. Thus we need: `LastByteSent – LastByteAcked  <= rwnd`

TCP still instructs the sender to continue sending segments of size 1 byte even after `rwnd = 0`. When the receiver acknowledges these segments, it will specify the `rwnd` value, and the sender will know as soon as the receiver has some room in the buffer. This prevents deadlocks.

## Congestion Control
> Controlling the transmission rate to  protect the network from congestion

- We do not want the combined transmission rate to be higher than the link's capacity as it can cause issues in the network such as long queues, packet drops, etc.
- Transport layer protocols need a mechanism for controlling the transmission rate at the sender to avoid congestion in the network.
- Important to note that a network's effective throughput is dynamic, as machines go on/off-line and as more applications make use of the network.

### Goals of congestion control
- **Efficiency**. We should get high throughput, or utilization of the network should be high.
- **Fairness.** Each user should have their fair share of the network bandwidth. The notion of fairness is dependent on the network policy. For this context, we will assume that every flow under the same bottleneck link should get equal bandwidth.
- **Low delay**. In theory, it is possible to design protocols with consistently high throughput assuming infinite buffer. Essentially, we could keep sending the packets to the network, and they will get stored in the buffer and eventually get delivered. However, it will lead to long queues in the network leading to delays. Thus, applications sensitive to network delays such as video conferencing will suffer. Therefore, we want the network delays to be minor. 
- **Fast convergence.** The idea here is that a flow should converge to its fair allocation fast. Fast convergence is crucial since a typical network’s workload is composed of many short flows and few long flows. If the convergence to fair share is not fast enough, the network will still be unfair for these short flows.

### Network-assisted Congestion Control
- Rely on the network layer to provide feedback to the sender about congestion in the network
- Routers could use an "ICMP source quench" to notify the source that the network is congested
- Even ICMP packets could be lost under severe congestion, rendering feedback ineffective

### E2E Congestion Control
- Network does not provide feedback
- Controlled by transport layer protocol
- TCP uses an E2E approach

2 main signals of congestion that hosts can use to infer congestion
- packet delay
	- queues in the routers build-up, leading to increased packet delays
	- increase in round-trip time (RTT)
	- can be estimated based on ACKs
	- packet delays are variable, making delay-based congestion inference tricky
- packet loss
	- as the network gets congestion, routers may start dropping packets
	- packets can also be lost due to other reasons such as
		- routing errors
		- hardware failure
		- time-to-live (TTL) expiration
		- error in the links
		- flow congestion problems

Earliest implementation of TCP used packet loss as a signal for congestion.

### Hybrid Approach
- transport layer implements its own congestion control mechanisms
- Routers in modern networks also supply feedback to the end hosts using protocols such as ECN and QCN
	- ECN: Explicit Congestion Notification (https://en.wikipedia.org/wiki/Explicit_Congestion_Notification)
	- QCN: Quantized Congestion Notification (https://www.ieee802.org/1/files/public/docs2007/au_prabhakar_qcn_overview_geneva.pdf)

## TCP: Limiting the Sending Rate
Each source can
- determine the network's available capacity
- choose how many packets to send without adding to the network's congestion level

Each source uses ACKs as a probing mechanism. If the receiving host received a packet sent earlier, it would release more packets into the network.

TCP uses a congestion window similar to the receive window used for flow control. It represents the max number of unACKed data that a sending host can have in transit (sent but not yet ACKed)

TCP uses a probe-and-adapt approach in adapting the congestion window. Under normal conditions, TCP increases the congestion window trying to achieve the available throughput. Once it detects congestion, the congestion window is decreased.

In the end, the number of unacknowledged data that a sender can have is the minimum between the congestion window and the receive window. 

`LastByteSent – LastByteAcked <= min{cwnd, rwnd}`

## Congestion Control at TCP - AIMD
> additive increase/multiplicative decrease (AIMD)

As network congestion increases, TCP:
- decreases the window when the level of congestion goes up
- increases the window when the level of congestion goes down

TCP will increase the window size linearly, but will decrease the window size drastically.

> The main reason for this approach is that the consequences of having too large a window are much worse than those of it being too small. When the window is too large, more packets will be dropped and retransmitted, making network congestion even worse; thus, it is crucial to reduce the number of packets being sent into the network as quickly as possible.

TCP continually increases and decreases the congestion window throughout the lifetime of the connection. If we plot `cwnd` with respect to time, we observe that it follows a sawtooth pattern as shown in the figure:

![[Pasted image 20230903123140.png]]

### Additive Increase
- Connections typically start with a constant initial window, typically with a size of 2
- The idea is to increase the window by one packet for each RTT (round-trip time)
- Every time the sending host successfully sends a CongestionWindow (`cwnd`) number of packets it adds 1 to `cwnd`.
- TCP does not wait for ACKs of all the packets from the previous RTT.
- Instead it increases the congestion window size as soon as each ACK arrives.
- In bytes, this increment is a portion of the Maximum Segment Size (MSS)
	- `Increment = MSS × (MSS / CongestionWindow)`
	- `CongestionWindow += Increment`

### Multiplicative Decrease
- Once TCP detects congestion, it reduces the rate at which the sender transmits.
- When the sender detects packet loss, it divides `cwnd` by 2

### TCP Reno
> Different implementations of TCP use variations to control congestion and maximize bandwidth usage. For example, TCP Reno uses two types of loss events as a signal of congestion. The first is the **triple duplicate ACKs, which is considered** mild congestion. In this case, the congestion window is reduced to half the original.

> The second kind of congestion detection is **timeout**, i.e., when no ACK is received within a specified amount of time. It is considered a more severe form of congestion, and the congestion window is reset to the initial window size.

Different implementations of TCP use variations to control congestion and maximize bandwidth usage. For example, TCP Reno uses two types of loss events as a signal of congestion.
- The first is the **triple duplicate ACKs, which is considered** mild congestion. In this case, the congestion window is reduced to half the original.
- The 2nd is timeouts.

![[Pasted image 20230903123336.png]]

## Slow Start
> AIMD takes forever to fully utilize a network that has low congestion. For a new connection, we need a mechanism that can rapidly increase the congestion window from a cold start.

TCP Reno has a **slow start phase** where the congestion window is increased exponentially instead of linearly.

![[Pasted image 20230903123701.png]]

![[Pasted image 20230903123725.png]]

It's called "slow start" (despite being a faster start than AIMD) because the exponential increase is slower than just starting with a large window.

A connection can die while waiting for a timeout to occur.
- This happens when the source has sent enough data as allowed by the flow control mechanism of TCP but times out while waiting for the ACK. 
- Thus, the source will eventually receive a cumulative ACK to reopen the connection.
- Then, instead of sending the available window size worth of packets at once, it will use the slow start mechanism.

> The source will have a fair idea about the congestion window from the last time it had a packet loss. It will now use this information as the “target” value to avoid packet loss in the future. This target value is stored in a temporary variable, `CongestionThreshold`.

Key terms
- congestion threshold (a knee point)
- increases window by 1 (additive increase)
- packet loss (cliff point)

## TCP Fairness
> Fairness means that for $k$ connections passing through one common link with capacity $R$, each connection gets an average throughput of $R/k$.

![[Pasted image 20230903124227.png]]

AIMD leads to fairness in bandwidth sharing. If both connections experience packet loss or a timeout, they will both divide their `cwnd` by 2. The connection that has the highest `cwnd` will lose more value from its `cwnd` than connections with comparatively lower `cwnd` values. After that, all connections will start linearly increasing their `cwnd` values again. Over successive cliff points, the average throughput of each connection will tend toward $R/k$.

This phenomenon is shown visually on the chart with points A, B, C, and D.

### AIAD vs MIMD vs MIAD vs AIMD
In AIAD and MIMD, the plotted throughput line will oscillate over the full bandwidth utilization line but will not converge as was shown for AIMD. On the other hand, MIAD will converge.

None of the alternative policies are as stable. The decrease policy in AIAD and MIAD is not as aggressive as AIMD, so those will not effectively address congestion control. In contrast, the increase policy in MIAD and MIMD is too aggressive.

### TCP Unfairness
> TCP Reno uses ACK-based adaptation of the congestion window. Thus, connections with smaller RTT values would increase their congestion window faster than those with longer RTT values. This leads to an unequal sharing of the bandwidth.

Another case of unfairness arises if a single application uses multiple parallel TCP connections. In this case, the application made by the savviest developer wins.

## TCP CUBIC: Congestion Control in Modern Network Environments
> TCP Reno has low network utilization, especially when the network bandwidth is high or the delay is large. Such networks are also known as high bandwidth delay product networks.

[[CUBIC - A new TCP-Friendly High-Speed TCP Variant.pdf]]

TCP CUBIC is one variation of TCP which attempts to be more efficient in high-bandwidth delay product networks. It uses a CUBIC polynomial as the growth function.

![[Pasted image 20230903130312.png]]

```python
md_factor = 2

if packet_loss_detected:
	wmax = cwnd
	wmin, cwnd = cwnd / md_factor

# Increase cwnd quickly
# On approach to wmax, increase cwnd slowly
# After a while, increase cwnd quickly again
```

$W(t) = C(t-K)^3 + W_{max}$

$K=\sqrt{\frac{W_{max}*\beta}{C}}$

- $W$ is the congestion window (`cwnd`)
- $W_{max}$ is the window when packet loss was detected
- $C$ is a scaling constant.
- $K$ is the time period that the above function takes to increase $W$ to $W_{max}$ when there is no further loss event.

TCP CUBIC RTT-fair because it's based on absolute time, not ACK-based. 

> \[...\] its window growth depends only on the time between two consecutive congestion events. One congestion event is the time when TCP undergoes fast recovery. This feature allows CUBIC flows competing in the same bottleneck to have approximately the same window size independent of their RTTs, achieving good RTT-fairness.

## TCP Throughput
![[Pasted image 20230903131348.png]]

Let's assume that our network has a probability of losing a packet $p$, our "probability of loss". We assume that the network on average delivers $p^{-1}$ consecutive packets per packet lost.

Because the congestion window (`cwnd`) size increases a constant rate of 1 packet for every RTT, the height of the sawtooth is $W/2$, and the width of the base is $W/2$, which corresponds to $W/2$ rounds trips, or $RTT(W/2)$.

The number of packets sent in one cycle is the area under the sawtooth.

$Total={(\frac{W}{2})}^2+0.5{(\frac{W}{2})}^2=\frac{3}{8}W^2$

Given our loss probability statement:

$p^{-1}=\frac{3}{8}W^2$

solving for W gives the max value:

$W=\sqrt{\frac{8}{3p}}$

Notation refresher
- $BW$ = bandwidth
- $MSS$ = "max segment size"
- $RTT$ = "round-trip time".

$BW=\frac{data \space per \space cycle}{time \space per \space cycle}=\frac{MSS*\frac{3}{8}W^2}{RTT*\frac{W}{2}}$

after plugging in our value for $W$ and doing some algebra

$BW = \frac{MSS}{RTT}*\sqrt{\frac{3}{2}}*\frac{1}{\sqrt{p}}$

> In practice, because of additional parameters, such as small receiver windows, extra bandwidth availability, and TCP timeouts, bandwidth is usually bounded according to:

$BW < \frac{MSS}{RTT}*\frac{1}{\sqrt{p}}$

## Datacenter TCP
A lot of research has gone into optimizing congestion control mechanisms.

Similarly, data center (DC) networks are other networks where new TCP congestion control algorithms have been proposed and implemented. 

There are mainly two differences that have led to this:
1. The flow characteristics of DC networks are different from the public Internet. For example, there are many short flows that are sensitive to delay. Thus, the congestion control mechanisms are optimized for delay and throughput, not just the latter alone.
2. A private entity often owns DC networks. This makes changing the transport layer easier since the new algorithms do not need to coexist with the older ones.

DCTCP and TIMELY are two popular examples of TCP designed for DC environments.

DCTCP is based on a hybrid approach of using both implicit feedback, e.g., packet loss, and explicit feedback from the network using ECN for congestion control. Paper: [[Data Center TCP (DCTCP).pdf]]

TIMELY uses the gradient of RTT to adjust its window. Paper: [[TIMELY - RTT-based Congestion Control for the Datacenter.pdf]]

AWS also has a fancy proprietary one: [[A_Cloud-Optimized_Transport_Protocol_for_Elastic_and_Scalable_HPC.pdf]]

