---
tags:
  - OMSCS
  - AI
---
# L02 - Relevant Concepts From Graph Theory

## Overview
- review concepts from graph theory and linear algebra
- review basic graph algorithms
- relate concepts to real-world networks

## Notes from Chapter 2
http://networksciencebook.com/chapter/2

- Famous problem, the Bridges of Königsberg (1735)
- Euler solved it by making an abstract representation of the map, and showing that no routes traversed all bridges uniquely
- Later a new bridge was added which made the problem solvable

> A walking path that goes through all bridges can have only one starting and one end point. Thus such a path cannot exist on a graph that has more than two nodes with an odd number of links. The Königsberg graph had four nodes with an odd number of links, A, B, C, and D, so no path could satisfy the problem.

- "digraph" = "directed graph"

### Degree

- Degree
	- A key property of each node is its "degree", representing the number of links it has to other nodes.
	- $k_i$ is the degree of node $i$
	- In an undirected graph, the total number of links $L$ can be expressed as the sum of node degrees, dividing by 2 to remove duplicates: $L=\frac{1}{2}\sum_{i=1}^{N}k_i$
	- In directed graph, we distinguish between "incoming degree" $k_i^{in}$ and  "outgoing degree" $k_i^{out}$. The node's total degree is $k_i = k_i^{in} + k_i^{out}$
- Average Degree
	- The average degree of the network's node's is the network's average degree
- Degree Distribution
	- the degree distribution $p_k$ provides the probability that a randomly selected node in the network has degree $k$
	- bell curve science
	- For a network with $N$ nodes, the degree distribution is the normalized histogram: $p_k=\frac{N_k}{N}$

### Adjacency matrix
- Model directed/undirected networks using a matrix of size $N \times N$.
- The degree of a node in an undirected network can be obtained by summing a row or column
- The degree of a node in a directed network can be obtained by summing the row and column corresponding to the node.

![[Pasted image 20240520160420.png]]

- real networks are sparse
- The max number of links in a network is given by $L_{max}=\frac{N(N-1)}{2}$
- In real networks, $L<<L_{max}$
- Adjacency matrices become less practical as $N$ increases

### Weighted networks
 - in many applications, links have independent weights ($w_{ij}$)
 - can't always measure the appropriate weights
 - often approximate weighted networks as unweighted networks

> Metcalfe's Law
>
> According to Metcalfe’s law the _cost_ of network based services increases linearly with the number of nodes (users or devices). In contrast the _benefits_ or _income_ are driven by the number of links $L_{max}$ the technology makes possible, which grows like $N^2$ according to (2.12). Hence once the number of users or devices exceeds some _critical mass_, the technology becomes profitable.

### Bipartite Networks
![[figure-2-9.jpg]]

- a bipartite graph (bigraph) is a network whos nodes can be divided into 2 disjoint sets U and V such that each link connects a U-node to a V-node
- "We can generate two projections for each bipartite network. The first projection connects two U-nodes by a link if they are linked to the same V-node in the bipartite representation. The second projection connects the V-nodes by a link if they connect to the same U-node"
- There's no U-U links and no V-V links in the actual network
- A well known bipartite network is the Hollywood actor network, where U nodes are actors and V nodes are movies.
- There's also tripartite networks, e.g. Recipes-Ingredients-Compounds

![[figure-2-11.jpg]]

### Paths and Distances
- shortest path
- network diameter - $d_{max}$ = max shortest path in the network
- $\langle d \rangle$ - average path length
- BFS is commonly used here
- UCS could/should be used in place of BFS if edges have weights/costs

## Connectedness
> If the network has disconnected components, the adjacency matrix can be rearranged into a block diagonal form, such that all nonzero elements of the matrix are contained in square blocks along the diagonal of the matrix and all other elements are zero.

![[Pasted image 20240520162142.png]]

We can find if a network is fully connected using BFS

### Clustering Coefficient
- For a node $i$ with degree $k_i$, the local clustering coefficient is defined as $C_i=\frac{2L_i}{k_i(k_i-1)}$
	- $L_i$ is the number of links between the $k_i$ neighbors of node $i$
	- $\langle C \rangle$ would be the average C over the whole network

![[Pasted image 20240520162420.png]]

## Module Notes
- Use the notation G=(V,E) to refer to a graph G with a set of vertices V and a set of edges E
	- undirected
	- unweighted
- Typically not allowed
	- edges linking a vertex to itself
	- duplicate edges between a pair of vertices

