---
tags:
  - OMSCS
  - AI
---
# Module 03 - Game Playing
Main Topics
- Adversarial Search
- Minimax Algorithm
- Alpha-Beta Pruning
- Evaluation Functions
- Isolation Game Player
- Multi-Player, Probabilistic Games

## Isolation
- NxM grid
- Player 1 places their piece anywhere on the board
- Player 2 places their piece on any remaining location on the board
- Players then move like queens, but can't pass through each other
- After moving, players leave a wall behind them that cannot be moved
- Objective is to be the last player to move

### Building a Game Tree
- using a 2x3 board
- O placement
![[Pasted image 20240125192427.png]]
- X placement
![[Pasted image 20240125192443.png]]
- Possible moves for O
![[Pasted image 20240125192642.png]]
- In most of the 2x3 isolation games, O wins.
![[Pasted image 20240125192919.png]]

How to keep the computer from making a bad opening moves?
- prerecord a table of good moves
- "best first moves table" AKA an "opening book"
- How to discover good first moves?

## Minimax Algorithm
- assume the opponent is a perfect opponent who always plays to win / maximize score
- Add a triangle pointing up whenever the agent is trying to maximize its own score ![[Pasted image 20240128184629.png]]
- Add a triangle pointing down whenever the opponent is trying to minimize the agent's score. ![[Pasted image 20240128184738.png]]
**implementation note:** the top layer of the game tree is always a "maximization level", indicating that the agent always goes first. If the agent is not going first, the game tree just starts at whatever turn when the agent makes its first move.

- start at the bottom of the tree
- propagate wins/losses/scores up the tree based on the min/max arrows
- Computer player then chooses a branch of the tree which has the highest value

![[Pasted image 20240128185100.png]]

## Max Number of Nodes
- 5x5 isolation board
- Upper limit: $25!$ nodes in the search tree
- $25! \approx 1.55 \times 10^{25}$
- If a computer can explore $10^9$ nodes per second, it would take 317 million years to explore the game tree.
- The search trees for interesting games cannot be fully explored.

### Better approximation
- Cannot have more than 25 moves in the game, search tree depth.
- After the opening moves ($25*24$ board states), there are 23 moves left
- Every state after the first move will generally have 12 or fewer moves available, branching factor
- $25*24*12^{23} > 10^{27}$
- Even better approximation: $3 \times 10^{23}$

### Average Branching Factor
- Code up a pair of random agents
- Check the branching factor at each step
- Take the average
- Thad's estimation: $b \approx 8$
- Estimate for num board states: $8^{25}$
- Still bad.

## Depth-Limited Search
- Waiting for the computer player is no fun.
- Assume some rate of nodes that can be explored per second: $r$
- Determine some duration that the human should have to wait: $d$
- Agent can search $r \times d$ nodes.
- Example: $10^9$ nodes per second, 2 seconds, $2 \times 10^9$ nodes.
- Take the branching factor $b$, and some value for search tree depth $x$
- $b^x=rd$
- Solve for $x$
- $x=log_b(rd)=\frac{log_{10}(rd)}{log_{10}(b)}$
- In the case of the 5x5 isolation board
	- estimated average branching factor of 8
	- assuming that the target hardware can process $10^9$ nodes per second, 
	- targeting a 2 second max wait time
	- our computer agent should search 10.3 levels of the game tree *at most*

## Evaluation Functions
- Can we create a function that, given a board generated at level 9 of our minimax game tree, computes a number which we can use to compare that board state to all other generated board states?
- Evaluation function should return a higher number when the game state is more beneficial to the computer player.
- Example evaluation function for games such as isolation
	- "number my moves": number of moves available to the agent at the ending board state
	- "ratio my/their moves": divide number of moves available to the agent by the number of moves available to the opponent. Set some max value for the case where the opponent lost.

![[Pasted image 20240128193405.png]]

> Is evaluation function X bad? Not necessarily. It might be that we're not searching deep enough.

### Quiescent Search
- Determine range of values that the evaluation function can search
	- Pick a value below that range for "agent lost"
	- pick a value above that range for "agent won"
- Calculate best moves based on evaluation function at depths 1, 2, 3, ...
- Keep track of the score at each move at each depth
- Keep going until the scores don't change much
- This is iterative deepening, in a sense
### Iterative Deepening
- Search the game tree at depth 1, 2, 3, ...
- At each depth, keep track of the move that gave the best answer
- If the agent runs out of time, return the best move found so far
- Theory behind iterative deepening: We're not wasting that much time by reexploring states that are higher up in the game tree, because the game tree is exponential, we're wasting WAY MORE time at the lower layers searched.
- Iterative deepening explores $<2x$ the number of nodes that a depth limited search explores at the same level.

