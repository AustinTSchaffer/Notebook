---
tags: OMSCS, Network Science, CS7280, Calculus, DiffEQ
---

# CS 7280: Network Science

## Q1: 2 Node System 1

![[./images/Pasted image 20220812235905.png]]

- 2 node system, connected in series
- Probability of the system working is the multiplication of those 2 probabilities

> $0.9 * 0.8 = 0.72$

## Q2: 2 Node System 2

![[./images/Pasted image 20220813000218.png]]

- 2 node system, connected in parallel
- Probability that the system _doesn't_ work is the multiplication of 1 minus each probability
- Probability that the system _does_ work is 1 minus that probability

>$(1 - 0.95) * (1 - 0.95) = 0.0025$
>$1 - 0.0025 = 0.9975$

Alternatively, you can use a decision tree to determine the probability that it does work

- 95% A works (1)
- 5% chance A doesn't
	- 95% chance B works
	- 5% chance B doesn't (0)

> $0.95(1)+0.05(0.95+0.05(0))$
> $=0.95+0.05(0.95)$
> $=0.95+0.0475$
> $=0.9975$

## Q3: Take X from Y, no replacements

![[images/Pasted image 20220813001855.png]]

The logic follows that the likelihood of getting one "A" part is 100 in 300 ($100 As + 200 Bs$). If you don't replace it, the likelihood of getting a 2nd "A" part is 99 in 299 ($99As + 200Bs$). These events are dependent, since the action taken in the first event decreases the sample space available for the 2nd event.

$P = \prod_{x=0}^3 \frac{100-x}{300-x} = 0.01185408$

## Q4: Taxe X from Y, with replacements

![[./images/Pasted image 20220813000337.png]]

This is actually easier than Q3. Just do $(1/3)^4=0.012345679$. Replacing the part in the sample sizes means the events are all independent.

## Q5: Standard Deviations, Variance, Z-Tables

![[./images/Pasted image 20220813002247.png]]

Things to note

- $\mu$ is the mean
- $\sigma$ is the standard deviation
- $X$ is the measured value
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

The derivative of $ln(x)$ is $1/x$. I don't think there's a clever way to arrive at that answer, you just have to memorize it.

The more generalized rule is
- $ln(e)=1$.
- $log_e(x)=ln(x)$
- $\frac{d}{dx}log_{a}(x)=1/(xln(a))$.

Therefore
- $\frac{d}{dx}ln(x)=1/(xln(e))=1/x$.

## Q8: Integrals

![[./images/Pasted image 20220813005328.png]]

Integration Rules: https://www.mathsisfun.com/calculus/integration-rules.html

The answer is C. Again, this is something that is memorize-able. Doing the derivatives of each option confirms this.

- For A, The derivative of $\frac{d}{dx}a^x+C=a^xln(a)$. 
- For B, The derivative of $\frac{d}{dx}a^{x-1}+C=a^{x-1}ln(a)$
- C looks scary, but it's just a constant times the $a^x$ expression, so taking the derivative results in one extra $ln(a)$, compared to B, which is a constant, which cancels out the $\frac{1}{ln(a)}$. The result is a single $a^x$.
- For D, $\frac{a^x}{ln(x)}$ you need to use the quotient rule.
	- Quotient Rule: $\frac{d}{dx}\frac{f(x)}{g(x)}=\frac{f'(x)g(x)-g'(x)f(x)}{g(x)^2}$
	- $f(x)=a^x$
	- $f'(x)=a^xln(a)$
	- $g(x)=ln(x)$
	- $g'(x)=1/x$
	- $\frac{d}{dx}\frac{f(x)}{g(x)}=\frac{(a^xln(a))(ln(x))-(1/x)(a^x)}{ln(x)ln(x)}$
	- I'm not an insane person, and I don't really feel like simplifying this right now. I plugged it into an online calculator, which found that the simplification is indeed not $a^x$

## Q9: Diff-EQ
![[./images/Pasted image 20220814155827.png]]

Integration Rules: https://www.mathsisfun.com/calculus/integration-rules.html

