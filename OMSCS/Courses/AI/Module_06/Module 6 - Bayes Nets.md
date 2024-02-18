---
tags:
  - OMSCS
  - AI
  - Probability
  - Bayes
---
# Module 6 - Bayes Nets

## Bayes Rule Graphically

![[Pasted image 20240217144613.png]]

Diagnostic Reasoning
- $P(A | B)$
- $P(A|\neg B)$

You need 3 parameters to specify a bayes network
- $P(A)$
- $P(B|A)$
- $P(B|\neg A)$

## Bayes Rule Refresher
$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

$$
P(\neg A | B) = \frac{P(B|\neg A)P(\neg A)}{P(B)}
$$

$$
P(A|B)+P(\neg A|B)=1
$$

- $P'(A|B)=P(B|A)P(A)$
- $P'(\neg A|B)=P(B|\neg A)P(\neg A)$
- For some normalizer value $\eta$
	- $P(A|B)=\eta P'(A|B)$
	- $P(\neg A|B)=\eta P'(\neg A|B)$
	- $\eta=(P'(A|B)+P'(\neg A|B))^{-1}$
- The advantage of using these pseudo probabilities is that you don't have to calculate $P(B)$ directly, which can be pretty complicated in some problems.

### 2-Test Cancer Example

![[Pasted image 20240217150019.png]]
- $P(C)=0.01$
- $P(\neg C)=0.99$
- $P(T_x=+|C)=0.9$
- $P(T_x=-|C)=0.1$
- $P(T_x=-|\neg C)=0.8$
- $P(T_x=+|\neg C)=0.2$
- $P(C|T_1=+, T_2=+)=?$

Working out
- Calculating $P(++|C)$
	- $P(T_1=+,T_2=+|C)=P(++|C)$
	- $P(++|C)=P(T_1=+|C)P(T_2=+|C)=0.9^2$
	- $P(++|C)=0.81$
- Calculating $P(++|\neg C)$
	- $P(T_1=+,T_2=+|\neg C)=P(++|\neg C)$
	- $P(++|\neg C)=P(T_1=+|\neg C)P(T_2=+|\neg C)=0.2^2$
	- $P(++|\neg C)=0.04$
- $P(C)=0.01$
- $P(++)$ $\leftarrow$ we can avoid calculating this
	- Calculating $P'(C|++)$
		- $P'(C|++)=P(++|C)P(C)$
		- $P'(C|++)=(0.81)(0.01)$
		- $P'(C|++)=0.0081$
	- Calculating $P'(\neg C|++)$
		- $P'(\neg C|++)=P(++|\neg C)P(\neg C)$
		- $P'(\neg C|++)=(0.04)(0.99)$
		- $P'(\neg C|++)=0.0396$
	- $\eta = (0.0081+0.0396)^{-1} = 20.9643...$
- Calculating $P(C|++)$
	- $P(C|++)=\eta P'(C|++)$
	- $P(C|++)=(20.9643...)(0.0081)$
	- $P(C|++)=0.1698$

I initially got the wrong answer for this due to using the wrong value of $P(T_1=+|\neg C)$ in the "Calculating $P(++|\neg C)$" step. I used 0.1 instead of 0.2, which multiplied the errors downstream.

|  | prior | + | + | P' | $P(C\|++)$ |
| ---- | ---- | ---- | ---- | ---- | ---- |
| $C$ | 0.01 | 0.9 | 0.9 | 0.0081 | 0.1698 |
| $\neg C$ | 0.99 | 0.2 | 0.2 | 0.0396 | 0.8301 |
### 2-Test Cancer Example 2

- $P(C)=0.01$
- $P(\neg C)=0.99$
- $P(T_x=+|C)=0.9$
- $P(T_x=-|C)=0.1$
- $P(T_x=-|\neg C)=0.8$
- $P(T_x=+|\neg C)=0.2$
- $P(C|T_1=+, T_2=-)=?$

Working out
- Calculating $P(+-|C)$
	- $P(T_1=+,T_2=-|C)=P(+-|C)$
	- $P(+-|C)=P(T_1=+|C)P(T_2=-|C)=(0.9)(0.1)$
	- $P(+-|C)=0.09$
- Calculating $P(+-|\neg C)$
	- $P(T_1=+,T_2=-|\neg C)=P(+-|\neg C)$
	- $P(+-|\neg C)=P(T_1=+|\neg C)P(T_2=-|\neg C)=(0.8)(0.2)$
	- $P(+-|\neg C)=0.16$
