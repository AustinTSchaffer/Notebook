---
tags:
  - SRE
---
# Chapter 02 - The Production Environment at Google, from the Viewpoint of an SRE

## Hardware
- Google Datacenters have largely homogenous hardware
- At Google
	- A "machine" is a deployment platform, either a VM or baremetal
	- A "server" is a piece of software that implements a service
	- Machines can run any server, so Google doesn't dedicate specific machines to specific server programs
	- There's no specific machine that runs the mail server, for example
	- Resource allocation is handled by Google's cluster operating system named "Borg"

### Google's Datacenter Topology
- datacenter campus
- datacenters
- clusters
- rows
- racks
- machines

![[Pasted image 20240603153308.png]]

### Networking
- Google employs a virtual switch with 10s of thousands of ports
- Google uses hundreds of Google-built switches in a Clos network fabric: https://ieeexplore.ieee.org/document/6770468
- Google's Clos network fabric is named Jupiter: https://research.google/pubs/jupiter-rising-a-decade-of-clos-topologies-and-centralized-control-in-googles-datacenter-network/
- Jupiter supports 1.3 Pbps bisection bandwidth among servers
- Datacenters are connected to each other with a globe-spanning backbone network named B4: https://dl.acm.org/doi/10.1145/2486001.2486019
- B4 is a software-defined networking architecture that uses OpenFlow
	- [[Lesson 07 - Software Defined Networking (SDN) Part 1]]
	- [[Lesson 08 - Software Defined Networking (SDN) Part 2]]

## System Software that "Organizes" the Hardware
- hardware failures are one notable problem that Google manages with software
- hardware failures occur quite frequently given the number of components
- Google abstracts away the hardware so that users and developers don't have to worry about hardware failures

## Managing Machines
- Borg is a distributed cluster operating system: https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/
- Borg is similar to Apache Mesos
- Kubernetes is descendent from Borg

![[Pasted image 20240603154114.png]]

- Borg runs jobs
	- daemon services
	- tasks
- Jobs can have replicas
- Borg uses a DNS service for service name to IP resolution, and calls it BNS. BNS names have hierarchical structure `/bns/<cluster>/<user>/<job>/<task>`
- Borg allocates resources to jobs (CPU/RAM config/limits)
- Borg won't run all of a job's tasks on the same rack, as that introduces a single point of failure (in this case, a single network switch)
- If a task uses more than its allowed resources, Borg will kill it and restart it somewhere else. Crashlooping is a common pattern in container-land.

## Storage
- Google datacenters have a clustered storage model similar to Lustre and HDFS
- Layers
	- D for disk (both disks and SSDs). File server running on almost all machines in the cluster.
	- Colossus is a layer on top of D, implementing a cluster-wide filesystem
		- successor to Google File System (GFS)
		- has standard file system semantics
		- supports replication and encryption
	- Sever database-like services are built on top of Colossus
		- BigTable - [[Week 11 - Bigtable - A Distributed Storage System for Structured Data.pdf]]
		- Spanner - Offers a SQL-like interface for users that require real consistency
		- Blobstore

![[Pasted image 20240603155210.png]]


## Networking
- Google uses dumb switches
- Google computes efficient paths through the datacenter then propagates that info to the switches
- Google implements a bandwidth enforcer (BwE), which manages the available bandwidth to maximize the cluster's average available bandwidth
- centralized traffic engineering has been shown to solve a number of problems that are traditionally extremely difficult to solve through a combination of distributed routing and traffic engineering
- Some services have jobs running in multiple clusters, distributed across the world.
- To minimize the latency for globally distributed services, Google directs users to the closest datacenter with available capacity.
- Global Software Load Balancer (GSLB)
	- Geographic load balancing for DNS requests
	- Load balancing at a user service level
	- Load balancing at the RPC level
- Service owners specify a symbolic name for a service, a list of BNS addresses of servers, and the capacity available at each of the locations (measured in queries per second)
- GSLB directs traffic to the BNS addresses

## Lock Service
- Google uses a service called "Chubby", a lock service for maintaining file locks. https://research.google.com/archive/chubby.html
- It also uses Paxos (those poor bastards)
- Chubby is also used to determine which replica(s) of a service are actually allowed to do work (kind of like leader election but for workers. Worker election?)
- BNS uses Chubby to store mapping between BNS paths and `IP:port` pairs

## Monitoring and Alerting


## Chapter Assessment

### Priming Questions
> What are the challenges and opportunities that Google faces in managing its proprietary datacenters, and how does it address them?

> What are the challenges and opportunities that Google faces in managing its proprietary datacenters, and how does it address them?

> How does Google optimize its network bandwidth allocation and load balancing to ensure efficient and effective service delivery?

### Summary
