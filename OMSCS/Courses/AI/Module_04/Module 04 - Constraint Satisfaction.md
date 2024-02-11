---
tags:
  - OMSCS
  - AI
---
# Module 04 - Constraint Satisfaction

## Map Coloring
- Color a map using the minimum number of colors.
- No neighboring territories can have the same color.

![[Pasted image 20240210104557.png]]

- Can list out all of the possible constraints: e.g. $WA \ne NT$

### Constraint Graph
![[Pasted image 20240210104707.png]]

- Nodes are the variables
- Edges show the constraints between the variables

![[Pasted image 20240210104901.png]]

- Minimum number of colors required for the map of italy: 4
- 4 also happens to be the max number of colors required for a 2D map.

## Constraint Types
- Unary constraints
- Binary Constraints
- Constraints can have 3 or more variables
- Constraints can have soft constraints

Problems with constraints can be called "Constraint Satisfaction Problems"

## Backtracking Search
> This is the stupid one.

![[Pasted image 20240210105140.png]]

You put values into the variables that don't conflict with the current state until there are no values available for one of the variables (dead end). Do this recursively so you can rewind.

![[Pasted image 20240210105235.png]]

### Least Constraining Values
You can improve this search by prioritizing the "least constraining value". This would be the variable which rules out the fewest values in the remaining variables.

![[Pasted image 20240210105408.png]]

### Minimum Remaining Values
Pick the variable which has the fewest possible values. In the case of ties, pick the variable with the most constraints, the most edges to other nodes.

![[Pasted image 20240210105424.png]]

![[Pasted image 20240210105455.png]]

![[Pasted image 20240210105559.png]]

### Forward Checking
For each assigned variable, we're going to keep track of the remaining legal values. If any of the variables end up with no possible values, you need to back up.

![[Pasted image 20240210105833.png]]

![[Pasted image 20240210105855.png]]

![[Pasted image 20240210105905.png]]

![[Pasted image 20240210105910.png]]

### Constraint Propagation and Arc Consistency
We could have stopped earlier in our forward-checking example from earlier. $NT$ and $SA$ are adjacent, but both can only also be blue. This is a conflict. We must however traverse the entire remaining constraint graph in order to see this issue, which can be inefficient.

![[Pasted image 20240210110041.png]]

> We can use arc consistency as a simple version of constraint satisfaction. A variable, in a constraint satisfaction problem, is arc consistent with respect to another variable, if there is some value still available for the second variable after we assign a value to the first variable.
> 
> If all variables satisfy this condition, then the network is arc consistent.

![[Pasted image 20240210110328.png]]

> Once we get to the stage of assigning green to $Q$, we look at all of its unassigned neighbors and see if the assignment of green reduces the number of colors available to them. If so, we remove that color from the neighboring region, and then look at its neighboring regions to see if we need to propagate the change onward.

In this example, propagating the change onward could mean seeing if the unassigned neighboring region only has one possible value, assigning that value, then propagating the change onwards.

We keep going until we need to make another decision, or until we find a conflict and need to backtrack.

### Arc Consistency Quiz
![[Pasted image 20240210110956.png]]

This map is mostly islands.

![[Pasted image 20240210111110.png]]

## Structured CSPs
![[Pasted image 20240210111129.png]]

> Suppose we have a problem with 80 binary variables. We can divide it into 4 problems of 20 variables. This reduces the search space from $2^{80}$ to $4\times2^{20}=2^2\times2^{20}=2^{22}$. 

![[Pasted image 20240210111208.png]]

> If we have a CSP with no loops (i.e. is a DAG), we can solve the problem in $O((nd)^2)$ (?) time instead of $O(d^n)$ time.

> $n$ is the number of variables.
> $d$ is the size of the domain.

- Pick any variable to be the root of the tree.
- Traverse the rest of the nodes in DAG order.
- For $j$ from $n$ down to $2$, apply $RemoveInconsistent(Parent(x_j), x_j)$ 
- For $j$ from $1$ to $m$, assign $x_j$ consistently with $Parent(x_j)$.

![[Pasted image 20240210111915.png]]

Sometimes you can reframe a problem as a tree. By assigning a value to SA first, then propagating the change to the other variables, you can then remove SA from the graph entirely, leaving a tree.

![[Pasted image 20240210111936.png]]

## Iterative Algorithms
![[Pasted image 20240210112100.png]]

![[Pasted image 20240210112129.png]]

> Iterative improvement algorithms work well when there are many solutions to the problem, and when there are very few.

