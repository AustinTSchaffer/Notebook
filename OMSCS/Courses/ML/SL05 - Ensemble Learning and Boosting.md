---
tags:
  - OMSCS
  - ML
---
# SL05 - Ensemble Learning and Boosting

- Spam email
- is it spam or not?
- Come up with some simple rules for classifying if it's spam
	- from spouse? not spam
	- body contains "manly"? spam
	- short? spam
	- just URLs? spam
	- just an image? spam
	- misspelled words? spam
	- blocklist of words? spam
	- make money fast? spam
- each simple rule is not good enough on its own
- combine each simple rule into a complex rule that works well enough on its own
- learn over subsets of the data to generate those simple rules

## Algorithm
- What is this notion of "combine"?
- How do we pick subsets?

![[Pasted image 20250128210750.png]]

## Bagging
- This is called Bagging (Bootstrap Aggregation)
- Take some random subset of the data
- Train over that data
- Keep doing it
- Take the average result of the models

![[Pasted image 20250128210950.png]]

![[Pasted image 20250128211015.png]]

## Boosting
- similar to bagging
- Take the "hardest" examples
- perform a weighted mean
- Error calculations should be based on the "likelihood" of each data point
- Which examples are important to learn? Which examples aren't important to learn?
- "Weak" learners
	- Does better than chance
	- Expected error is always less than half
- Given training $(x_i, y_i)$ where $y_i \in \{-1, +1\}$
- For t=1 to T
	- Construct distribution D
	- find weak classifier $h_t(X)$
		- with small error
		- $\epsilon_t = P_{D_t}[h_t(x_i) \ne y_i]$
		- This looks crazy, but we're essentially doing a weighted average.
- output $H_{\text{final}}$

- Start off with uniform distribution: $D_1(i)=\frac{1}{n}$
$$
D_{t+1}(i)=D_t(i)e^{-\alpha_ty_ih_t(x_i)}Z_t^{-1}
$$
$$
\alpha_t=\frac{1}{2}ln(\frac{1-\epsilon_t}{\epsilon_t})
$$

When $h_t(x)=y_i$, sometimes the $D_{t+1}(i) \le D_t(i)$. It usually goes down. Sometimes it stays the same. It depends on how the rest of the distribution is affected.

When $h_t(x_i) \ne y_i$, $D_{t+1}(i) \gt D_t(i)$. It always increases, to put more weight on the examples it got wrong.

$$
H_{\text{final}}=\text{sgn}(\sum_t\alpha_th_t(x))
$$

## Three Little Boxes
![[Pasted image 20250128214602.png]]

- $H$ is the set of axis-aligned semi-planes
- (Everything on one side of a line is in the range)

![[Pasted image 20250128215046.png]]

![[Pasted image 20250128215156.png]]

