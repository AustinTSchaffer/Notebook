---
tags:
  - OMSCS
  - AI
  - ML
---
# Module 7 - Machine Learning

## Decision Trees
![[Pasted image 20240305201845.png]]

Answer is C
- It classifies 50% of the training examples in the first decision
- The other answers are wrong due to
	- less compact (more decisions) (D)
	- incorrect labeling (B)
	- poor performance in first decision (25/75 split) (A)

## K-Nearest Neighbors
- one of the simplest techniques to understand
- shows the challenges of picking the right parameters

![[Pasted image 20240305202237.png]]

- Bite from cookie cutter shark?
- +'s are from cookie cutter shark
- O's are all other bite marks
- All bite marks were observed on whales

![[Pasted image 20240305202349.png]]

![[Pasted image 20240305202402.png]]

![[Pasted image 20240305202454.png]]

- New bitemark observed (X)
- Is this a cookiecutter shark bite?
- 1 nearest neighbor?
- 2 nearest neighbors?
- What's the appropriate value for K?

## Cross Validation
- testing technique for tuning the parameters of an algorithm
- can be used to evaluate the performance of our algorithm
- can estimate the difficulty of a problem
- can help avoid overfitting

- important assumptions
	- training data is a good representation of the problem we're trying to solve
	- training data spans the space of the unknown examples we might encounter
- Often researchers put a lot of effort into tuning parameters on a specific model only to discover that the data does not actually fit the problem, or that there are rare but important examples which don't occur in the training set.

- split the data
	- 10% randomly selected and reserved for later
	- 18% randomly selected for a testing dataset
		- "independent" test set
		- This is a good buzzword to always include when referring to a testing dataset. It means that the test set was chosen randomly, and that none of the test data was in the training dataset.
	- 72% remaining for a training dataset
	- Never mix any of these datasets
- One of the main challenges in ML is the tension between generalization and overfitting.
- randomly selecting training/testing sets helps reduce bias
- Multiple trails - you can perform multiple trials with the same dataset by re-splitting the data and running everything all over again, keeping the 10% reservation off to the side. Keep going until you get bored, or until the average converges.
- The reserved 10% is our final testing set. The results of classifying this data set is what really counts.
	- This is how kaggle.com works
	- Netflix prize was based on this as well
- Leave One Out Cross Validation (LOOCV) - This technique is used when there's a small corpus of data. Only one example is reserved. The remaining data is split into test/train sets. In LOOCV, you often can test/train with all combinations of the data.
- If there's huge variations as a result of relatively small parameter changes, that can mean we're using the wrong approach. This can show how sensitive the algorithm is to getting the parameters exactly right
- If we're having trouble achieving high accuracy even on the training data, that can mean that the problem is hard, or that we're using the wrong algorithm

