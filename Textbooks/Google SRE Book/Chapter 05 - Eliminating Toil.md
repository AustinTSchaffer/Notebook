---
tags:
  - SRE
---
# Chapter 05 - Eliminating Toil
> If a human operator needs to touch your system during normal operations, you have a bug. The definition of normal changes as your system grows.
> \- Carla Geisser, Google SRE

SRE's role is to spend time on long-term engineering projects instead of operational work. We define this class of operational work as "toil"

## Toil Defined
- overhead is often work not directly tied to running a production service and includes tasks like team meetings, setting and grading goals, snippets, and HR paperwork.
- overhead is not toil
- toil is the kind of work tied to running a production service that tends to be **manual, repetitive, automatable, tactical, devoid of enduring value, and scales linearly with system size/complexity.**
- manual
	- running scripts that automate some task
- repetitive
	- running something for the first or second time? not toil
- automatable
	- if human judgement is essential for the task, it's likely not toil
- tactical
	- toil is interrupt-driven and reactive, rather than strategy-driven and proactive.
	- Pager alerts result in toil.
	- must continually work to minimize that work toward elimination, though elimination may never be achieved
- no enduring value
	- if the service remains in the same state after you finished a task, the task was likely toil
- $O(n)$ with service growth
	- An ideally managed and designed service should be able to grow by an order of magnitude without forcing any employee to do additional work (apart from one-time efforts to add resources)

## Less Toil is Better
- toil should be below 50% of an SRE's time
- an SRE's remaining time should be spent on long-term engineering projects
	- reducing future toil
	- adding service features
		- improve reliability
		- improve performance
		- improve utilization
	- toil reduction is often a second-order effect of adding service features
- SRE is not a typical ops org

## Calculating Toil
- there's a floor on the amount of toil any SRE has to handle if they are on-call
- Biggest source of toil is interrupts
- toil is often a self-reported metric

## What qualifies as engineering?
- novel
- requires human judgement
- permanent improvement
- guided by a strategy
- frequently creative and innovative
- design-driven approach
- the more generalized, the better

Approximate categories of SRE work activities
- software engineering
- systems engineering
- toil
- overhead

## Is toil always bad?
- not always
- becomes toxic in large quantities
	- career stagnation
	- low morale
	- creates confusion
	- slows progress
	- sets a precedent
	- promotes attrition
	- causes breach of faith

## Conclusion
> If we all commit to eliminate a bit of toil each week with some good engineering, we’ll steadily clean up our services, and we can shift our collective efforts to engineering for scale, architecting the next generation of services, and building cross-SRE toolchains. Let’s invent more, and toil less.

