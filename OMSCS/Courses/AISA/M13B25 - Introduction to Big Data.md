---
tags: OMSCS, AISA
---
# M13B25 - Introduction to Big Data

Characteristics "the 3 V's"
- volume  (scale)
- velocity (speed)
- variety (complexity)

Big data refers to data sets...
- that are beyond the ability of legacy approaches to manage at an acceptable level of quality and/or
- that exceed the capacity of conventional systems (hardware and/or software) to process within an acceptable elapsed time

Definition is subjective and evolving
- as technology advances over time, the size of datasets that qualify as big data will also increase
- the definition is varying by sector, depending on
	- what kinds of software tools are commonly available
	- what sizes of datasets are common in a particular industry or science domain

### Data Volume
- 44x increase from 2009-2020, from 0.8 zettabytes to 35 zettabytes (35,000 exabytes, 35,000,000 petabytes)
- data volume is increasing exponentially

Examples of big data
- WWW
	- 8 billion pages indexed
	- Deep web is supposedly 100 times larger
- Credit card transactions
	- 200+ billion transactions in the US alone
	- 150+ terabytes of data transmitted to processing center annually

### Data Velocity
- data are generated fast and need to be processed fast
- online data analytics + real time data analytics
- delayed decisions -> missed opportunities

Examples
- E-Promotions
	- based on current location / purchase history / preferences / recorded ratings
	- send promotions right now for store next to you
- Healthcare monitoring
	- sensors monitor your activities and body responses
	- any abnormal measurements require immediate action/reaction
- Covid19 vaccine results and side effect monitoring via Crowd Computing
- Video streams are everywhere
	- Every phone, every vehicle, every highway, every building

### Data Variety
input data related complexity
- various formats types and structures
- text, numerical, images, audio, video, sequences, timeseries, social media data, multidimensional arrays
- static data vs streaming data
- A single application may be generating/collecting many types of data
- No unified system of schemas, no clear globally unique keyspaces

Algorithmic related complexity
- different algorithms may derive different insights/outputs from the same collection of datasets
- what analysis does make sense?

Metrics (quality and performance measurement)
- different measures can be used to measure performance, effectiveness, and utility of big data
- What metrics do make sense?

## Why Now?
- Better/faster storage technology
- Larger data sets are more affordable
- Cloud Computing
	- pay as you go
	- elasticity
	- multi-tenancy
	- economics of scale
- Everything is reporting data all the time now. The problem isn't generation and storage, it's processing at scale.

![[Pasted image 20230410164034.png]]

![[Pasted image 20230410164446.png]]

![[Pasted image 20230410164518.png]]

## Big Data Challenge

### In-Memory Computing
![[Pasted image 20230410164801.png]]

![[Pasted image 20230410164851.png]]

![[Pasted image 20230410165045.png]]

![[Pasted image 20230410165103.png]]

![[Pasted image 20230410165135.png]]

Limitations and considerations
- Need tools to allow developers to code explicitly for the GPU
	- There are new APIs that give close control of the device
	- Uses familiar concepts and paradigms for GPU experts
	- Convenience and productivity improvements from language
	- Fundamental building blocks for higher-level algorithms
- Requires the developer to identify suitable GPU workloads
	- Re-code routines to operate on data in parallel
	- Minimize branching flow of control in kernels
- Amortizing overhead of moving work to GPU
	- Time taken to copy data between host and device over PCIe
	- Overhead of switching flow of control from CPU to GPU

### Storage
- Large memory is a growing trend
- Software platforms
	- Spark, Redis, Memcached
- Hardware Platforms
	- AWS, Oracle, Google Cloud Platform (GCP)

![[Pasted image 20230410170049.png]]

![[Pasted image 20230410170125.png]]

![[Pasted image 20230410170346.png]]

![[Pasted image 20230410170409.png]]

![[Pasted image 20230410170454.png]]

![[Pasted image 20230410170514.png]]

![[Pasted image 20230410170541.png]]

![[Pasted image 20230410171201.png]]

## New Challenges
![[Pasted image 20230410171327.png]]

![[Pasted image 20230410171532.png]]

![[Pasted image 20230410171958.png]]

![[Pasted image 20230410172017.png]]

![[Pasted image 20230410172026.png]]

![[Pasted image 20230410172038.png]]

