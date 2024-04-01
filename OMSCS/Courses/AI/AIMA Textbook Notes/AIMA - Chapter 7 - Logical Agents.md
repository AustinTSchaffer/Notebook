---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 7 - Logical Agents
> knowledge-based agents use a process of reasoning over an internal representation of knowledge to decide what actions to take.

- the atomic representations used by problem-solving agents are limiting
- in partially observable environments, a PS agent must list all possible concrete states
- [[AIMA - Chapter 6 - Constraint Satisfaction Problems]] introduces factored representations
	- states are assignments of variables
	- some parts of the agent can work in a domain-independent way
- this chapter develops logic as a general class of representations to support knowledge-based agents.
	- they combine and recombine information
	- accept new tasks in the form of explicitly defined goals
	- achieve competence quickly by being told or learning new knowledge about the environment
	- adapt to change in the environment by updated relevant knowledge

OMSCS has a whole separate course on [Knowledge-Based AI (KBAI)](https://omscs.gatech.edu/cs-7637-knowledge-based-artificial-intelligence-cognitive-systems). I've heard mixed reviews of this course. Regardless, I don't think this chapter is necessarily going to be a focus on the final.

## 7.1 Knowledge-Based Agents
- central component is a knowledge-base (KB)
	- KB is a set of sentences
	- a sentence is expressed in a language called "knowledge representation language"
	- a sentence represents some assertion about the world
	- when a sentence isn't derived from other sentences, it's called an "axiom"
- 2 main operations
	- Tell
	- Ask
	- Both involve inference
		- deriving new sentences from old
		- when a questioned is `Ask`ed, the answer should follow from what has already been `Tell`ed to the KB
- The KB can be pre-populated or start from scratch, depending on the needs of the agent

## 7.2 The Wumpus World
- the wumpus world is a cave consisting of rooms connected by passageways
- in the cave, there's a monster (the wumpus) which eats anything that enters its room
- the wumpus can be killed by the agent, but the agent has one chance (one shot, one opportunity)
- some rooms contain traps, which can trap the agent, but not the wumpus
- one room contains a heap of gold
- PEAS description
	- Performance
		- +1000 for getting the gold and leaving
		- -1000 for dying (trap/pit or wumpus)
		- -1 for each action taken
		- -10 for using the one-shot weapon
	- Environment
		- NxM grid of rooms
		- agent starts at $(1,1)$, facing east
		- wumpus and gold locations are chosen randomly (excluding $(1,1)$)
		- each square (other than $(1,1)$) has a probability $p$ of being a pit.
	- Actuators
		- agent can move
			- Forward
				- Dies if resulting location is trap or **live** wumpus
				- No change in location if wall detected
			- TurnLeft (90 deg)
			- TurnRight (90 deg)
		- agent can grab the gold if in the same square
		- agent can shoot to fire its weapon
			- projectile travels in the direction they are facing
			- projectile continues until it hits/kills the wumpus or a wall
		- agent can climb out of the cave at square $(1,1)$
	- Sensors
		- In squares adjacent to a wumpus, the agent will perceive a stench. The cell containing the wumpus will also smell, but that precept is only available if the agent kills the wumpus before entering the cell.
		- In squares adjacent to a pit, the agent will feel a directionless breeze.
		- In squares adjacent to the gold, the agent will perceive a glitter.
		- When the agent walks into a wall, it'll feel a bump.
		- If the wumpus is killed, the agent will hear a scream. The scream can be heard across the entire cave network.
		- These sensors are vectorized, so multiple can be perceived at the same time: $(Stench=T/F, Breeze=T/F, Glitter=T/F, Bump=T/F, Scream=T/F)$
![[Pasted image 20240401091004.png]]

- wumpus world characterization
	- deterministic
	- discrete
	- static
	- single-agent (stationary wumpus)
	- sequential
	- partially observable
		- agent's location
		- is wumpus alive?
		- do I have ammunition?
	- transition model is known/unknown depending on how you define knowable
- main challenge is its initial ignorance of the configuration of the environment
- "in most instances of the wumpus world, it's possible for the agent to retrieve the gold safely"
- some board states don't allow the agent to retrieve the gold
	- board partitioned by the pits/wumpus
	- frontier of unsafe board squares
- in general, the agent can form an understanding of which cells are "safe" to visit, then come up with a strategy to optimize which cells to visit efficiently.

## 7.3 Logic
- syntax
- semantics
- truth
- possible world
- model
- satisfies
- entailment
- logical inference
- model checking
- sound / truth-preserving
- completeness
- grounding
- learning

## 7.4 Propositional Logic
- syntax
	- atomic sentences
	- proposition symbols
	- complex sentences
	- logical connectives
	- negation
	- literal
	- positive literal
	- negative literal
	- conjunction
	- conjuncts
	- disjunction
	- disjuncts
	- premise / antecedent
	- conclusion / consequent
	- rules / if-then
	- biconditional
	- truth value
- semantics
	- truth value
	- truth table
- simple knowledge base
- simple inference procedure
	- sound
	- complete

## 7.5 Propositional Theorem Proving
- theorem proving
- logical equivalence
- validity
- tautologies
- deduction theorem
- satisfiability
- SAT
- *reductio ad absurdum*
- refutation
- contradiction
- inference and proofs
	- inference rules
	- proof
	- Modus Ponens
	- And-Elimination
	- monotonicity
- proof by resolution
	- resolution
	- resolvent
	- unit resolution
	- complementary literals
	- clause
	- unit clause
	- factoring
	- conjunctive normal form (CNF)
	- resolution closure ($RC(S)$ of a set of clauses $S$)
	- ground resolution theorem
- horn clauses and definite clauses
	- definite clause
	- Horn clause
	- goal clauses
	- body / head / fact
	- forward-chaining
	- backward-chaining
	- logic programming
- forward and backward chaining
	- AND-OR graph
	- sound
	- complete
	- data-driven
	- goal-directed reasoning

## 7.6 Effective Propositional Model Checking
- a complete backtracking algorithm
	- Davis-Putnam algorithm (DPLL)
	- early termination
	- pure symbol heuristic
	- pure symbol
	- unit clause heuristic
	- unit clause
	- unit propagation
	- component analysis
	- components
	- variable and value ordering
	- degree heuristic
	- intelligent backtracking
	- conflict cause learning
	- random restarts
	- clever indexing
- local search algorithms
	- hill climbing
	- simulated annealing
	- WalkSAT
- landscape of random SAT problems
	- under-constrained
	- satisfiability threshold conjecture

## 7.7 Agents Based on Propositional Logic
- fluent
- atemporal variables
- transition model
- effect axioms
- frame problem
- frame axioms
- representational frame problem
- inferential frame problem
- successor-state axiom
- qualification problem
- hybrid agent
- logical state estimation
	- cache
	- belief state
	- state
	- estimation
	- conservative approximation
- making plans by propositional inference
	- precondition axioms
	- action exclusion axioms

## Summary

Take the course on KBAI if you find these terms compelling.