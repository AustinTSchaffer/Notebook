---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 3 - Solving Problems by Searching

Key terms and takeaways from the "search" chapter of "AI: A Modern Approach", 4th edition.

- Standardized Search Problem Terms
	- States
	- Initial States
	- Actions
	- Transition Model
	- Goal States
	- Action Cost
- Sokoban Puzzle: Type of puzzle where an agent pushes blocks around on a grid. Examples:
	- "Rush Hour" puzzles
	- Sliding tile puzzle
- Uses for search problems
	- Touring problems
	- Infamous Traveling Salesman Problem (TSP)
	- Bus routing
	- VLSI layout
	- Robot navigation
	- Map navigation
	- Automatic assembly sequencing
- Satisficing solution
	- When a search generates a "good enough" solution.
	- Typically happens as a result of intentionally using an inadmissible heuristic, causing the algorithm to ignore more efficient but less direct paths.
- Detour index
	- Term coined by road/civil/traffic engineers
	- Defined as a multiplier applied to the straight-line distance from point A to point B
	- Heuristic which estimates the typical curvature of a road network
	- Typically between 1.2 and 1.6
	- A detour index of 1.3 means that traversing 10 miles "as the crow flies" typically requires 13 miles of roads.

## Search Algorithms
### Key terms
- Completeness: Is it guaranteed to find a solution if one exists?
- Cost Optimality: Is it guaranteed to find the most optimal solution?
- Time Complexity
- Space Complexity
- Depth
- Branching Factor
- Search Strategies
	- Uninformed Search (BFS, DFS, etc)
	- Informed Search (A*)
### Queue types
- FIFO Queue
- LIFO (FILO) Queue (a stack)
- Priority Queue (Informed search)
### Uninformed Search Types
#### Breadth First Search
- Node frontier is a queue
#### Depth First Search
- Node frontier is a stack
- Variants include backtracking search (uses even less memory)
#### Best-First Search
- Node frontier is a PQ.
- Next frontier node chosen has the lowest value for some function $f(n)$.
- No indication on the quality of these kinds of searches, depends on $f(n)$.
#### Dijkstra's algorithm
- aka "Uniform cost search"
- Best-first search with $f(n)=path\_cost(n)$
#### Backtracking search
- Variant of DFS which uses even less memory.
- Trades memory complexity for time complexity. Regenerates a lot of nodes.
#### Depth limited search
- Only search nodes that are some distance `d` away from the start.
- Can be implemented using any algorithm.
- Raises a fault if it doesn't find the answer.
#### Iterative Deepening Search
- Keeps executing a depth-limited search, increasing the depth `d`.
#### Bidirectional Search
- Simultaneously searches from initial state(s) and from goal state(s).
- Idea being that in uninformed searches $b^d>b^{d/2}+b^{d/2}$.
- Keep track of 2 frontiers, and 2 tables of reached states.
- Need to calculate actions / node traversals in reverse from goal states.
- Solution is found when the 2 frontiers collide.

#### Useful Selection Criteria
| Criterion    | BFS      | Uniform-Cost                            | DFS      | Depth-Limited | Iterative-Deepening | Bidirectional |
| ------------ | -------- | --------------------------------------- | -------- | ------------- | ------------------- | ------------- |
| Complete?    | Yes      | Yes                                     | No       | No            | Yes                 | Yes           |
| Optimal Cost | Yes      | Yes                                     | No       | No            | Yes                 | Yes           |
| Time         | $O(b^d)$ | $O(b^{1+\lfloor{C^*/\epsilon}\rfloor})$ | $O(b^m)$ | $O(b^l)$      | $O(b^d)$            | $O(b^{d/2})$              |
| Space        | $O(b^d)$ | $O(b^{1+\lfloor{C^*/\epsilon}\rfloor})$ | $O(bm)$  | $O(bl)$       | $O(bd)$             | $O(b^{d/2})$              |

