---
tags:
  - OMSCS
  - Algorithms
---
# 00 - Introduction

## Course Textbook
> *Algorithms*
> Authors: S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani
> Copyright 2006
> Published July 18, 2006

Referred to colloquially as \[DPV\].

## Course Outline
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

## Properties of Exponents

### Relation with Logarithms
$$log_aN=x \space\space\space\space a^x=N$$

### Properties of Exponents

| $$a^x \cdot a^y = a^{x+y}$$ | $$(a^x)^y=a^{x \cdot y}$$                      | $$a^{x^y}=a^{(x^y)}$$      |
| --------------------------- | ---------------------------------------------- | -------------------------- |
| $$\frac{a^x}{a^y}=a^{x-y}$$ | $$\frac{a^x}{b^x}=\left(\frac{a}{b}\right)^x$$ | $$a^x \cdot b^x = (ab)^x$$ |
| $$a^{(x/y)}=(a^{(1/y)})^x$$ | $$a^0=1$$                                      | $$a^{-b}=\frac{1}{a^b}$$   |

## Properties of Logarithms

### Relation with Exponents
$$log_aN=x \space\space\space\space a^x=N$$

### Properties of Logarithms

| $$log_a(a)=1$$ where $a>0,a \ne 1$     | $$log_{c}(ab)=log_{c}(a)+log_{c}(b)$$ | $$log_{c}\left(\frac{a}{b}\right)=log_{c}(a)-log_{c}(b)$$       |
| -------------------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| $$log_{c}(a^b)=b \cdot log_{c}(a)$$    | $$a^{log_{a}(N)}=N$$                  | $$log_{b}(a)=\frac{log_c(a)}{log_c(b)}$$ where $c > 0, c \ne 1$ |
| $$log_a^b(x)=\left(log_a(x)\right)^b$$ |                                       |                                                                 |

## Sequences
A _sequence_ is an ordered list of elements. For example, $A=a_1, a_2, ..., a_n$. In this case, we have a sequence of a known length $n$. By mathematical convention, the indexing starts at 1 unless specified otherwise.

A _subsequence_ is some ordered subset of indices from a sequence, containing =at most the full sequence. For example, $a_2, a_4, a_6$.

### Contiguous
A _contiguous subsequence_ is some ordered and consecutive subset of indices from a sequence, For example, $a_2, a_3, a_4$ is a contiguous subsequence. $a_2, a_4, a_6$ is not.

The lectures use a few more specialized terms for contiguous subsequence.
- A _string_ is a sequence of lexicographic values.
- A _substring_ is a contiguous subsequence of a string.
- A _subarray_ is a contiguous subsequence of an array.

### Monotonic
A sequence $A=a_1, a_2, ..., a_n$ is
- _monotonically increasing_ when $a_i \le a_{i+1}$ for all $1 \le i \lt n$
- _monotonically decreasing_ when $a_i \ge a_{i+1}$ for all $1 \le i \lt n$

When a sequence is described as increasing or decreasing with no additional qualifiers, it is implied to be monotonic.

### Strict
A sequence $A=a_1, a_2, ..., a_n$ is
- _strictly increasing_ when $a_i \lt a_{i+1}$ for all $1 \le i \lt n$
- _strictly decreasing_ when $a_i \gt a_{i+1}$ for all $1 \le i \lt n$

## Series
A series is the sum of a sequence, $a_1 + a_2 + \space ... \space + a_n$

### First $n$ Natural Numbers
There is a special series for the first $n$ natural numbers such that $1 + 2 + \space ... \space + n = \frac{n(n+1)}{2}$. This has common application because indices are always expressed as $n$ natural numbers.

### Geometric Series
This is a series where each element in the series is multiplied by a common ratio. Expressed mathematically:
$$\sum^{n}_{k=0}ax^k=a+ax+ax^2+\space ... \space ax^n$$
This has the known solution for $x>1$:
$$\sum^{n}_{k=0}ax^k=\frac{a(x^{n+1}-1)}{x-1}$$
When $x=1$, the series becomes the arithmetic series:
$$\sum^{n}_{k=0}ax^k=\sum^{n}_{k=0}a=a(n+1)$$
When $x \lt 1$, the infinite series converges as $n$ goes to infinity
$$\lim_{n \rightarrow \infty}\sum^{n}_{k=0}ax^k=\frac{a}{1-x}$$
## Sets
A _set_ is a collection of distinct elements. A _subset_ is a collection of elements that are also members of some set. Note that subsets have inclusive implications. **All** elements which meet the subset properties must be included.

