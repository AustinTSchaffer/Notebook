---
tags:
  - OMSCS
  - AI
---
# Module 01 - Search
[[AIMA - Chapter 3 - Solving Problems by Searching]]
## Notes from Korf Paper
This paper explores different heuristics and their effectiveness on allowing an informed search algorithm to find the optimal solution for solving a Rubik's cube with the fewest number of moves. This paper appears to predate the 20-move proof (aka "god's number").

The core search algorithm is IDA*. Initially they tried using manhattan distance (with some tricks to ensure admissibility) as their heuristic, but that was not sufficient for the hardware that they were using. The heuristic that they ended up using was:

```
h(s) = max(
   pattern_db_8_corners(s),
   pattern_db_6_edges_group_1(s),
   pattern_db_6_edges_group_2(s),
)
```

The pattern DBs were prepopulated with the number of moves required to orient simplified versions of the puzzle. 

From here, they generated all possible valid orientations of each corner piece. For each of those initial states, they solved the puzzle only caring about the positions of the corner pieces using a BFS, saving that number of moves for the given initial state. They did the same for 2 disjoint groups of 6 edge pieces. They did not really go into why they didn't just put all 12 edges into the same pattern DB, though I assume it was due to memory limitations.

> We can improve this heuristic by considering the edge cubies as well. The numb er of possible combinations for six of the twelve edge cubies is $12!/6!*2^6 = 42,577,920$. \[...\]. At four bits per entry, this table requires 21,288,960 bytes, or 20 megabytes. A table for seven edge cubies would require 244 megabytes of memory.

This paper was from 1997.

Important to note as well that the authors "locked" the center pieces in place. Effectively, the agent always oriented the cube such that the same color always "faced the camera" and the same color always "faced the ceiling". They also did not attempt to read in arbitrary Rubik's cube states as input, so there was no need to validate that the initial state was solvable (though re: "12 subgraphs" from earlier, unsolvable initial conditions would simply not exist in the pattern DBs). Their tests were run against solved cube states after making 100 random moves.

More notes on pattern DBs in the Chapter 3 notes from AIMA: [[AIMA - Chapter 3 - Solving Problems by Searching]].

### "12 separate but isomorphic subgraphs"
Another thing I found interesting in this paper, not related to the methods they used, was the note about there being 12 disconnected subgraphs within the state space of all Rubik's cubes.

> \[...\] the entire problem space consists of 12 separate but isomorphic subgraphs, with no legal moves between them.

