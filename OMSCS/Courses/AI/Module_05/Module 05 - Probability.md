---
tags:
  - OMSCS
  - AI
  - Statistics
  - Probability
  - Bayes
---
# Module 05 - Probability

## Bayes' Network Example
- influence diagram can show the many ways that all of the variables in a network can affect the outcome
	- variables
	- sensors
	- results / states
	- causes / effects

![[Pasted image 20240217102838.png]]

- Red is the resulting condition
- Blue are possible variables, which influence each other and the result
- Black are different meters you can use to asses your confidence levels of specific variables.

![[Pasted image 20240217103040.png]]

![[Pasted image 20240217103114.png]]

> The Bayes Network is a compact representation of a distribution over this very large joint probability distribution of all of these variables.

- Specify
- Observe
- Compute (Probabilities of Hypotheses)

This unit specifically covers
- Binary events
- Probability
- Simple Bayes Networks
- Conditional Independence
- D-Separation
- Parameter Counts
- Inference in Bayes Networks

![[Pasted image 20240217103714.png]]

![[Pasted image 20240217103720.png]]

## Coin Flips

- $P(H) = 1/2 \rightarrow P(T) = 1/2$
- $P(H) = 1/4 \rightarrow P(T) = 3/4$
- $P(H) = 1/2 \rightarrow P(H,H,H) = (1/2)^3 = 1/8 = 0.125$
- Complex example
	- $X_i$ is the result of the i-th coin flip
	- $X_i \in \{H,T\}$
	- $P(H) = P(T) = 1/2$
	- $P(X_1 = X_2 = X_3 = X_4)$?
	- Answer is $1/8$. My rationale:
		- If $X_1=H$, then all of the other $X$'s must be $H$.
		- $P(H,H,H,H)=P(H)^4=1/16$
		- The same logic works for if $X_1=T$
		- $P(T,T,T,T)=P(T)^4=1/16$
		- The probability of $P(H,H,H,H)$ or $P(T,T,T,T)$ will just be the sum of those 2 values.
		- $1/16+1/16=2/16=1/8=0.125$
- Another complex example
	- $P(\{X_1, X_2, X_3, X_4\})$ contains $\ge 3$ $H$
	- Working out
		- $P(H,H,H,H)=1/16$
		- $P(H,H,H,T)=1/16$
		- $P(H,H,T,H)=1/16$
		- $P(H,T,H,H)=1/16$
		- $P(T,H,H,H)=1/16$
		- 5 possibilities, each with $1/16$ chance of occurring
		- Answer = $5/16=0.3125$
		- Is there a smarter way?

## Probabilities
### Complementary probability
$P(A)=\rho \space\space \Rightarrow \space\space P(\neg A)=1-\rho$

### Independence
- $X \perp Y$: "2 random variables named X and Y are independent."
- $X \perp Y : P(X,Y)=P(X)P(Y)$
- $P(X)P(Y)$ are the "marginals"
- $P(X,Y)$ is the "joint probability"

### Dependence
$P(X_2=H \space | \space X_1=H) = 0.9$ is the symbolic representation of "The probability of $X_2$ being heads, **given that** $X_1$ was heads, is $0.9$"

- $P(X_1=H)=1/2$
- $P(X_2=H \space | \space X_1=H) = 0.9$
- $P(X_2=T \space | \space X_1=T) = 0.8$
- $P(X_2=H)=\space?$

Working out
- Branch 1, $X_1=H$, $\rho=1/2$, $P(X_2=H)=0.9$
- Branch 2, $X_1=T$, $\rho=1/2$, $P(X_2=H)=1-P(X_2=T)=1-0.8=0.2$
- $P(X_2=H)=0.5(0.9)+0.5(0.2)=0.55$
- This answer makes sense. There's a 50/50 shot of the first coin being heads or tails. The branch that favors heads does so slightly more strongly than the branch which favors tails, 0.9 vs 0.8. This indicates that the answer should be more than 1/2.

Instructor's notes
- This follows the theorem of total probability.
$$
P(X_2=H)=P(X_1=H)P(X_2=H \space | \space X_1=H) + P(X_1=T)P(X_2=H \space | \space X_1=T)
$$

