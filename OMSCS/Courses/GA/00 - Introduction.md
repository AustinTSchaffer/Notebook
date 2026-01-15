---
tags:
  - OMSCS
  - Algorithms
---
# 00 - Introduction

Course Outline
- Dynamic Programming
- Randomized Algorithms
- Divide and Conquer (Incl FFT)
- Graph Algorithms
	- DFS
		- 2-stat problem
		- pagerank
- Max-Flow
- Linear Programming
- NP-Completeness
	- Computational Complexity

## Big O

From DPV:
> Let $f(n)$ and $g(n)$ be functions from positive integers to positive reals. We say $f=O(g)$ (which means that "$f$ grows no faster than $g$") if there is a constant $c>0$ such that $f(n) \le c \cdot g(n)$. 

Note that $c$ must also be finite, meaning $c<\infty$. More generalized definitions also specify that this bounding applies for all $n \ge n_0$, where $n_0$ is some positive constant.

Other useful rules:
1. Multiplicative (or equivalent) constants are omitted.
2. Higher-order polynomials dominate lower-order polynomials.
3. Any exponential dominates any polynomial.
4. Any polynomial dominates any logarithm.

### Guaranteed vs. Average
Some runtimes are expressed in terms of amortized or average $O(\cdot)$ runtime. This course is only concerned about the deterministic, guaranteed runtime.

This carries important implications. Uniform generalized hash tables are often cited as $O(1)$ amortized runtime for operations, though they have theoretical $O(n)$ guaranteed deterministic runtime.

## Big-O Simplification
### What is "Fastest"?
The fastest $O(\cdot)$ runtime is the fastest accurate runtime expressed as a guaranteed (i.e. deterministic), asymptotic upper-bound proportional to the size of the input. Some sources such as _Algorithm Design_ describe this as the _tightest_ upper-bound for the given algorithm.
### Multiple Inputs
When we talk about a "worst case" runtime for a particular algorithm, we are describing its $O(\cdot)$ for _fixed_ inputs. At the same time, they are arbitrary, meaning we only know the inputs meet any given constraints. By discussing arbitrary inputs, we can make assertions that hold no matter what the input is to the algorithm. For example, some constraint $m<n$ does _not_ support an assertion that $m=n-1$ since that would necessarily create a grown correlation that does not exist. It's important to recognize that $O(\cdot)$ never describes the exact growth rate of a function, nor the exact relative growth rate of multiple functions.

The classic runtime for Depth First Search (DFS) is $O(n+m)$ because in the general case, it's unknown if the number of vertices dominates the number of edges or vice versa.

## Graphs
- **Simple Graph:** A graph with no self-edges and no parallel edges.
	- In undirected graphs, parallel edges use the same 2 vertices. In directed graphs, parallel edges have the same source and target vertex. $(u,v)$ and $(v,u)$ are not parallel in a directed graph.
	- Note that while graphs are commonly expressed in ordered pair notation as $G=(V,E)$ where $V$ is the set of vertices and $E$ is the set of edges, they are generally expressed as a combined adjacency list structure.
	- The size of the graph is often expressed in terms of $|V|=n$ for vertices and $|E|=m$ for edges.
- **Subgraph:** Formally, some graph $G'=(V',E')$ of a graph $G=(V,E)$ such that $V' \subseteq V$ and $E' \subseteq E$.
- **Path:** A sequence of vertices connected by edges in a graph with no repeated edges. All paths are assumed to be _simple_ paths which further do not contain repeated vertices.
- **Walk:** A sequence of vertices connected by edges in a graph which may repeat vertices.
- **Cycle:** A simple path with at least one edge with the same first and last vertices. In an undirected graph, the smallest cycle has 3 vertices. In a directed graph, 2 vertices.
- **Connected Graph:** A graph where there is some path $u \rightsquigarrow v$, $v \rightsquigarrow u$, or both, between any pair of vertices $u,v \in V$. This applies to both directed and undirected graphs. The permissiveness of this definition is often referred to as a "weakly connected graph" in DiGraphs.
- **Strongly Connected Graph:** A directed graph where there is some path $u \rightsquigarrow v$ and some path $v \rightsquigarrow u$ between every pair of vertices $u,v \in V$.
- **Tree:** An undirected, connected, acyclic graph.
- **Spanning Tree:** A tree with all $|V|$ vertices in the graph. Also has these properties.
	- **Induced Subgraph:** A set of vertices $S$ such that when induced on some graph $G=(V,E)$, $S \subseteq V$ forms a subgraph containing all edges in $E$ which connect two vertices in $S$. The induced subgraph must contain all edges $E' \subseteq E$ which are between vertices in $S$.
	- **Isomorphic Graphs:** Given two graph $G$ and $H$, there is a 1-to-1 equivalent structure for each vertex and edge between the graphs.
	- **Bipartite Graph:** A graph whose vertices can be divided into 2 discrete sets such that all edges connect a vertex in one set with a vertex in the other set. ![[Pasted image 20260114205815.png]]
- **Degree:** The number of incident edges on a given vertex in an undirected graph. In a directed graph, this is sometimes separated into "indegree" and "outdegree".
- **Vertex Disjoint:** Two or more paths or cycles which do not share any common vertices.
- **Edge Disjoint:** Two or more paths or cycles which do not share any common edges.
## Math Properties
### Properties of Exponents
Relation with Logarithms
$$log_aN=x \space\space\space\space a^x=N$$

Properties of Exponents

| $$a^x \cdot a^y = a^{x+y}$$ | $$(a^x)^y=a^{x \cdot y}$$                      | $$a^{x^y}=a^{(x^y)}$$      |
| --------------------------- | ---------------------------------------------- | -------------------------- |
| $$\frac{a^x}{a^y}=a^{x-y}$$ | $$\frac{a^x}{b^x}=\left(\frac{a}{b}\right)^x$$ | $$a^x \cdot b^x = (ab)^x$$ |
| $$a^{(x/y)}=(a^{(1/y)})^x$$ | $$a^0=1$$                                      | $$a^{-b}=\frac{1}{a^b}$$   |

### Properties of Logarithms
Relation with Exponents
$$log_aN=x \space\space\space\space a^x=N$$

Properties of Logarithms

| $$log_a(a)=1$$ where $a>0,a \ne 1$  | $$log_{c}(ab)=log_{c}(a)+log_{c}(b)$$ | $$log_{c}\left(\frac{a}{b}\right)=log_{c}(a)-log_{c}(b)$$       |
| ----------------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| $$log_{c}(a^b)=b \cdot log_{c}(a)$$ | $$a^{log_{a}(N)}=N$$                  | $$log_{b}(a)=\frac{log_c(a)}{log_c(b)}$$ where $c > 0, c \ne 1$ |
