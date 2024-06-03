---
tags:
  - OMSCS
  - NS
---
# L04 - Random vs Real Graphs and Power-Law Networks

## Overview
- See examples of real networks with highly skewed degree distributions 
- Understand the math of power-law distributions and the concept of “scale-free” networks 
- Learn about models that can generate networks with power-law degree distribution
- Explain the practical significance of power-law degree distributions through case studies

## Required Reading
- [[Chapter 04 - The Scale-Free Property]]
- [[Chapter 05 - The Barabasi-Albert Model]]

## Module Notes
- Real networks cannot be modeled as random ER graphs
- such networks follow the binomial distribution
- real networks actually have highly skewed degree distributions
- For many networks, the power law degree distribution $p_k \propto k^{-\alpha}$ is a more appropriate model

![[Pasted image 20240526212703.png]]

## Power-Law Degree Distribution
- $p_k=ck^{-\alpha}$
- The probability that the degree of a node is equal to a positive integer $k$ is proportional to $k^{-\alpha}$

![[Pasted image 20240526213600.png]]

## How to plot a power-law degree distribution
- linear scale: bad
- log-log scale with linear binning: good, but higher end will be noisy
- log-log scale with logarithmic binning.
	- bin width of the histogram increases exponentially with $k$
	- A potential issue with this approach is that you need to do some analysis for picking how fast to increase the bin with with $k$
- C-CDF

![[Pasted image 20240526214235.png]]

## Scale-free nature of power-law networks
scale-free == power-law

