---
tags:
  - OMSCS
  - Algorithms
---
# 2026-03-11 - Office Hours with Dr. Brito
## Solution 1 to HW
We can modify Dijkstra such that we track the size of the largest/smallest edge on the path so far, instead of the total 

This runs in $O((n+m) \space log \space n)$.

We can't modify the black-box algorithms in this course. Therefore, this solution is off-limits. The point was the force the actual solution, which involves Prim's and/or Kruskal's.

[[04.0.1 - Graphs - Black Box Algorithms]]

## Solution 2
- $m=min\space\{w(e):e \in P\}$
- $M=min \space\{w(e) : e \in P\}$

We want the path from $s$ to $t$ with the largest "smallest edge".

- Let $G_d=(V,E_d)$
- $E_d = \{e \in E : w(e) \ge d\}$

- For $d : M \rightarrow m:$
	- Explore($G_d, s)$
- Stop when we find the first time that $t$ is visited!

This outputs the correct result. We iterate backwards through edges in order of weight. Once we add enough edges to $G_d$ such that there is a path from $s$ to $t$, then that path maximizes the minimum weight of all edges from $s$ to $t$. This algorithm is $O((n+m)(M-m))$.

If we binary search over $(M, ..., m)$, then we can get this down to $O((n+m) \space log \space M)$

## Solution 3
"Maximum Spanning Tree"