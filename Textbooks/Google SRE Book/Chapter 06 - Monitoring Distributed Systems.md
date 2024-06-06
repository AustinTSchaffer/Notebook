---
tags:
  - SRE
---
# Chapter 06 - Monitoring Distributed Systems

- monitoring
	- collecting
	- processing
	- aggregating
	- displaying
	- real-time
	- quantitative
	- examples
		- query counts
		- error counts
		- response times
		- number of replicas up
- white-box monitoring
	- logs
	- interfaces like the Java VM Profiling Interface
	- HTTP handler statistics
- black-box monitoring
	- is it up?
	- client-side response times
- dashboard
	- summary view of core metrics
	- custom panels for aggregating/displaying monitored metrics
	- graphs, charts, etc
- alert
	- notification intended to be read by a human
	- bug/ticket
	- email alerts
	- pages
- root cause
	- defect in software/human system
	- the original/actual problem
	- not a specific incident caused by the root cause
- node/machine
	- interchangeable term to indicate the application host
	- physical server
	- VM
	- container
	- all 3
- push
	- deploying a new version of a piece of software
	- deploying new configuration to a piece of software

## Why monitor?
- analyze long-term trends
	- DB growth
	- daily active user count
- comparing over time or experiment groups
- alerting
- building dashboards
- conducting ad-hoc retrospective analysis (debugging)
- supply raw input into business analytics and in facilitating analysis of security breaches
- monitoring and alerting
	- shows what's broken
	- shows what's about to break
	- doesn't show things that are "weird" (unless you're a security team)

## Setting reasonable expectations for monitoring
- try to avoid complex hierarchical monitoring. If the DB is slow and the website is slow, alert for both.
- Google has some fancy rules such as "We've redirected traffic away from this datacenter (aka "draining" it), so don't raise alerts about apps in this datacenter."
- Keep noise low and signal high

## Symptoms vs Causes
- "what's broken" is the symptom
- "why" indicates cause

## Black-box vs white-box
- black-box monitoring is symptom-oriented
- black-box monitoring represents active problems, not predicted
- white-box monitoring allows detection of imminent problems
- in a multilayered system, one symptom is another's cause

## Four Golden Signals
- latency
	- important to distinguish between the latency of successful requests and the latency of failed requests
	- important to track error latency (seperately) as opposed to just filtering out errors
- traffic
- errors
	- explicit errors based on response code
		- load balancer can catch/record these
	- implicit errors where the response code is "good" but the content is "bad"
		- E2E tests should be checking for these
	- policy
		- e.g. response times are higher than upper bound threshold
- saturation
	- how "full" is the service
	- usually depends on CPU/network utilization where there's a known upper bound
	- 99th percentile response times can be a good indicator of saturation

## Worrying About Your Tail (or, Instrumentation and Performance)
- it can be tempting to design monitoring systems that take an average of a metric
- CPU utilization can be imbalanced
- Remember that metric distribution is important for SLOs

## Choosing an appropriate resolution for measurements
- observing CPU load averaged by the minute won't reveal spikes that drive up high tail latencies
- for a webservice targeting 99.9% annual uptime, the amount of downtime allowed per year is 9 hours. Probing more than once per minute is probably unnecessarily frequent.
- checking hard-drive fullness for a service targeting 99.9% availability more than once a minute is probably unnecessarily frequent
- increasing granularity of metric collection increases cost (storage, retrieval, processing)
- CPU utilization case study
	- record the current CPU utilization every second
	- using buckets of 5% granularity, increment the appropriate CPU utilization bucket every second
	- Aggregate those values every minute
	- Allows you to get an estimate of the CPU utilization distribution without storing per-second data

## As simple as possible, no simpler
- these requirements are complex when taken in aggregate. Perfectly configured monitoring therefore becomes a complex task
	- alerts on different latency thresholds, at different percentiles, on all kinds of metrics
	- extra code to detect and expose possible causes
	- associated dashboards for each of these possible causes
- design monitoring systems with care taken to improve simplicity
	- the rules that catch real incidents should be simple, predictable, and reliable
	- data collection/aggregation/alerting that is rarely exercised should be removed
	- signals that are collected but not exposed in any dashboards should be removed. If they're important signals, make a dashboard.

## Tying these principles together
- this philosophy is aspirational, but so is all engineering
- good starting point for writing/reviewing a new alert

> Does this rule detect an otherwise undetected condition that is urgent, actionable, and actively or imminently user-visible?
> 
> Will I ever be able to ignore this alert, knowing it’s benign? When and why will I be able to ignore this alert, and how can I avoid this scenario?
> 
> Does this alert definitely indicate that users are being negatively affected? Are there detectable cases in which users aren’t being negatively impacted, such as drained traffic or test deployments, that should be filtered out?
>
> Can I take action in response to this alert? Is that action urgent, or could it wait until morning? Could the action be safely automated? Will that action be a long-term fix, or just a short-term workaround?
> 
> Are other people getting paged for this issue, therefore rendering at least one of the pages unnecessary?

There's also a fundamental philosophy on pages and pagers

> Every time the pager goes off, I should be able to react with a sense of urgency. I can only react with a sense of urgency a few times a day before I become fatigued.
> 
> Every page should be actionable.
> 
> Every page response should require intelligence. If a page merely merits a robotic response, it shouldn’t be a page.
> 
> Pages should be about a novel problem or an event that hasn’t been seen before.

## Monitoring for the Long Term
> Monitoring systems track an ever-evolving system with changing software architecture, load characteristics, and performance targets.

- rare alerts whose fixes are hard to automate might become more frequent in the future
- Deciding whether to engineer automated solutions to root causes follows a cost/benefit analysis
- Monitoring decisions should be thought of having long-term consequences

> Every page that happens today distracts a human from improving the system for tomorrow, so there is often a case for taking a short-term hit to availability or performance in order to improve the long-term outlook for the system.

## Conclusion
- features of healthy monitoring/alerting pipelines
	- focus primarily on symptoms for paging
	- reserves cause-oriented heuristics to serve as aids for debugging
- monitoring symptoms is easier the further up the stack you monitor
- monitoring saturation and performance of subsystems (ex: databases) usually is performed on the subsystem itself
- email alerts are of limited value and tend to be ignored
- dashboards are critical
- logging is critical for debugging/investigations
- all pages should be actionable. SREs can't become jaded of pages.

## Priming Questions
> What are the benefits and uses of monitoring in distributed systems?

If you don't have any monitoring, you don't know when there's problems. Doesn't matter if the system is distributed or not.

> How can a monitoring system be designed to be both effective and simple?

- Focus on the SLOs
- Don't get too creative with it.
- Remember that each metric has some kind of distribution. Make the monitoring, visualization, and alerting pay attention to the distribution.
- Measurement granularity should be in some way based on the SLOs. Too granular, you're just burning money. Too coarse, you'll miss important features.
- Be kind to the people who have the pager.

 > What are some key principles of Google's monitoring and alerting philosophy for their SRE teams?
 
 See the section above with all of the quoted text.