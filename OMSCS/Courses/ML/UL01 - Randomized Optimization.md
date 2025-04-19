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

## MIMIC
See: [[isbell-mimic-nips-1997.pdf]]

- only points, no structure
	- convey structure
- unclear probability distribution
	- directly model distribution
	- successively refine model

$$
P_\theta(X)=
\begin{cases}
	\frac{1}{Z_\theta} \text{ if } f(X) \ge \theta \\
	0 \text{ otherwise} \\
\end{cases}
$$
- $P_{\theta_{min}}(X)$
	- The output is the uniform distribution
- $P_{\theta_{min}}(X)$
	- The output is optima distribution

![[Pasted image 20250310104533.png]]

![[Pasted image 20250310104614.png]]

- Similar to GA
	- define some population
	- select only the fittest from that population
	- estimate a new distribution that's similar to those
	- The structure is how we represent the probability distribution
- Gradually move from $\theta_{min}$ to $\theta_{max}$
- $P_{\theta} \approx P_{\theta+\epsilon}$
- $P_{\theta_t}$ should contain all of the samples that exist in $P_{\theta_{t+1}}$. This allows you to refine from the uniform distribution toward the optimum distribution.

### Estimating Distributions (MIMIC)
- $P(X)=P(X_1 \space|\space X_{2..n})P(X_2 \space|\space X_{3..n})...P(X_n)$
- $X=\{X_1, X_2, X_3, ... X_n\}$
- "The probability of seeing all of the features of some example is just the joint distribution over all of the features."