![[Pasted image 20240128194748.png]]

- Tree nodes at depth $d$, branching factor $b$: $n=\sum_{x=0}^{d}b^x=\frac{b^{d+1}-1}{b-1}$ 
- Iterative deepening nodes at depth $d$, branching factor $b$: $n=\sum_{x=0}^{d}\sum_{y=0}^{x}b^y$. Closed form expansion is below thanks to WolframAlpha.

$$
n = \sum_{x=0}^{d}\sum_{y=0}^{x}b^y = \frac{b^{d+2}-b(d+2)+d+1}{(b-1)^2}
$$

> In games like chess, players are given an amount of time for the whole game, not individual moves. An agent may want to spend more time searching deeper in some parts of the game, and shallower in others. \[...\] We can create a strategy for how deep we want to search in certain parts of the game.

## The Horizon Effect
> A human player might see an obvious move at a pivotal part of the game that an agent cannot see because it can't see far enough into the future.

![[Pasted image 20240128202750.png]]

In the screenshot, the best move for O is to move down/left, trapping X in a smaller partition. The payoff of this move is 13 moves in the future.

The evaluation function defined earlier additionally falls apart at this part of the game. "Num my moves" encourages O to create smaller and smaller partitions for itself near the end of its search depth.

Can the evaluation function determine the size of the partition that O is in vs X is in? Making the evaluation function more complicated is not always good. More computation is equivalent to searching deeper in the tree. More computation means you won't be able to search as deep.

## Alpha-Beta Pruning
The idea is that you can propagate 2 parameters "a" and "b" down the search tree. Any 

## Reducing the Search Space
### Symmetry
Some games have reflection and rotational symmetry, just like isolation. In these kinds of games, you can be more efficient in how the tree is expanded by checking for equivalent move sequences that you've already expanded.

Taking symmetry into account cuts down on the number of nodes that you need to expand.

![[Pasted image 20240205193129.png]]

![[Pasted image 20240205193241.png]]

In this game, there's very little symmetry in the game tree after move 3 or so, so symmetry checking can be phased out as you delve deeper in the search tree.

### Partitions
You already know the result of the game once the board state has a partition.

![[Pasted image 20240205193505.png]]

### Heuristics
- In this game, if both players play optimally, player 2 always wins.
- If you're player 1, always move to the center square, then reflect player 2's moves.

## Multiplayer Games (N>2) + MAXN
For games with more than 2 players, we can abstract minimax into the "MAX N" algorithm. In MAXN, the game tree keeps track of a vector of scores for each player. At each level of the tree, the players take turns selecting the move which maximizes their own score. Evaluation function returns the vector.

![[Pasted image 20240205210905.png]]

Complications
- Some players may run out of moves before others.

## 3-Player Alpha Beta
- Works if the evaluation function has an upper and lower bound for each player.
- Some shallow pruning is possible, deep pruning is not possible.

## Expectimax
In stochastic games like backgammon, we can use an algorithm called "expectimax" to build a game tree.

## Example Stochastic Game: Sloppy Isolation

![[Pasted image 20240205211737.png]]

![[Pasted image 20240205211836.png]]

- 80% chance that a move will hit the intended square.
- 10% chance of undershooting
- 10% chance of overshooting
- For boundary conditions
	- if overshooting is beyond the edge of the board, 0% chance of overshooting
	- if undershooting is the current player's location, 0% chance of undershooting

![[Pasted image 20240205212047.png]]

- Green nodes are probability nodes.
- When propagating utility scores upward, utility scores are multiplied by probabilities at probability nodes.
- With expectimax, you can use a variant of alphabeta pruning if the evaluation function never goes negative. If it can go negative, you can't prune. If the evaluation function can go negative, but the bounds are known, you can always translate the utility function's output such that it's always positive, re-enabling pruning

## Expectimax $\alpha \space \beta$
- Works similarly to standard alpha-beta
- Effectively we need to do algebra to determine which branches are worth exploring
- In the diagram below, we can avoid exploring the right branch of the middle subtree, because the evaluation function is bounded by \[0, 10\]. The probability of that branch is 0.5, and the max value is 10, so the expected value of that branch is at most 5. We already know from the left subtree that we can get an expected value of 6.5, so that allows the agent to prune that whole subtree.
- For optimal pruning
	- Evaluate branches with the highest probabilities first
	- Evaluate branches with the highest expected values first.

![[Pasted image 20240205213057.png]]
