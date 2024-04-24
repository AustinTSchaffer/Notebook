---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 11 - Automated Planning

## Chapter Summary
- Planning systems are problem-solving algorithms that operate on explicit factored representations of states and actions. These representations make possible the derivation of effective domain-independent heuristics and the development of powerful and flexible algorithms for solving problems.
- PDDL, the Planning Domain Definition Language, describes the initial and goal states as conjunctions of literals, and actions in terms of their preconditions and effects. Extensions represent time, resources, percepts, contingent plans, and hierarchical plans. State-space search can operate in the forward direction (progression) or the backward direction (regression). Effective heuristics can be derived by subgoal independence assumptions and by various relaxations of the planning problem.
- Other approaches include encoding a planning problem as a Boolean satisfiability problem or as a constraint satisfaction problem; and explicitly searching through the space of partially ordered plans.  
- Hierarchical task network (HTN) planning allows the agent to take advice from the domain designer in the form of high-level actions (HLAs) that can be implemented in various ways by lower-level action sequences. The effects of HLAs can be defined with angelic semantics, allowing provably correct high-level plans to be derived without consideration of lower-level implementations. HTN methods can create the very large plans required by many real-world applications.
- Contingent plans allow the agent to sense the world during execution to decide what branch of the plan to follow. In some cases, sensorless or conformant planning can be used to construct a plan that works without the need for perception. Both conformant and contingent plans can be constructed by search in the space of belief states. Efficient representation or computation of belief states is a key problem.
- An online planning agent uses execution monitoring and splices in repairs as needed to recover from unexpected situations, which can be due to nondeterministic actions, exogenous events, or incorrect models of the environment.
- Many actions consume resources, such as money, gas, or raw materials. It is convenient to treat these resources as numeric measures in a pool rather than try to reason about, say, each individual coin and bill in the world. Time is one of the most important resources. It can be handled by specialized scheduling algorithms, or scheduling can be integrated with planning.
- This chapter extends classical planning to cover nondeterministic environments (where outcomes of actions are uncertain), but it is not the last word on planning. [[AIMA - Chapter 17 - Maxing Complex Decisions]] describes techniques for stochastic environments (in which outcomes of actions have probabilities associated with them): Markov decision processes, partially observable Markov decision processes, and game theory. In [[AIMA - Chapter 22 - Reinforcement Learning]] we show that reinforcement learning allows an agent to learn how to behave from past successes and failures.