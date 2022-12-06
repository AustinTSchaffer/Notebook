---
tags: OMSCS, GIOS, 
---
# P4L3: DSM: Concepts and Systems
> [[P4L3 DSM Concepts and Systems.pdf]]

## Pure Hardware Approach to DSM
- TLDR; expensive

## Pure Software Approach to DSM
- TLDR; poor performance

## Hybrid Approach to DSM
- to improve performance, without breaking the bank, think hybrid
- a hybrid approach can be called _cooperative shared memory_
	- programmer-supplied annotations
	- programmers identify data segments that use shared data with corresponding *check-in* (exclusive or shared access) and *check-out* (relinquish) annotations
	- performance primitives do not change program semantics
	- reduce unintended communication caused by thrashing and false sharing
	- cooperative prefetch can hide latency
- software effectively tells the DSM when it does and doesn't need access to a specific set of memory pages. The DSM can then make decisions about when and which pages it needs to move between which nodes.
- address translation and triggering invalidations are tasks that the hardware is better suited for.