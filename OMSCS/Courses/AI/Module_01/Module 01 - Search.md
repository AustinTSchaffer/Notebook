---
tags:
  - OMSCS
  - AI
---
# Module 01 - Search

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

More notes on pattern DBs in the Chapter 3 notes from AIMA: [[AIMA - Chapter 3]].

### "12 separate but isomorphic subgraphs"
Another thing I found interesting in this paper, not related to the methods they used, was the note about there being 12 disconnected subgraphs within the state space of all Rubik's cubes.

> \[...\] the entire problem space consists of 12 separate but isomorphic subgraphs, with no legal moves between them.

It's an interesting thought experiment (to me at least) to try and figure out how to produce a single state for each of those 12 subgraphs, starting from a solved cube. Obviously the solved cube belongs to the "canonical" subgraph, i.e. the subgraph which contains a solved Rubik's cube. You can get another by rotating a single corner piece in-place, as it's impossible to solve a Rubik's cube if the corners are individually rotated some number of times which is not a multiple of 3 (see "orienting the last layer" in the beginner's method). I don't know if that results in 2 additional subgraphs, as I'm not sure what the paper authors mean by "isomorphic". It's possible that rotating a single piece once results in a new state, but rotating it twice gives you two states which are equivalent.

Anyways, from here, I think you can follow a similar process by rotating different combinations of corner pieces and edge pieces, such that you end up with a new state which cannot be solved, and is not isomorphically equivalent to a state that you've already generated.