## Gaussian Distribution
$$p(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$

- $\mu$ is the mean
- $\sigma$ is the standard deviation
- $\sigma^2$ is variance, which they mentioned in the slides, but is not present in this diagram

### Central Limit Theorem
> If you have enough independent variables, their distribution will form a normal distribution, aka a bell curve, aka a gaussian distribution.

### Grasshoppers vs Katydids
![[Pasted image 20240305213109.png]]

![[Pasted image 20240305213238.png]]

![[Pasted image 20240305213249.png]]

![[Pasted image 20240305213325.png]]

### Decision Boundary
![[Pasted image 20240305220035.png]]

This one has 2 decision boundaries

![[Pasted image 20240305220130.png]]

### Decision Boundaries in Higher Dimensions
- 2D gaussians will have decisions boundaries which can be defined as conic sections
	- Lines
	- Parabolas
	- Hyperbolas
	- Ellipses
	- Circles

![[Pasted image 20240305220504.png]]

![[Pasted image 20240305220510.png]]

![[Pasted image 20240305220531.png]]

![[Pasted image 20240305220541.png]]

![[Pasted image 20240305220549.png]]

3D gaussian distributions result in bayes decision boundaries that are 2D hyperquadratics.

![[Pasted image 20240305220610.png]]

### Error
> We can use our graphs to understand how much error we are going to have as a result of setting a decision boundary at a certain point.

![[Pasted image 20240305220833.png]]

- Measurements from the red set which fall to the right of the decision boundary will be misclassified as being part of the blue set
- Measurements from the blue set which fall to the left of the decision boundary will be misclassified as being part of the red set

![[Pasted image 20240305221027.png]]

- We can determine the error by adding together the percentages of each curve that overlap.
	- Take the area of the red gaussian that's to the right of the DB. Assuming a normal distribution, this should be a percentage.
	- Take the area of the blue gaussian that's to the right of the DB. Assuming a normal distribution, this should be a percentage.
	- Adding them together in this example yields $20.22\%$.
- What if misclassifying a member of one set is MUCH worse than misclassifying the member of another set? Suppose only one of the types of mosquito is a carrier of a deadly virus.
- How much do we move the decision boundary?
	- If misclassifying one member of one set is a 10x worse outcome than misclassifying the member of the other set, we should move the decision boundary such that the error contributed by the important set is 10x lower than the error contributed by the less-serious set.

## Bayes Classifier
$$
p(c_j|d)=\frac{p(d|c_j)p(c_j)}{p(d)}
$$

> It's just bayes rules again.

- $p(d|c_j)$ is the probability of generating instance $d$ given class $c_j$
- $p(c_j)$ is the probability of the occurrence of class $c_j$. This is the ratio of the different measurements in the training set.
- $p(d)$ is the probability of instance $d$ occurring.

> The hard part seems to be $p(d|c_j)$ 

### Example

| Name    | Gender |
| ------- | ------ |
| Drew    | Male   |
| Claudia | Female |
| Drew    | Female |
| Drew    | Female |
| Alberto | Male   |
| Karen   | Female |
| Nina    | Female |
| Sergio  | Male   |

- $P(Male | Drew) = \frac{P(Drew | Male)P(Male)}{P(Drew)}$
- $P(Male|Drew) = \frac{(1/3)*(3/8)}{3/8}=0.125/3/8=1/3=0.\bar3$
- $P(Female|Drew)=\frac{P(Drew|Female)P(Female)}{P(Drew)}$
- $P(Female|Drew)=\frac{(2/5)*(3/8)}{3/8}=2/5=0.4$

### Naive Bayes
> When using Bayes rule, one of our problems is calculating the probability of a given data point, given a class ($p(d|c_j)$). So far in our examples, we used 1D data. When we use multiple features, things get pretty complicated.

If we assume that the variables are independent, then we can use the naive bayes.

![[Pasted image 20240305223111.png]]

> Is "Drew" male or female?

![[Pasted image 20240305223152.png]]

### Example
![[Pasted image 20240309201026.png]]

$$
\rho = P(S \space|\space \neg{P}, B, \neg{D})
$$

start off by just using regular Bayes rule

$$
\rho = \frac{P(\neg{Piazza}, Bank, \neg{Diplomat} \space|\space Spam)P(Spam)}{P(\neg{Piazza}, Bank, \neg{Diplomat})}
$$

Expand the top term by assuming they are independent ($P \perp B$, $B \perp D$, $P \perp D$)

$$
\rho = \frac{P(\neg{Piazza} \space|\space Spam)P(Bank \space|\space Spam)P( \neg{Diplomat} \space|\space Spam)P(Spam)}{P(\neg{Piazza}, Bank, \neg{Diplomat})}
$$

What the known probability values are

- Spam
	- $P(Spam)=0.3$
	- $P(\neg Spam) = 0.7$
- Piazza
	- $P(Piazza \space|\space Spam) = 0.001$
	- $P(\neg Piazza \space|\space Spam)=0.999$
	- $P(Piazza \space|\space \neg Spam)=0.25$
	- $P(\neg Piazza \space|\space \neg Spam)=0.75$
- Bank
	- $P(Bank \space|\space Spam) = 0.2$
	- $P(\neg{Bank} \space|\space Spam) = 0.8$
	- $P(Bank \space|\space \neg Spam) = 0.1$
	- $P(\neg{Bank} \space|\space \neg{Spam}) = 0.8$
- Diplomat
	- $P(Diplomat \space|\space Spam) = 0.3$
	- $P(\neg{Diplomat} \space|\space Spam) = 0.7$
	- $P(Diplomat \space|\space \neg Spam) = 0.01$
	- $P(\neg{Diplomat} \space|\space \neg{Spam}) = 0.99$

Note that we don't have $P(P)$, nor $P(B)$, nor $P(D)$. We can instead use naive bayes to figure out the denominator.

$P(\neg Piazza, Bank, \neg Diplomat)$
- $=P(\neg{P}, B, \neg{D} \space|\space S)P(S)+P(\neg{P}, B, \neg{D} \space|\space \neg S)P(\neg S)$
- $= P(\neg P \space|\space S)P(B\space|\space S)P(\neg D \space|\space S)P(S)$
- $+ P(\neg P \space|\space \neg S)P(B\space|\space \neg S)P(\neg D \space|\space \neg S)P(\neg S)$
- $=(0.999)(0.2)(0.7)(0.3)+(0.75)(0.1)(0.99)(0.7)$

$$
\rho=\frac{(0.999)(0.2)(0.7)(0.3)}{(0.999)(0.2)(0.7)(0.3)+(0.75)(0.1)(0.99)(0.7)}
$$

## No Free Lunch
(Continue from video 22)