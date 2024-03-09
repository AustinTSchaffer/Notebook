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
- If for a specific value of $A$, all of $S_v$ has the same classification, ID3 will add a terminal node with the $S_v$ classification.
- The tree will never cause any root->leaf path to contain a duplicate attribute. If there are no more attributes left to evaluate, the tree will add a terminal node with the most common $S_v$ classification.

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

### Reduced Error Pruning
- consider each of the decision nodes in the tree to be candidates for pruning
- pruning a decision node consists of removing the subtree rooted at that node, assigning it as a leaf node with the most common classification of the training examples affiliated with that node
- nodes are only removed if the resulting pruned tree performs no worse than the original over the validation set
	- nodes are pruned, choosing the node whose removal most increases the decision tree accuracy over the validation set
	- pruning continues until the further pruning decreases overall accuracy over the validation set
- typically the data is split into 3 categories
	- training set
	- pruning validation set
	- true validation set

### Rule Post-Pruning
- infer the decision tree from the training set, growing the tree until the training data is fit as well as possible, allowing overfitting
- convert the learned tree into an equivalent set of rules by creating one rule for each path from the root node to a leaf node
- Prune (generalize) each rule by removing any preconditions that result in improving estimated accuracy
- sort the pruned rules by their estimated accuracy, and consider them in sequence when classifying subsequent instances

Advantages of this pruning approach
- Converting the tree to distinct logical rules and then operating on those boolean expressions allows for more nuanced pruning compared to full tree pruning, where entire subtrees are either retained or pruned.
- Removes the distinction between attribute tests that occur near the root of the tree and those that occur near the leaves. Therefore we avoid messy bookkeeping issues such as how to reorganize the tree if the root node is pruned while retaining subtree(s) below the root.
- Converting to rules improves readability over parsing a decision tree.

Disadvantages
- more computations are required for determining the classification of a datum. With a tree, each attribute is only compared once per datum. With a disjunction of conjunctions, each attribute is used in a boolean expression multiple times, depending on the complexity of the original tree.

Example
- Precondition: $IF \space (Outlook=Sunny)\land(Humidity=High)$
- Postcondition: $THEN \space PlayTennis=No$
- Post-pruning would consider removing the $Outlook=Sunny$ term, then consider removing the $Humidity=High$ term. It will select one of these pruning steps which produces the greatest improvement in estimated rule accuracy, then potentially remove the other. It will never perform a pruning operation which decreases overall accuracy
- The "estimated accuracy" can be determined using a few different methods
	- Using a random disjoint validation set.
	- Using the testing set again but being pessimistic about it. There's some math involved here.

## Further Reading and Research
-  Incorporating Continuous-Values Attributes
	- Add a simple thresholding test
	- Split the attribute's values into multiple ranges
	- Threshold linear combinations of several continuous valued attributes
- Alternate Measures for Selecting Attributes
	- you don't need to use "information gain" as your heuristic
	- You can instead compare the ratio between the information gain, and how uniformly the attribute splits the (remaining) data.
	- $GainRatio(S,A)=\frac{Gain(S,A)}{SplitInformation(S,A)}$
	- $SplitInformation(S,A)=-\sum_{i=1}^{c}\frac{|S_i|}{|S|}log_{2}\frac{|S_i|}{|S|}$
- Handling training examples with missing attribute values
- Handling attributes with different costs

## Exercises
> Give decision trees to represent these boolean functions.

1. $A \land \neg B$
2. $A \lor |B \land C|$
3. $A \space xor \space B$
4. $|A \land B| \lor |C \land D|$

There's more in the PDF.