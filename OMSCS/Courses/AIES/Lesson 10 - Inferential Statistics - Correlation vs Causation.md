---
tags: Inferentuial, Statistics, OMSCS, AIES
---
# Lesson 10 - Inferential Statistics: Correlation vs Causation

> Researchers in the early 1900s believed that there was a causal relationship between ice cream and polio, because polio cases spiked in the summer, and ice cream sales also spiked in the summer.

## Introduction
- Correlation tells us that 2 variables are related.
	- Height vs Weight
	- Time spent exercising vs calories burned
- Types of relationships reflected in correlation
	- Causal relationships
		- X causes Y or
		- Y causes X
	- Spurious relationships
		- X and Y are caused by a third variable Z

> Ice cream sales spike on hot summer days. You can't say that ice cream causes hot summer days.

**Correlation does not imply causation.**

**CORRELATION DOES NOT IMPLY CAUSATION.**

![[Pasted image 20230624103632.png]]

- Weak Positive Correlation: 0.0 to 0.39
- Moderate Positive Correlation: 0.4 to 0.69
- Strong Positive Correlation: 0.7 to 1.0
- There's also "X Negative Correlation". Just multiply all these values by `-1.0`

https://rpsychologist.com/correlation/

![[Pasted image 20230624104022.png]]

## Examples
![[Pasted image 20230624104249.png]]

![[Pasted image 20230624104303.png]]

http://www.tylervigen.com/

## Relationships
- A strong relationship between 2 variables does not always mean that changes in one variable causes changes in the other
- The relationship between 2 variables is often influenced by other variables which are lurking in the background
- There are 2 relationships which can be mistaken for causation
	- **Common response:** refers to the possibility that a change in a lurking variable is causing changes in both our explanatory variable and our response variable
	- **Confounding**: refers to the possibility that either the change in our explanatory variable is causing changes in the response variable, OR that a change in a lurking variable is causing changes in the response variable.

## Measuring Linear Correlation with SciPy
**Linear correlation coefficient:** a measure of the strength and direction of a linear association between two random variables (also called the Pearson product-moment correlation coefficient)

```python
from scipy import stats
scipy.stats.pearsonr(X, Y)
```

- The linear correlation coefficient quantifies the strengths and directions of movements in two random variables
- Correlations of -1 or +1 imply an exact linear relationship
- Positive correlations imply that as x increases, so does y.
- Negative correlations imply that as x increases, y decreases.
