---
tags:
  - OMSCS
  - ML
---
# UL01 - Randomized Optimization
## Hill Climbing
- determine neighbors of current X
- pick neighbor with highest fitness (F)
- continue until no neighbors are better.
## Random Restart Hill Climbing
- Do HC.
- Pick a random X when a local optimum is reached.
- Multiple tries to find a good starting place.
- Not much more time expensive. Multiple time complexity of HC by number of restarts.
- Can try to be more systematic about covering space

![[Pasted image 20250222002442.png]]

![[Pasted image 20250222002529.png]]

RHC pretty much always explores the whole state space redundantly. That's inefficient and slow.
## Simulated Annealing
- Balances exploiting (improving) with exploring (search).
	- Only "improving" leads to overfitting.
	- Only "searching" leads to underfitting.
- For a finite set of iterations
	- Sample new point $X_{t+1}$ from $N(X_t)$
	- Jump to new sample with probability given by an acceptance probability: $P(X_t, X_{t+1}, T)$
		- if $F(X_{t+1}) \ge F(X_t) : 100\%$
		- otherwise: $$e^{\frac{F(X_{t+1})-F(X_t)}{T}}$$
	- Decrease temperature.
- Properties
	- $T \rightarrow 0:$ like hill climbing
	- $T \rightarrow \infty:$ like random walk
- Want to decrease T slowly
- Probability of ending at any given point $X$ in the space is equal to the fitness of X, divided by T, then normalized.
$$
P(\text{ending at } x)=\frac{e^{F(x)/T}}{Z_T}
$$
> More likely to end at places with high fitness.

Boltzmann Distribution (analogy).

## Genetic Algorithms
https://edstem.org/us/courses/71185/lessons/126665/slides/706912

