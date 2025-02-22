---
tags:
  - OMSCS
  - ML
---
# Information Theory

## Random Variables and Probability
- A variable is an object that can take on any value from a set of values.
- Can be discrete or continuous
- Random variables have unpredictable values
- A value that a random variable has taken on is called a "trial"
- A collection of trials is called a "sample"
- Every random variable has a probability distribution (discrete) or probability density (continuous)
- Random variables may be dependent on each other, or they may be independent.
- A joint distribution tells us everything about the co-occurrence of 2 different variables.
	- [[Module 05 - Probability]]
	- [[Module 6 - Bayes Nets]]

$$
P(X) = \sum_{y \in \Omega_y}P(X,Y=y)
$$

- Variables are independent iff: $P(X,Y)=P(X)*P(Y)$
- dependent variables use the conditional distribution: $P(Y|X)=\frac{P(X,Y)}{P(X)}$
- This leads to bayes rule: $P(X|Y)=P(Y|X)\frac{P(X)}{P(Y)}$
- It's possible to do this with more than 2 variables.

## Moments
- average = mean = expected value
- "avg/mean/E.V. of X": $E[X]$
- Variance measures the variation of values above/below the mean: $Var(X)=E[X^2]-E[X]^2$
- The standard deviation: $\sigma(X)=\sqrt{Var(X)}$
- Variables have many "moments". There are $k$ moments, each expressed as: $E[X^k]$
	- Central moment: $E[(X-E[X])^k]$
	- Variance is the second central moment of X
	- Normalized central moment: $\frac{E[(X-E[X])^k]}{\sigma(X)^k}$
	- The fourth normalized central moment is called "kurtosis" which measures the "peakedness" of a distribution.

## Entropy
- Fundamental measure in information theory
- captures the amount of randomness or uncertainty in a variable

$$
H(X) = -E[\text{log}P(X)] = -\sum_{x \in \Omega_X}P(X=x)\text{log}P(X=x)
$$
(logarithm base is usually 2)

- measure of the average length of a message that would have to be sent to describe a sample
	- Fair coin:
		- $H(X)=–(0.5 \space\text{log}\space 0.5 + 0.5 \space\text{log}\space 0.5) = 1$.
		- 100 flips requires 100 bits.
	- One sided coin:
		- $H(X) = -(1 \space\text{log}\space 1 + 0\space\text{log}\space 0)=0$.
		- 100 flips requires 0 bits.
	- 75% coin:
		- $(0.75\space\text{log}\space0.75 + 0.25\space\text{log}\space0.25)=0.8113$.
		- 100 flips requires 82 bits.
	- Just because you only need $M$ bits to describe a sample doesn't mean it's easy to formulate the message required to describe the sample.
	- "There exists a coder that can construct messages of length $H(X)+1$."
- Joint entropy
	- $H(X,Y)=-E_X[E_Y[\text{log}(\space P(X,Y) \space)]]$
	- $$H(X,Y)=-\sum_{x \in \Omega_X, y \in \Omega_Y}P(X=x,Y=y) \space\text{log}(\space P(X=x,Y=y)\space)$$
- Conditional entropy
	- $H(X|Y)=-E_X[E_Y[\text{log}(\space P(Y|X) \space)]]$
	- $$H(X,Y)=-\sum_{x \in \Omega_X, y \in \Omega_Y}P(X=x,Y=y) \space\text{log}(\space P(Y=y|X=x)\space)$$
## Mutual Information
- Conditional entropy can tell when 2 variables are completely independent
- This is not an adequate measure of dependence.
- "A small value for $H(Y|X)$ implies that $X$ tells us a great deal about $Y$ or that $H(Y)$ is small to begin with."
- We measure dependence using mutual information: $I(X,Y)=H(Y)-H(Y|X)$
- Measure of the reduction of randomness of a variable given knowledge of another variable.
	- $I(X,Y)=H(Y)-H(Y|X)$
	- $I(X,Y)=H(X)-H(X|Y)$
	- $I(X,Y)=H(X)+H(Y)-H(X,Y)$
	- $I(X,Y)=I(Y,X)$

