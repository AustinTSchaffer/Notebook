---
tags: OMSCS, AISA
---
# Module 8 - Block 16 - P2P Trust and Reputation Management

## Decentralized Overlay Networks
> Trust and Reputation

![[Pasted image 20230304145546.png]]

![[Pasted image 20230304145611.png]]

![[Pasted image 20230304145655.png]]

## Managing Trust
- Security approach
	- Agent identity validation
	- Integrity, non-repudiation, authenticity of messages
- Institutional Approach
	- Agents are deployed over a specific infrastructure called institution, which has power over the agents
	- observe their behavior
	- reward or punish agents
- Social approach
	- each agent observes its neighborhood, evaluates its neighbors by way of a reputation model, and exchange this information with others
	- entities that do not behave well will see/get their reputations decrease and will be progressively excluded from subsequent interaction and then from the society

All three approaches are complementary and cover different aspects of interaction.

The reputation of a peer node (entity, agent) is the opinion of the node by the other peers in the network, an estimation of the consistency of some attributes over time.

Reputation trust is also called social trust.

## Reputation Types
- Primary reputation
	- direct reputation
	- observed reputation
- Secondary reputation
	- collective reputation
	- propagated reputation
	- stereotyped reputation

## Reputation Systems...
- help establish mutual trust/distrust by assigning a reputation to each peer.
- Aggregate, process and disseminate transaction-based feedback
- Reputation is an assumption that past behavior is indicative of future behavior.
- Challenges of a reputation system
	- provide information that allows peers to distinguish between trustworthy and non-trustworthy peers
	- encourage peers to be trustworthy
	- discourage participation from those who are not

## Centralized Trust Management
![[Pasted image 20230304150602.png]]

![[Pasted image 20230304150642.png]]

## Decentralized Trust Management
![[Pasted image 20230304150756.png]]

![](./images/Pasted%20image%2020230304150815.png)

![](./images/Pasted%20image%2020230304150940.png)

![[Pasted image 20230304151214.png]]

![[Pasted image 20230304151328.png]]

![[Pasted image 20230304151626.png]]

![[Pasted image 20230304151733.png]]

![[Pasted image 20230304152502.png]]

![[Pasted image 20230304152511.png]]

![[Pasted image 20230304152546.png]]

![[Pasted image 20230304152623.png]]

![[Pasted image 20230304152644.png]]

![[Pasted image 20230304152656.png]]

## EigenTrust Algorithm
We want each peer to 
- know all peers
- perform minimal computation and storage

- Comprehensive
	- iterative friend-friend reference
	- ![[Pasted image 20230304152843.png]]
- When the number of round n is large, converge to the same vector for every peer i (the of C) eigen vector
	- Peers can coorperate to compute and store `t_i`

![[Pasted image 20230304152941.png]]

![[Pasted image 20230304153012.png]]

![[Pasted image 20230304153040.png]]

![[Pasted image 20230304153046.png]]

## Pretrusted Peers in EigenTrust
![[Pasted image 20230304153124.png]]

![[Pasted image 20230304153145.png]]

![[Pasted image 20230304153225.png]]

![[Pasted image 20230304153326.png]]

![[Pasted image 20230304153504.png]]

![[Pasted image 20230304153544.png]]

![[Pasted image 20230304154450.png]]

## Secure EigenTrust: Strategies to Handle Dishonest Peers
![[Pasted image 20230304154622.png]]

![[Pasted image 20230304154645.png]]

![[Pasted image 20230304154734.png]]

![[Pasted image 20230304155044.png]]

![[Pasted image 20230304155102.png]]

