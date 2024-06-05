---
tags:
  - SRE
---
# Chapter 03 - Embracing Risk
- past a certain point, increasing reliability is worse for a service
	- maximizing stability limits how fast new features can be developed
	- limits how quickly products can be products can be delivered to users
	- dramatically increases cost
	- reduces the number of features a team can afford to offer
- users typically don't notice the difference between high reliability and extreme reliability
- SRE balances the risk of unavailability with the goals of rapid innovation and efficient service operations
- optimizing for user satisfaction

## Managing Risk
- cost does not increase linearly with reliability increments
- there are diminishing returns on spend vs reliability
- cost associated with redundant equipment allows SRE teams to take systems offline for routine/unforeseen maintenance
- provides space to store parity code blocks that provide a minimum data durability guarantee
- opportunity cost - the cost borne by an org when it allocates funds to increasing reliability vs added new user-facing features
- SRE teams manage risk as a continuum
	- equal importance to reliability and risk tolerance
	- cost/benefit analysis
	- where on the non-linear risk continuum should we place each application or service?
- align the risk taken by a given service with the risk the business is willing to bear
- services should be reliable, but not MORE reliable than it needs to be
	- make a service more reliable that it's availability target, but not TOO much more reliable
	- going too far past a service's availability target would be a waste of resources/opportunities
		- new features
		- technical debt
		- reducing operational cost
	- availability targets should be a minimum with an implicit maximum

## Measuring Service Risk
- setting targets means you can assess the current performance and track improvements/degradations
- service failures come in many different metrics
- focus on **unplanned downtime**
- **service availability** is the main metric, but there are multiple ways to calculate that
- **service availability** is often expressed as a percentage, with "number of nines" being a common way to specify it.

### Time-based availabillity
$$
availability = \frac{uptime}{uptime+downtime}
$$
- Can be used to calculate the acceptable amount of downtime that a service can incur over a period of time.
- Not a super meaningful metric for globally-distributed services.
- Instead, services can also use **request success rate**

![[Pasted image 20240605105420.png]]

### Aggregate Availability
$$
availability=\frac{\text{successful requests}}{\text{total requests}}
$$
- a system that serves 2.5M reqs/day with an availability target of 99.99% can serve 250 errors/day
- not all requests are equal
	- user signup >> polling for new email
- Availability calculated as the request success rate of all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective
- "Most nonserving systems (e.g., batch, pipeline, storage, and transactional systems) have a well-defined notion of successful and unsuccessful units of work"
- This line of thinking doesn't just apply to always-on user-facing applications. Even batch processing ETL pipelines can have availability targets.
- availability targets should be set quarterly and evaluated weekly

## Risk Tolerance of Services
- the risk tolerance of services is typically built directly into the basic product or service definition
- service risk tolerance at Google tends to be less clearly defined
- SREs need to work with product owners to turn business goals into explicit engineering objectives
### Identifying Risk Tolerance of Consumer Services
- consumer-facing services often have an associated product team
- PTs/PMs
	- understand the users/business
	- shape the product for success in the marketplace
	- usually the best resource for discussing the reliability of the service
- without PTs, engineers play this role implicitly
- factors to consider
	- level of availability
	- do different types of failures have different effects on the service
	- does the service cost determine where the service falls on the risk continuum
	- what other service metrics are important
#### Target level of availability
- issues to consider
	- what level of service do the users expect
	- is the service tied directly to revenue
	- is the service paid or free
	- are there competitors in the marketplace
	- what level of service do competitors provide
	- is the service B2B or B2C
- B2B services typically will have strict availability targets (promote stability, business contracts with penalties)
- B2C services (especially freemium services and bleeding-edge services) typically will have lower availability targets (promote innovation)
#### Types of failures
- how resilient is the business to service downtime
- which is worse
	- constant low rate of failures
	- occasional full-site outage
- planning downtime can help alleviate unplanned downtime
#### Cost
- key factor in determining appropriate availability targets
	- if we increase reliability by one more 9, what will the increase in revenue be?
	- what will be the cost of that additional 9?
- this calculation will be more difficult if requests don't equate directly to revenue
- honestly, just push the error rate below the ISP error rate
- ISP typical background error rate: 0.01% to 1%
#### Other Metrics
- service latency

### Risk Tolerance of Infrastructure Services
#### Target level of availability
- infra services need higher reliability than the services that depend on them
- infra services need to support high throughput, low latency, sometimes both
#### Types of failures
- partition the infra and offer it at multiple independent levels of service
	- build out low-latency cluster
	- build out high-throughput cluster
- delivering infra services with clearly delineated levels of service means clients can make risk/cost tradeoffs when building their system

## Motivation for Error Budgets
- How hardened do we make the software to unexpected events?
- How much testing is the right amount?
- How much should we work on reducing the risk associated with push frequency, versus doing other work?
- How big do we make our canary deployments and how long should we wait before propagating a change to the entire deployment?

### Forming error budgets
- product management defines an SLO, which sets an expectation for how much uptime the service should have
- actual uptime is measured by the monitoring system
- the difference between the 2 numbers is the "budget" available for the rest of the quarter
- If the uptime is above the SLO, new releases can be pushed

## Priming Questions
> What is the relationship between risk management and service reliability at Google?

Service reliability is both a minimum AND a maximum, allowing the service to act reliably, while not hindering the development/deployment of new features.

> How does Google define and measure service availability and risk tolerance?

There's a few metrics you can look at, with the most important 2 being uptime and request success rate.

> What factors does Google consider when assessing the risk tolerance of its services, and how does cost figure into the decision-making process?