Symbols:
- $b$ - branching factor
- $d$ - solution depth
- $C^*$ - optimal solution cost
- $m$ - max depth of search tree
- $l$ - depth limit
- $\epsilon$ - minimum edge cost ($\epsilon > 0$)

### Heuristics
- denoted $h(n)$
- $h(n)$ gives the estimated cost of the cheapest path from the state at node $n$ to its nearest goal state.
- usage of a heuristic makes a search algorithm an "informed" search
- Key terms
	- Admissibility
		- an admissible heuristic never overestimates the optimal cost to a goal
		- $h(n) \le C^{*}_{n,goal}$
	- Consistency
		- a consistent heuristic follows the triangle inequality
		- $h(n) \le c(n, a, n') + h(n')$
	- ad9y vs co8y
		- Every consistent heuristic is admissible (not vice-versa)
		- Inconsistent heuristics are fine. Consistent heuristics have benefits.
		- Inadmissible heuristics are not fine. Admissible heuristics are necessary for finding $C^*$
- Monotonic
	- $g$ costs should be monotonic, i.e. always increasing.
- Pruning
	- This is when you avoid searching nodes
### Informed Search Types
#### Greedy best-first search
- only search the node with the lowest heuristic
- Best-first search with $f(n) = h(n)$
#### A* search
- best-first search with $f(n)=g(n)+h(n)$
- $g$ gives the cost so far
- $h$ gives the estimated remaining cost
- $f(n)$ gives the "estimated cost of the best path that continues from $n$ to the goal"
#### Weighted A* search
- best-first search with $f(n)=g(n)+W \times h(n)$ with $W > 1$
- Find paths which cost between $C^*$ and $W \times C^*$
- In practice, results are closer to $C^*$ than they are to $W \times C^*$
- Sometimes called a "somewhat greedy" search

| Search Strategy   | $f$ definition         | effective $W$    |
| ----------------- | ---------------------- | ---------------- |
| A*                | $g(n) + h(n)$          | 1                |
| Uniform-cost      | $g(n)$                 | 0                |
| Greedy best-first | $h(n)$                 | $\infty$         |
| Weighted A*       | $g(n) + W \times h(n)$ | $1 < W < \infty$ |

#### Other suboptimal search types
- bounded suboptimal search (weighted A*)
- bounded-cost search (total cost $\le C$ (note $C$, not $C^*$))
- unbounded cost search (any solution will do)
#### Speedy Search
- unbounded cost search
- greedy best-first search
- $h$ returns estimated number of actions required to reach goal, regardless of the cost of those actions
- same as greedy best-first when all action costs are the same
- finds crappy solutions quickly
#### memory-bounded search
- A* uses a lot of memory
- MB search places restrictions on size of queue and size of "reached" DB
- possible to prune nodes from the "reached" DB once the node is no longer reachable from the frontier (e.g. by using a ref counter)
- Some search algorithms put limits on the size of the frontier, keeping only some number of nodes based on $f$ or $h$ scores.
- possible to avoid using a reached table altogether by eliminating U-turns and redundant paths within the frontier queue/stack
#### Beam Search
- the frontier queue only keeps track of $k$ nodes that have the best $f$ scores.
- can result in incomplete/suboptimal results for low values of $k$
- Alternative implementations keep track of only the nodes that have $f$ scores within some $\delta$ of the best $f$ score so far.
#### Iterative Deepening A* (IDA*)
- Iterative Deepening search, but it uses a heuristic
- at each iteration, the cutoff value is the smallest $f$-cost of any node that exceeded the cutoff in the previous iteration
- Each iteration exhaustively searches an $f$-contour, finds a node just beyond that contour, and uses that node's $f$ cost as the next contour.
- Works great for problems that have uniform cost edges
- Can be inefficient for problems where every node has a different $f$ cost.
- Suffers from using _too little_ memory
#### Recursive Best First Search (RBFS)
- mimics the operation of standard best-first search, but has linear space complexity
- resembles a recursive DFS
- uses an $f\_limit$ and keeps track of the $f$ value of the best alternative path from any ancestor of the current node
- If the current node exceeds this limit, the recursion unwinds back to the alt path.
- RBFS then replaces the $f$-value of each nodes along the path with a backed-up value of the best $f$-value of its children.
- Effectively what's going on here is that RBFS is keeping track of the $f$-value of the best leaf in forgotten subtrees, which it can later use to decide if it's worth re-expanding those nodes.
- Somewhat more efficient than IDA*, suffers from excessive node regeneration
- Finds optimal solutions as long as $h$ is admissible, but time complexity is hard to characterize.
- Suffers from using _too little_ memory
#### Simplified Memory-bound A* (SMA*)
- Simplified version of "Memory-bounded A* (MA*)". The chapter only really covers SMA*.
- Proceeds like standard A* until "memory is full"
- Drops the "worst" leaf node based on node with highest $f$ score.
- In the case of ties, drops the oldest leaf.
- Backs up $f$ scores of each forgotten node to the node's parent, similar to RBFS
- Will regenerate forgotten subtrees in the event all other paths with lower $f$ scores are exhausted.
- Finds the optimal path if the optimal path fits in memory.
- Finds the best reachable solution otherwise.
- Fails if all paths from the initial state to any goal are larger than available memory.
- Great choice for an algorithm in cases where
	- state space is a graph
	- action costs are not uniform
	- node generation is expensive compared to the overhead of maintaining the frontier and reached set.