- $P(C)=0.01$
- $P(+-)$ $\leftarrow$ we can avoid calculating this
	- Calculating $P'(C|+-)$
		- $P'(C|+-)=P(+-|C)P(C)$
		- $P'(C|+-)=(0.09)(0.01)$
		- $P'(C|++)=0.0009$
	- Calculating $P'(\neg C|+-)$
		- $P'(\neg C|+-)=P(+-|\neg C)P(\neg C)$
		- $P'(\neg C|+-)=(0.16)(0.99)$
		- $P'(\neg C|+-)=0.1584$
	- $\eta = (0.1584+0.0009)^{-1} = 6.2774...$
- Calculating $P(C|+-)$
	- $P(C|+-)=\eta P'(C|+-)$
	- $P(C|+-)=(6.2774...)(0.0009)$
	- $P(C|++)=0.005649...$

|  | prior | + | - | P' | $P(C\|++)$ |
| ---- | ---- | ---- | ---- | ---- | ---- |
| $C$ | 0.01 | 0.9 | 0.1 | 0.0009 | 0.0056 |
| $\neg C$ | 0.99 | 0.2 | 0.8 | 0.1584 | 0.9943 |

## Conditional Independence
Useful assumptions in the examples above.
- Both $T_x$ variables are conditionally independent
- $P(T_2|C,T_1)=P(T_2|C)$ is one way of specifying conditional independence. 

![[Pasted image 20240217153405.png]]

$B \perp C \space | \space A \ne B \perp C$

> Getting a positive test result about cancer (B) increases the probability of having cancer (A) above the prior probability for A, which changes the probability that another test will result in a positive (C).

### Cancer Example 3

- $P(C)=0.01$
- $P(\neg C)=0.99$
- $P(T_x=+|C)=0.9$
- $P(T_x=-|C)=0.1$
- $P(T_x=-|\neg C)=0.8$
- $P(T_x=+|\neg C)=0.2$
- $P(T_2=+ \space | \space T_1=+)=?$

Ok so the theory here is that by having a positive result for $T_1$, that raises the probability of $C$ above it's prior value, which affects the calculations for $T_2$.

> For this problem, we want to apply the principle of total probability.

- $P(T_2=+ \space | \space T_1=+) = P(+_2 | +_1)$
- $P(+_2 | +_1)=P(+_2|+_1, C)P(C|+_1)+P(+_2|+_1, \neg C)P(\neg C | +_1)$
- $P(C|+_1)=0.043$
- $P(\neg C|+_1)=1-0.043=0.957$
- Thanks to conditional independence
	- $P(+_2|+_1, C)=P(+_2|C)=0.9$
	- $P(+_2|+_1, \neg C)=P(+_2|\neg C)=0.2$
- $P(+_2 | +_1)=(0.9)(0.043)+(0.2)(0.957)$
- $P(+_2 | +_1)=0.2301$
- Baseline: $P(+_x)=0.207$

## Absolute and Conditional Independence
- $A \perp B$ - means that A and B have "absolute independence"
- $A \perp B \space | \space C$ - means that A and B are "conditionally independent" on C
- Absolute independence does not imply conditional independence.
- Conditional independence does not imply absolute independence.

![[Pasted image 20240217160022.png]]

- $P(R | S) = P(R)$
	- We don't know anything about $H$, so $S$ has no effect on $R$.

### Sunny, Raise, and Happy - Quiz 1

- $P(R|H,S)=?$

> Using Bayes Rule we can transform this question.

$$
P(R|H,S)=\frac{P(H|R,S)P(R|S)}{P(H|S)}
$$

Where the hell did $P(H|S)$ come from?

> thanks to the rules of conditional independence: $P(R|S)=P(R)$
> 
> thanks to the rules of total probability:
> $P(H|S)=P(H|R,S)P(R)+P(H|\neg R,S)P(\neg R)$
>
> Substituting these values in to the equation above.
$$
\frac{P(H|R,S)P(R|S)}{P(H|S)}=\frac{P(H|R,S)P(R)}{P(H|R,S)P(R)+P(H|\neg R,S)P(\neg R)}
$$

- $P(H|R,S)=1$
- $P(R)=0.01$
- $P(H|R,S)P(R)=0.01$
- $P(H|\neg R,S)P(\neg R)=(0.7)(0.99)=0.693$
- $P(R|H,S)=0.01422...$

### Sunny, Raise, and Happy - Quiz 2
- $P(R|H)=?$

