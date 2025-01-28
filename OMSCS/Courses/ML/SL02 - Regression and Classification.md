---
tags:
  - OMSCS
  - ML
---
# SL02 - Regression and Classification
Using calculus and equations to correlate continuously valued data with continuously labeled data.

- error functions = loss functions
	- error
	- squared error
- order of polynomials
	- k=0: constant
	- k=1: line
	- k=2: parabola
	- $f(x) = c_0+c_1x+c_2x^2...c_kx^k$
	- You can fit a line to data via parabolic functions as long as the algorithm sets $c_{i\ge2}=0$.
- You increase $k$ to prevent underfitting.
- You decrease $k$ to prevent overfitting.
- Actual algorithm uses a bunch of linear algebra, very efficient for computers.
- Regression algorithms can use a variety of data set partitioning schemes
	- 3-tier sets
		- training set
		- a cross validation set
		- a test set
	- "folds"
		- create $N$ folds
		- for each $i$ in $N$, train on all folds except fold $i$, then check on fold $i$
		- pick the model that had the lowest error
- can also do multivariate inputs