- On hard problems, SMA* is forced to switch back and forth continually among many candidate solution paths, of which only a subset can fit in memory (thrashing)
- If this algorithm is failing, and there's not enough memory for standard A*, and you can't decide on the tradeoffs between time and space complexity, drop the optimality requirement.
#### Bidirectional A*
- $f(n) = g(n) + h(n)$ does not guarantee optimal solutions when the search is bidirectional
- Instead, use a lower-bound equation which is based on using a PQ containing pairs of nodes: $lb(m,n)=max(g_F(m)+g_B(n),f_F(m),f_B(n))$
	- $F$ refers to $g$ and $f$ being calculated relative to heading toward the (a) goal
	- $B$ refers to $g$ and $f$ being calculated relative to heading toward the (a) initial state.
- Alternatively, use a best-first search with 2 frontiers, and take a node from either frontier queue based on whichever minimizes this $f$ score: $f_2(n)=max(2g(n), g(n)+h(n))$
- $f_2$ guarantees that that the algorithm never expands a node from either frontier with $g(n)>C^*/2$
- Sometimes BiD A* is more efficient than a unidirectional search. Sometimes not. A* with a really accurate heuristic is often good enough.
- With an average heuristic, BiD search tends to expand fewer nodes.

## Heuristic Functions
- Effective branching factor formula: $N+1=\sum^{d}_{n=0}(b^*)^n$
	- $N$ is the number of nodes expanded by the search
	- $d$ is the depth of the search
	- $b^*$ is the effective branching factor. Solve for $b^*$.
