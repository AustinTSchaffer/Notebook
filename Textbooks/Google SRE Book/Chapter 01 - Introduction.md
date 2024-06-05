---
tags:
  - SRE
---
# Chapter 01 - Introduction
> Hope is not a strategy.

## The Sysadmin Approach
- involves assembling existing software components and deploying them to work together to produce a service
- tasked with running the service and responding to events and updates as they occur
- the sysadmin team grows to meet the demand required by the volume of issues with the system
- often not part of the dev team
- advantages
	- relatively easy to implement - hire someone with experience
	- many examples to learn from and emulate
	- large talent pool
	- array of exiting tools / software
- disadvantages
	- direct cost
		- sysadmin team sizes grow as the system grows in scale/complexity (linear relationship)
		- manual intervention is time consuming
	- indirect cost
		- having a separate ops team means you have a different set of skills required to maintain systems built by developers
		- different vocabularies
		- different sets of assumptions
		- conflicts of interests between dev/ops
			- dev teams want to launch features as fast as possible
			- ops teams want to make sure that the system doesn't break while they're holding the pager (which is always)
		- this conflict leads to developers crafting processes designed to hinder the ops team from hindering the dev team, often making the system harder to understand and maintain

## Site Reliability Engineering Approach
- hires software engineers to run the products
- create systems to accomplish the work that would otherwise be performed manually by sysadmins
- SRE is what happens when you ask a software engineer to design an ops team
- Google SRE resources can be broken into 2 main categories
	- software engineering
	- UNIX system internals and networking
- Best quality for an SRE: Someone who will get bored of doing a task manually and who will instead write some software to automate it.
- There needs to be an upper bound on the percentage of time that an SRE engineer spends manually dealing with issues (traditional "ops" work). They must have time in their schedule for actually automating solutions to problems. Solutions must be automated AND automatic.
- benefits
	- team size scales sublinearly with system size/complexity
	- rapid innovation and acceptance of change
	- circumvents the disfunctionality of the dev/ops split
	- improves product dev teams by enabling cross-team training/collaboration
- challenges
	- SDE teams and SRE teams have to compete for candidates from the same talent pool
	- talent pool is smaller for SREs because of the unique balance of skills/aptitude/desire/etc
	- management needs to enforce the relationships between SDE teams and SRE teams

## DevOps vs SRE
This book makes the claim that DevOps is a superset containing SRE, and that SRE is a specific implementation of DevOps. It makes this claim by saying that the meaning of the term "DevOps" is still in a state of flux.

## Tenents of SRE
- availability
- latency
- performance
- efficiency
- change management
- monitoring
- emergency response
- capacity planning

## Ensuring a durable focus on engineering
- if the SRE team breaches their cap on "ops" work, the developers start getting the pager as well.
- target volume gives on-call engineers enough time to
	- handle the event accurately and quickly
	- clean up and restore normal service
	- conduct a postmortem
- postmortems should be written for all significant incidents, regardless of whether or not they paged
- postmortems that did not trigger a page likely point to monitoring gaps
- investigations should
	- establish what happened in detail
	- find root causes of the event
	- assign actions to correct the problem or improve how it is addressed next time
- "blame-free postmortem culture"
	- expose faults
	- apply engineering to fix the faults
	- don't avoid/minimize them

## Error Budgets - pursuing maximum change velocity without violating a service's SLO
- no service can truly achieve 100% uptime
- users can't really tell the difference between 100% uptime and 99.999% uptime. Typically the infrastructure between the "site" and the "user" are less reliable than 99.999%
- the higher the uptime, the higher the system cost
- How to pick a reliability target?
	- What level of availability will the users be happy with, given how they use the product?
	- What alternatives are available to users who are dissatisfied with the product's availabillity?
	- What happens to users' usage of the product at different availability levels?
- The error budget is the availability target minus one.
- The error budget is spent when launching features
- Error budget can be hacked with phased rollouts and "1% experiments"
- Resolves the structural conflict of incentives between SDE and SRE. The goal isn't "0 outages" anymore.

## Monitoring
> Monitoring should never require a human to interpret any part of the alerting domain. Instead, software should do the interpreting, and humans should be notified only when they need to take action.

Three kinds of valid monitoring output
- alerts
	- signify that a human needs to take action immediately in response to something happening
- tickets
	- signify that a human needs to take action, but not immediately
	- the system cannot automatically handle the situation, but no damage will result from letting it fester
- logging
	- recorded for diagnostic / forensic purposes
	- no one reads the logs unless an alert/ticket leads an engineer to the logs

## Emergency response
- reliability is a function of mean time to failure (MTTF) and mean time to repair (MTTR)
- most relevant metric in evaluating the effectiveness of emergency response is how quickly the response team can bring the system back to health
- avoiding emergencies that require human intervention avoids the incredibly slow latency added when a human is in the loop
- "playbooks", documentation that records best practices ahead of time, produce a roughly 3x improvement in MTTR compared to "winging it"
- SRE relies on "on-call" playbooks and exercises such as the "Wheel of Misfortune"

## Change Management
- roughly 70% of outages are due to changes in a live system
- best practices in this domain use automation
	- implementing progressive rollouts
	- quickly and accurately detecting problems
	- rolling back changes when problems arise

## Demand Forecasting and Capacity Planning
- ensuring that there is sufficient capacity and redundancy to serve projected future demand with the required availability
- mandatory stems
	- accurate organic forecast demand, extended beyond the lead time required to acquire capacity
	- accurate incorporation of inorganic demand sources into the demand forecast
	- regular load testing
- SRE must be in charge of capacity planning and provisioning

## Provisioning
- combines change management and capacity planning
- provisioning must be conducted quickly and only when necessary, since capacity is expensive
- adding new capacity often involves
	- spinning up a new instance or location
	- making modifications to existing systems (config changes mostly)
	- validating the new capacity
- Can be riskier than load-shifting

## Efficiency and Performance
- SRE controls provisioning, and must also be involved in any work on utilization
- utilization is a function of how a given service works and how it is provisioned
- resource use is a function of demand/load, capacity, and efficiency
- services slowdown as they process more load and eventually stop responding entirely
- SREs provision to meet a capacity target at a specific response speed

## Chapter Assessment

### Priming Questions
> How does google measure the time spent by SREs on dev vs ops work?

The chapter doesn't really get into that. That seems like management overhead. I'm not sure how Google tracks work completed, i.e. I doubt they use Jira, but they probably use some other kind of agile-adjacent work tracking software. That system would likely be able to estimate the amount of time spent on development tasks vs operational tasks. That, and regular standups, would likely give you an idea of how much of the workweek is being consumed by incident response.

> What is the rationale behind the 50% cap on ops work?

The 50% cap on ops work gives the SRE team breathing room, giving them time to build software systems designed to automate incident response and build systems that make the whole platform more reliable.

> What are the key principles and responsibilities of an SRE team according to this document, and how do they differ from traditional operations teams?

Traditional ops teams do not devote any time to automating solutions to problems, and instead focus on manual intervention. SRE teams are software engineers at their core. The key principles are primarily organized around reliability/uptime.

> What are the key principles and responsibilities of an SRE team according to this document, and how do they differ from traditional operations teams?

See the above section.

### Summary
Traditional sysadmin is a model that is easy to implement and works fine for smaller systems, but becomes incredibly expensive as the system grows in scale and complexity. Traditional sysadmin is also somewhat at odds with software engineering, which can slow down the software development lifecycle, reducing an organization's ability to innovate and ship features. SRE puts software engineers in that role and gives them time and space to automate everything which can be automated.

