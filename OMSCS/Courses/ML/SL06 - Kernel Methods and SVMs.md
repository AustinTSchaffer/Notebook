---
tags:
  - OMSCS
  - ML
---
# SL06 - Kernel Methods and SVMs
- Support Vector Machines (SVMs)

![[Pasted image 20250129085648.png]]

The lines closer to the existing datapoints are likely to overfit the training data.

The middle line does the best job of separating / describing the data while also "committing the least to it".

The line should leave "as much space as possible" from the boundaries.

![[Pasted image 20250129090534.png]]

- Line eq: $y=mx+b$
- Hyperplane eq: $y=w^Tx+b$
	- $y$ is the classification label
	- $w$ and $b$ are parameters of the plane

- $y=0$ at the decision boundary
- $y=+1$ at the top grey line
- $y=-1$ at the bottom grey line
- Distance between the grey lines should be as far as possible. (this is a "vector")
	- $w^Tx_1+b=+1$
	- $w^Tx_2+b=-1$
	- $(w^Tx_1-w^Tx_2)+(b-b)=(+1-(-1))$
	- $w^T(x_1-x_2)=2$
	- $w^T(x_1-x_2)/||w||=2/||w||$
	- $m=w^T(x_1-x_2)/||w||$
	- $m=2/||w||$
	- $m \text{ is the margin}$

## Still Support Vector Machines

Maximize $\frac{2}{||w||}$ while classifying everything correctly:
$$
y_i(w^Tx_i+b)\ge1 : \forall_i
$$
We're multiplying by $y_i$ as a clever trick for making the inequality work.

- The same thing can be accomplished by minimizing $\frac{1}{2}||w||^2$
- This is "easier" because it's a quadratic programming problem
	- These always have a solution and it's always a unique solution.
	- It's a whole field unto itself.
	- We can just plug and play.

Maximize:
$$W(\alpha)=\sum_i\alpha_i-\frac{1}{2}\sum_{i,j}
\alpha_i\alpha_jy_iy_jx_i^Tx_j$$
-with constraints:
$$
\alpha_i\ge0,\space\sum_i\alpha_iy_i=0
$$
> Other people know how to do this and have written code for us.

## Goal: Use Quadratic Programming
- $w=\sum_i\alpha_iy_ix_i, \space b$
- $\alpha$ is mostly 0
- Some of the vectors matter for this
- Some of the vectors do not.
- Only the vectors with non-zero alphas matter.
- The points that are far away from the decision boundary don't matter.
- "It's like KNN except you've already done the work of figuring out which points matter and which don't." Essentially, you just need to keep the points that define the boundary.
- The quadratic program determines which points matter.
- From the earlier equation: $x_i^Tx_j$
	- This is the "dot product" of $x_i$ and $x_j$
	- The result is a number. It's a large number if the vectors are pointing in the same direction. It's a large negative number of the vectors are pointing in the opposite direction. It's near zero of the vectors are perpendicular. #LinAlg
	- This effectively determines how similar the datapoints are and we're then multiplying the result by their classification labels

## Linearly Married
Define a function 
$$\Phi(q)=\langle q_1^2, q_2^2, q_1q_2\sqrt{2} \rangle$$
We're reprojecting the data into an additional dimension. So then this

$$W(\alpha)=\sum_i\alpha_i-\frac{1}{2}\sum_{i,j}
\alpha_i\alpha_jy_iy_jx_i^Tx_j$$
$x^Ty$ becomes $\Phi(x)^T\Phi(y)$ 

$$\Phi(x)^T\Phi(y)$$
$$=\langle x_1^2,x_2^2,x_1x_2\sqrt{2} \rangle^T\langle y_1^2,y_2^2,y_1y_2\sqrt{2} \rangle$$
$$=x_1^2y_1^2+2x_1x_2y_1y_2+x_2^2y_2^2$$
$$=(x_1y_1+x_2y_2)^2$$
$$=(x^Ty)^2$$

![[Pasted image 20250129105129.png]]

- With all this crazy math, we can reproject data that is not linearly separable into a higher dimensional space, making it now linearly separable.
- We then did more math to avoid performing that transformation.
- This is the "Kernel Trick". We were able to avoid $\Phi$.

$$W(\alpha)=\sum\alpha_i-\frac{1}{2}\sum_{i,j}\alpha_i\alpha_jy_iy_jK(x_i,x_j)$$
- Options for $K$
	- $K=(x^Ty)^2$
	- $K=x^Ty$
	- Polynomial Kernel: $K=(x^Ty+c)^P$
	- Sigmoidal (gaussian-ish): $K=e^{-(||x-y||^2/2\sigma^2)}$
	- $K=\text{tanh}(\alpha x^Ty+\theta)$
- Kernel functions are a dime a dozen. Which ones work better in which circumstances requires research.
- Mercer Condition - Requirement for a kernel function to work

## SVMs
- margins
	- generalization
	- overfitting
- big is better
- quadratic programming: optimization problem for finding max margins
- support vectors
- kernel functions / kernel "trick"
	- project data into a higher dimensional space
	- kernel functions must satisfy the Mercer Condition

## Back to Boosting
- Doesn't seem to overfit
- error
- confidence

$$\text{H}_{\text{find}}(x)=\text{sign}(\frac{\sum_t\alpha_th_t(x)}{\sum\alpha_t})$$
Reminders
- $\alpha$ is a measure of how good a hypothesis was
- $\alpha$ is always better than "chance"

As you add more and more weak learners to the aggregate model, it effectively creates bigger and bigger margins between positive and negative examples, increasing its confidence and reducing its error.

![[Pasted image 20250129210425.png]]


