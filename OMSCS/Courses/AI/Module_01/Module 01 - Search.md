---
tags:
  - OMSCS
  - AI
---
# Module 01 - Search

## Notes from Korf Paper
This paper explores different heuristics and their effectiveness on allowing an informed search algorithm to find the optimal solution for solving a Rubik's cube with the fewest number of moves. This paper appears to predate the 20-move proof (aka "god's number"). The core search algorithm is IDA*. Initially they tried using manhattan distance (with some tricks to ensure admissibility) as their heuristic, but that was not sufficient for the hardware that they were using. The heuristic that they ended up using was:

```
max(
   pattern_db_8_corners(n),
   pattern_db_6_edges_group_1(n),
   pattern_db_6_edges_group_2(n),
)
```

More notes on pattern DBs in the Chapter 3 notes from AIMA: [[AIMA - Chapter 3]].

Another thing I found interesting in this paper, not related to the methods they used, was the note about there being 12 disconnected subgraphs within the state space of all Rubik's cubes.

> \[...\] the entire problem space consists of 12 separate but isomorphic subgraphs, with no legal moves between them.

It's an interesting thought experiment (to me at least) to try and figure out how to produce a single state for each of those 12 subgraphs, starting from a solved cube. Obviously the solved cube belongs to the "canonical" subgraph, i.e. the subgraph which contains a solved Rubik's cube. You can get another by rotating a single corner piece in-place, as it's impossible to solve a Rubik's cube if the corners are individually rotated some number of times which is not a multiple of 3 (see "orienting the last layer" in the beginner's method). I don't know if that results in 2 additional subgraphs, as I'm not sure what the paper authors mean by "isomorphic". It's possible that rotating a single piece once results in a new state, but rotating it twice gives you two states which are equivalent.

Anyways, from here, I think you can follow a similar process by rotating different combinations of corner pieces and edge pieces, such that you end up with a new state which cannot be solved, and is not isomorphically equivalent to a state that you've already generated.