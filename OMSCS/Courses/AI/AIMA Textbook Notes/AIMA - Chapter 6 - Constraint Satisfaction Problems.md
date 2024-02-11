---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 6 - Constraint Satisfaction Problems
- [[AIMA - Chapter 3 - Solving Problems by Searching]] and Chapter 4 (no chapter notes, module notes link: [[Module 02 - Simulated Annealing]])
	- These prior chapters considered the "state" of a problem to be a black box, atomic, indivisible.
	- Searching for solutions within the state space required domain-specific code to describe the transition between states.
	- Transitioning between states often resulted in a graph-representation of the state space.
- In this chapter
	- the state is broken open using a factored representation for each state
	- Each state comprises a **set of variables**, each with a value taken from a **domain**.
	- Each variable has a **constraint** on its values, typically based on some operation on or comparison with the other variables.
	- Problems that can be described this way are called **constraint satisfaction problems** or **CSP**.

> CSP search algorithms take advantage of the structure of states and use general rather than domain-specific heuristics to enable the solution of complex problems. The main idea is to eliminate large portions of the search space all at once by identifying variable/value combinations that violate the constraints.
> 
> ...
> 
> In atomic state-space search we can only ask: is this specific state a goal? No? What about this one? With CSPs, once we find out that a partial assignment violates a constraint, we can immediately discard further refinements of the partial assignment. Furthermore, we can see why the assignment is not a solution—we see which variables violate a constraint—so we can focus attention on the variables that matter. As a result, many problems that are intractable for atomic state-space search can be solved quickly when formulated as a CSP.

## Defining CSPs

- $X$ is a set of variables, $\{X_1, ..., X_n\}$
- D is a set of domains, $\{D_1,...,D_n\}$
	- There can be one set of domains available to all variables, or one set of domains available for each variable.
	- A domain $D_i$ consists of a set of allowable values $\{v_1,...,v_n\}$ for variable $X_i$. A boolean variable would have the domain $\{true, false\}$. 
- $C$ is a set of constraints that specify allowable combinations of values. 
	- Each constraint $C_j$ consists of a pair $\langle scope, rel \rangle$
		- $scope$
			- a tuple of variables that participate in the constraint
		- $rel$
			- a relation that defines the values those variables can take on.
			- can be represented as an explicit set of all tuples of values that satisfy the constraint, or as a function that can compute whether a tuple is a member of the relation

We formulate problems with this formal definition so that we can abstract the problem. Any CSP-solving strategy that operates on this formal definition will apply to all CSPs that can be formulated this way. In fact, may years of research have gone into solving these kinds of problems.

- SMT-LIB: http://smtlib.cs.uiowa.edu/index.shtml
- Z3 Theorem Prover: https://github.com/Z3Prover/z3
- OR-Tools: https://developers.google.com/optimization
- GeCode (generic constraint development environment): https://www.gecode.org/
- There's a yearly competition put on by MiniZinc:
	- https://www.minizinc.org/challenge2022/results2022.html
	- https://www.minizinc.org/index.html

You may think that defining a problem in this way means that you're missing out on important nuance that might make solving a particular CSP more efficient. However, you could always encode that nuance using MORE constraints.

**Definitions**
- CSPs deal with assignments of values to variables: $\{X_i=v_i,X_j=v_j,...\}$
- An assignment that does not violate any constraints is called a **consistent** or legal assignment.
- A **complete assignment** is one in which every variable is assigned a value, and a **solution** to the CSP is a consistent, complete assignment.
- A **partial assignment** is one that leaves some variables unassigned
- A **partial solution** is a partial assignment that is consistent

**Hardness**
- CSPs are NP-complete in general.
- There are subclasses of CSPs that can be solved efficiently.

### Example 1: A > B
- English: "Two variables can have values 1, 2, or 3. The first variable must be larger than the 2nd."
- Variables: $\{X_1, X_2\}$
- Domain: $\{1, 2, 3\}$ (global domain, i.e. $D_1 = D_2$)
- Constraint: $X_1>X_2$
	- Formally, option 1: $\langle (X_1, X_2), \{(3,1), (3,2), (2,1)\} \rangle$
	- Formally, option 2: $\langle (X_1, X_2), X_1 > X_2 \rangle$

