---
tags: OMSCS, GIOS, Datacenters
---
# P4L4: Datacenter Technologies

## Overview
- Brief and high-level overview of challenges and technologies facing data centers
- The space of DC tech is too vast to cover in 24 short videos
- This is mostly a primer
- The goal is to provide context for mechanisms from the previous lessons in this course
- multi-tier architecture for internet services
- cloud computing
- cloud and "big data" technologies

## Stats
In 2011, there were 510,000 data centers world-wide, covering 285 million square feet.

## Internet Services
- an internet service is any type of service provided via a web interface
- common pattern
	- send request
	- see response
- presentation component: static content
- business logic: dynamic content
- database tier: data store
- these are not necessarily separate processes running on separate machines
- many available open source and proprietary technologies fill this space
- middleware: supporting, integrative, or value-added software technologies

- in multi-process configurations, some form of IPC used, included RPC/RMI, shared memory, ...

## Internet Service Architectures
- For scale: multi-process, multi-node
	- this is called "scale out" architecture
	- run multiple replicas of a single service

Patterns
1. "Boss-Worker": frontend distributes requests to nodes
2. "All Equal": all nodes execute any possible step in request processing, for any request. "Functionally homogeneous"
3. "Specialized Nodes": nodes execute some specific step(s) in request processing, for some request types. "Functionally heterogeneous"

### Homogeneous Architectures
> "All Equal" model of scaling out.

each node can do any processing step
- Request routing can be more simple in this model. It doesn't need to keep state about which backend node does what
- This doesn't mean that each node has all data, just that each node can get to all data.
- Hard to benefit from local caching in this model.

scaling up
- use a load balancer
- add more workers/processes on each node
- add more servers
- add more storage

### Heterogeneous Architectures
> "Specialized Nodes" model of scaling out.

Supplemental: [[Lessons from Giant-Scale Services.pdf]]

- different nodes, different tasks/requests
- data doesn't have to be uniformly accessible everywhere
- benefit of locality and caching
- more complex routing mechanisms
- more complex management of the system

Scale up by
- profiling the kinds of requests that are most in demand
- profiling the services that those requests use
- scale up those services
- refactor and split off an overworked service into multiple services
- scale up the ones that are overworked
- scale down the ones that are underworked

## Cloud Computing Poster Child: Animoto

**Amazon**
- provisioned hardware resources for holiday sale season
- resources were idle the rest of the year
- "opened" access to its resources via web-based APIs
- third party workloads on Amazon hardware, for a fee

This was the birth of AWS and Amazon's Elastic Compute Cloud (EC2).

**Animoto**
- rented "compute instances" (VMs) in EC2
- In April 2008, became available to Facebook users
	- Monday: 50 VMs
	- Friday: 3400 VMs
	- 750,000 new users in 3 days
- cannot achieve this with traditional in-house machine deployment and provisioning tools

![[Pasted image 20221205190908.png]]

## Cloud Computing Requirements
### Traditional Approach

![[Pasted image 20221205191247.png]]

- buy and configure resources
- determine capacity based on expected demand (peak)
- when demand exceeds capacity
	- dropped requests
	- lost opportunity

### Ideal Cloud

![[Pasted image 20221205191502.png]]

- capacity scales elastically with demand
- scaling in/out instantaneously, both up and down
- cost is proportional to demand, to revenue opportunity
- all of this should happen automatically, no need for hacking wizardry
- can access anytime, anywhere
- don't own the resources

### Summarized
- On-demand elastic resources and services
- fine grained pricing based on usage (dynamic pricing to follow demand)
- professionally managed/hosted resources
- APIs exposed to allow customers to provision virtual resources (and pay for them)

## Cloud Computing Overview
- shared resources
	- infrastructure and software/services
	- virtual clustering
- APIs for access and configuration
	- web based, libraries, command line, ...
- billing and accounting services
	- many models: spot, reservation, entire marketplace
	- typically discrete quantities: tiny, medium, X-large
- managed by (cloud) provider

## Why Does Cloud Computing Work?
**Law of Large Numbers**
- per customer there is large variation in resource needs
- average across many customers is roughly constant

**Economies of Scale**
- unit cost of providing resources or service drops when it's purchased/managed "in bulk"

## Cloud Computing Vision
> If computers of the kind I have advocated become the computers of the future, then computing may some day be organized as a public utility, just as the telephone system is a public utility \[...\] The computer utility could become the basis of a new and important industry.
>
> John McCarthy, MIT Centennial, 1961

- Computing as a fungible utility
- limitations exist
	- API lock-in
	- hardware dependency
	- latency
	- privacy/security

> Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g. network, servers, ...) that can be rapidly provisioned and released with minimal management effort or service provider interactions.
>
> National Institute of Standards and Technology (NIST), Oct 25, 2011

## Cloud Deployment Models
**public**
- third-party customers/tenants

**private**
- leverage technology internally

**hybrid (public + private)**
- failover, dealing with spikes, testing

**community**
- used by certain type of users, common mission, common locality

## Cloud Service Models
**On-Premises (On Prem)**
- you manage everything
- ex: a RaspberryPi in a closet

**Infrastructure as a Service (IaaS)**
- you manage apps, data, runtime, middleware, OS
- ex: AWS EC2

**Platform as a Service (PaaS)**
- you manage applications, data
- ex: Google App Engine

**Software as a Service (SaaS)**
- you don't manage anything except your own data
- ex: Gmail

![[Pasted image 20221205193436.png]]

## Cloud Requirements
1. "fungible" resources
	- All provisioned resources of the same type are the exact same
	- Ephemeral resources
2. elastic, dynamic resource allocation methods
3. scale: management at scale, scalable resource allocations
4. dealing with failures
5. multi-tenancy: performance and isolation
6. security
	- guarantee privacy
	- protect customer from provider
	- protect provider from customer

## Cloud Failure Probabilities

- Probability of a single component NOT failing: $(1-p)$
- Probability of none of the $n$ components failing: $(1-p)^n$
- Probability of a failure anywhere in the system: $1 - (1-p)^n$

Hypothetical cloud:
- failure probability of $p=0.03$
- 10 components
	- probability that there will be a failure SOMEWHERE in the system
	- 26%
- 100 components
	- " " " " " " " "
	- 95%

## Cloud-Enabling Technologies
- Virtualization
- Resource provisioning (scheduling)
	- mesos
	- yarn
- BigData™
	- processing
		- Hadoop
		- MapReduce
		- Spark
	- storage
		- Distributed FS ("append only")
		- NoSQL, distributed in-memory caches
- Software-defined X
	- s-d networking
	- s-d storage
	- s-d datacenters
- monitoring
	- real-time log processing
		- Flume
		- CloudWatch
		- DataDog
		- Log Insight
	- Metrics
		- Prometheus
		- DataDog again

## The Cloud as a Big Data Engine
> TCaaBDE? No?
> 
> As long as you can pay, you have effectively infinite resources.

In 2011, 1.8 zettabytes were created and replicated on the internet.

The cloud is a...
- data storage layer
- data processing layer
- caching layer
- language front-end (e.g. querying engine)
- analytics engine (e.g. ML)
- continuous data streaming service

## Example: Big Data Stacks
- Hadoop
- Berkeley Data Analytics Stack (BDAS)

![[Pasted image 20221205195410.png]]

![[Pasted image 20221205195500.png]]