Using bayes theorem

$$
P(R|H)=\frac{P(H|R)P(R)}{P(H)}
$$

- $P(H|R)$
	- $= P(H|\neg S,R)P(\neg S) + P(H|S,R)P(S)$
	- $=(0.9)(0.3)+(1)(0.7)$
	- $=0.97$
- $P(R) = 0.01$
- $P(H)$
	- $= P(H|S,R)P(S, R)$
		- $=P(H|S,R)P(S)P(R)$
		- $=(1)(0.7)(0.01)$
		- $=0.007$
	- $+ \space P(H|\neg S, R)P(\neg S, R)$
		- $=P(H|\neg S, R)P(\neg S)P(R)$
		- $= (0.9)(0.3)(0.01)$
		- $=0.0027$
	- $+ \space P(H|S,\neg R)P(S, \neg R)$
		- $=P(H|S,\neg R)P(S)P(\neg R)$
		- $=(0.7)(0.7)(0.99)$
		- $=0.4851$
	- $+ \space P(H|\neg S, \neg R)P(\neg S, \neg R)$
		- $=P(H|\neg S, \neg R)P(\neg S)P(\neg R)$
		- $=(0.1)(0.3)(0.99)$
		- $=0.0297$
	- $=0.007+0.0027+0.4851+0.0297$
	- $=0.5245$
- $\frac{P(H|R)P(R)}{P(H)}$
	- $=(0.97)(0.01)(0.5245)^{-1}$
	- $=(0.97)(0.01)(1.9065...)$
	- $=0.01849...$

Using the "pseudo-probabilities" method

$$
P(R|H)=\frac{P(H|R)P(R)}{P(H|R)P(R)+P(H|\neg R)P(\neg R)}
$$

- $P(H|R)$
	- $= P(H|\neg S, R)P(\neg S) + P(H|S,R)P(S)$
	- $=(0.9)(0.3)+(1)(0.7)$
	- $=0.97$
- $P(H|\neg R)$
	- $= P(H|\neg S, \neg R)P(\neg S) + P(H|S,\neg R)P(S)$
	- $= (0.1)(0.3) + (0.7)(0.7)$
	- $= 0.03+0.49$
	- $=0.52$
- $P'(R|H)=P(H|R)P(R)$
	- $=(0.97)(0.01)$
	- $=0.0097$
- $P'(\neg R|H)=P(H|\neg R)P(\neg R)$
	- $=(0.52)(0.99)$
	- $=0.5148$
- $\eta = (P'(R|H)+P'(\neg R|H))^{-1}$
	- $=(0.0097+0.5148)^{-1}$
	- $=0.5245^{-1}$
	- $=1.9065...$
- $P(R|H)=\eta P'(R|H)$
	- $=(1.9065...)(0.0097)$
	- $=0.01849...$

### Sunny, Raise, and Happy - Quiz 3
- $P(R|H, \neg S)$

Using bayes theorem

$$
P(R|H,\neg S)=\frac{P(H|R,\neg S)P(R|\neg S)}{P(H|\neg S)}
$$

- $P(H|R,\neg S)=0.9$
- $P(R|\neg S)$
	- $=P(R) : R \perp S$
	- $= 0.01$
- $P(H|\neg S)$
	- $=\space P(H|R, \neg S)P(R)$
		- $=(0.9)(0.01)$
		- $=0.009$
	- $+\space P(H|\neg R, \neg S)P(\neg R)$
		- $=(0.1)(0.99)$
		- $=0.099$
	- $=0.009+0.099$
	- $=0.108$
- $P(R|H,\neg S)$
	- $=\frac{(0.9)(0.01)}{0.108}$
	- $=0.08\bar3$

### SRH - Quiz Recap

- $P(R)=0.01$
	- This is the "prior"
- $P(R|S)=0.01$
	- This is exactly equal to the prior because $R \perp S$.
	- This is also true for $P(R|\neg S)=P(R)$
- $P(R|H)=0.01849...$
	- If the person is happy, then the probability that they got a raise will increase over the prior.
- $P(R|H,S)=0.01422...$
	- If the person is happy AND we've observed that it's sunny, then the probability that they got a raise will still increase over the prior. However that probability will be less than the $P(R|H)$ probability, because the existence of the $S$ observation "explains away" $R$. Essentially, $R$ is no longer as impactful.
