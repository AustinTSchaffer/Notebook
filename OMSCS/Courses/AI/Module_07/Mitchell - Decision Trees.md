---
tags:
  - OMSCS
  - AI
  - Trees
---
# Mitchell - Decision Trees

Notes on paper/chapter: [[Mitchell - Decision Trees]]

## ID3

This paper proposes a decision-tree generation algorithm named ID3
- At each node in the tree, ID3 selects an attribute. Each branch leading from that node represents one discrete value for that attribute.
- At its core, ID3 doesn't do any backtracking.
- ID3 attempts to maximize "information gain" at each node. This function is calculated based on the following definitions

$$Entropy(S) = \sum_{i=1}^{c}-p_{i}log_{2}p_{i}$$
- $S$ represents the entire dataset
- $c$ is the number of different values that the _current_ attribute can have (has) in the dataset
- $p_i$ is the proportion/fraction of $S$ where the current attribute is $c_i$

$$Gain(S, A) = Entropy(S)-\sum_{v \in Values(A)}\frac{|S_v|}{|S|}Entropy(S_v)$$

- $Gain$ refers to the information gained by picking $A$ for the current decision node out of a dataset $S$
- $S$ is the dataset. This is a filtered dataset, given that the algorithm for building the decision tree is recursive. $S$ only evaluates the dataset at the current decision point, filtered by the decision points above. At the root of the tree, $S$ will be the full unfiltered dataset.
- $A$ is the attribute that we're currently evaluating.
- $Values(A)$ is the set of all possible values for $A$
- $S_v$ is the subset of $S$ for which $A=v$. Formally: $S_v=\{s\in S \space|\space A(s)=v\}$

- At each node in the tree, ID3 algorithm will pick the attribute $A$ which maximizes the value of $Gain(S, A)$.
- If for a specific value of $A$, all of $S_v$ has the same result, ID3 will add a terminal node with the $S_v$ result.
- The tree will never cause any root->leaf path to contain a duplicate attribute. If there are no more attributes left to evaluate, the tree will add a terminal node with the most common $S_v$ result.

## Overfitting

- Overfitting occurs in decision tree learning when a given tree performs better than all alternative trees on the training data, but performs worse than at least one alternative tree over the entire data space.
- The performance of each tree is calculated based on their error rates.
- ID3 prefers shorter trees because it's accuracy tends to fall off when trees are taller.
- Overfitting can occur when the training examples contain random errors or noise
- Overfitting can be avoided in DT learning by
	- stop the tree growth earlier before it perfectly classifies the training data.
	- allow the tree growth to produce an overfit tree, and then prune the tree later. This one tends to be more successful in practice.
- A key question is what criterion is to be used to determine the correct final tree size.
	- Use a separate set of examples as a testing set to evaluate the utility of post-pruning nodes from the tree. This is the most common approach.
	- Use all available data for training, but apply a statistical test to estimate whether expanding or pruning a node is likely to produce an improvement beyond the the training set.
	- Use an explicit measure of the complexity for encoding the training examples and the decision tree, halting growth when this encoding size is minimized. This is based on a heuristic called the Minimum Description Length principle.

(CONTINUE FROM 3.7.1.1 REDUCED ERROR PRUNING, PAGE 18)