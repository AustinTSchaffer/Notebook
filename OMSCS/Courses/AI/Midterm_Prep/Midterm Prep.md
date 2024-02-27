---
tags:
  - OMSCS
  - AI
---
# Midterm Prep

## Problem 1: Game Playing
- Player 1 is "X"
- Player 2 is "O"
- Both players have a single piece, and this piece can move to adjacent squares, but cannot move diagonally.
- Players cannot visit an occupied space, nor a previously visited space
- The winner is the last one to move.

![[Pasted image 20240225123322.png]]

> Use the Minimax algorithm to determine the value of this first move for Player 1. Does Player 1 have a guaranteed win?

- Transition from red layers to blue layers are "min" layers
- Transition from blue layers to red layers are "min" layers
- We can see the whole game tree, so we'll just propagate +1 for win and -1 from loss from the bottom of the tree to the top

|  |  |  |  |  |  |  |  |  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|  |  | +1 min |  |  |  |  |  |  |
|  |  | +1 max |  | +1 max |  |  |  |  |
|  | -1 min | +1 |  | +1 | +1 min |  |  |  |
| -1 | +1 | +1 max |  | +1 | +1 max |  | +1 max |  |
| -1 | +1 | +1 | -1 | +1 | +1 | +1 | +1 | -1 |
| -1 | +1 win | +1 | -1 | +1 | +1 win | +1 | +1 | -1 |
| -1 loss |  | +1 | -1 loss | +1 |  | +1 | +1 | -1 |
|  |  | +1 |  | +1 |  | +1 win | +1 win | -1 |
|  |  | +1 |  | +1 |  |  |  | -1 loss |
|  |  | +1 win |  | +1 win |  |  |  |  |

- X has a guaranteed win. No matter what O chooses as its first move, X can ensure a win.

> Apply alpha-beta pruning to the tree (traversing branches from left to right). How many leaves are pruned?

|  |  |  |  |  |  |  |  |  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|  |  | +1 min |  |  |  |  |  |  |
|  |  | +1 max |  | +1 max |  |  |  |  |
|  | -1 min | +1 |  | +1 | ~~+1 min~~ |  |  |  |
| -1 | ~~+1~~ | +1 max |  | +1 | ~~+1 max~~ |  | ~~+1 max~~ |  |
| -1 | ~~+1~~ | +1 | ~~-1~~ | +1 | ~~+1~~ | ~~+1~~ | ~~+1~~ | ~~-1~~ |
| -1 | ~~+1 win~~ | +1 | ~~-1~~ | +1 | ~~+1 win~~ | ~~+1~~ | ~~+1~~ | ~~-1~~ |
| -1 loss |  | +1 | ~~-1 loss~~ | +1 |  | ~~+1~~ | ~~+1~~ | ~~-1~~ |
|  |  | +1 |  | +1 |  | ~~+1 win~~ | ~~+1 win~~ | ~~-1~~ |
|  |  | +1 |  | +1 |  |  |  | ~~-1 loss~~ |
|  |  | +1 win |  | +1 win |  |  |  |  |

- 25 nodes are never explored.
- Those 25 nodes contain 6 leaves.

> Search Depth of 6. Heuristic function of (num my moves - num their moves). Killer moves (win: $+\infty$, loss: $-\infty$). Alpha-Beta pruning.
> 
> How many leaves are pruned?

![[Pasted image 20240225141302.png]]

|           |                               |                               |          |                         |                         |     |          |     |
| --------- | ----------------------------- | ----------------------------- | -------- | ----------------------- | ----------------------- | --- | -------- | --- |
|           |                               | $[-\infty, +\infty]$ (min, B) |          |                         |                         |     |          |     |
|           |                               | $[0, +\infty]$ (max, A)       |          | $[0, +\infty]$ (max, A) |                         |     |          |     |
|           | $[-\infty, -\infty]$ (min, B) | $[0, +\infty]$                |          | 0                       | $[0, +\infty]$ (min, B) |     |          |     |
| $-\infty$ | (pruned)                      | $[0, +\infty]$ (max, A)       |          | 0                       | $[+\infty, +\infty]$ (max, A)                |     | $[0, +\infty]$ (max, A) |     |
| $-\infty$ | (pruned)                      | 0                             | (pruned) | 0                       | $+\infty$               | (pruned)    | 0         |     |
| $-\infty$ | (pruned)                      | 0                             | (pruned) | 0                       | $+\infty$               | (pruned)    | 0         |     |

- We can prune the 2nd column branch pretty obviously. It's a min node, the left branch found $-\infty$, nothing in the 2nd column branch will ever be better for the opponent.
- We can prune the 4th column branch a little less obviously.
	- We know from looking at the first 2 columns that $\alpha$ is "at least" $-\infty$. 
	- By exploring the branch in the 3rd column, we find a 0, which is higher than $-\infty$.
	- This is enough information to know that the agent should pick the column 3&4 branch over the column 1&2 branch, given the opportunity.
	- With that information in hand, the search doesn't need to explore the branch further, pruning column 4.
- Nothing else really interesting happens until column 6. In column 6, we find a $+\infty$ right before a (max, A) decision. This allows the search to prune the 7th column.
- I don't freaking know man.

## Problem 2: Search
### Part 1: Search Knowledge
> You are given an admissible heuristic $h_1(n)$ for A∗, and that $h_2(n) = 2h_1(n)$.

- $h_2(n)$ is not always admissible.
- A* using $h_2(n)$ would not be guaranteed to find the optimal solution.
- An A* tree search solution with $h_2(n)$ has a guaranteed cost $\le 2C^*$

> You are given two different admissible A∗ heuristics, $a(n)$ and $b(n)$.

