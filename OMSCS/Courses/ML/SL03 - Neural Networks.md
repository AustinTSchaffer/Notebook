---
tags:
  - OMSCS
  - ML
---
# SL03 - Neural Networks
- perceptron unit
	- incoming vector ($X$)
	- weights vector ($W$)
	- activation function (typically $\sum_i X_iW_i$)
	- threshold ($\theta$)

## How powerful is a perceptron unit?
A single perceptron is effectively a linear thresholding function

![[Pasted image 20250111145357.png]]

This perceptron represents an AND gate.

![[Pasted image 20250111145552.png]]

- You can make an OR gate with $W=\{0.5, 0.5\}, \theta=0.5$
- You can make a NOT gate with $W=\{-1\}, \theta=0$
- You can chain 2 perceptrons together to create an XOR gate.
	- Make one of the perceptrons an AND gate
	- Feed $X_1$ and $X_2$ to the 2nd perceptron as inputs
	- feed the output of the AND gate to the 2nd perceptron as $X_3$
	- set the weights to $\{1, 1, -2\}$, so that the result of the AND gate overrides the X values when both are on.
	- set $\theta=1$

## Perceptron Training
- perceptron rule (threshold)
- gradient descent (aka delta rule) (unthresholded)

### Perceptron Rule
$W_i=W_i+\Delta W_i$
$\Delta W_i = n (y - \hat{y})X_i$
$\hat{y}=\sum_iW_iX_i\ge 0$

Run this in a loop while there is "some error". The "error" value is $y-\hat{y}$.

- $n$ is the "learning rate" (it's a scale down factor)
- $y$ is the actual value (the target)
- $\hat{y}$ is the predicted value

If the data is "linearly separable", then the perceptron rule will be able to find the line that separates the data with a finite number of iterations.

### Gradient Descent
"activation": $a=\sum_iX_iW_i$ 
$\hat{y}=\{a\ge0\}$
$E(W)=\frac{1}{2}\sum_{(x,y)\in D}(y-a)^2$

Taking a partial derivative of $E(w)$ gets you: $\sum_{(x,y)\in D}(y-a)(-X_i)$

$\Delta W_i=n(y-a)X_i$

> The difference between the activation and the input data variable.

More robust to data sets that are not linear separable, but converges to a local optima.

The $\Delta W_i$ equations look pretty similar between this one and the perceptron rule.

### Sigmoid, a differentiable threshold
It's an S-curve function. It's an activation function that's differentiable.

$$\sigma(a)=\frac{1}{1+e^{-a}}$$
- $\sigma(a=0)=\frac{1}{2}$
- $a \rightarrow -\infty: \sigma(a)\rightarrow0$
- $a \rightarrow +\infty: \sigma(a)\rightarrow1$
- The derivative of the sigmoid function is $\sigma(a)(1-\sigma(a))$
- How do we x-scale the sigmoid output?

## Neural Network
> Using a network of sigmoid units, we can connect an input layer to an output prediction.

![[Pasted image 20250112150316.png]]

- The whole thing is differentiable.
- Using back propagation, a computationally beneficial organization of the chain rule, we can adjust the weights of the network.
- sometimes called "error back propagation"
- We can replace the sigmoid units with another differentiable function.
- This is NOT a perceptron.
- The error function can have many local optima. Simulated annealing may help with this?

## Optimizing Weights
$Optimization \approx learning$

- gradient descent
- advanced methods
- "momentum", descent can pop over a small hill toward a potentially deeper local minimum
- higher-order derivatives
- randomized optimization
- penalty for "complexity" in the network
	- similar to regression overfitting
	- similar to large tree overfitting
	- more nodes $\rightarrow$ fewer nodes
	- more layers $\rightarrow$ fewer layers
	- larger numbers $\rightarrow$ smaller numbers

## Restriction Bias
- representational power
- set of hypotheses we will consider
- perceptron: half-spaces
- sigmoids
	- much more complex
	- not much restriction
- boolean
	- network of threshold-like units
- continuous
	- "connected" no jumps - hidden
- arbitrary
	- stitch together - two hidden
- typically give a neural net...
	- bounded number of layers
	- bounded number of nodes in each layer
	- typically use cross-validation to determine these settings and also decide when to stop training

## Preference Bias
- Algorithm selection of one representation over another?
- What algorithm?
- Gradient descent?
- Initial weights? Typically small random values.
- Occam's razor of ML: If you're getting similar results with a complex algorithm and a simpler algorithm (similar error rates), prefer the simpler algorithm.