- $P(R|H, \neg S)=0.08\bar3$
	- This is the extreme case. Given that $P(H|\neg R, \neg S)$ is only $0.1$, and we've already observed $H$ and $\neg S$, we need to dramatically increase $P(R)$ over its prior in order to determine that .

## Conditional Dependence
- In the SRH example, S and R are independent. However, H adds a "conditional dependence" between S and R.
- In the absence of information about H, S and R are independent.
- However, given information about H, additional information about S influences the probability of R, and vice versa.
- This is what we mean when we say "$A \perp B \not \Rightarrow A \perp B \space | \space C$". If C is dependent on both A and B, then information about C allows A and B to influence each other's probabilities.
- In these examples
	- $S \perp R$
	- ${S \not\perp R \space | \space H}$

## General Bayes Networks
Given the network below, we can define it with just 5 distributions.

![[Pasted image 20240218131801.png]]

1. $P(A)$
2. $P(B)$
3. $P(C|A,B)$
4. $P(D|C)$
5. $P(E|C)$

We can also define a joint distribution across all of the variables by multiplying everything together.

$P(A,B,C,D,E)=P(A)\times P(B)\times P(C|A,B)\times P(D|C)\times P(E|C)$

The advantage of defining problems this way is that we can use way fewer probability values to define the joint distribution.

Determining the joint probability of the 5 variables without these distributions would require $2^5-1$ probability values.

Defining it with the distributions above only requires 10 probability values.

- $P(A)$ - 1 probability value
- $P(B)$ - 1 probability value
- $P(C|A,B)$ - 4 probability values:
	- $P(C|A,B)$
	- $P(C|\neg A, B)$
	- $P(C|A,\neg B)$
	- $P(C|\neg A, \neg B)$
- $P(D|C)$ - 2 probability values:
	- $P(D|C)$
	- $P(D|\neg C)$
- $P(E|C)$ - 2 probability values:
	- $P(E|C)$
	- $P(E|\neg C)$

### Counting Probability Values Quiz 1

![[Pasted image 20240218132942.png]]

- $P(A)$ - 1 prob val
- $P(B|A)$ - 2 prob vals
- $P(E|B)$ - 2 prob vals
- $P(C|A)$ - 2 prob vals
- $P(D|A)$ - 2 prob vals
- $P(F|C,D)$ - 4 prob vals
- Total: 13
- "13 parameters are required to specify the joint distribution of this bayesian network"

### Counting Probability Values Quiz 2

![[Pasted image 20240218133220.png]]

- $P(A)$ - 1
- $P(B)$ - 1
- $P(C)$ - 1
- $P(D|A,B,C)$ - 8
- $P(E|D)$ - 2
- $P(F|D)$ - 2
- $P(G|D,C)$ - 4
- 19

### Counting Probability Values Quiz 3

![[Pasted image 20240218133432.png]]

The naive joint distribution will require 65535 probability parameters in order to specify the joint distribution.

Using bayesian distributions, we only need to specify $2^A$ different probability values per variable, where $A$ is the number of incoming arcs.

- layer 1
	- BA - 1
	- AB - 1
	- FB - 1
	- total: 3
- layer 2
	- BD - 2
	- NC - 4
	- total: 6
- layer 3
	- BM - 2
	- BF - 4
	- NO - 1
	- NG - 1
	- FLB - 1
	- SB - 1
	- total: 10
- layer 4
	- L - 2
	- OL - 4
	- GG - 4
	- CWS - 16
	- DS - 2
	- total: 28
- total: 47

## D-Separation

### D-Separation Quiz 1

![[Pasted image 20240218135038.png]]

- $C \not \perp A$
- $C \perp A \space | \space B$
- $C \not \perp D$
	- If I know something about D, that influences the probability of A, which I can use to infer something about C.
- $C \perp D \space | \space A$
- $E \perp C \space | \space D$

### D-Separation Quiz 2

![[Pasted image 20240218135459.png]]

- $A \not \perp E$
- $A \not \perp E \space | \space B$
- $A \perp E \space | \space C$
- $A \perp B$
- $A \not \perp B \space | \space C$
	- We've discussed this before. This is the "explain away" effect.


### Reachability
- There's a concept of "reachability" for determining if 2 variables are independent.

![[Pasted image 20240218141233.png]]

### D-Separation Quiz 3

![[Pasted image 20240218141343.png]]

- $F \perp A$
- $F \not \perp A \space | \space D$
- $F \not \perp A \space | \space G$
- $F \perp A \space | \space H$

## Probabilistic Inference
TODO