### Example 2: Coloring Australia
This was beaten to death over in [[Module 04 - Constraint Satisfaction]] already, but here's the formal definition.

![[Pasted image 20240211092439.png]]

- $X=\{WA, NT, Q, NSW, V, SA, T\}$
- $D=\{color_1, color_2, color_3\}$
- $C = \{...\}$ (expanded for readability below)
	- $\langle (SA, WA), SA \ne WA \rangle$
	- $\langle (SA, NT), SA \ne NT \rangle$
	- $\langle (SA, Q), SA \ne Q \rangle$
	- $\langle (SA, NSW), SA \ne NSW \rangle$
	- $\langle (SA, V), SA \ne V \rangle$
	- $\langle (WA, NT), WA \ne NT \rangle$
	- $\langle (NT, Q), NT \ne Q \rangle$
	- $\langle (Q, NSW), Q \ne NSW \rangle$
	- $\langle (NSW, V), NSW \ne V \rangle$

The constraint graph on the right of the screenshot is / can be generated from the formal definition of the constraints.

**Note:** This problem only needs 3 colors. We're omitting the 4th color which is required for 2D maps in general. Using 4 colors on this problem makes this problem too easy. In general, you could use the principles from "iterative deepening" to determine the domain for any $X$ and $C$ regardless of dimensionality.

```python
Colors = iterator(c1, c2, c3, c4, c5, ...)
X = {...}
D = {}
C = {...}

while True:
    D.append(next(Colors))
	result = SolveCSP(X, D, C)
    if result is not failure:
        return result
```

### Example 3: Job Scheduling
> We consider a small part of the car assembly, consisting of 15 tasks: install axles (front and back), affix all four wheels (right and left, front and back), tighten nuts for each wheel, affix hubcaps, and inspect the final assembly. We can represent the tasks with 15 variables.

$$
X = \{Axle_F, Axle_B, Wheel_{RF}, Wheel_{LF}, Wheel_{RB}, Wheel_{LB}, LugNuts_{RF}, LugNuts_{LF}, LugNuts_{RB}, LugNuts_{LB}, HubCap_{RF}, HubCap_{LF}, HubCap_{RB}, HubCap_{LB}, Inspect\}
$$

> Next, we represent precedence constraints between individual tasks. Whenever a task $T_1$ must occur before task $T_2$, and task $T_1$ takes duration $d_1$ to complete, we add an arithmetic constraint of the form:

$$T_1+d_1 \le T_2$$

In this model, the variables are being assigned some integer timestamp for when the installation team can begin the installation of that component. The domain is then just positive integers, so $D=\mathbb{N}$. 

Some example constraints:
- Axles take 10 minutes to install, and must precede Wheels.
	- $\langle (Axle_F, Wheel_{RF}), Axle_F+10\le Wheel_{RF} \rangle$
	- $\langle (Axle_F, Wheel_{LF}), Axle_F+10\le Wheel_{LF} \rangle$
	- $\langle (Axle_B, Wheel_{RB}), Axle_B+10\le Wheel_{RB} \rangle$
	- $\langle (Axle_B, Wheel_{LB}), Axle_B+10\le Wheel_{LB} \rangle$
- Wheels take 1 minute to install, and must precede Lug Nuts
	- $\langle (Wheel_{LF}, LugNuts_{LF}), Wheel_{LF}+1\le LugNuts_{LF} \rangle$
	- $\langle (Wheel_{RF}, LugNuts_{RF}), Wheel_{RF}+1\le LugNuts_{RF} \rangle$
	- $\langle (Wheel_{LB}, LugNuts_{LB}), Wheel_{LB}+1\le LugNuts_{LB} \rangle$
	- $\langle (Wheel_{RB}, LugNuts_{RB}), Wheel_{RB}+1\le LugNuts_{RB} \rangle$
