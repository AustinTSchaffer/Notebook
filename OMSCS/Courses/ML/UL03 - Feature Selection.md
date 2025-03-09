---
tags:
  - OMSCS
  - ML
---
# UL03 - Feature Selection
- knowledge discovery
	- interpretability
	- insight
	- which features actually matter?
- curse of dimensionality
	- if we can reduce the inputs to our models, they become easier to train, especially if there's less data to work with.
	- Amount of data you need grows exponentially in the amount of features you have ($2^N$)

## Feature Selection Algorithms
- Take $F$, a set of features, $|F|=N$
- Choose a subset of $F$ ($F'$ where $|F'|=M$)
- What's the algorithmic complexity?
	- We have a function $f$ which takes a set of features $F'$ and returns a score.
	- We have to check all subsets of $F$ 
	- There are $2^N$ subsets of $N$ features.
	- $O(2^{|F|})$
	- The problem is NP-hard.
	- It's an optimization problem!
	- If you "know" $M$, you "only" need to check $|F| \choose M$ combinations
- 2 major ways of doing this
	- $L$ is the learning algorithm
	- $M$ is the resulting model
	- Filtering: $F \rightarrow \left[\text{SEARCH}\right] \rightarrow F' \rightarrow \left[L\right] \rightarrow M$
	- Wrapping: $F \rightarrow \left[\left[SEARCH\right] \leftrightarrow \left[L\right]\right] \rightarrow (F', M)$
### Filtering
![[Pasted image 20250309131636.png]]

- Filter features before training $L$
- $L$ can't inform search algorithm.
- Faster. Isolated features.
- No information about $L$ performance can be fed backward.
- Decision Trees are, in a way, a type of filtering algorithm.
	- A DT learner can be used for $[SEARCH]$
	- The features that the DT used to split on can then be used to define $F'$.
	- Information gain ($I$) is a good function for deciding which feature is most important. DT learners simply wrap $I$ iteratively.
- Other useful metrics for SEARCH
	- Information Gain
	- Variance, Entropy
	- "Useful" features for model class $M$
	- Independent / Non-redundant features
		- 2 features with high correlation can be reduced to a single feature
		- $X_2=X_1+X_3$. Drop $X_2$ from $F$

### Wrapping
![[Pasted image 20250309132621.png]]

- Use $L$ as part of the search.
- $L$ informs search algorithm.
- Less efficient.
- Local search algorithms that use $L$ for defining fitness
	- Hill climbing
	- Simulated annealing
	- Neural Nets and Backpropagation
	- All other random opt algorithms
	- Just use DTs for $L$
	- Most importantly, don't look through all $2^N$ subsets of $F$
- Forward/Backward Search
	- Forward Search
		- Start with a feature
		- Look at all features in isolation
		- Pass just one feature at a time and see the resulting score from $L$
		- Take the best feature $F_{W,1}$ and then search the rest of $F$ for the next best feature $F_{W,2}$
		- Graph the results, decide when to stop.
	- Backward Search
		- Start with all features, determine which one to eliminate.
	- Both of these are pretty much hill climbing

![[Pasted image 20250309133321.png]]

## Smallest Subset of Features (Relevance)
![[Pasted image 20250309134033.png]]

- C gives no information, but it can be used to hack the simple origin-limited perceptron, adding a bias term.
- $X_i$ is strongly relevant if removing it degrades B.O.C.
	- (Bayes-Optimal Classifier [[SL09 - Bayesian Learning]])
	- BOC is the best you can do
- $X_i$ is weakly relevant if
	- Not strongly relevant
	- $\exists$ subset of features $X'$ such that adding $X_i$ to $X'$ improves BOC
- $X_i$ is otherwise irrelevant

Relevance measures effect on BOC
- Usefulness measures effect on a particular predictor
- relevance ~ information
- usefulness ~ error | model/learner

