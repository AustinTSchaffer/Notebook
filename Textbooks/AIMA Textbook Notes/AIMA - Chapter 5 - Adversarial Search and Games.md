---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 5 - Adversarial Search and Games
- chapter covers competitive environments
- 2 or more agents have conflicting goals
- adversarial search
- Focuses on games

## Game Theory
- For many opponents, aggregate all of them and think if them as an "economy"
- Min-max search is a generalization of and-or search
- pruning makes search more efficient by preventing the exploration of portions of the search tree
- for each state, we can apply an "evaluation function" a heuristic, which determines who is winning and by approximately how much
- later sections cover games of "imperfect information", i.e. poker, bridge, games where not all of the available information is visible to all players.

### 2-player 0-sum games
- **deterministic**: No randomness.
- **2-player**: only 2 agents, diametrically opposed foes.
- **turn-taking**: players take turns, cannot act simultaneously.
- **perfect-information**: game state is fully observable by all agents.
- **zero-sum**
	- what's good for one player is bad for the other.
	- There is no win-win, only win-lose, and sometimes draw-draw.
	- It can be also defined as a "constant sum" game, where the number of points available to be awarded across all players at the end of the game is fixed to some constant.
- Games can be formally defined with the following elements
	- $S_0$: the initial state
	- $ToMove(s)$: The player whose turn it is to move in state $s$
	- $Actions(s)$: The set of legal moves available to the current player in state $s$.
	- $Result(s, a$: The transition model, which defines the state resulting from taking action $a$ in state $s$
	- $IsTerminal(s)$: A **terminal test**, which returns true if the game is over. States where the game has ended are called **terminal states**
	- $Utility(s,p)$: A **utility function** (aka **objective function**, **payoff function**), defines the final numeric value to player $p$ in state $s$. In the terminal states of chess, the output of this function will be $1$, $0$, or $1/2$, referring to win, lose, and draw respectively. Backgammon has a wider range of possible outcomes, ranging from $0$ to $192$.
- $S_0$, $Actions$ and $Result$ define the **state space graph**
- We can superimpose a **search tree** over part of the graph to determine the moves to make.
- We define the complete **game tree** as a search tree that follows every sequence of moves all the way to a terminal state. The game tree may be infinite.

> For tic-tac-toe the game tree is relatively small—fewer than terminal nodes (with only 5,478 distinct states). But for chess there are over nodes, so the game tree is best thought of as a theoretical construct that we cannot realize in the physical world.

### Optimal Decisions in Games
> Given a game tree, the optimal strategy can be determined by working out the **minimax** value of each state in the tree, which we write as $MINIMAX(s)$. 

- The minimax value is the utility (for MAX) of being in that state, assuming that both players play optimally from there to the end of the game.
- The minimax value of a terminal state is just its utility.
- In a non-terminal state, MAX prefers to move to a state of maximum value when it is MAX’s turn to move, and MIN prefers a state of minimum value (that is, minimum value for MAX and thus maximum value for MIN).

$Minimax(s)=$
- $\text{if} \space IsTerminal(s) \rightarrow Utility(s, p_1)$
- $\text{if} \space ToMove(s)=p_1 \rightarrow max_{a \epsilon Actions(s)}Minimax(Result(s, a))$
- $\text{if} \space ToMove(s)=p_2 \rightarrow min_{a \epsilon Actions(s)}Minimax(Result(s, a))$

> This definition of optimal play for MAX assumes that MIN also plays optimally. What if MIN does not play optimally? Then MAX will do at least as well as against an optimal player, possibly better. However, that does not mean that it is always best to play the minimax optimal move when facing a suboptimal opponent. Consider a situation where optimal play by both sides will lead to a draw, but there is one risky move for MAX that leads to a state in which there are 10 possible response moves by MIN that all seem reasonable, but 9 of them are a loss for MIN and one is a loss for MAX. If MAX believes that MIN does not have sufficient computational power to discover the optimal move, MAX might want to try the risky move, on the grounds that a 9/10 chance of a win is better than a certain draw.

The Minimax algorithm performs a complete depth-first exploration of the game tree.
- Time complexity: $O(b^m)$
- Space complexity: $O(bm)$ or $O(m)$

Time complexity is exponential, making this strategy impractical for complex games. Mathematically satisfying algorithm nonetheless. You can derive more practical algorithms by approximating minimax.

### Extending Minimax to $n>2$ player games
- replace the single value at each node with a vector of values, one for each player
- In terminal states, this gives the utility of the state from each player's viewpoint. In 2 player games, this vector can be simplified to a single value, because the sum of the 2 values is always the same constant value.
- Each player will chose the value at each ply which maximizes their own utility function.

![[Pasted image 20240124185412.png]]

- Unstable alliances can occur naturally and selfishly in zero-sum games, if the best move of 2 opponents is to attack a common enemy who is winning by too much.
- Stable alliances can occur naturally in games that are not zero sum.

### Alpha-Beta Pruning
- The number of game states is exponential with the depth of the tree
- No algorithm can completely eliminate the exponent, but reducing the value of the exponent helps a lot.

![[Pasted image 20240124190236.png]]
![[Pasted image 20240124190250.png]]

> The general principle is this: consider a node $n$ somewhere in the tree, such that Player has a choice of moving to $n$. If Player has a better choice either at the same level or at any point higher up in the tree, then Player will never move to $n$. So once we have found out enough about $n$ (by examining some of its descendants) to reach this conclusion, we can prune it.

- alpha-beta gets its name from 2 extra params in $MaxValue(s, \alpha, \beta)$
- $\alpha$ and $\beta$ describe bounds on the backed-up values that appear anywhere along the path to the current $s$
	- $\alpha$ is the value of the best (i.e., highest-value) choice found so far at any choice point on the route to $s$, for the player. (Think: $\alpha$ = "at least")
	- $\beta$ is the value of the best (i.e., lowest-value) choice found so far at any choice point on the route to $s$, for the opponent. (Think: $\beta$ = "at most")

### Move Ordering
- The effectiveness of alpha–beta pruning is highly dependent on the order in which the states are examined.
- If this could be done perfectly, alpha–beta would need to examine only $O(b^{m/2})$ nodes to pick the best move, instead of $O(b^m)$ for minimax.
- alpha-beta with perfect move ordering can solve a tree roughly twice as deep as minimax in the same amount of time.
- For chess, a fairly simple ordering function (such as trying captures first, then threats, then forward moves, and then backward moves) gets you to within about a factor of 2 of the best-case $O(b^{m/2})$ result.
- Adding dynamic move-ordering schemes, such as trying first the moves that were found to be best in the past, brings us quite close to the theoretical limit.
- The past could be the previous move or it could come from previous exploration of the current move through a process of **iterative deepening**
	- First, search one ply deep and record the ranking of moves based on their evaluations.
	- Then search one ply deeper, using the previous ranking to inform move ordering
	- The increased search time from iterative deepening can be more than made up from better move ordering.
	- The best moves are known as killer moves, and to try them first is called the **killer move heuristic**.
- In game tree search, repeated states can occur because of **transpositions**, different permutations of the move sequence that end up in the same position, and the problem can be addressed with a **transposition table** that caches the heuristic value of states.

> Even with alpha–beta pruning and clever move ordering, minimax won’t work for games like chess and Go, because there are still too many states to explore in the time available. In the very first paper on computer game-playing, Programming a Computer for Playing Chess (Shannon, 1950), Claude Shannon recognized this problem and proposed two strategies: a Type A strategy considers all possible moves to a certain depth in the search tree, and then uses a heuristic evaluation function to estimate the utility of states at that depth. It explores a wide but shallow portion of the tree. A Type B strategy ignores moves that look bad, and follows promising lines “as far as possible.” It explores a deep but narrow portion of the tree.

## Summary

- A game can be defined by the initial state (how the board is set up), the legal actions in each state, the result of each action, a terminal test (which says when the game is over), and a utility function that applies to terminal states to say who won and what the final score is.
- In two-player, discrete, deterministic, turn-taking zero-sum games with perfect information, the minimax algorithm can select optimal moves by a depth-first enumeration of the game tree.  
- The alpha–beta search algorithm computes the same optimal move as minimax, but achieves much greater efficiency by eliminating subtrees that are provably irrelevant. Usually, it is not feasible to consider the whole game tree (even with alpha–beta), so we need to cut the search off at some point and apply a heuristic evaluation function that estimates the utility of a state.
- An alternative called Monte Carlo tree search (MCTS) evaluates states not by applying a heuristic function, but by playing out the game all the way to the end and using the rules of the game to see who won. Since the moves chosen during the playout may not have been optimal moves, the process is repeated multiple times and the evaluation is an average of the results.
- Many game programs precompute tables of best moves in the opening and endgame so that they can look up a move rather than search.  
- Games of chance can be handled by expectiminimax, an extension to the minimax algorithm that evaluates a chance node by taking the average utility of all its children, weighted by the probability of each child.
- In games of imperfect information, such as Kriegspiel and poker, optimal play requires reasoning about the current and future belief states of each player. A simple approximation can be obtained by averaging the value of an action over each possible configuration of missing information.
- Programs have soundly defeated champion human players at chess, checkers, Othello, Go, poker, and many other games. Humans retain the edge in a few games of imperfect information, such as bridge and Kriegspiel. In video games such as StarCraft and Dota 2, programs are competitive with human experts, but part of their success may be due to their ability to perform many actions very quickly.