> In mathematics, a **differential equation** is an [equation](https://en.wikipedia.org/wiki/Functional_equation "Functional equation") that relates one or more unknown [functions](https://en.wikipedia.org/wiki/Function_(mathematics) "Function (mathematics)") and their [derivatives](https://en.wikipedia.org/wiki/Derivative "Derivative").

> In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), an **ordinary differential equation** (**ODE**) is a [differential equation](https://en.wikipedia.org/wiki/Differential_equation "Differential equation") containing one or more functions of one [independent variable](https://en.wikipedia.org/wiki/Independent_variable "Independent variable") and the [derivatives](https://en.wikipedia.org/wiki/Derivative "Derivative") of those functions. The term _ordinary_ is used in contrast with the term [partial differential equation](https://en.wikipedia.org/wiki/Partial_differential_equation "Partial differential equation") which may be with respect to _more than_ one independent variable.

> In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), **separation of variables** (also known as the **Fourier method**) is any of several methods for solving [ordinary](https://en.wikipedia.org/wiki/Ordinary_differential_equation "Ordinary differential equation") and [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equation "Partial differential equation"), in which algebra allows one to rewrite an equation so that each of two variables occurs on a different side of the equation.

So, given an equation identified by $\frac{dx}{dt}=f(x)$, first we need to rewrite it as $\frac{dx}{f(x)}=dt$. Then we need to use the Fourier Method by first slapping an integration sign on each side: $\int{\frac{dx}{f(x)}}=\int{dt}$. Now we need to substitute $f(x)$ and get to work!

$\int{\frac{1}{5x-3}dx}=\int{dt}$

The integral of $1$ "with respect to $t$ ", is a linear function of $t$. $\int{dt}={t+C}$ 

It's going to take some additional explaining to reach the integral of $\int{\frac{1}{5x-3}dx}$.

Firstly, the integral of 1/x is the natural log of the absolute value of x, plus some constant.
$\int{\frac{1}{x}}dx=\ln{|x|}+C$

If you have some original function that is "A times natural log of x", the derivative is simply "A times one over x". 
$y=A\ln{x}$
$\frac{dy}{dx}=\frac{A}{x}$

This is because you can pull the constant A outside of the integral when integrating "A over x".
$\int{\frac{A}{x}dx}$
$=A\int{\frac{1}{x}dx}$
$=A\ln{|x|}+C$

This works no matter how the simplification of A looks.
$\int{\frac{3}{5x}dx}$
$=\frac{3}{5}\int{\frac{1}{x}dx}$
$=\frac{3}{5}\ln{|x|}+C$

For something like $y=\ln(3x-2)$, where the original function includes the natural log of some linear equation, we have to use the "Chain Rule". The chain rule works simply by "hiding" the $3x-2$ in a new function called $T$:

$\frac{dy}{dx}=\frac{dy}{dT}*\frac{dT}{dx}$
$y=\ln(T)$
$T=3x-2$
$\frac{dy}{dT}=\frac{1}{T}=\frac{1}{3x-2}$
$\frac{dT}{dx}=3$
$y=\ln(3x-2)\space\rightarrow\space\frac{dy}{dx}=\frac{3}{3x-2}$

In a more general form:
$y=A\ln(mx+b)\space\rightarrow\space\frac{dy}{dx}=\frac{Am}{mx+b}$

And going backwards (doing the integration):
$\int{\frac{A}{mx+b}dx}=A\frac{1}{m}\ln|mx+b|+C$

That makes this integral look super easy now.
$\int{\frac{1}{5x-3}dx}$
$=\frac{1}{5}\ln|5x-3|+C$

Back to the top of the question
$\frac{dx}{dt}=5x-3$
$\frac{dx}{5x-3}=dt$
$\int{\frac{1}{5x-3}dx}=\int{dt}$
$\int{dt}=t+C_1$
$\int{\frac{1}{5x-3}dx}=\frac{1}{5}\ln|5x-3|+C_2$
$\frac{1}{5}\ln|5x-3|+C_2=t+C_1$
$\ln|5x-3|=5(t+C_1-C_2)$
$\ln|5x-3|=5t+C_3$
$5x-3=e^{5t+C_3}$
$5x-3=e^{C_3}e^{5t}$
$5x-3=C_4e^{5t}$
$5x=C_4e^{5t}+3$
$x=\frac{C_4}{5}e^{5t}+\frac{3}{5}$
$$x=C_5e^{5t}+\frac{3}{5}$$
Oh thank fuck, that's one of the answers.

## Q10: 