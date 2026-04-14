---
tags:
  - OMSCS
  - Algorithms
---
# 2026-04-12 - TA Office Hours - Exam 3
- The Dual LP is a "certificate of optimality" for the Primal LP
- We use the Dual to prove Feasibility and Boundedness
- When checking for infeasibility, "try to find at least one contradiction"
	- In the example $(\max \space x,x \le -3, x \ge 0)$, we can see that $x$ has no valid values.
	- In the example $(\max \space x+y, x+y \le 1, x+y \ge 3, x,y \ge 0)$, then if we change it to standard form, we have the following conflicting expressions:
		- $x+y \le 1$
		- $-(x+y) \le 3$
	- We can't always check $(0,0)$
- Primal is Unbounded -> Dual is Infeasible
- Primal is Infeasible -> Dual is Unbounded OR Infeasible
- Primal is Bounded -> Dual is Bounded AND Feasible
- Dual of Dual is the Primal
- LP's cannot be Infeasible AND Bounded.

## Optimal Solution Example
- $\max 5x+3y$
- s.t.
	- $5x - 2y \ge 0$
	- $x+y \le 7$
	- $x \le 5$
	- $x, y \ge 0$

## Max Flow as LP
![[Pasted image 20260412153326.png]]

![[Pasted image 20260412153443.png]]

## Graph Transformation Ideas (NP Proofs)
- Transforming each vertex/edge
- Duplicate the original graph
- Add a structure to every existing vertex.
	- Bowtie -> clique to every vertex
	- The kite problem -> add a tail to every vertex
- Create a "complement" graph
	- $\overline{G}$
	- Clique and IS are complements of each other
- Be mindful to remember the budget/target.

## Graph Transformation Pitfalls
- Attempting to find the structure in the graph, where finding that structure is NP-Complete.
- Adding edges to every vertex, which may break the induced subgraph
- Forgetting the budget and/or target
- Pseudo-polynomial runtimes that reference the budget or target. If you use $O(g^2)$, make sure to assert $g \le n$.
- Removing added vertices. Example, in the Bowtie problem, the original G may have contained a bowtie. Removing all added vertices doesn't necessarily mean you've converted the bowtie solution to a clique. Make sure the output matches the output for the NP-Complete problem.

## SAT Transformation Ideas
- $(A)$ - Add a unit clause
- $(A \vee \overline{A})$ - Add a tautology.
- "Exactly one of A or B" - $(A \vee B)(\overline{A} \vee \overline{B})$
- "At most one of A or B" - $(\overline{A} \vee \overline{B})$
- "At least one of A or B" - $(A \vee B)$

## SAT Transformation Pitfalls
- Cannot add true/false constants
- Need to maintain CNF
- Variables do not exist in the boolean formula (they're called literals)
- Literals do not exist in the satisfying assignment (they're variables)

## 3SAT Verification Runtime
- $\le 3$ literals per clause
- We can lookup variable assignment in $O(1)$
- There are $m$ clauses.
- We need at most 3 lookups per clause
- $O(3m) = O(m)$

The SAT runtime require $O(nm)$ runtime, since we don't have a restriction on the number of literals per clause, apart from the number of variables ($n$) in the problem.

## Set Transformations
- Create the equivalent sets (e.g. Homework 10)
- Watch out for set membership checks ($O(n)$)
- "Don't worry about optimizing everything with boolean arrays"
- Watch for terms $n$ and $m$. Use $|S|$, $|V|$, $|D|$, etc.