- Lug Nuts take 2 minutes to install, and must precede hubcaps
	- $\langle (LugNuts_{LF}, HubCap_{LF}), LugNuts_{LF}+2\le HubCap_{LF} \rangle$
	- $\langle (LugNuts_{RF}, HubCap_{RF}), LugNuts_{RF}+2\le HubCap_{RF} \rangle$
	- $\langle (LugNuts_{LB}, HubCap_{LB}), LugNuts_{LB}+2\le HubCap_{LB} \rangle$
	- $\langle (LugNuts_{RB}, HubCap_{RB}), LugNuts_{RB}+2\le HubCap_{RB} \rangle$
- Suppose that there's only one tool available for installing Axles, meaning they cannot be installed simultaneously. To represent this, we must use a disjunctive constraint which prevents the scheduler from placing the axle installations in overlapping time ranges.
	- $\langle (Axle_F, Axle_B), Axle_F+10 \le Axle_B \rangle$
	- $\langle (Axle_B, Axle_F), Axle_B+10 \le Axle_F \rangle$
- We need to assert that the inspection comes last and takes 3 minutes. For every variable except inspect, we add a constraint of the form $X_i+d_i \le Inspect$. We could also use one constraint for this, given the definition of constraint from earlier.
	- $\langle X, \forall_X (X_i + d_i) \le Inspect \rangle$
- Suppose we need to make sure that the assembly needs to be done in 30 minutes. We can achieve that by limiting the domain of all variables. Given that the last step takes 3 minutes, the max timestamp must be 27.
	- $D_i=\{0,1,2,3,...,27\}$

> A discrete domain can be **infinite**, such as the set of integers or strings. (If we didn’t put a deadline on the job-scheduling problem, there would be an infinite number of start times for each variable.) With infinite domains, we must use implicit constraints like $T_1+d_1 \le T_2$ rather than explicit tuples of values. Special solution algorithms \[...\] exist for **linear constraints** on integer variables—that is, constraints, such as the \[assembly problem\], in which each variable appears only in linear form. It can be shown that no algorithm exists for solving general **nonlinear constraints** on integer variables—the problem is undecidable.

> Constraint satisfaction problems with continuous domains are common in the real world and are widely studied in the field of operations research. For example, the scheduling of experiments on the Hubble Space Telescope requires very precise timing of observations; the start and finish of each observation and maneuver are continuous-valued variables that must obey a variety of astronomical, precedence, and power constraints. The best-known category of continuous-domain CSPs is that of linear programming problems, where constraints must be linear equalities or inequalities. Linear programming problems can be solved in time polynomial in the number of variables. Problems with different types of constraints and objective functions have also been studied—quadratic programming, second-order conic programming, and so on. These problems constitute an important area of applied mathematics.

## Types of Constraints
- Unary Constraints
	- $\langle (V_1), Constraint(V_1) \rangle$
	- Example: $NSW \ne green$
- Binary Constraints
	- $\langle (V_1, V_2), Constraint(V_1, V_2) \rangle$
	- Example: $NSW \ne SA$
- Higher order constraints
	- Anything with 3 or more variables
	- "Y must be between X and Z": $\langle (X, Y, Z), X < Y < Z \rangle$
- A constraint involving an arbitrary number of constraints is a **global constraint**
	- Example: "The inspection step must be last."
	- Most common example: "All variables must be different." aka "All Different" aka $AllDiff$

## Cryptarithmetic Puzzles
Each letter in a cryptarithmetic puzzle represents a different digit.

![[Pasted image 20240211140456.png]]

- $O+O=R+10*C_1$
- $C_1+W+W=U+10*C_2$
- $C_2+T+T=O+10*C_3$
- $C_3=F$
- $X=\{T, W, O, F, U, R, C_1, C_2, C_3\}$
- $D_{\{W,O,U,R\}}=\{0,1,2,3,4,5,6,7,8,9\}$
- $D_{\{F,T\}}=\{1,2,3,4,5,6,7,8,9\}$
	- The problem would be less interesting if T or F are 0.
	- This may not actually be true for the real problem.