- You can combine them using $max(a(n), b(n))$. Doing so guarantees admissibility, and results in the fewest node expansions.
	- $min$ - guarantees admissibility, but is less efficient
	- $avg$ - guarantees admissibility, but is less efficient
	- $ln(a(n), b(n))$ - `TypeError: ln() takes 1 positional argument but 2 were given`

> Let $h^∗(n)$ be the true cost function, what are the relationships between $h^∗(n)$ to $a(n)$ and $h^∗(n)$ to $b(n)$?

- $a(n) \le h^*(n)$
- $b(n) \le h^*(n)$
- $max(a(n), b(n)) \le h^*(n)$

### Part 2: Robotic Assembly
![[Pasted image 20240225160754.png]]

> As a lead engineer at Ploetz-Tharner, you are selected to design the new robotic assembly program. A 5-part sequencing will be performed by a robotics system with 3DOF (3 degrees of freedom). The robot can move in the x,y,z space, and the parts are arranged in a grid on a conveyor. The robot will optimally move the parts to the target positions.
> 
> \[...\]

- The robot can move in one of 8 directions at a time. This means the branching factor is 8.
- The number of states at depth $k$ is bounded by $8^k$ as an upper limit.

> The parts must be moved one at a time toward their prescribed goal position aligning the parts for assembly. Only one part can occupy a cell, and your robot can sense what cell a part is in. Your robot can perform the following actions:
> 
> 1. Ready (positions the robot at i0) no cost (Only available for step 0, result returns i0)
> 2. Move (direction, # of cells) (Result returns current cell)  
	(a) Moving N, S, W, E has a cost of 1 per cell moved.  
	(b) Diagonal movement (i.e. NW, NE, SW, SE) has a cost of 1 per cell moved.

- The state space of the parts is $20 \space nCr \space 5$, which is $20*19*18*17*16=1860480$
- The state space of the robot is $20$
- The full state space is $1860480*20=37209600$
- Doesn't matter where the initial positions of the parts are, the answer is the same.
- I think the sample exam is missing a 0.
- Admissible heuristics (they did not do a good job of describing this problem)
	- Manhattan is not an admissible heuristic. A single diagonal move costs 1. Manhattan distance for a diagonal move would cost 2.
	- Euclidean distance is not an admissible heuristic. A single diagonal move costs 1. ED for a diagonal move is $\sqrt{2}$ which is $\gt 1$.
	- $max(VertDist, HorizDist, DiagDist)$ would be admissible according to the answer key, but they did not describe what $DiagDist$ means.
	- Number of misplaced parts would be admissible, just not very efficient. I don't know why it's not marked as such in the answer key. This whole thing needs a fucking redo too.
	- $|dist(part, robot)| + |dist(part, goal)|$ is not admissible. In the event that all of the parts are on their goal and the robot is far away from some of the parts, the heuristic would return $>0$, when $h^*(n)=0$

> What would be the most effective strategy to transform the search to solve for optimal sequence and path concurrently? (multiple-option correct MCQ)

The study guide says we can
- Add a final goal to the end of the search
- Set all of the g-values to infinity
- Add linking nodes between the end-goals and initial locations

Interestingly the guide does _not_ include using a PQ that keeps paths from init to end goals.

The study guide also says ID-A* is the best algorithm of the bunch, even better than regular A*.

## Problem 3: Optimization Algorithms
### Part 1: Gradient Descent
- $x_{k+1}=x_k - \eta_{k} f'(x_k)$
- $f(x)=2x^2 - 4x + 5$
- $f'(x) = 4x - 4$
- $x_k = 3$
- $\eta_k=0.25$
- $\forall k = 1, 2, 3, ...$
- $f(3)$
	- $=2(3^2)-(4)(3)+5$
	- $=2(9)-12+5$
	- $=18-12+5$
	- $=6+5$
	- $=11$
- $x_{k+1}$
	- $= 3 - (0.25)(4(3)-4)$
	- $= 3 - (0.25)(12 - 4)$
	- $= 3 - (0.25)(8)$
	- $= 3 - 2$ 
	- $= 1$
- $x_{k+2}$
	- $=1-(0.25)(4(1)-4)$
	- $=1-(0.25)(0)$
	- $=1-0$
	- $=1$

- Assuming an arbitrary function which does not go to negative infinity
	- You can always find a local minimum through one round of gradient descent.
	- It's not guaranteed that the local minimum you find is the global minimum.

### Part 2: Line Search
- $f(x)=2x^2-4x+5$
- $x_1=3$
- $f(x_k-t'\triangledown f(x_k))=min_{t\in R}f(x_k-t\triangledown f(x_k))$

> What is the optimal step size for $k=2$?

The question fundamentally here seems to be "What value of $\eta_k$ causes GD to immediately arrive at the global minimum in one step, starting at $x_k$?"

$min_{t\in R}f(x_k-t\triangledown f(x_k))$, essentially we're trying to find a value $x_{k+1}$ which minimizes the function $f$.

From https://personal.math.ubc.ca/~CLP/CLP1/clp_1_dc/ssec_find_maxmin.html

> If $f(x)$ has a global maximum or global minimum, for $a≤x≤b$, at $x=c$, then there are 3 possibilities. Either $f'(c)=0$, $f'(c)$ does not exist, $c=a$, or $c=b$

- $min_{x \in R} \space f(x)=min_{x \in R} \space 2x^2-4x+5$
- $= x : \space 4x-4=0$
- $min_{x \in R} \space f(x)=1$

- $x_{k+1}=x_k-(\eta_k)(4)(x_k-1)$
- $1=3-(\eta_k)(4)(3-1)$
- $-2=-(\eta_k)(4)(2)$
- $2=\eta_k(8)$
- $\eta_k=0.25$

### Part 3: Acceleration Scheme