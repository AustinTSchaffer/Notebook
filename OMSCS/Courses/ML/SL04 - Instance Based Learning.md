---
tags:
  - OMSCS
  - ML
---
# SL04 - Instance Based Learning

- Other Supervised Learning algorithms train a model based on the data then throw the data away.
- In IBL, we put the data into a database and then lookup data in the database when we need to train on a new datapoint.

- Simple Database
	- Just store the examples, look them up when asked
	- Advantages
		- Reliable / dependable ((X, Y) -> DB, Lookup(X) -> Y)
		- Fast (to "train", there's basically no training)
		- Simple
	- Disadvantages
		- No generalization
		- Overfitting (querying datapoints that had mistakes always yields the same mistake)

## Cost of a House
- Have a DB of house costs
	- size
	- date sold
	- price of property when sold
	- location
	- zip code
- Nearest Neighbor
	- Find the nearest existing datapoint, use that cost
	- Falls apart if the unclassified datapoint is too far from a neighbor
- K Nearest Neighbor (KNN)
	- Take the $K$ nearest existing datapoints
	- Take the average of those $K$ datapoints
		- Can (should?) be a weighted average based on "distance"/"similarity"
		- The weighting function used is a "hyperparameter" of KNN
		- weighting function can be as simple as $1/k$ (unweighted)

## Comparison

![[Pasted image 20250128103204.png]]

- Do all the work upfront? (eager learner)
- Do all the work on the backend (at query time)? (lazy learner)
- Combination of approaches? No reason why you can't "cache" the result via a linear regression.

## KNN Example

![[Pasted image 20250128103648.png]]

```python
import sklearn.neighbors

X = [[1, 6], [2, 4], [3, 7], [6, 8], [7, 1], [8, 4]]
Y = [7, 8, 13, 44, 50, 68]
Q = [[4,2]]

# We need to use KNeighborsRegressor. KNeighborsClassifier
# uses "majority vote" or "weighted majority vote".
# KNeighborsRegressor returns the "average" or "weighted avg".

sklearn.neighbors\
	.KNeighborsRegressor(1, metric='euclidean')\
	.fit(X, Y)\
	.predict(Q)
# 8

sklearn.neighbors\
	.KNeighborsRegressor(3, metric='euclidean')\
	.fit(X, Y)\
	.predict(Q)
# 42

sklearn.neighbors\
	.KNeighborsRegressor(1, metric='manhattan')\
	.fit(X, Y)\
	.predict(Q)
# 8

sklearn.neighbors\
	.KNeighborsRegressor(3, metric='manhattan')\
	.fit(X, Y)\
	.predict(Q)
# 23.66666667 
```

| $d()$     | $K$ | `sklearn`        | Empirical | Notes                                   |
| --------- | --- | ---------------- | --------- | --------------------------------------- |
| Euclidean | 1   | $8$              |           |                                         |
| Euclidean | 3   | $42$             |           |                                         |
| Manhattan | 1   | $8$              | 29        | (4,2) is equidistant to (2,4) and (7,1) |
| Manhattan | 3   | $23 \frac{2}{3}$ | 35.5      | (4,2) is equidistant to (3,7) and (8,4) |
> Regarding the Nearest Neighbors algorithms, if it is found that two neighbors, neighbor `k+1` and `k`, have identical distances but different labels, the results will depend on the ordering of the training data.

![[Pasted image 20250128110752.png]]

## KNN Bias
Preference Bias
- Locality -> Near Points are Similar
- Smoothness -> Averaging
- **All features matter equally**

## Curse of Dimensionality
> As the number of features or dimensions grows, the amount of data we need to generalize accurately grows exponentially.

Intuition says "let's add more features, that'll help it classify better". In reality, that makes the problem worse if you have insufficient data.

If you have one dimension, the information density of the space is $1/N$, where $N$ is the number of datapoints. If you add another dimension, you need $N^2$ datapoints in order to achieve the same level of information density. If you add a 3rd dimension, you need $N^3$ datapoints to achieve the same level of information density.

![[Pasted image 20250128204050.png]]

Weighting different dimensions differently can help with the curse of dimensionality.

## Other Stuff
- Distance functions
	- Euclidean
	- Manhattan
	- Hamming
- Weighted vs Unweighted distances
- What's the best value for $K$?
- Weighted vs unweighted average
- Locally weighted regression
- Locally weighted linear regression
- Locally weighted quadratic regression
- Locally weighted $WHATEVER regression

## Summary
- lazy vs eager learning
- knn
- similarity = distance
- classification vs regression
- averaging
- domain knowledge matters
