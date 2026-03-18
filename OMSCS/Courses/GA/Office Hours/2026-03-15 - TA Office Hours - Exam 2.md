---
tags:
  - OMSCS
  - Algorithms
---
# 2026-03-15 - TA Office Hours - Exam 2
This OH covers the following strategies, outlined below. It also covers the following practice problems:
- [[4.3 - Squares]]
- [[5.9 - Properties of Weighted Undirected Graphs]]
- [[7.22 - Fast Max-Flow Recomputation (TODO)]]
- [[7.24 - Direct Bipartite Matching (TODO)]]

## Graph Strategies
- Check for connectivity with BFS or DFS
- Create DAGs using SCC
- Traversing metagraphs/DAGs in toposort order
	- In-degree / out-degree calculation
	- Forward propagation of information
- Removing edges before/after graph algorithm executions
- Isolating subgraphs first
- Add a new auxiliary "super-source" or "super-sink" vertex

## MST Strategies
- Remove edges(s) then run MST
- Change weights to avoid/deprioritize edges
- Change weights to choose/priorities edges
- Create partial MSTs for the next steps
- Use MST properties in justification to support algorithm
	- Correct: "The chosen edge must be in the MST due to the Cut Property."
	- Incorrect: "The algorithm is correct due to the Cut Property".
- **Don't** rebuild the entire MST if/when you don't need to.
	- [[5.22 - Fast MST Recomputation]]
	- [[5.23 - Light Spanning Trees]]

## Max-Flow Strategies
- Convert to flow network
	- [[7.3 - Cargo Plane (TODO)]]
	- Adding new source and sink
- Updating capacities
	- infinite capacity
	- Additional constraints
- Adding nodes/edges to change flow
- Create and manipulate residual graph
- What do we do about anti-parallel edges?
