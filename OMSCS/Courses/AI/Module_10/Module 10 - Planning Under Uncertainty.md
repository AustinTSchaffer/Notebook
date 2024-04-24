---
tags:
  - OMSCS
  - AI
---
# Module 10 - Planning Under Uncertainty

## Markov Decision Process (MDP)
- States: $S_1, S_2, ..., S_N$
- Actions: $a_1, a_2, ..., a_K$
- State transition matrix: $T(S, a, S')=P(S'|a,S)$
- Reward function: $R(S)$
- Policy: $\pi(S) \rightarrow a$

### Policy vs Search
Issues with search in nondeterministic spaces
- High branching factor
- Search tree too deep
- can reach each state more than once

Benefit of policies
- for each cell, determine which direction the agent should move

![[Pasted image 20240417154932.png]]

Objective: minimize all cost, maximize profit

$$
\text{E} \left[ \sum_{t=0}^{\infty} \delta^t R_t \right] \rightarrow max
$$

$\delta$ is a "discount factor". $< 1$. Decays the weighting associated with future rewards.

![[Pasted image 20240417155353.png]]

![[Pasted image 20240417155829.png]]

![[Pasted image 20240417160151.png]]

![[Pasted image 20240422112901.png]]

![[Pasted image 20240422112825.png]]

![[Pasted image 20240422131504.png]]