- $D_{C_i}=\{0, 1\}$
	- Might help if the solver knows that the auxiliary variables can never be higher than 1, since it otherwise doesn't know the quirks of remainders in 2 number addition.
	- We really need to teach this MF everything 🙄
	- We can probably exclude $0$ for $C_3$, but that's covered by $C_3=F$
- $AllDiff(T, W, O, F, U, R)$

![[Pasted image 20240211140708.png]]

- The diagram above is a **constraint hypergraph**.
- The blue circle nodes represent individual variables
- The green squares represent the constraints.
- The domains are not represented in this graph.

> \[...\] every finite-domain constraint can be reduced to a set of binary constraints if enough auxiliary variables are introduced. This means that we could transform any CSP into one with only binary constraints—which certainly makes the life of the algorithm designer simpler. Another way to convert an $n$-ary CSP to a binary one is the **dual graph** transformation: create a new graph in which there will be one variable for each constraint in the original graph, and one binary constraint for each pair of constraints in the original graph that share variables.

Reasons not to do the above
- Could be error-prone
- Looks like crap
- Probably not necessary
- There already exist special-purpose inference algorithms for global constraints which are more efficient than operating with primitive constraints.

## Preference Constraints
- Many real-world CSPs include preference constraints indicating which solutions are preferred.
- Preference constraints can often be encoded as costs on individual variable assignments
	- Assigning an afternoon slot for Prof. R costs 2 points against the overall objective function
	- Assigning a morning slot for Prof R costs 1 point against the overall objective function
- CSPs with preferences can be solved with optimization search methods, either path-based or local
- such a problem a **constrained optimization problem**, or COP
- Linear programs are one class of COPs

## Contraint Propagation: Inference in CSPs
Notes incomplete. Subsection headers:
- Node consistency
- Arc consistency
- Path consistency
- K-consistency
- Global contraints
- Sudoku

## Backtracking Search for CSPs
Notes incomplete. Subsection headers and key terms:
- Variable and value ordering
	- least-constraining-value
	- minimum remaining values (MRV)
- Interleaving search and inference
	- Forward checking
	- Maintaining Arc Consistency (MAC)
- Intelligent Backtracking: Looking Backwards
	- Chronological backtracking
	- Backjumping
	- Conflict-directed backjumping
- Constraint Learning
	- No-good

## Local Search for CSPs
Notes incomplete. Key terms:
- Min conflicts
- Constraint weighting

## The Structure of Problems
Notes incomplete. Subsection headings and key terms:
- (main header terms)
	- independent subproblems
	- connected components
	- directed arc consistency
	- topological sort
- Cutset conditioning
	- Cycle cutset
- Tree decomposition
	- Tree width
- Value symmetry
	- Symmetry-breaking constraint

## Summary
- **Constraint satisfaction problems** (CSPs) represent a state with a set of variable/value pairs and represent the conditions for a solution by a set of constraints on the variables. Many important real-world problems can be described as CSPs.
- A number of **inference** techniques use the constraints to rule out certain variable assignments. These include node, arc, path, and $k$-consistency.
- **Backtracking search**, a form of depth-first search, is commonly used for solving CSPs. Inference can be interwoven with search.
- The **minimum-remaining-values** and **degree** heuristics are domain-independent methods for deciding which variable to choose next in a backtracking search.
- The **least-constraining-value** heuristic helps in deciding which value to try first for a given variable.
- Backtracking occurs when no legal assignment can be found for a variable. 
- **Conflict-directed backjumping** backtracks directly to the source of the problem.
- **Constraint learning** records the conflicts as they are encountered during search in order to avoid the same conflict later in the search.
- Local search using the **min-conflicts** heuristic has also been applied to constraint satisfaction problems with great success.
- The complexity of solving a CSP is strongly related to the structure of its constraint graph. Tree-structured problems can be solved in linear time. **Cutset conditioning** can reduce a general CSP to a tree-structured one and is quite efficient (requiring only linear memory) if a small cutset can be found. **Tree decomposition** techniques transform the CSP into a tree of subproblems and are efficient if the **tree width** of the constraint graph is small; however they need memory exponential in the tree width of the constraint graph. Combining cutset conditioning with tree decomposition can allow a better tradeoff of memory versus time.