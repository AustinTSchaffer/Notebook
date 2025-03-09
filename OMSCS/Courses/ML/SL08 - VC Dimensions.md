---
tags:
  - OMSCS
  - ML
---
# SL08 - VC Dimensions

## Infinite Hypothesis Space

$$
M \ge \frac{1}{\epsilon}\left(ln|H|+ln\frac{1}{\delta}\right)
$$

- $M$ - Minimum number of samples needed
- $\epsilon$ - error parameter
- $|H|$ - size of hypothesis space
- $\delta$ - failure parameter

## Which Hypothesis Spaces are Infinite?
- linear separators
	- halfplanes
	- lines
- artificial neural networks
	- continuous weights
	- unlimited layer config options
- decision trees with continuous inputs (DTs with discrete inputs have a finite $|H|$)
	- continuous thresholds means infinite configurations
- KNN?
	- It's often referred to as a non-parametric model.
	- There's either 0 parameters or $\infty$ parameters, depending on your philosophy.

## Possible Counterexample

- Setup
	- $X: \{1,2,3,4,5,6,7,8,9,10\}$
	- $H:h(x)\ge \theta$
	- $\theta \in \Bbb R$
	- $|H|=\infty$
- Track all hypotheses
	- only track non-negative integers ten or below
	- $\theta \ge 0, \space \theta \le 10, \space \theta \in \Bbb Z$
	- finite _and_ same answer
- Keep version space

## Power of a Hypothesis Space
- What is the largest set of inputs that the hypothesis class can label in all possible ways?
- In the $H$ class above, there are only $|X|+1$ possible unique labeling outputs.
- This is VC dimension
- VC - Vapnik-Chervonenkis. The amount of data needed to learn.

## Internal Training
- Example
	- $X=\Bbb R$
	- $H = \{h(x)=x \in [a, b]\}$
	- $a \lt b, \space a \in \Bbb R, \space b \in \Bbb R$
- $VC=2$

![[Pasted image 20250308112718.png]]

Need to prove that no example exists for a given $VC$.

## Linear Separators

- Example
	- $X=\Bbb{R}^2$
	- $H=\{h(x)=W^\text{T}X\ge\theta\}$

![[Pasted image 20250308113037.png]]

- VC = 3 (We ignore the case where all 3 points fall on the same line, because all other orientations can be classified.)
- VC can't be 4 no matter the orientation of the points.

![[Pasted image 20250308113709.png]]

## The Ring
- VC dimension of a hypothesis class is often equal to the number of parameters.
- VC of a d-dimensional hyperplane is $d+1$ (assuming binary classification)

## Convex Polygon
- $X : \Bbb{R}^2$
- $H:$ points inside some convex polygon
- $VC=\infty$
- In the limit, convex polygons become circles
- For any given point that you don't want to include in the positive classification, don't include it in the polygon

![[Pasted image 20250308122826.png]]

## Sample Complexity 8 VC Dimension
Infinite case:
$$
M \ge \frac{1}{\epsilon}\left(8*VC(H)*log_2\frac{13}{\epsilon}+4*log_2\frac{2}{\delta}\right)
$$
Finite case:
$$
M \ge \frac{1}{\epsilon}\left(ln|H|+ln\frac{1}{\delta}\right)
$$

## VC of Finite H
- $d=VC(H) \rightarrow \exists \space 2^d$ distinct concepts (each gets a different h)
- $2^d\le|H|$
- $d \le log_2|H|$

Theorem: H is PAC-learnable if and only if VC dimension is finite.

