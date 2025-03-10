---
tags:
  - OMSCS
  - ML
---
# UL04 - Feature Transformation

Supplemental:
- [[ICA-Algorithms-and-Applications.pdf]]
- [[PCA-Tutorial-Intuition.pdf]]

> The problem with pre-processing a set of features to create a new (smaller? more compact?) feature set, while retaining as much (relevant? useful?) information as possible.

- $X \rightarrow X':|X'|\le|X|$
- $\rightarrow : P^Tx$ (usually a linear transformation)
- Feature Selection: $X=\{X_1, X_2, X_3, X_4\} \rightarrow X'=\{X_1, X_2\}$
- Feature Transformation: $X=\{X_1, X_2, X_3, X_4\} \rightarrow X'=\{2X_2+X_3\}$
- Sometimes we can project UP. $|X'|\ge|X|$

## Why?
- information retrieval (ad hoc)
	- The "Google" problem
	- retrieve subset of documents that are relevant to some query
	- query is unknown in some feature space
	- hard to do "clever things" up front
- words are the obvious features
	- might want to remove articles
	- might want to transform plurals to singular
	- there's a LOT of them. Curse of dimensionality
	- **polysemy**: some words mean more than one thing
		- car -> (automobile, first element in cons cell (Lisp))
		- apple -> (fruit, music company, tech company)
		- results in false positives
	- **synonymy**: many words mean the same thing
		- automobile <- (car, truck, SUV, automobile)
		- results in false negatives
	- feature selection does not solve these problems
	- we need to combine words into features which reduce document <-> query ambiguity

## Principal Components Analysis (PCA)
- eigenproblem
- maximizes variance
	- projecting the points onto the red diagonal in the graph below maximizes the "variance" i.e. maximizes the length of the segment that contains all of the datapoints. Also maximizes the variance (1)
	- (1) is the "principal component"
- Then PCA takes the vector that's perpendicular to that vector (2)

![[Pasted image 20250310092343.png]]


- finds directions that maximize variance
- finds directions that are mutually orthogonal
- global algorithm
- best reconstruction
	- returning features (1) and (2) loses no information (compared to keeping X and Y)
	- min $L_2$ error moving from $N$ to $M$ dimensions
- results in eigenvalues
	- the eigenvalues are monotonic
	- throwing away the eigenvalues with the smallest value is equivalent to throwing away the least important features
	- some dimensions may have a 0-eigenvalue, meaning it's entirely ignorable.
- re-projects the data into a new space where feature selection is easier
- quick note about implementation, often we end up subtracting the means of all the original features from all of the datapoints so that the "blob" of data is recentered around the origin before running PCA
- well studied -> fast algorithms
- classification?
	- It's a type of filter method.
	- If one feature has very low variance but is directly related to the data classification, PCA may end up throwing it away.

## Independent Components Analysis (ICA)
- PCA
	- correlation
	- maximizing variance
	- reconstruction
- ICA
	- independence
	- $X \rightarrow X'$
		- $|X| \perp |X'|$
		- $X_i' \perp X_j':i\ne j$
		- $I(X_i',X_j')=I(X_j',X_i')=0:i \ne j$
		- Maximize $I(X', X)$ to be able to reconstruct the data
	- also a linear transformation algorithm
	- If you then perform a linear combination of the resulting independent variables, you end up with a gaussian (Central Limit Theorem)
- Idea
	- there exists hidden variables that are mutually independent of one another
	- we can see observables that are based on the hidden variables
	- ICA attempts to reconstruct the hidden variables, and use those as the features
	- 
- blind source separation problem

![[Pasted image 20250310094752.png]]

## ICA Mechanics
- create a matrix of samples of all the sounds

![[Pasted image 20250310095435.png]]

![[Pasted image 20250310095538.png]]

![[Pasted image 20250310095547.png]]

- find a projection $P^T$ of the matrix such that each new feature has no mutual information (statistically independent)


## ICA vs PCA Analysis
| Property                              | PCA | ICA |
| ------------------------------------- | --- | --- |
| Mutually Orthogonal                   | ✅   | ❌   |
| Mutually Independent                  | ❌   | ✅   |
| Maximimal Variance                    | ✅   | ❌   |
| Maximimal (Joint) Mutual Information  | ❌   | ✅   |
| Maximimal Data Reconstruction         | ✅   | ❓   |
| Ordered Features                      | ✅   | ❌   |
| Bag of Features                       | ✅*  | ✅   |
| Blind Source Separation (BSS) Problem | ❌   | ✅   |
| Directional                           | ❌*  | ✅*  |
ICA does not produce ordered features. PCA does, meaning you can chop off features with low variance / importance. ICA doesn't have a notion of any hidden variables being more important than others. That's not its primary role.

PCA results in an ordered bag of features.

If you give PCA a transposed matrix of values, it will produce the same results. If you give ICA a transposed matrix of values, it will produce very different results. This further highlights the roles of each algorithm. Transposing the data before feeding it to ICA makes no sense.

For face analysis:
- PCA is a global algorithm. It finds brightness of faces. It then finds the "average face"
- ICA finds nose selectors, eye selectors, mouth selectors, hair selectors, etc.

For natural scene analysis:
- PCA does the same thing. Finds global properties and then the "average image".
- ICA finds **edges**. There exist better edge detectors for images than ICA.

Documents:
- ICA finds **topics**. You can then write better algorithms for extracting topics from documents.

ICA is good for finding what the important parts of the data are. You can then go write better algorithms for extracting those features from the data.

## Alternative - Random Components Analysis (RCA)
- Generates random directions and projects data out into those directions
- $P^TX$ where $P^T$ is a random linear transformation
- $X \rightarrow X':|X'| << |X|$
- Somehow works
- Generally: $|X'_{RCA}|\gt|X'_{PCA}|$
- manages to capture some correlations
- Advantage?
	- It's fast. The "feature transformation" stage of RCA is fast. Later stages of your ML pipeline might be slower.
	- It's cheap. It's easy.

> As ML scientists, we want to make things complicated. You must earn your complexity.

## Alternative - Linear Discriminant Analysis (LDA)
Finds a projection that discriminates based on the label.
