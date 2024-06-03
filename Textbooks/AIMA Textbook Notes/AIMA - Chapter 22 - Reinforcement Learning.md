---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 22 - Reinforcement Learning
- learning from rewards
	- rewards can be sparse (chess)
	- rewards can be continuous/intermediate 
		- car driving agents (Trackmania)
		- baby crawling

- model-based reinforcement learning
	- state estimation
	- utility function
- model-free reinforcement learning
	- action-utility learning
		- "Q-Learning" is most common
	- policy search
		- this is a "reflex agent"
- passive reinforcement learning
- active reinforcement learning
- principle issue is "exploration"
- apprenticeship learning

## Chapter Summary
- The overall agent design dictates the kind of information that must be learned:
	- A model-based reinforcement learning agent acquires (or is equipped with) a transition model for the environment and learns a utility function.
	- A model-free reinforcement learning agent may learn an action-utility function or a policy.
- Utilities can be learned using several different approaches:
	- Direct utility estimation uses the total observed reward-to-go for a given state as direct evidence for learning its utility.  
	- Adaptive dynamic programming (ADP) learns a model and a reward function from observations and then uses value or policy iteration to obtain the utilities or an optimal policy. ADP makes optimal use of the local constraints on utilities of states imposed through the neighborhood structure of the environment.  
	- Temporal-difference (TD) methods adjust utility estimates to be more consistent with those of successor states. They can be viewed as simple approximations of the ADP approach that can learn without requiring a transition model. Using a learned model to generate pseudoexperiences can, however, result in faster learning.  
- Action-utility functions, or Q-functions, can be learned by an ADP approach or a TD approach. With TD, Q-learning requires no model in either the learning or action- selection phase. This simplifies the learning problem but potentially restricts the ability to learn in complex environments, because the agent cannot simulate the results of possible courses of action.  
- When the learning agent is responsible for selecting actions while it learns, it must trade off the estimated value of those actions against the potential for learning useful new information. An exact solution for the exploration problem is infeasible, but some simple heuristics do a reasonable job. An exploring agent must also take care to avoid premature death.
- In large state spaces, reinforcement learning algorithms must use an approximate functional representation of or in order to generalize over states. Deep reinforcement learning—using deep neural networks as function approximators—has achieved considerable success on hard problems.
- Reward shaping and hierarchical reinforcement learning are helpful for learning complex behaviors, particularly when rewards are sparse and long action sequences are required to obtain them.  
- Policy-search methods operate directly on a representation of the policy, attempting to improve it based on observed performance. The variation in the performance in a stochastic domain is a serious problem; for simulated domains this can be overcome by fixing the randomness in advance.  
- Apprenticeship learning through observation of expert behavior can be an effective solution when a correct reward function is hard to specify. Imitation learning formulates the problem as supervised learning of a policy from the expert’s state–action pairs. Inverse reinforcement learning infers reward information from the expert’s behavior.

> Reinforcement learning continues to be one of the most active areas of machine learning research.

- frees us from manual construction of behaviors and from labeling vast data sets
- huge application in robotics
- there is so far no single-best approach to RL
- given enough data, model-free methods may be able to succeed in any domain
- not all domains have sufficient data
- "as the environment becomes more complex, the advantages of a model-based approach become more apparent."
