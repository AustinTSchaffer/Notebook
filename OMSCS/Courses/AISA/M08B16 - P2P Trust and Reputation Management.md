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

![](Pasted%20image%2020230304150940.png)

