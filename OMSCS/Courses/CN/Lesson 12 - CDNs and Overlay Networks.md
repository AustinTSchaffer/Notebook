---
tags:
  - OMSCS
  - CN
---
# Lesson 12 - CDNs and Overlay Networks
> The classic way of providing content on the Internet was to put the content on a single, publicly accessible web server. This traditional method is pretty straightforward - even at scale, having a single, massive data center to service all the requests for one Internet video company is a simple design. However, this traditional approach has three significant drawbacks when discussing the modern Internet and usage patterns.

- users are located all over the globe.
- there’s a potentially vast geographic distance between the users and the data center
- further distance means packets traverse more inter-ISP links. Each user's effective bandwidth is limited by the weakest link.
- requests for the same content result in redundant data being sent out of the same links. This is inefficient, expensive, and wasteful
- the datacenter becomes a single point of failure. The links out of the datacenter are also a single point of failure

- almost all major video-streaming companies use CDNs (**Content Distribution Networks)**
- CDNs are networks of multiple, geographically distributed servers and/or data centers, with copies of content (videos, but also many other types of Web content), that direct users to a server or server cluster that can best serve the user’s request. 
- new challenges come with this approach

## CDN Challenges

- **Peering point congestion.**
	- There’s the business and financial motivation to upgrade the “first mile” (like web hosts) and the “last mile” (end users), but not for the “middle mile” where expensive peering points between networks and no revenue happens.
	- These points end up being bottlenecks causing packet loss and increased latency. 
- **Inefficient routing protocols.**
	- BGP has worked well over the decades and the massive growth of the best-effort Internet, but it was never designed for modern demands. 
	- the algorithm only uses AS hop count
	- does not taking into account other factors (like congestion, latencies, etc.)
	- BGP has well-documented vulnerabilities to malicious actions
	- BGP is not an efficient interdomain routing protocol for the modern Internet.
- **Unreliable networks**
	- Outages happen all the time.
	- Some are accidents - like misconfigured routers, power outages in an area, and accidental severing of undersea fiber cables.
	- Some are malicious, such as DDoS attacks or BGP hijacking.
	- Some are caused by natural disasters
- **Inefficient communication protocols.**
	- Like BGP, TCP was not designed for the demands of the modern Internet.
	- TCP provides reliability and congestion avoidance, there’s a lot of overhead. 
	- TCP requires an ACK for each window of data packets sent
	- the distance between the server and the end user becomes the overriding bottleneck.
	- Enhancements to TCP are slow to actually get implemented across the whole Internet.
- **Scalability.**
	- Scalable internet applications can respond to current demand by changing resource usage, whether it be a video unexpectedly going viral or a planned event (like Black Friday shopping traffic peaks).
	- Scaling up infrastructure is expensive and takes time, and it is hard to forecast capacity needs.
- **Application limitations and slow rate of change adoption**. 
	- it can take a long time for newer/better protocols to get adopted. 
	- EOL software, such as internet explorer, do not support newer protocols. 
	- if the server side is upgraded, there’s no benefit unless the end users also upgrade to client software that also supports the newer protocols

## CDNs and the Internet Ecosystem
- The internet was not originally designed for large-scale content distribution
- There is ever increasing demand for high-fidelity content delivery
- The demand has spurred the development and growth of CDNs
- The internet has also seen a topological flattening thanks to IXPs
- The internet shows more traffic being generated and exchanged locally instead of traveling to a centralized server

![[Pasted image 20231120123522.png]]

CDNs mean increased infrastructure costs
- real estate
- physical devices
- power / electricity
- maintenance
- upgrades

Some CDNs are private
- Google's CDN for YouTube

Some CDNs are 3rd party
- Akamai
- Limelight
- Distribute content on behalf of multiple content providers

## CDN Server Placement Approaches
### Enter Deep
![[Pasted image 20231120203033.png]]

- deploy many small clusters
- clusters are deployed "deep" into the access networks around the world
- Akamai uses this strategy
- Minimizes the distance between a user and the closest server cluster
- reduces delay, and increases the available throughput for each user
- downside is that it's hard to manage and maintain such a large number of smaller deployments

### Bring Home
![[Pasted image 20231120203048.png]]

- place larger clusters at key points, typically in IXPs
- fewer servers overall, so fewer hosts to manage
- larger delays/latencies, lower throughput, for end users

### Hybrid
- few large server clusters at key points
- many small server clusters closer to end users