It's an interesting thought experiment (to me at least) to try and figure out how to produce a single state for each of those 12 subgraphs, starting from a solved cube. Obviously the solved cube belongs to the "canonical" subgraph, i.e. the subgraph which contains a solved Rubik's cube. You can get another by rotating a single corner piece in-place, as it's impossible to solve a Rubik's cube if the corners are individually rotated some number of times which is not a multiple of 3 (see "orienting the last layer" in the beginner's method). I don't know if that results in 2 additional subgraphs, as I'm not sure what the paper authors mean by "isomorphic". It's possible that rotating a single piece once results in a new state, but rotating it twice gives you two states which are equivalent.

Anyways, from here, I think you can follow a similar process by rotating different combinations of corner pieces and edge pieces, such that you end up with a new state which cannot be solved, and is not isomorphically equivalent to a state that you've already generated.

## Challenge 1: Tri-City Search (Tri-Cities Problem)
- Problem
	- 3 locations need to be visited
	- Start from one of the locations (can choose start)
	- Visit all 3 locations (order not specified)
- Solution
	- Need to start from each of the three points simultaneously
	- This is called a tri-directional A* search.
	- Start at all 3 nodes
	- Keep adding nodes to the frontier/explored data structures until 2 of the frontiers meet
	- Keep going until the 3rd node meets with one of the 2 
- BFS and Uniform-Cost Search
	- Both methods would find shortest paths, but would visit nodes multiple times

## Challenge 2: Rubik's Cube
- Iterative Deepening A* (IDA*) is still the best algorithm for solving rubik's cubes

## Definition of a Problem
- initial state $s_0$
- $actions(state) \rightarrow \{ a_1, a_2, ..., a_n \}$
- $result(s, a) \rightarrow s'$
- $GoalTest(s) \rightarrow T|F$
- $PathCost(s_0 \rightarrow^{a_0} s_1 \rightarrow^{a_1} s_2) \rightarrow n$
- $StepCost(s, a, s') \rightarrow n$
- $PathCost$ is defined as the sum over $StepCost$

## Components of a Graph Search
- Frontier - consists of states which are the furthest out of what's been explored
- Explored - consists of states which have not yet been fully expanded
- Unexplored - consists of states which have not yet been reached

## Tree Search
family of functions with the general definition:

```
func TreeSearch(problem):
  frontier = {Initial}
  loop:
    if not frontier: return FAIL
    path = remove_choice(frontier)
    s = path.end
    if goaltest(s): return path
    for a in actions(path):
      frontier.add(result(path, a))
```

Different definitions for `remove_choice` result in differently behaving searches.

This search only works on DAGs. We need to keep track of explored nodes.

## Graph Search
family of functions with the general definition:

```
func GraphSearch(problem):
  frontier = {Initial}
  explored = {}
  loop:
    if not frontier: return FAIL
    path = remove_choice(frontier)
    s = path.end
    explored.add(s)
    if goaltest(s): return path
    for a in actions(path):
      frontier.add(result(path, a))
```

- BFS: frontier is a queue, remove_choice takes head of queue
- DFS: frontier is a stack, remove_choice takes top of stack
- Cheapest-First / Uniform-Cost / Dijkstra: Take path with lowest total cost so far
- Greedy Best-First Search: Take path with lowest estimated remaining cost
- A*: Take path with lowest (total cost so far plus the estimated remaining cost)

## Uniform Cost Search
- start at start state
- expanding out from there looking at different paths
- expands in terms of "contours", similar to a topographical map
- contours of similar "height" contain nodes that take the same cost to reach
- note that this is essentially a BFS, inefficient if you have a heuristic of any kind

## A*
- $f(n) = g(n) + h(n)$
- g - total cost so far
- h - estimated remaining cost
- will find the lowest cost path if $h(s) \le C^*(s, goal)$
- AKA if $h$ is "optimistic"
- AKA if $h$ is "admissible"

## Complicated Vacuum World State Space
![[Pasted image 20240108215251.png]]

- 1 robot
	- 3 power options
	- 2 camera options
	- 5 brush height options
	- 10 positions
- 10 positions
	- 2 dirtiness level options

> answer is a cross product

$StateSpaceSize = 3*2*5*10*2^{10} = 307,200$

## AI-Generated Heuristics
The 15-puzzle's problem description:
> A block can move A->B if (A adjacent to B) and (B is blank). The puzzle is solved when all pieces are in the right place.


Simplified puzzle variants
1. A block can move A->B if ~~(A adjacent to B) and~~ (B is blank)...
	1. $C^*$ is the number of misplaced blocks, + 1 if the open spot is currently in the right place.
2. A block can move A->B if (A adjacent to B) ~~and (B is blank)~~...
	1. $C^*$ is the manhattan distance of each block to where it belongs.
3. A block can move A->B ~~if (A adjacent to B) and (B is blank)~~...
	1. $C^*$ is the number of misplaced blocks.
4. ... The puzzle is solved. ...
	1. $C^*=0$

> Adding new operators only makes the problem easier, which means $C^*$ in simplified versions of a problem is always an admissible heuristic in the real problem.

## Problem solving with search works when...
- Initial state must be fully observable.
- All available actions from each state must be known.
- The number of actions from each state must be discrete/finite.
- All actions must be deterministic.
- Search space must be static, only the agent can affect the state

## Algorithm Implementations
- Algorithms talk about paths
- Implementations should talk about "nodes"

```
class Node:
  state: T1
  action: T2
  cost: int
  parent: Node?
```

- 2 data structures operate on nodes
	- Frontier: Queue, Stack, PQ, Tree, Hashtable
		- Remove best/next/random item
		- Add new item.
	- Explored: Single set, hash table
		- Add new members.
		- Check membership.
		- Optional: Prune nodes that the frontier will never see again.

## Additional Readings
- [[Korf_-_Finding_Optimal_Solutions_to_Rubiks_Cube_Using_Pattern_Databases.pdf]]
- [[Goldberg-Harrelson-computing-the-shortest-path.pdf]]
- [[Gutman-reach-based-routing.pdf]]