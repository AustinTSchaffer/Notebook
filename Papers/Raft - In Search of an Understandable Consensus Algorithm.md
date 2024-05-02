---
tags:
---
# Raft - In Search of an Understandable Consensus Algorithm

- Was originally developed as a learning tool
- Spiritual successor to Paxos
	- "Too many pages for any man to understand"
- Almost all design choices were made in service of making the algorithm more understandable. For example, in cases decisions were arbitrary, the algorithm used RNG
- Entire system is designed around a "log", representing the state that the cluster is attempting to maintain consensus over.

## Key Concepts
- State
	- persistent state on all nodes
		- current leader term
		- voting results
		- the log
	- volatile state
		- the index of the highest log entry known to be committed
		- index of the highest log entry applies to the state machine
	- volatile state on leaders
		- array of indexes, one per node, which keeps track of the index of the next log entry to send to each server.
		- an array of indexes, one per server, indicating the index of the highest log entry known to be replicated on each server.
- Appending entries to the log
- voting for a new leader
	- followers
	- candidates
	- leader
- election
	- if a node has not heard a heartbeat from the leader in some number of milliseconds (randomly initialized to between ~300ms and ~1s) then the node will begin a new election, voting for itself.
	- each node will receive/respond to votes by indicating the candidate it voted for. Each node simply votes for the candidate whose ballot it received first, for a given term.
	- only one leader can be elected

![[Pasted image 20240501220735.png]]

I have not read into how Raft keeps the log in sync yet.

## Conclusion
- Algorithm correctness is a worthy goal
- Algorithm understandability is also a worthy goal.
- Ideals only matter if it's possible to implement them.
- 