---
tags:
  - OMSCS
  - NS
---
# Chapter 02 - Graph Theory
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

### Connectedness
> If the network has disconnected components, the adjacency matrix can be rearranged into a block diagonal form, such that all nonzero elements of the matrix are contained in square blocks along the diagonal of the matrix and all other elements are zero.

![[Pasted image 20240520162142.png]]

We can find if a network is fully connected using BFS

### Clustering Coefficient
- For a node $i$ with degree $k_i$, the local clustering coefficient is defined as $C_i=\frac{2L_i}{k_i(k_i-1)}$
	- $L_i$ is the number of links between the $k_i$ neighbors of node $i$
	- $\langle C \rangle$ would be the average C over the whole network

![[Pasted image 20240520162420.png]]
