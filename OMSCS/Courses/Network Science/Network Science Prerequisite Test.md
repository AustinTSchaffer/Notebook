---
tags: OMSCS, Network Science, CS7280
---

# CS 7280: Network Science

## Q1: 2 Node System 1

![[./images/Pasted image 20220812235905.png]]

- 2 node system, connected in series
- Probability that the first node works is 0.9
- Probability that the 2nd node works in 0.8
- Probability of the system is the multiplication of those 2 probabilities

> $0.9 * 0.8 = 0.72$

## Q2: 2 Node System 2

![[./images/Pasted image 20220813000218.png]]

- 2 node system, connected in parallel
- Probability that either node works is 0.95
- Probability that the system _doesn't_ work is the multiplication of 1 minus each probability
- Probability that the system _does_ work is 1 minus that probability

>$(1 - 0.95) * (1 - 0.95) = 0.0025$
>$1 - 0.0025 = 0.9975$

## Q3: Take X from Y, no replacements

![[images/Pasted image 20220813001855.png]]

The logic follows that the likelihood of getting one "A" part is 100 in 300 ($100 As + 200 Bs$). If you don't replace it, the likelihood of getting a 2nd "A" part is 99 in 299 ($99As + 200Bs$). These events are dependent, since the action taken in the first event decreases the sample space available for the 2nd event.

$P = \prod_{x=0}^3 \frac{100-x}{300-x} = 0.01185408$

## Q4: Taxe X from Y, with replacements

![[./images/Pasted image 20220813000337.png]]

This is actually easier than Q3. Just do $(1/3)^4=0.012345679$. Replacing the part in the sample sizes means the events are independent.

## Q5: Standard Deviations, Variance, Z-Tables

![[./images/Pasted image 20220813002247.png]]

Things to note

- $\mu$ is the mean
- $\sigma$ is the standard deviation
- $X$ is the measured
- $\sqrt{variance} = \sigma$
- $Z=\frac{X-\mu}{\sigma}$
- Z-table (AKA "Standard Normal Table"): https://en.wikipedia.org/wiki/Standard_normal_table

> $P=1-Prob(\frac{13-10}{\sqrt{4}})$ 
> $Prob(\frac{13-10}{\sqrt{4}})=Prob(1.5)=0.93319$
> $P=1-0.93319=0.06681$

## Q6: Limits and Small Hospitals

![[./images/Pasted image 20220813003324.png]]

Derivative Rules: https://www.mathsisfun.com/calculus/derivatives-rules.html

Googled how to do limits. This is an indeterminate form, which means we can use L'Hopital's Rule:

> L'Hopital's Rule
> $\lim_{x\rightarrow0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow0}\frac{f'(x)}{g'(x)}$
> 
> $f(x) = sin(x)+x$
> $f'(x) = cos(x)+1$
> 
> $g(x)=2x^2+x$
> $g'(x) = 4x+1$
> 
> $\lim_{x\rightarrow0}\frac{sin(x)+x}{2x^2+x}$
> $=\lim_{x\rightarrow0}\frac{cos(x)+1}{4x+1}$
> $=\frac{cos(0)+1}{4(0)+1}$
> $=\frac{2}{1}$
> $=2$

## Q7: More Derivatives 

![[./images/Pasted image 20220813004749.png]]

The derivative of $ln(x)$ is $1/x$

## Q8: Integrals

![[./images/Pasted image 20220813005328.png]]

Integration Rules: https://www.mathsisfun.com/calculus/integration-rules.html

The answer is C.
- The derivative of $a^x+C$ is $a^xln(a)$. 
- The derivative of $a^{x-1}+C$ is $a^{x-1}ln(a)$
- The 3rd one looks scary, but it's just a constant times the $a^x$ expression, so taking the derivative results in one more $ln(a)$, which is a constant, which cancels out the $\frac{1}{ln(a)}$.
- It's 1am, not going to attempt number 4 tonight.