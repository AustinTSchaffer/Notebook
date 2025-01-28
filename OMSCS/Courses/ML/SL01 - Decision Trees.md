---
tags:
  - OMSCS
  - ML
---
# SL01 - Decision Trees
- supervised learning algoritm

## Supervised Learning
2 types
- classification
	- take input
	- map it to a discrete label (M, F)
- regression
	- take input
	- map it to a continuous field of values

## Classification Learning Definitions

- instances
	- inputs
	- vectors of attributes
	- pictures (the image bytes)
	- credit score data
- concept
	- function
	- maps inputs to outputs
	- "what is (category)-ness?"
	- mapping between objects in the world and members of a set
- target concept
	- the answer
	- the actual process we're trying to approximate
- hypothesis
	- class
	- the set of all concepts we're willing to entertain
	- can be "all possible functions in the world"
	- $x^a$ would be a hypothesis
- sample
	- the training set
	- set of inputs paired with labels that are the correct outputs
- candidate
	- the current concept might be the target concept
- testing set
	- set of inputs paired with labels that are the correct outputs
	- the algorithm can't see these during the training step

## Decision Trees
- you have a tree
- there are decision nodes
- each decision nodes represents some attribute
- edges leading from DNs represent some comparison against that attribute (comparison on continuous values attribute, equality of discrete valued attribute)
- leaves of the tree are the answer/output/classification
- at each decision node, the goal of the tree construction algorithm is to narrow the space of possibilities as much as possible. There are ways to quantify this. Each "question" must further narrow the possibilities.

## Decision Tree Learning
1. Pick the "best" attribute
	1. "best" splits the training data roughly in half
2. ask question about it
3. receive bacon or pick another attribute

## Decision Tree Expressiveness
- can represent logical AND (doesn't require a decision node beyond $A=F$)
- can represent logical OR (doesn't require a decision node beyond $A=T$)
- can represent logical XOR (requires a separate leaf for all possible inputs)

Something we try to quantify is how big the decision tree is as a sort of Big O notation. "Is the number of decision nodes linear in the number of attributes?"

- For N-OR: Linear $O(N)$
- For N-XOR (AKA "parity"): Exponential $O(2^N)$

> The hardest problem is coming up with a better representation.

Decision trees work best when the data does not represent a "pairity" problem.

## ID3
- generic decision tree algorithm
- take "best" attribute (A)
	- "best" is determined by an "information gain" function
	- $Gain(S,A)=Entropy(S)-\sum_{v \in S} \frac{|S_v|}{|S|}Entropy(S_v)$
	- Entropy is a measure of randomness (it'll be discussed further later in the course)
- assign A as as decision attribute for current node
- for each value of A
	- create a descendent
	- if all of the filtered training examples have the same label, stop, create a decision leaf
	- otherwise, repeat the algorithm

## ID3 Bias
- Inductive bias
- restriction bias
	- "We're only considering a specific class of functions to model these training examples."
- preference bias
	- "What sort of hypotheses within the space of possible hypotheses is preferred?"
	- this is at the heart of inductive bias
- ID3 bias
	- prefers good splits near the top
	- prefers correct over incorrect
	- prefers shorter trees to longer trees

## Decision Trees Continuous Attributes
- thresholding
- ranges
- can lead to an attribute being considered multiple times along a single path in the tree, depending on how decision nodes ask questions about the continuous attributes.

## When do we really stop?
- If everything in the training set is classified correctly, then obviously you stop.
- Real data isn't that clean most of the time (imagine 2 identical rows apart from 2 different classifications)
- Noise
- At a certain point, you just need to decide "good enough" and pick the majority classification of the remaining examples along a path in the decision tree.
- We have to worry about overfitting. Cross validation can help with this.
- We can prune decision trees after generation.

## Regression
- splitting?
- variance?
- tree node outputs:
	- average of training set
	- local linear fit