## Adjacency Matrix
- Dense graphs are can be represented by an adjacency matrix
- Useful because it allows you to use linear algebra tools for analyzing networks
- For example, the maximum node degree in a network is greater than or equal to the largest eigenvalue of its symmetric adjacency matrix.
- idk why you wouldn't just use argmax

## Adjacency List
- For undirected graphs, adjacency lists require $n+2m$ space, because every edge is included twice.
- A graph is sparse when the number of edges $m$ is is much closer to the number of node $n$ than to the max number of nodes $n(n-1)/2$.
- A graph is dense if the opposite is true.

## Walks, Paths, and Cycles
> How can we efficiently count the number of walks of length k between nodes s and t?

The number of walks of length $k$ from node $s$ to node $t$ can be retrieved by raising the network's adjacency matrix to the $k$-th power, then grabbing element $(s,t)$: $A^k_{s,t}$.

For $k=1$, the number of walks is either 1 or 0, depending on whether the nodes are directly connected or not.

## Trees and other regular networks
- tree
- $k$-regular graph, every vertex has the same degree $k$
- Complete graphs, aka "clique", every vertex is connected to every other vertex.

## Directed Graphs
- adjacency matrices are generally no longer symmetric except when every edge has an edge coming back the other direction
- nodes have an in-degree and an out-degree

## Weighted Directed Graphs
- in some cases, weights represent capacity
- in some, weights represent cost
- in undirected networks, the "strength" of a node is the sum of weights of all edges that are adjacent to that node
- for directed networks, we have in-strength and out-strength
- in signed graphs, edge weights can be negative, sometimes representing competitive interactions

## (Weakly) Connected Components
- an undirected graph is connected if there's a path between any pair of nodes
- directed graphs are "weakly connected" if the graph is connected when the direction of the edges between nodes is ignored
- directed graphs are "strongly connected" if you don't ignore edge directions
- in real networks, you often find multiple fully connected subgraphs
- BFS can find the set of nodes that are connected and include the starting node

## Strongly Connected Components
![[Pasted image 20240520190947.png]]

Linear time algorithm for determining if a directed graph is strongly connected
- run BFS from one node
- reverse all edges in the graph, then run BFS from the same node
- if either BFS iteration don't visit all nodes, then the graph is not strongly connected

Computing the set of strongly connected components in a directed graph
- Tarjan's algorithm
- Kosaraju's algorithm
- Both use DFS
- $\Theta(n+m)$ time complexity

## Directed Acyclic Graphs (DAGs)
- has a topological order
- must include at least one source node, a node with no incoming edges
	- best method for finding a source node would be to traverse the graph following edges in reverse.
- must have at least one sink node, a node with no outgoing edges

## Dijkstra’s Shortest Path Algorithm
Also called "Uniform Cost Search"

See [[Module 01 - Search]]

## Random Walks
- used for network discovery
- if you don't know the full network, but you have a way of visiting new nodes from your current node, you can discover a set of nodes that are strongly connected
- make probabilities of selecting each edge a function of the weights of each edge
- the "stationary distribution" is the probability that the walker is found on any particular node. This is found by randomly walking and recording the number of times it transitions along a particular edge
- given a transition matrix $P$ computed from the weights of the edges in the graph, you can calculate the "stationary distribution"
	- $q_{t+1}=P^Tq_t$
	- $P^T$ is the transpose of the transition matrix
	- for each iteration $t$, the $i_{th}$ element of the resulting vector $q_{t+1}$ is the probability of $i$ being the current node calculated as the probability incoming edge $(j,i)$ was taken, times the probability that the walker was at previous node $j$.
	- $P(n_{c}=i)=\sum_{j=1}^N P(edge(n_{p}=j,n_{c}=i))\times P(n_{p}=j)$
		- $N$ is the total number of nodes in the graph
		- $n_c$ is the current node
		- $n_p$ is the previous node
		- $P$ is for probability
	- Let $q$ be the stationary distribution expressed as a column vector
		- For transition matrix $P$: $P^Tq=q$
		- A transition matrix $T$ has an eigenvector $v$ if $Tv=\lambda v$ for an eigenvalue $\lambda$
		- The eigenvectors of $P^T$ are the stationary distribution expressed as column vectors where $\lambda=1$
		- This means that in undirected and connected networks, a stationary distribution always exists.

## Minimum Cut
![[Pasted image 20240520201505.png]]

The $cut(s,t)$ of a graph is a set of edges that, if cut, will separate $s$ from $t$

- In unweighted networks, the minimum cut is the fewest number of edges that need to be removed.
- In weighted networks, the minimum cut is the lowest sum of edges that need to be removed.