- Well designed heuristics should have a $b^*$ close to 1.
- Another good way of characterizing A* pruning is that it reduces the effective depth by a constant $k_h$ compared to the true depth. Total search cost will be $O(b^{d-k_h})$ compared to $O(b^d)$ for an uninformed search. More details in [[Korf_-_Finding_Optimal_Solutions_to_Rubiks_Cube_Using_Pattern_Databases.pdf]]
### Heuristic domination
- if 2 admissible heuristics $h_a$ and $h_b$ have the property $h_a(n) \ge h_b(n)$ for all $n$, then $h_a$ **dominates** $h_b$
- essentially $h_b$ should never be used, unless $h_a$ is super inconsistent and/or has a higher computational complexity.
### Relaxed problems
- A problem with fewer movement restrictions is called a relaxed problem
- state graph of a relaxed problem is a _supergraph_ of the state graph of a more strict problem
- Optimal solutions in a strict problem result in (usually suboptimal) solutions in the relaxed problem.
- The cost of an optimal solution in the relaxed problem is an admissible heuristic in the strict problem
- Example: taking a 9-puzzle and allowing multiple pieces to occupy the same space, means that all pieces move a manhattan distance from their location to their destinations, resulting in $\sum^{8}_{n=1}manhattan(tile_n, goal_n)$ moves in the relaxed problem, which is an admissible heuristic in the strict version where spaces can only contain one tile.
- If the relaxed problem is hard to solve, then calculating a heuristic based on that relaxed problem will also be hard.
### Aggregate heuristics
- If a collection of heuristics are all admissible and easily calculable, but it's not clear which one performs better, you can just take the max over all of them
- $h_{agg}=max(h_1(n), ..., h_k(n)$
- $h_{agg}$ dominates all of its component heuristics
- Could also use an alternative aggregation function instead of $max$, i.e. machine learning or `random.choice`
### Pattern Databases
- Admissible heuristics can be derived from solution costs of subproblems of a given problem.
- Idea of a pattern database is to store the solution costs for every possible subproblem instance for a given subproblem definition.
- The expense of doing all this pre-calculation works in your favor if you have to solve A LOT of problems in the format of the strict version of the problem.
- e.g. For a 9-puzzle, picking 4 tiles, erasing the markings on the other 4, taking all possible tile combinations and solving those problems, storing the results in a database, using those results as "patterns" for forming a heuristic for the real puzzle.
- In the 9-puzzle example, we don't care where the 4 anonymous tiles end up, but their move cost counts towards the solution cost.
- Could also construct databases for each other combination of 4 non-anonymous tiles, and could use an aggregate heuristic on top of those pattern databases. Diminishing returns unfortunately.
- If you don't count the movement of the anonymous tiles toward the total move count for each pattern, you've formed a "disjoint" pattern database. In disjoint pattern databases, you can add the solution costs for non-overlapping patterns to form better heuristics.
### Landmarks
- You can precompute distances from problem states to a few key landmarks in order to help inform future searches.
- The time/space complexity of doing so will be amortized over many routing requests.
- More time/space efficient to use landmarks than to precompute the distances between all pairs of nodes.
- One possible inadmissible heuristic would be $h(n)=min_{L \space\in\space landmarks} \space C^*(n, L)+C^*(L, goal)$
- One possible admissible heuristic would be to use a "differential heuristic"
	- $h(n)=max_{L \space\in\space landmarks} \space | C^*(n, L) - C^*(L, goal)|$
	- Provides very accurate $h$ values when $goal$ is along the most efficient path from $n$ to the best $L$.
	- Provides very low (i.e. inaccurate) $h$ values when the best $L$ is along the best path from $n$ to $goal$
- Another possible inadmissible heuristic would be effectively finding the distance from "you" to your nearest hub, and the distance from the goal to its nearest hub, then finding the distance between those 2 hubs. $h(n)=(min_{L_1 \space\in\space landmarks} \space C^*(n, L_1))+(min_{L_2 \space\in\space landmarks} \space C^*(n, L_2)) + C^*(L_1, L_2)$
	- Could be accurate over long distances.
	- There may be a differential version of this as well.
- Landmark picking strategies are important and their effectiveness very much depends on the heuristic(s) you intend to use
	- Picking landmarks based on most frequently seen nodes in user search/request history
	- Picking landmarks based on top $k$ largest cities by population
	- Picking landmarks by randomly picking a seed, generating the landmark entry for that seed, then picking landmarks that are the furthest away from the all existing landmarks.
	- Only picking landmarks that are all along the perimeter of the search area makes differential heuristics more accurate

## Metalevel Search Space
- designing AI agents which "learn" how to search better
- Each state in a metalevel search space captures the internal state of a program that is searching in an ordinary state space such as a map
- A standard search operates on an "object-level search space"

