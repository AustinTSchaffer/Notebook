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

### Quiz 1

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

### Quiz 2
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