## Max Flow Problem
- Given a source node $s$ and a target node $t$, compute a "flow" from $s$ to $t$.
- Edge weights represent link capacity.
- Edges cannot have negative flow.
- The total flow that arrives at a non-terminal $v$ has to be equal to the total flow that departs from $v$. Only $t$ is a sink.
- Ford-Fulkerson algorithm
	- $O(mF)$
	- $m$ is the number of edges
	- $F$ is the max capacity of any edge
	- Algorithm concepts
		- constructs a residual network, which shows the residual capacity of each edge.
		- In each iteration, the algorithm finds a path from $s$ to $t$ with some residual capacity, using either BFS or DFS
		- The minimum residual on that path $f$ is subtracted from each edge's capacity along that path, and $f$ is added to the overall flow.
		- We can also add $f$ on the capacity of every reverse edge of the residual network, which can later reduce the flow along the reverse direction if needed by routing some flow on the edge.

## Max-Flow = Min-Cut
- the min-cut and max-flow results are the same value
- Any $cut(L,R)$ such that $s\in L$ and $t \in R$ has capacity $C \ge f$ where $f$ is a flow from $s$ to $t$. Therefore $mincut(s,t) \ge maxflow(s,t)$
- If $f^*=maxflow(s,t)$, the network can be partition in two sets of nodes $L$ and $R$ with $s \in L$ and $t \in R$ such that
	- all edges from L to R have $flow=capacity$
	- all edges from R to L have $flow = 0$
	- Therefore edges from L to R define a $cut(s,t)$ with $capacity=maxflow(s,t)$
	- Because of the previous part, this cut is the min-cut

## Bipartite Graphs
![[Pasted image 20240520203130.png]]

In a bipartite graph, a set of nodes V can be partitioned into two subsets, L and R, so that every edge connects a node from L and a node from R, with no edges between 2 L nodes – nor between 2 R nodes.

Apparently it's impossible to form a bipartite graph if there's an odd length cycle, which is why that's on the left side of the image above.

## A Recommendation System as a Bipartite Graph
- practical application of bipartite graphs
- user-item matrix
- [[M06B11 - Collaborative Recommendations]]
- [[Collaborative Filtering beyond the User-Item Matrix.pdf]]
- [[Week 06 - Collaborative Filtering beyond the User-Item Matrix.pdf]]
- [[M06B12 - Model-Based CF]]
- Any tables that have an A-B relationship form a Bipartite graph

## Co-citation and Bibliographic Coupling
https://gatech.instructure.com/courses/394342/pages/l2-co-citation-and-bibliographic-coupling?module_item_id=4042246

The one-mode projections can also be computed using the adj matrix $A$ that represents the bipartite graph.

- The element $(i,k)$ of $A$ is 1 if there is an edge from $i$ to $k$ and 0 otherwise.
- co-citation
	- The co-citation metric $C_{i,j}$ for nodes $i$ and $j$ is the number of nodes that have outgoing edges to both $i$ and $j$
	- If $i$ and $j$ are items, then the co-citation metric is the number of users that purchased both $i$ and $j$
- bibliographic coupling
	- The bibliographic coupling metric $B_{i,j}$ for nodes i and j is the number of nodes that receive incoming edges from both $i$ and $j$
	- if $i$ and $j$ are users, then $B$ is the number of items that have been purchased by both i and j.

![[Pasted image 20240520204818.png]]

## Knowledge Check
![[Pasted image 20240520205023.png]]

- $L_{max}=\frac{9*8}{2}=36$
- Density $=8/36=2/9$
- $\sum_i k_i = 16$

![[Pasted image 20240520205317.png]]

- 3 nodes on the left form a strongly connected component.
- 4 nodes on the right form a strongly connected component. Extending this group:
	- Add the central node
	- Add the node S of central
	- Add the node N of central
	- Add the node W of central
- 1 node at the bottom form a strongly connected component
- 3 total SCCs

![[Pasted image 20240520205512.png]]

- It's bipartite, meaning no odd-length cycles
- X-E-Y-B-X is a cycle of length 4
- B and D only have one connected node in common, making their coupling 1

![[Pasted image 20240520205750.png]]

![[Pasted image 20240520210819.png]]

Notes
- Dijkstra’s shortest path algorithm has better running time complexity than the Bellman-Ford algorithm on both **dense** and **sparse** non-negative weighted networks.
- DAGs don't have a unique topological ordering
- Adjacency matrices require fewer memory accesses compared to adjacency lists
- The node strength definition doesn't necessarily apply to graphs that have negative weights.