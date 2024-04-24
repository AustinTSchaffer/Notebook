---
tags:
  - OMSCS
  - AI
---
# Module 9 - Logic and Planning

## Propositional Logic
- belief is based on assigning boolean values to states
- $E \lor B \Rightarrow A$ - "The alarm will go off if an earthquake occurred or that a burglary occurred"
- $A \Rightarrow J \land M$ - "J and M will call if the alarm goes off"
- $J \Leftrightarrow M$ - "J will call iff M calls"
- $J \Leftrightarrow \neg M$ - "J will call only if M doesn't call"
- Belief state: $\{B: True, E: True, ...\}$
- Truth tables come up a lot

| P   | Q   | $\neg{P}$ | $P \land Q$ | $P \lor Q$ | $P \Rightarrow Q$ | $P \Leftrightarrow Q$ |
| --- | --- | --------- | ----------- | ---------- | ----------------- | --------------------- |
| 0   | 0   | 1         | 0           | 0          | 1                 | 1                     |
| 0   | 1   | 1         | 0           | 1          | 1                 | 0                     |
| 1   | 0   | 0         | 0           | 1          | 0                 | 0                     |
| 1   | 1   | 0         | 1           | 1          | 1                 | 1                     |

| P   | Q   | A: $P \land (P \Rightarrow Q)$ | B: $\neg (\neg P \lor \neg Q)$ | $A \Leftrightarrow B$ |
| --- | --- | ------------------------------ | ------------------------------ | --------------------- |
| 0   | 0   | 0                              | 0                              | 1                     |
| 0   | 1   | 0                              | 0                              | 1                     |
| 1   | 0   | 0                              | 0                              | 1                     |
| 1   | 1   | 1                              | 1                              | 1                     |

- types of propositions
	- valid: true in all scenarios
	- satisfiable: true in at least one scenario
	- unsatisfiable: false in no scenarios
- cannot handle uncertainty
- cannot handle/model objects
- no shortcuts

| Models              | World                             | Beliefs                   |
| ------------------- | --------------------------------- | ------------------------- |
| First-Order Logic   | Relationships, Objects, Functions | True / False / Unknown    |
| Propositional Logic | Facts                             | True / False / Unknown    |
| Probability Theory  | Facts                             | $(0 \space ... \space 1)$ |

- atomic
	- problem solving
	- is the current state valid or a goal?
- factored
- structured

## First-Order Logic
![[Pasted image 20240403142859.png]]

It's called first-order because the relations are on objects, not on relations/functions. Those kinds of relations require higher-order logic.

### Syntax
![[Pasted image 20240403143201.png]]

- $\forall_R\space Transitive(R)\Leftrightarrow(\forall_{a,b,c} \space R(a,b)\land R(b,c) \Rightarrow R(a,c))$
	- This is invalid in first-order logic, but would be valid in higher order logic
### Vacuum World - FOL
- Variables
	- Locations: $L_1$, $L_2$, ...
	- Vacuum: $V$
	- Dirt: $D_1$, $D_2$, ...
- Functions
	- Is a location: $Loc(o)$
	- Is a Vacuum: $Vacuum(o)$
	- Is dirt: $Dirt(o)$
	- Is located at: $At(o, l)$
- Example sentences
	- Vacuum is at Location 1: $At(V, L_1)$
	- There is no dirt anywhere: $\forall_d \forall_l \space Dirt(d) \land Loc(l) \Rightarrow \neg At(d, l)$
	- The vacuum is in a location with dirt: $\exists_l \exists_d \space Dirt(d) \land Loc(l) \land At(V, l) \land At(d, l)$

## Planning

### Planning vs Execution
- stochastic environments
	- nondeterministic environments
	- driving on a road network that could be slippery and/or has traffic signals
- multi-agent environments
- partial observability
- unknown
- hierarchical

## Vacuum Cleaner Example
![[Pasted image 20240403150047.png]]

- conformant plans - plans that get to a goal state given information about the initial world state but no sensor information

## Classical Planning
- State space: k-boolean ($2^k$)
- World State: Complete assignment
- Belief state
	- complete assignment
	- partial assignment
	- arbitrary formula in boolean logic
		- Action representation
		- Property/classification assignment

Example:
![[Pasted image 20240412171452.png]]

- Regression search: Start with goal states, determine possible actions which move the belief state closer to the goal state. Search for the initial state from the goal state. Can be useful when there's a high branching factor



