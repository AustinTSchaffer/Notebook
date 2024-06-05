---
tags:
  - SRE
---
# Chapter 04 - Service Level Objectives (SLOs)
- Service level indicators (SLIs)
	- quantitative measure of some aspect of the level of service
	- request latency (milliseconds)
	- error rate (%errors)
	- system throughput (requests per second)
	- availability (%uptime, minutes down per quarter)
- service level objectives (SLOs)
	- a target value or range of values for a service level measured by an SLI
	- natural structure for SLOs is $SLI \le target$
	- https://research.google/blog/speed-matters/
	- without explicit SLOs, users form beliefs about desired performance which may be unrelated to the beliefs held by the designers/operators of the service.
		- Can lead to an over-reliance on the service.
		- Can lead to an under-reliance on the service.
- service level agreements (SLAs)
	- explicit/implicit contract with users that includes consequences of missing/meeting SLOs
	- consequences can be a financial payout
	- Breach of SLA often results in a lawsuit. Breach of SLO means you might trigger a clause in an SLA. Important difference.
	- SLAs are designed by business/product decisions

## Indicators in Practice
### What do you and your users care about?
- choosing too many SLIs makes it hard to pay attention to the ones that matter
- choosing too few may leave significant behaviors of the system unexamined
- services tend to fall into a few broad categories in terms of which SLIs they find relevant
	- user-facing serving systems
		- availability
		- latency
		- throughput
	- storage systems
		- latency
		- availability
		- durability
	- big data systems
		- throughput
		- end-to-end latency (ingestion to completion)
	- all systems
		- correctness

### Collecting Indicators
- use a monitoring system like prometheus
- some systems should have client-side collection
- measuring server latency is good, measuring JS execution latency is also good

### Aggregation
- most metrics are better thought of as distributions rather than averages
- averages can hide important features of your SLIs
- think of viewing your data with various percentiles
	- Example: 50th, 85th, 95th, 99th
	- high order percentiles (99th, 99.9th) show plausible worst-case values
	- 50th percentile shows the median, i.e. typical response rate
- users tend to prefer slightly slower systems to systems with high latency variability
- If the 99.9th percentile behavior is good, then the typical experience is likely to be good.

![[Pasted image 20240605142645.png]]

- metric distribution will likely be written into the SLOs

## Choosing Targets
- don't pick targets based on current performance
- keep SLOs simple. Complicated SLI aggregations can make it hard to optimize the system
- avoid absolute statements
- reduce the number of SLOs as much as possible
	- if you can't ever win a conversation about priorities by quoting a particular SLO, it's probably not worth having that SLO
	- not all product attributes are amenable to SLOs
	- it's hard to specify "user satisfaction" as an SLO
- perfection can wait
	- start with loose targets
	- refine the targets as the system approaches maturity
- SLOs help define priorities
	- too strict = no innovation
	- too loose = poor quality product

## Control Measures
- SLIs and SLOs are used in control loops to manage systems
	- monitor and measure SLIs
	- compare SLIs to SLOs
	- if action is needed, figure out what needs to happen in order to meet the SLO
	- take action

## SLOs Set Expectations
- published SLOs set expectations on the systems behavior
- users want to know what they can expect from a service to determine if it's appropriate for their use case
- keep a safety margin
	- using a tighter internal SLO (compared to the public SLO for a system/service/app) gives you room to respond to chronic problems before they become visible externally
	- an SLO buffer makes it possible to accommodate reimplementations that trade performance for other attributes. Examples:
		- cost
		- ease of maintenance
- don't overachieve
	- users build on the reality of what you offer, rather than what you say you'll supply
	- if service's actual performance is better than the SLO, people will notice and rely on that actual performance
	- take a service deliberately offline occasionally
	- throttle some requests
	- design the system so that it isn't faster under light loads

## Agreements in Practice
- SLA requires business and legal teams to pick appropriate consequences and penalties for a breah
- SRE should help business/legal understand the likelihood and difficulty of meeting the SLOs contained in the SLA
- Advice on SLO construction is applicable for SLAs
- It's harder to change an existing SLA to make it less strict

