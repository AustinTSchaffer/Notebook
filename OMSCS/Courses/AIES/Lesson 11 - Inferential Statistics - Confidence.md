---
tags: Inferentuial, Statistics, OMSCS, AIES
---
# Lesson 11 - Inferential Statistics - Confidence

## Empirical Rule
![[Pasted image 20230624115353.png]]

- The bell curve is defined by the mean ($\mu$) and the standard deviation ($\sigma$)
- Empirical Rule: for a normal distribution, 99.7% of all data will fall within 3 standard deviations of the mean.
- Data must follow a normal distribution.
- Many data types do not follow a normal distribution
	- Wealth distribution (long tail)
	- Human behavior (skewed normal)
- Real world data shows high and low variations
- IQ is a normal distribution
	- $\mu = 100$
	- $\sigma = 15$
	- How do you show that 95% of IQ scores in the population are between 70 and 130?
	- 95% Upper bound: $U_{95\%}=\mu+2\sigma$
	- 95% Lower bound: $L_{95\%}=\mu-2\sigma$
- Assume that Subway sandwich sales follows a normal distribution
![[Pasted image 20230624115856.png]]

![[Pasted image 20230624120012.png]]

![[Pasted image 20230624120029.png]]

## Population Proportions and Margin of Error
- A sample of 25 students in a school were asked if they spent over $5 on phone calls over the last week.
- 10 students spent over $5.
- The proportion of the sample of 25 who spent over $5 was: $\frac{10}{25}=0.4=40\%$
- Can we say that 40% of the students in the school (the population) spent over $5?
- We can say whatever we want, but we can't say **for certain**.
- However, we could say with a certain degree of confidence if the sample was large enough and representative, then the proportion of the sample would be approximately the same as the proportion of the population.
- Key terms
	- Population proportions
	- Margin of error
- How confident we are is expressed as a percentage.
- We already saw from the empirical rule that approximately 95% of the area of a normal curve lies within $\pm2$ standard deviations of the mean
- This means that we are 95% certain that the population proportion is within $\pm2$ standard deviations of the sample proportion.
- $\pm2$ standard deviations is our margin of error and the percentage margin of error that this represents depends on the sample size.
	- At 95% level of confidence
	- Margin of Error = $\frac{1}{\sqrt{n}}$
	- Where $n$ is the sample size.
	- Example: if $n=1000$, the percentage margin of error is $\pm3\%$

![[Pasted image 20230624120905.png]]

We can also estimate the confidence interval for population proportion

![[Pasted image 20230624121050.png]]

![[Pasted image 20230624121132.png]]

## Sample Size vs Margin of Error
- The size of the population does not matter when calculating margin of error
	- Assumes that the population is larger than the sample
	- Assumes that the sampling was unbiased
- Margin of error estimates how accurately the results of a poll reflect the "true" feelings of the population
- As sample size increases, margin of error decreases.
- There are diminishing returns in increasing the sample size ($E=n^{-0.5}$).

![[Pasted image 20230624140824.png]]

![[Pasted image 20230624140953.png]]

![[Pasted image 20230624141050.png]]

![[Pasted image 20230624141126.png]]

![[Pasted image 20230624141212.png]]

$n=500$
$n_{green}=60$
$\hat{p}=60/500=12\%$
$MoE=1/\sqrt{500}=4.5\%$