> Google has 16 "mega data centers", ~50 clusters of hundreds of servers at IXPs, and many hundreds of clusters of tens of servers at access ISPs. These different server clusters deliver different types of content (like the ones at the access networks store the static portions of search result web pages). So they use a hybrid of both the enter deep and bring home approaches.

## How a CDN Operates
- the hard part is correctly managing DNS
- the CDN will need to intercept content requests in order to be able to decide which server cluster should service the request. Potential factors include
	- the location of the user
	- the load on the servers
	- current traffic

> Let’s consider a simple scenario: a content provider, ExampleMovies, pays ExampleCDN to distribute their content. ExampleMovies has URLs with “video” and an ID for the video (so _Star Wars 37_ might have a URL of http://video.examplemovies.com/R2D2C3PO37). Let’s walk through the six steps that occur when a user requests to watch _Star Wars 37_ on ExampleMovies.

1. The user visits examplemovies.com and navigates to the web page with _Star Wars 37._ 
2. The user clicks on the link http://video.examplemovies.com/R2D2C3PO37 and the user’s host sends a DNS query for the domain "video.examplemovies.com".
3. The DNS query goes to the user’s local DNS server (LDNS), which in many cases is a DNS server in their access ISP’s network. This DNS server issues an iterative DNS query for "video" to the authoritative DNS server for examplemovies.com, which is ExampleMovies’s DNS server. ExampleMovies’s DNS server knows that the "video" domain is stored on ExampleCDN, so it sends back a hostname in ExampleCDN’s domain, like a1130.examplecdn.com.
4. The user’s LDNS performs an iterative DNS query to ExampleCDN’s name server for a1130.examplecdn.com. ExampleCDN’s name server system (eventually) returns an IP address of an appropriate ExampleCDN content server to the user’s LDNS.
5. The user’s LDNS returns the ExampleCDN IP address to the user. Notice - from the user’s perspective, all that happened was they asked for an IP address for "video.examplemovies.com", and then they got an IP address back.
6. The user’s client directly connects via TCP to the IP address provided by the user’s LDNS, and then sends an HTTP GET request for the video.

![[Pasted image 20231120203947.png]]

### Cluster and Server Selection
> Recall that the content in CDN can be served from multiple servers that are geographically distributed. The first thing that needs to be done in order to serve the content to an end-user is to select the server to serve the content from. This process is quite important as it significantly impacts the end-user performance. If we end up picking a cluster that’s too far away or overwhelmed, the user’s video playback will end up freezing.

> There are two main steps in this process. The first step consists of mapping the client to a cluster. Recall that a CDN constitutes of geographically distributed clusters with each cluster containing a set of servers. In the next step, a server is selected from the cluster.

![[Pasted image 20231120204244.png]]

![[Pasted image 20231120204303.png]]

### Cluster Selection in Detail
- simplest strategy, closest geospatial distance, using approx lat/lon coordinates. Caveats:
	- a DNS server is the first point of contact for the CDN
		- "picking the cluster that's geographically closest to the user actually means you're picking the cluster that's geographically closest to the DNS/LDNS server that's making the domain name request"
		- This works fine most of the time. Some users use a remote LDNS.
		- Some suggestions have been made to include the end user's IP as part of the DNS request.
	- The geographically closest cluster might not have the best end-to-end network performance
		- BGP routing inefficiencies
		- network distances can differ from physical distances
		- can lead to higher RTTs, even if the server is closer
		- congested links are also a complicating factor
- Relying on a static cluster selection policy can be sub optimal, given that underlying network conditions are dynamic.
- Cluster selection can be based on realtime measurements of e2e performance metrics, such as delays

![[Pasted image 20231121111438.png]]

- RTT is likely not the only metric that CDN owners care about.
- instead they might combine few metrics and then optimize the overall value.

![[Pasted image 20231121111454.png]]

- example metrics
	- network-layer metrics
		- delay
		- available bandwidth
	- application-layer metrics
		- content type (video vs text)
		- page load time
- how to obtain real time measurements?
	- active measurements
		- LDNS could probe multiple clusters, using ping for example
		- monitor RTTs
		- use the cluster with the lowest RTT
		- Most LDNS are not equipped to perform active measurements
		- this generates a lot of traffic
	- passive measurements
		- the CDNs name server system could keep track of network conditions
		- current traffic conditions
		- metrics are aggregated for efficient analysis
		- clubbing IPs from the same subnet together
			- IPs under the same subnet are likely to have similar paths to different clusters
			- the best cluster for the same subnet can be noted based on the performance observed by existing sessions
		- measurement results are cached to be used by future requests
		- requires
			- a centralized controller which has a real-time view of the network conditions between all client-cluster pairs, or
			- an efficient distributed datastore

![[Pasted image 20231121111834.png]]

- a centralized controller means the whole system is dependent on a single bottleneck
- alternative, a distributed system which has 2 layers:
	- coarse-grained global layer
		- operates at larger time scales (10s of seconds to minutes)
		- global view of client quality measurements
		- builds a data-driven prediction model of video quality
	- fine-grained per-client decision layer
		- operates at the millisecond timescale
		- makes actual decisions upon a client request
		- based on the latest (but possible stale) pre-computed global model, and latest per-client state
- system is dependent on a database of subnet-cluster pairs
- Some clients will be routed to sub-optimal clusters in the event that the system has no data on certain subnet-cluster pairs

![[Pasted image 20231121115411.png]]

### Server Selection in Detail
- once a cluster has been selected, the client will then need to be given a server within the cluster
- simplest strategy is to assign servers randomly
	- workloads between servers may be heterogeneous
	- servers may have heterogeneous hardware
- load-balancers could route client requests to the least loaded servers
	- still not optimal
	- CDNs distribute content for a variety of content providers
	- same cluster could be serving both video and web content
	- could also be serving the same type of content for a variety of content providers
	- not all servers have all the content at the same time, due to disk space limitations
	- proactively fetching all the content to the servers is not feasible

![[Pasted image 20231121115949.png]]

- data is lazily fetched to CDN edge servers from an origin
- when a client makes a request for content
	- (refer to the previous section for cluster selection)
	- the client's request is routed to a server within the cluster
	- the server requests the content from an origin server
	- once the content has been fetched, it is served to the client
		- Note: It's possible for the server to stream the data to the client at the same time that it stores the content to its content cache
	- the server can then cache the content for future requests
- If we use random or simple LB server selection method, it's likely that the selected server does not have the content in its local cache
	- This results in the same content existing on multiple servers within a single cluster
	- This results in higher delays across all requests and less cache efficiency across the cluster
- Another solution, map requests to servers based on "what exists in the cache"
	- requests for the same piece of content should go to the same server
	- based on content-based hashing
	- hash the ID/URL of the content, distribute content requests to servers based on those ID hashes
		- similar to key-value systems discussed in the AISA notes
		- [[M11B21 - Key-Value Systems]]
		- [[M03B06 - P2P Overlay Networks]]
- Cluster environments are actually pretty chaotic
	- machine restarts
	- machine failures / crashes
	- load changes
	- server maintenance actions
- When servers go down and come back online, the hash table needs to be recomputed
	- recompute the hash function for all objects (thorough, expensive)
	- only move objects that were assigned to servers that are no longer online (complicated)

#### Consistent Hashing
- put server hashes and content hashes in the same ID space
- organize the ID space as a circle (wrap around IDs when you get to the end of the number line)
- requests for content ID x goes to the server that's located next on the numberline from x
- If a server goes down, the requests for that server's content instead go to the next server in the circle. No other content needs to be moved.
- This is the famous "Chord" algorithm but used entirely within the context of a datacenter.

![[Pasted image 20231121144409.png]]

![[Pasted image 20231121144450.png]]

- [[Chord - A Scalable Peer-to-peer Lookup Protocol for Internet Applications.pdf]]
- [[M03B05 - P2P Computing]]
- [[M03B06 - P2P Overlay Networks]]

#### IP Anycast
- The main goal of IP anycast is to route a client to the "closest" server, as determined by BGP (Border Gateway Protocol), a routing protocol used for inter-AS routing
- Achieved by assigning the same IP address to multiple servers belonging to different clusters
- each of these servers will use the standard BGP to advertise this IP address
- multiple BGP routes for the same IP address corresponding to different cluster locations will propagate in the public Internet
- when a BGP router receives multiple route advertisements for this IP address, it would treat them as multiple paths to the same locations
- in reality these routes correspond to different physical locations
- this strategy can enable CDNs to deliver content using the "closest" server to a client
- Breakdowns
	- The fewest number of hops doesn't always equate to the best network performance
- Not commonly used by CDNs because it's not a comprehensive solution. It does work though.
- It's used by DNS servers. For example, `8.8.8.8` and `8.8.4.4` are anycast IPs used buy Google's Public DNS service.

#### HTTP Redirection
- the protocol works at the HTTP-layer in the network stack
- when a client sends a GET request to a server, it can redirect the client to another server, by sending an HTTP response with a code 3xx and the name of the new server
- this instructs the client to fetch the content from the other server
- this incurs at least one additional HTTP request
- this can be useful for load balancing
	- especially useful in cases where the cost of a 2nd HTTP redirect response and a 2nd HTTP request is negligible in comparison to the cost of the real response (ex. streaming a film)
	- an overwhelmed server can redirect some percentage of incoming requests to use another server
	- does not require a central coordinator, except to provide servers some mechanism for discovering other servers that are capable of handling redirected requests
	- YouTube allegedly does this sometimes

### Network Protocols Used for Cluster/Server Selection

#### Domain Name Service (DNS)
- DNS translates hostnames into IP addresses
- Application-layer protocol
- distributed and hierarchical database of hostnames and IP addresses
- General flow
	- The user's host runs a DNS client
	- A web client extracts the hostname from requests and passes it to client side of the DNS application.  
	- The DNS Client sends a query containing the hostname of DNS
	- The DNS Client eventually receives a reply which included IP address for the hostname
	- the web client can initiate a connection to the IP address that the domain points to
- Other DNS notes
	- canonical host names can be aliases for more complicated host names
	- hosts can have multiple names
	- a name can point to many different IPs, which can be used for load distribution. The DNS will just use a different IP address each time
- Hierarchy
	- we don't have centralized DNS servers because that would result in the internet having a single point of failure

![[Pasted image 20231121145441.png]]

- when a client requests the IP address for a specific domain
	- the client will contact a root server
	- the root server will return the IP of a top level domain server
	- the client will contact the top level domain server
	- the top level domain server will refer the client to an authoritative server
	- the client will make a query to the authoritative server
	- the authoritative server will return the IP address for the desired hostname
- Root DNS Servers
	- there are 13 root DNS servers
	- network of replicated services mostly located in North America
	- total number of server instances was more than 900 in 2019
- Top level domain (TLD) servers
	- responsible for the top level domains
	- TLDs are the "dot something" part of a domain name
- Authoritative servers
	- managed by individual organizations
- Local DNS (LDNS) servers
	- Not strictly part of the DNS model, but are very common in practice
	- ISPs maintains LDNS servers
	- act as a proxy cache for DNS requests
	- they probably store information about what sites are being accessed, which can be sold to advertisers
- recursive vs iterative queries
	- Iterative queries are when the client has to initiate multiple requests to get an IP for a given hostname
	- Recursive queries are when a DNS server brokers the request on behalf of the client
	- The global DNS system uses a combination of approaches
- caching
	- in both iterative and recursive queries, after a server receives the DNS reply of mapping from any host to IP address,  it stores this information in the Cache memory before sending it to the client.
	- DNS records have a TTL which tells DNS servers how long they can cache the information

![[Pasted image 20231121150054.png]]

![[Pasted image 20231121150103.png]]

#### DNS Record Types
- DNS servers store mappings between hostnames and IP addresses as resource records (RRs)
- Resource records and contained inside DNS reply messages
- A DNS RR has 4 fields
	- name
	- value
	- type
	- Time to live (TTL), in terms of seconds, how long the record can be cached
- Most common 4 RR types
	- `TYPE=A`
		- name is a domain name
		- value is an IP address
	- `TYPE=NS`
		- name is the domain name
		- value is the appropriate authoritative DNS server that can obtain IP addresses for hosts in that domain
		- example: `(abc.com, dns.abc.com, NS)`
	- `TYPE=CNAME`
		- name is a hostname alias
		- value is the canonical name
		- example: `(abc.com, relay1.us-east-1.abc.com, CNAME)`
	- `TYPE=MX`
		- the name is the alias hostname of a mail server
		- the value is the canonical name of the email server
		- example: `(abc.com, mail.dnsserver.abc.com, MX)`
- message format
	- ID field
	- flags
	- information about the DNS request
		- hostname
		- type of query (A, MX, etc)
	- answer
		- RRs
	- authority
		- RRs for more authoritative servers
	- additional helpful info at the discretion of the entities running the DNS server
		- For example, if the original query was for an MX record, then the answer section will contain the resource record for the canonical hostname of the mail server, and the additional section will contain the IP address for the canonical hostname.

![[Pasted image 20231121151108.png]]