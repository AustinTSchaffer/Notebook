---
tags:
  - OMSCS
  - NS
---
# L03 - Degree Distribution and The Friendship Paradox

## Overview
- Measure and interpret the degree distribution of a network
- Understand the _“friendship paradox”_ to illustrate the importance of the degree distribution 
- An application of the friendship paradox: vaccination targets when the network topology is unknown
- Learn the $G(n,p)$ model as the most basic type of random graph
- Degree correlations and assortative networks

## Reading
- [[Chapter 03 - Random Networks]]
- [[Chapter 07 - Degree Correlations]]
- Recommended: [Simulated Epidemics in an Empirical Spatiotemporal Network of 50,185 Sexual Contacts.](http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1001109) Luis E. C. Rocha, Fredrik Liljeros, Petter, Holme (2011)

## Notes from Module

- degree distribution is a normalized histogram showing probabilities

## Degree Distribution Moments

- average degree
- second moment
- variance

![[Pasted image 20240525095430.png]]

- Complementary Cumulative Distribution Function (CCDF)
- Shows the probability that a variable has a probability $\ge$ a specific value.
- Useful for large networks, where a histogram will be hard to read.

![[Pasted image 20240525095457.png]]

## Two Special Degree Distributions

![[Pasted image 20240525095707.png]]

- CCDF plots are typically shown with at least one log scale
	- log-linear: Exponential decay
	- log-log: power law distribution

- degree distribution of a sex-contact network (video)

## Friendship Paradox

- $q_k$ equals the number of nodes of degree K, times the probability that an edge connects to a specific node of degree K
- $q_k=(np_k)(\frac{k}{2m})$
- $q_k=\frac{kp_k}{\frac{2m}{n}}$
- $q_k=\frac{kp_k}{\bar{k}}$

- $m$ is the number of edges
- $n$ is the number of nodes
- $p_k$ is the probability that a node has degree $k$
- $k$ is the degree that we're currently considering

> the probability that the randomly chosen stub connects to a node of degree k is proportional to both k and the probability that a node has degree k.

Expected value of the degree of a node's neighbor.

$$\bar{k_{nn}}=\sum_{k=0}^{k_{max}}kq_k$$

The friendship paradox is that $\bar{k_{nn}}$ tends to be higher than $\bar{k}$
- Networks where every node has the same $k$ have no disparity between $\bar{k_{nn}}$ and $\bar{k}$
- Star networks tend to have the highest disparity between $\bar{k_{nn}}$ and $\bar{k}$

## The G(n,p) Model (aka ER Graphs, aka Gilbert Model)
- random graphs
- network has n nodes
- the probability that any two distinct nodes are connected with an undirected edge is p
- All formulas assume that there are no self-edges
- the number of edges $m$ in a $G(n,p)$ model is a random variable
- The expected number of edges is: $p\frac{n(n-1)}{2}$
- The average node degree is: $p(n-1)$
- The density of the network is: $p$
- the degree variance is: $p(1-p)(n-1)$
- The degree distribution of the $G(n,p)$ model  follows the binomial distribution: $Binomial(n-1,p)$
- There is no correlations between the degrees of neighboring nodes.
- If we reach a node v by following an edge from another node, the expected value of v’s degree is one more than the average node degree.
- $\bar{S}=1-S$ is the probability that a node does not belong to the largest connected component (LCC) of the network
- $\bar{S}=\left((1-p)+(p\bar{S})\right)^{n-1}$
- $p=\frac{\bar{k}}{n-1}$
- $\bar{S}=\left(1-\frac{\bar{k}}{n-1}(1-\bar{S})\right)^{n-1}$
- $S=1-e^{-\bar{k}S}$
- If the average degree is larger than one ($\bar{k}\gt1$), the size of the LCC is $S>0$
- The LCC suddenly explodes when the average node degree is larger than 1. This is referred to as a "phase transition"
- Once the average node degree reaches/exceed $\bar{k}=1$, the network suddenly acquires a giant connected component that includes a large fraction of all network nodes
- The critical point corresponds to a connection probability of $p=\frac{1}{n-1}\approx\frac{1}{n}$ because $\bar{k}=(n-1)\times{p}$
- The probability that a node does not connected to any node in the LCC: $(1-p)^{Sn}\approx(1-p)^n$ (if $S\approx1$)
- When the average degree $(\bar{k}=np)$ is higher than $ln(n)$, we expect to have a single connected component.

## Assortative, Neutral and Disassortative Networks
Some of the above work assumes that there is no statistical correlation between $\bar{k}$ and $\bar{k_{nn}}$. In practice, some networks do have associations between the two metrics.

![[Pasted image 20240526205925.png]]

- In an Assortative Net, highly connected nodes will tend to have neighbors that are also highly connected
- In a Disassortative Net, highly connected nodes will tend to have neighbors which have fewer connections.
- In a Neutral Net, there is little-to-no correlation between the connectiveness of a node and the connectiveness of its neighbors.

Looking into the correlation between $\bar{k}$ and $\bar{k_{nn}}$ gives some insight into the network, and what effect highly connected nodes have in its neighbors.

![[Pasted image 20240526205619.png]]