### Total Probability
- $P(Y)=\sum_{i}P(Y \space | \space X=i) \times P(X=i)$
- $P(\neg X \space | \space Y) = 1 - P(X \space | \space Y)$
- $P(X \space | \space \neg Y) \ne 1 - P(X \space | \space Y)$

## More Examples
### Weather
- $S=sunny$
- $R=rainy$
- $P(D_1=S)=0.9$
- $P(D_2=S|D_1=S)=0.8$
- $P(D_2=R|D_1=S)=1-P(D_2=S|D_1=S)=1-0.8=0.2$
- $P(D_2=R|D_1=S)=0.2$
- $P(D_2=S|D_1=R)=0.6$
- $P(D_2=R|D_1=R)=1-P(D_2=S|D_1=R)=1-0.6=0.4$
- $P(D_2=R|D_1=R)=0.4$
- $P(D_2=S)$
	- B1: $D_1=S$, $\rho=0.9$, $P(D_2=S|D_1=S)=0.8$
	- B2: $D_1=R$, $\rho=0.1$, $P(D_2=S|D_1=R)=0.6$
	- $P(D_2=S)=0.9(0.8)+0.1(0.6)=0.72+0.06$
	- $P(D_2=S)=0.78$
- $P(D_3=S)$
	- B1: $D_2=S,\rho=0.78,P(D_3=S|D_2=S)=0.8$
	- B2: $D_2=R,\rho=1-0.78,P(D_3=S|D_2=R)=0.6$
	- $P(D_3=S)=0.78(0.8)+0.22(0.6)=0.624+0.132$
	- $P(D_3=S)=0.756$

### Cancer
- $P(C)=0.01$
- $P(\neg C) = 0.99$
- $P(+|C)=0.9$
- $P(-|C)=0.1$
- $P(+|\neg C)=0.2$
- $P(-|\neg C)=0.8$
- Find
	- $P(+, C)$
		- $P(C)=0.01$
		- $P(+|C)=0.9$
		- $P(+,C)=P(C)P(+|C)=0.009$
	- $P(-,C)$
		- $P(C)=0.01$
		- $P(-|C)=0.1$
		- $P(-,C)=P(C)P(-|C)=0.001$
	- $P(+,\neg C)$
		- $P(\neg C)=0.99$
		- $P(+|\neg C)=0.2$
		- $P(+,\neg C)=P(\neg C)P(+|\neg C)=0.198$
	- $P(-,\neg C)$
		- $P(\neg C)=0.99$
		- $P(-|\neg C)=0.8$
		- $P(-,\neg C)=P(\neg C)P(-|\neg C)=0.792$
	- $P(+)$
		- B1: $C, \rho = 0.01, P(+|C)=0.9$
		- B2: $\neg C, \rho = 0.99, P(+|\neg C)=0.2$
		- $P(+)=0.01(0.9)+0.99(0.2)=0.009+0.198$
		- $P(+)=P(+,C)+P(+, \neg C)$
		- $P(+)=0.207$
	- $P(-)=1-P(+)=0.793$
	- $P(C|+)$
		- $=\frac{P(+,C)}{P(+,C)+P(+,\neg C)}$
		- $=\frac{P(+,C)}{P(+)}$
		- $=0.009/0.207$
		- $P(C|+)=0.043$
		- Note: We need to normalize the probability of $P(+, C)$ by the total probability of $P(+)$ in order to find $P(C|+)$. The reason why the resulting probability is so small is due to $P(C)$ being so small ($0.01$). The positive test result effectively increases your belief of being in that population.

## Bayes Rule
> This is probably the most important piece of math in this whole course.

$$
P(A|B)=\frac{P(B|A)*P(A)}{P(B)}
$$

- $P(B|A)$ is the "likelihood"
- $P(A)$ is the "prior"
- $P(B)$ is the "marginal likelihood"
- $P(A|B)$ is the "posterior"
- Typically $B$ is the "test result" or the "evidence"

$$
P(B)=\sum_a P(B|A=a)P(A=a)
$$
Back to the cancer example

$$
P(C|+)=\frac{P(+|C)*P(C)}{P(+)}=\frac{0.9(0.01)}{0.207}=0.043
$$
