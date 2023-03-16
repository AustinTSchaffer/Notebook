---
tags: OMSCS, AISA
---
# M10B20 - Server Virtualization Technology

![[Pasted image 20230315194029.png]]

Hadoop Strengths
- batch processing by maximizing parallelism

Hadoop Weakness
- inefficient for jobs that require multiple MapReduce rounds
- Interactive computation (ML models)

![[Pasted image 20230315194636.png]]

![[Pasted image 20230315194650.png]]

![[Pasted image 20230315194700.png]]

## Apache Spark
Extends the mapReduce model to better support 2 common classes of analytics apps
- Interactive algorithms (many in ML)
- Interactive data mining tools (R, excel, Python)
- Core ideas: Spark makes working sets a first-class concept to efficiently support the applications that repeatedly reuse a working set of data

- Hadoop uses the disk for data sharing
- Spark uses memory for data sharing

![[Pasted image 20230315194927.png]]

## About Spark
- Started at UC Berkeley in 2009
- Fast and general-purpose cluster computing system
- 10x (on disk) - 100x (in-memory) faster than Hadoop
- Most popular for running _Iterative ML Algorithms_
- Provides high-level APIs
	- Java
	- Scala
	- Python
- Integration with Hadoop and its ecosystem and can read existing data
- RDD-powered in-memory computing architecture

## Memory-Centric Design

Executors
- each executor must configure its resources (CPU/Memory) at compile time, and no adaption during runtime
- no memory over-commitment is supported
- Multi-threaded JVM

RDD (Resilient Distributed Dataset)
- aims to support memory usage outside JVM queue, on disk, in remote node

![[Pasted image 20230315195544.png]]

## Spark Runtime + Programming

![[Pasted image 20230315195650.png]]

![[Pasted image 20230315195713.png]]

![[Pasted image 20230315195726.png]]

![[Pasted image 20230315195743.png]]

## Regression Modelling
Goal: find best line separating 2 sets of points

![[Pasted image 20230315195924.png]]

- start with random initial line
- compute distance of each point to line
- use distances/directions to inform next line

![[Pasted image 20230315200026.png]]

![[Pasted image 20230315200058.png]]

![[Pasted image 20230315200146.png]]

![[Pasted image 20230315200502.png]]

## Cloud Computing Characteristics
- Rapid elasticity
- On-demand self-service
- Location-independent resource pooling
- Ubiquitous network access
- Measured services (serverless)
	- pay for what you use

![[Pasted image 20230315201053.png]]

## Virtual Servers

Three dominant virtual server deployment platforms
- Virtual Machines (VMs)
	- VMware
	- KVM
	- Xen
- Containers
	- Docker
- Java Virtual Machines (JVMs)
	- Spark Executors
	- Hadoop MapReduce

All require static memory allocation
- allocate memory prior to runtime
- applications at runtime are constrained to the allocated memory resource

Server Virtualization Technology
- Container
- VM

![[Pasted image 20230315201337.png]]

![[Pasted image 20230315201345.png]]

![[Pasted image 20230315201358.png]]

![[Pasted image 20230315201436.png]]

![[Pasted image 20230315201524.png]]

![[Pasted image 20230315201536.png]]

![[Pasted image 20230315201622.png]]

![[Pasted image 20230315201634.png]]

![[Pasted image 20230315201650.png]]

## Multi-Tier Cloud Service

![[Pasted image 20230315201811.png]]

![[Pasted image 20230315201922.png]]

![[Pasted image 20230315201937.png]]

![[Pasted image 20230315201955.png]]

![[Pasted image 20230315202050.png]]

![[Pasted image 20230315202108.png]]

![[Pasted image 20230315202530.png]]

![[Pasted image 20230315202811.png]]

![[Pasted image 20230315203046.png]]

![[Pasted image 20230315203718.png]]

![[Pasted image 20230315203733.png]]

![[Pasted image 20230315203742.png]]
