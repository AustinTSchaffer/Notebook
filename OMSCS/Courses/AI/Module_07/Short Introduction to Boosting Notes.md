---
tags:
  - OMSCS
  - AI
  - ML
---
# Short Introduction to Boosting Notes

Notes on: [[Short-Introduction-to-Boosting_Freund-Schapire.pdf]]

 > The goodness of a weak hypothesis is measured by its error

## AdaBoost
- We pick some max $T$, indicating the max number of iterations we want to follow.
- We initialize the weights of the distribution $D_t(i)=1/m$
- The "error" is calculated based on how many examples were classified incorrectly. The symbol for error is $\epsilon$

$$
\epsilon_t = Pr_{i \space\sim\space D_t} \left[ h_t(x_i) \ne y_i \right]=\sum_{i:h_t(x_i)\ne y_i}D_t(i)
$$

- Using this new definition of error, we train some ML model against the data, minimizing this error.
- Using the resulting error, we calculate $\alpha$

$$
\alpha_t = \frac{1}{2}ln\left(\frac{1-\epsilon_t}{\epsilon_t}\right)
$$

- We always make sure that $\alpha_t \ge 0$.
	- $\epsilon_t \le 1/2 \rightarrow \alpha_t \ge 0$
- Then we update the weights of $D_t$ to create $D_{t+1}$
	- For each example classified correctly: $D_{t+1}=\frac{D_t(i)}{Z_t}*e^{-\alpha_t}$
	- For each example classified incorrectly: $D_{t+1}=\frac{D_t(i)}{Z_t}*e^{\alpha_t}$
	- $Z_t$ is a normalization factor, chosen to make sure that $\sum D_{t+1} = 1$
- The effect is that in the next iteration...
	- examples that were classified correctly in this iteration are deemed less important in the next iteration
	- examples that were classified incorrectly in this iteration are deemed more important in the next iteration
	- These importance values are tuned as the simulation iterates.
- Once we're done learning, the final hypothesis is the weighted sum of all hypotheses. We set $T$ to be the number of hypotheses generated.

$$
H(x)=f\left(\sum_{t=1}^{T} \alpha_th_t(x) \right)
$$

- $f$ is some activation function. It could be the "sign" of the result ($\langle -1, +1 \rangle$. It could return the integer component of the result. etc.

> Intuitively, $\alpha_t$ measures the importance that is assigned to $h_t$.

We can apply this algorithm to more complicated classification problems (more than 2 classes) by breaking those classification problems into a series of binary comparisons. e.g.
- is $y_1$ the classification of $x$?
- is $y_2$ the classification of $x$?
- etc

Probably better methods have been developed since this paper (1999 publish date)
## Analysis
- Benefits
	- Fast simple and easy
	- no parameters except $T$ (and the ML algorithm we want to boost, plus all of its parameters)
	- Applicable to pretty much any ML model
	- The weak hypotheses that are aggregated only have to be better than random for this algorithm to be effective
- Caveats
	- Performance of boosting is dependent on the data and the weak learner. A poor algorithm-problem fit is still possible.
	- Boosting can fail given 
		- insufficient data
		- overly complex weak hypothesis
		- weak hypothesis which is too weak
	- Especially susceptible to noise
- Notes on outliers
	- Examples with the highest weights often turn out to be outliers in the data
	- When the number of outliers is large, the emphasis placed on hard examples can become detrimental to the performance of AdaBoost
	- Variants of AdaBoost periodically check for outliers then de-emphasize them in the training set.