### Cardinality
The number of elements in a set is represented with cardinality notation. For some set $S$, the size of that set is represented as $|S|$.

### Operations
Let $S$, $T$ represent some sets.
- Adding one element: $O(|S|)$. This is the time to add an element into the set.
- Finding or removing one element: $O(|S|)$. This is the time to iterate the unordered set.
- Finding the cardinality of a set: $O(|S|)$. This is the time to iterate and count the elements in the set.
- Find the union $S \cup T$ containing all elements in $S$ or $T$: $O(|S|)$. This is inserting all elements in $S$ to $T$.
- Find the intersection $S \cap T$ containing all elements in both $S$ and $T$: $O(|S| * |T|)$. This requires a pairwise comparison between all elements in $S$ and $T$.

## Constrained Optimization Expressions
These take the general form
$$\text{operator } \{ \text{ function} : \text{conditional } \}$$
As an example:
$$max \space \{ x_i : x_i < 1000 \}$$
The runtime of each of these is assumed to scale proportionally to the size of its inputs. This also includes evaluating a constant number of inputs in $O(1)$.

### Bounds
Bounds can be properly specified inside or outside the operator. For example:
$$L(i)=1+max\{L(j):a_j<a_i, \space 1 \le j \lt i\} \text{ where }1 \le i \le n$$
Another correct variation:
$$L(i)=1+max\{L(j):a_j<a_i \} \text{ where }1 \le j \lt i \le n$$

### Null Set
In the lectures, there are several instances of expressions which cannot satisfy the conditional for the given indices. In these cases, the expression will evaluate to 0 to complete the recurrence.

For example, the recurrence relation for the Longest Increasing Subsequence (LIS):
$$L(i)=1+max\{L(j):a_j<a_i, \space 1 \le j \lt i\} \text{ where }1 \le i \le n$$

At $i=1$, we get $L(1)=1+0=1$, because there is no satisfying value for $j$ with the given inequality: $1 \le j \lt 1$.

## Combinations
The general formula is:
$$\binom{n}{k}=\frac{n!}{k!\cdot(n-k)!}$$
This is most often applied for $k$ as some constant. For a constant $k$, we get a the general simplification: $\binom{n}{k}=O(n^k)$

## First Order Logic
### Boolean Formula
This is an expression of propositional logic consisting of clauses and variables. Each variable is represented in the boolean formula by literals. For example, boolean formula $f=(x) \wedge (\neg y)$ consists of 2 unique clauses and 2 variables $(x, y)$ where $x$ is a positive literal and $\neg y$ is a negative literal. Other valid representations of a negative literal include $\bar{y}$, $\sim{y}$, and $!y$.

### Satisfying Assignment
This is some boolean assignment of True and Fale values to each of the variables in the boolean formula. In order for all clauses in the boolean formula $f=(x) \wedge (\neg y)$ to evaluate to True, we would use the satisfying assignment $\{x=T,y=F\}$.

See the Satisfying Assignment example below. A "satisfying assignment" is essentially just a projection of a truth-table including only the parameter variables and only the rows for which the boolean expression evaluates to True.

| $z$     | $y$     | $x$     | $(x \vee y) \wedge (\neg{y} \vee z)$ |
| ------- | ------- | ------- | ------------------------------------ |
| F       | F       | F       | F                                    |
| ***F***   | ***F***   | ***T***   | ***T***                                |
| F       | T       | F       | F                                    |
| F       | T       | T       | F                                    |
| T       | F       | F       | F                                    |
| ***T*** | ***F*** | ***T*** | ***T***                              |
| ***T*** | ***T*** | ***F*** | ***T***                              |
| ***T*** | ***T*** | ***T*** | ***T***                              |

### Conjunctive Normal Form
A conjunction of clauses forming a boolean expression. Normal form implies that all clauses are joined by conjunctions ($\wedge$) and the literals within each clause are joined by disjunctions ($\vee$).

### Unit Clause
A clause containing a single literal.

### Tautology
A propositional expression which necessarily evaluates to true. $(x \vee \neg x)=T$ .

### Contrapositive
Logically-equivalent form of an implication. For example, $(A \Rightarrow B) \equiv (\neg B \Rightarrow \neg A)$

### Converse
The reverse of an implication. For example, the converse of $A \Rightarrow B$ is $B \Rightarrow A$.