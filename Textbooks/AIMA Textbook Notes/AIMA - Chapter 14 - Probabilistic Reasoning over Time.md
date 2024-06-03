---
tags:
  - OMSCS
  - AI
  - AIMA
---
# AIMA - Chapter 14 - Probabilistic Reasoning over Time

Agents in partially observable environments must
- maintain a belief state
- use a transition model to predict how the world might evolve
- use a sensor model to update their belief state

This chapter describes three specific kinds of models
- hidden Markov models (HMMs)
- Kalman filters
- dynamic Bayesian networks
	- super-set which includes HMMs and Kalman filters as special cases

## 14.1 Time and Uncertainty
- previous chapters have covered static worlds, where random variables have single fixed values
- this chapter covers dynamic worlds, where random variables can change over time
### states and observations
- this chapter covers "discrete-time" models
- the world is viewed as a series of snapshots or "time slices"
- the time interval between slices ($\Delta$) is typically assumed to be the same between all pairs of slices
- Uncertainty over continuous time can be modeled by **stochastic differential equations** (SDEs). The models in this chapter can be viewed as discrete-time approximations to SDEs.
- Each time slice contains a set of random variables, some observable, some not. For simplicity, we assume that the same subset of variables are observable at each time slice
	- $X_t$ denotes the set of state variables at time $t$
	- $E_t$ denotes the set of observable evidence variables
	- The observation at time $t$ is $E_t=e_t$ for some set of values $e_t$
	- The notation $X_{a:b}$ denotes the set of variables from $X_a$ to $X_b$, inclusive of $X_b$.
### transition model
- the transition model specifies the probability distribution over the latest state variables, given the previous values.
- $P(X_t \space|\space X_{0:t-1})$
- Problem: $X_{0:t-1}$ is unbounded as time increases
- We make a **Markov assumption** that the current state depends on only a *finite fixed number* of previous states
- Processes that use this assumption are called **Markov processes** or **Markov chains**
- First-order Markov chains
	- only use the previous state
	- $P(X_t \space|\space X_{0:t-1}) = P(X_t \space|\space X_{t-1})$
- Second-order Markov chains
	- only use the last 2 states
	- $P(X_t \space|\space X_{t-2},X_{t-1})$
- We assume that changes in the world state are caused by a **time-homogenous** process, a process that does not change over time. The advantage is simplicity, we don't need a separate probability table for each $t$.
### sensor model
- We make a **sensor Markov assumption** to reject the idea that $E_t$ could depend on previous variables as well as the current state variables.
- $P(E_t \space|\space X_{0:t}, E_{1:t-1}) = P(E_t \space|\space X_t)$
- $P(E_t \space|\space X_t)$ is the sensor model, also called the **observation model**

![[Pasted image 20240319170128.png]]

### Combining it all
We also need an initial state model: $P(X_0)$. Now we have enough to specify the complete joint distribution over all variables for any time step $t$
$$
P(X_{0:t},E_{1:t})=P(X_0)\prod_{i=1}^{t}P(X_i \space|\space X_{i-1})P(E_i \space|\space X_i)
$$
Recap
- Markov chains are very similar to Bayesian networks except they can handle an infinite number of variables.
- Initial state model: $P(X_0)$
- Transition model: $P(X_i \space|\space X_{i-1})$ (For first-order markov chains)
- Sensor model: $P(E_i \space|\space X_i)$

2 methods for increasing the accuracy of a Markov model
- Increase the order of the Markov process model.
- Increasing the set of state variables.

## 14.2 Inference in Temporal Models
- **Filtering** or **state estimation** is the task of computing the **belief state** $P(X_t \space|\space e_{1:t})$
- The belief state is the posterior distribution over the most recent state given all evidence to date
- Filtering is what a rational agent does to keep track of the current state so that rational decisions can be made.
- The term "filtering" comes from signal processing, where a lot of work has gone into filtering noise out of a signal by estimating its underlying properties.
- Prediction
	- task of computing the posterior distribution over the future state, given all evidence to date
	- Goal is to compute: $P(X_{t+k} \space|\space e_{1:t})$
- Smoothing
	- This is the task of computing the posterior distribution over a past state, given all evidence up to the present.
	- Goal is to compute: $P(X_{k} \space|\space e_{1:t})$
	- $0 \le k \lt t$
- Most likely explanation
	- Given a sequence of observations, find the sequence of states that is most likely to have generated those observations.
	- Goal is to compute: $argmax_{x_{1:t}} P(x_{1:t} \space|\space e_{1:t})$
- Learning
	- The transition and sensor models can be learned from observations.
	- Dynamic bayes net learning can be done as a by-product of inference.
	- See [[AIMA - Chapter 20 - Learning Probabilistic Models]]

### Filtering and Prediction
- a useful filtering alg needs to maintain a current state estimate and update it, rather than going back over the entire history of percepts for each update.
- Given the result of filtering up to time $t$, the agent needs to compute the result for $t+1$ from the new evidence $e_{t+1}$.
$$
P(X_{t+1} \space|\space e_{1:t+1})=f(e_{t+1}, P(X_t \space|\space e_{1:t}))
$$
- This is called **recursive estimation**
- we can view the calculation as
	- the current state distribution is project forward from $t$ to $t+1$
	- the projected state distribution is updated using new evidence
- $P(X_{t+1} \space|\space e_{1:t+1})$
	- $=P(X_{t+1} \space|\space e_{1:t},e_{t+1})$ (dividing up the evidence)
	- $=\alpha P(e_{t+1} \space|\space X_{t+1},e_{1:t})P(X_{t+1} \space|\space e_{1:t})$ (using bayes rule given $e_{1:t}$)
	- $=\alpha P(e_{t+1} \space|\space X_{t+1})P(X_{t+1} \space|\space e_{1:t})$ (by the sensor Markov assumption)
		- The update: $P(e_{t+1} \space|\space X_{t+1})$
		- The prediction: $P(X_{t+1} \space|\space e_{1:t})$
	- $\alpha$ is a normalizing constant used to make probabilities sum to 1.

If we plug in an expression for the one-step prediction $P(X_{t+1} \space|\space e_{1:t})$ obtained by conditioning on the current state $X_t$, the result is the central point of this chapter.

![[Pasted image 20240320165008.png]]

- all the terms come from either the model or from the previous state estimate
- we can think of the filtered estimate $P(X_t \space|\space e_{1:t})$ as a "message" $\text{f}_{1:t}$ that is propagated forward along the sequence, modified by each transition and updated by each new observation
- $\text{f}_{1:t+1}=\text{Forward}(\text{f}_{1:t},e_{t+1})$
- $\text{Forward}$ implements the update described in the "central point" of this chapter. (Equation 14.5)
- The process begins with $\text{f}_{1:0}=P(X_0)$
- When all the state variables are discrete, the time and space required for each update is constant (independent of $t$)
- The task of **prediction** can be seen simply as filtering without the addition of new evidence.
- It is possible to derive the following recursive computation for predicting the state at $t+k+1$ from a prediction for $t+k$

![[Pasted image 20240320165832.png]]

- this computation only involves the transition model and not the sensor model

- the **stationary distribution** is what you get when you try to predict arbitrarily far into the future. The predicted distribution will converge to a fixed point, after which it remains constant.
- the **mixing time** is roughly the time required to reach the fixed point without any new evidence.
- The mixing time is shorter for more uncertain transition models
- you can't reliably predict more than $s$ steps into the future
	- $t_m$ is the mixing time
	- $s << t_m$

### Smoothing
- recap: it's the process of computing the distribution over past states given evidence up to the present
- we can split the computation into 2 parts, the evidence in range $1:k$ and the evidence in range $k+1:t$

![[Pasted image 20240320171012.png]]

- we can also run the simulation in reverse

![[Pasted image 20240320171054.png]]

We can wrap this computation in a function called $\text{Backward}$

$$
b_{k+1:t}=\text{Backward}(b_{k+2:t},e_{k+1})
$$

For performance, cache results to reduce the amount of re-computation required.

Yo, check out this algorithm

![[Pasted image 20240320171626.png]]

- This is an application of the clustering algorithm, which yields a linear time algorithm, which computes smoothed estimates for the entire sequence.
- Forms the computational backbone for many applications that deal with sequences of noisy observations.
- It has 2 practical drawbacks
	- Space complexity
		- can be too high when the state space is large and the sequences are long.
		- It uses $O(|\text{f}|t)$ space, where $|\text{f}|$ is the size of the representation of the forward message.
		- In some cases we can swap $t$ for $log(t)$ or even $1$.
	- offline
		- needs to be modified to work in an online setting, where smoothed estimates must be computed for earlier time slices, as new observations are added to the end of the sequence.
		- Most common requirement is for **fixed-lag smoothing**, which requires computing a smoothed estimate for some fixed number of $d$ past states: $P(X_{t-d} \space|\space e_{1:t})$
		- Sometimes can be done in constant time per new data point, independent of the lag $d$
### Finding the most likely sequence
- wrong approach
	- use smoothing to find the posterior distribution at each time step
	- construct the sequence, using at each step the weather that is most likely according to the posterior
	- wrong because it only considers distributions over single time steps, not the joint probabilities over all time steps
- there is a recursive relationship between the most likely paths to each state $x_{t+1}$ and most likely paths to each state $x_t$
- we can use the recursive property to construct a recursive algorithm for computing the most likely path given the evidence. $m_{1:t}$ is a recursively computed message.
$$
m_{1:t}=\max_{x_{1:t-1}}P\left( x_{1:t-1}, X_t, e_{1:t} \right)
$$
- to obtain the recursive relationship between $m_{1:t+1}$ and $m_{1:t}$, just follow this hot garbage

![[Pasted image 20240320195026.png]]

- This is the **Viterbi algorithm**
	- $O(t)$ time and space complexity
	- needs to keep pointers that identify the best sequence leading to each state
- on a practical note, numerical underflow is a significant issue for the Viterbi algorithm. implementations either
	- normalize $m$ at each step by scaling everything up
	- use logarithm trickery

## 14.3 Hidden Markov Models (HMMs)
- temporal probabilistic model in which the state of the process is described by a single, discrete random variable.
- models with two or more state variables encode the variables in a tuple
- this allows the algorithms to use matrix algebra
- there is no restriction on the evidence variables
	- one, or many?
	- discrete or continuous?
	- all's good my dude.

### Simplified matrix algorithms
- let the state variable $X_t$ have values denoted by integers 1 to $S$, where $S$ is the number of possible states
- the transition model $P(X_t \space|\space X_{t-1})$ becomes an $S \times S$ matrix $\text{T}$ where: $\text{T}_{ij}=P(X_t=j \space|\space X_{t-1}=i)$
- $T_{ij}$ is the probability of a transition from state i to state j
- We also put the sensor model in matrix form
- For mathematical convenience, we encode the evidence as an $S\times S$ diagonal **observation matrix**, $\text{O}_t$
- The i-th diagonal entry of $\text{O}_t$ is $P(e_t \space|\space X_t=i)$
- If we use column vectors to represent the forward and backward messages, all the computations become simple matrix-vector operations
	- Forward: $\text{f}_{1:t+1}=\alpha \text{O}_{t+1}\text{T}^\top \text{f}_{1:t}$
	- Backward: $\text{b}_{k+1:t}=\text{T} \text{O}_{k+1} \text{b}_{k+2:t}$
- Alg complexity of this
	- Time: $O(S^2 t)$ - $S$-element vector being multiplied by an $S\times S$ matrix.
	- Space: $O(St)$ - forward pass stores $t$ vectors of size $S$
- We can also manipulate the forward equation to be applied backward through inversion and transposition: $\text{f}_{1:t}=\alpha' (\text{f}^\top)^{-1} \text{O}^{-1}_{t+1} \text{f}_{1:t+1}$

Here's another algorithm definition

![[Pasted image 20240320201314.png]]

### Hidden Markov model example: Localization
The chapter contains an example from robot world, where the robot moves to a random adjacent square and each of its 4 wall-detecting sensor report errors with a frequency of $\epsilon$

![[Pasted image 20240320202138.png]]

This example, and added a few additional parameters to the number of possible states, shows that encoding the transition matrix as described above is not manageable when the number of possible states is high.

| Number of states | size of $\text{T}$ |
| ----------------:| ------------------:|
|               42 |             $42^2$ |
|              168 |            $168^2$ |
|         $2^{42}$ |       $(2^{42})^2$ |

> HMMs have many uses in areas ranging from speech recognition to molecular biology, they are fundamentally limited in their ability to represent complex processes.

## 14.4 Kalman Filters
- Reminder that filtering is estimating state variables from noisy observations over time.
- If the variables are discrete, we can model them with a hidden Markov model.
- If variables are continuous, we can use **Kalman filtering**.

- Take newtonian motion as an example
- Taking only $X$ position and $\dot{X}$ velocity into consideration, with gaussian noise added to account for wind or whatever, we obtain a linear-Gaussian transition model.
$$
P(X_{t+\Delta}=x_{t+\Delta} \space|\space X_t=x_t,\dot{X}_t=\dot{x}_t)=N(x_{t+\Delta};x_t+\dot{x}_t\Delta, \sigma^2)
$$
- ezpz
- The chapter will go into more depth later, but for the purposes of immediacy
	- We're using a **multivariate Gaussian** distribution
	- $d$ variables
	- specified by a $d$-element mean $\mu$ and a $d\times d$ covariance matrix $\Sigma$

![[Pasted image 20240320205831.png]]

### Updating Gaussian distributions
- a key property of the linear-Gaussian family of distributions is that they remain closed under bayesian updating
- given any evidence, the posterior is still in the linear-Gaussian family

1. If the current distribution $P(X_t \space|\space e_{1:t})$ is Gaussian and the transition model $P(X_{t+1} \space|\space x_t)$ is linear-Gaussian, then the one-step predicted distribution given by the following equation is also a Gaussian distribution. $$\int_{x_t}P(X_{t+1}|x_t)P(x_t|e_{1:t})dx_t$$
2. If the prediction $P(x_{t+1}|e_{1:t})$ is Gaussian and the sensor model $P(e_{t+1}|X_{t+1})$ is linear-Gaussian, then the updated distribution is also a Gaussian distribution. $$P(X_{t+1}|e_{1:t+1})=\alpha P(e_{t+1}|X_{t+1})P(X_{t+1}|e_{1:t})$$

The forward operator for Kalman filtering takes a Gaussian forward message ($\text{f}_{1:t}$), specified by a mean ($\mu_t$), and covariance ($\Sigma_t$), and produces a new multivariate Gaussian forward message, specified by a new mean and covariance.

![[Pasted image 20240321174612.png]]

- we can interpret the calculation for the new mean as a weighted mean of the new observation and the old mean.
	- if the observation is unreliable, then the variance of the observation ($\sigma_z^2$) is large, and we pay more attention to the old mean
	- if the old mean is unreliable, then the variance of the old mean ($\sigma_t^2$) is large and we pay more attention to the new observation
	- if the process is highly unpredictable, then that variance ($\sigma_x^2$) is large, and we pay more attention to the new observation
- the update for the variance is independent of the observation. This means we can compute what the sequence of variance values will be in advance.
- The sequence of variance values quickly converges to a fixed value that depends only on $\sigma_x^2$ and $\sigma_z^2$, simplifying calculations

### The general case
- both the transition model and the sensor model are required to be a linear transformation with additive gaussian noise

![[Pasted image 20240321175912.png]]

$$
K_{t+1}=(\text{F}\Sigma_t\text{F}^\top+\Sigma_x)\text{H}^\top\left(\text{H}\left(\text{F}\Sigma_t\text{F}^\top+\Sigma_x\right)\text{H}^\top+\Sigma_z\right)^{-1}
$$

This is the **Kalman gain matrix**

![[Pasted image 20240321180324.png]]

### Applicability
- radar tracking of
	- missles
	- aircraft
- acoustic tracking of submarines and ground vehicles
- visual tracking of vehicles and people
- "Kalman filters are used to reconstruct particle trajectories from bubble-chamber photographs and ocean currents from satellite surface measurements"
- any system characterized by continuous state variables and noisy measurements
	- pulp mills
	- chemical plans
	- nuclear reactors
	- plant ecosystems
	- economies
- the **extended Kalman filter (EKF)** attempts to overcome nonlinearities in the system being modeled. A system is **nonlinear** if the transition model cannot be described as a matrix multiplication of the state vector.

![[Pasted image 20240321180855.png]]

The standard solution to the problem in the diagram above is a **switching Kalman filter**
- multiple Kalman filters run in parallel
- each uses a different model of the system
- a weighted sum of predictions is used, where the weight depends on how well each filter fits the current data

## 14.5 Dynamic Bayesian Networks
- Abbreviated **DBNs**
- handle probability models
- each slice of a DBN can have any number of state variables and evidence variables
- for simplicity
	- assume that all variables/links/conditional-distributions are exactly replicated from slice to slice
	- assume that the DBN represents a first-order Markov process (each variable can have parents only in its own slice or the immediately preceding slice)
- Corresponds to a Bayesian network with infinitely many variables.
- every HMM can be represented as a DBN with a single state variable. and a single evidence variable
- every discrete-variable DBN can be represented as an HMM

> by decomposing the state of a complex system into its constituent variables, we can take advantage of sparseness in the temporal probability model.

- an HMM representation for a temporal process with $n$ discrete variables, each with up to $d$ values, needs a transition matrix of size $O(d^{2d})$
- The DBN representation has size $O(nd^k)$ if the number of parents of each variable is bounded by $k$

![[Pasted image 20240321200703.png]]

## Summary

This chapter has addressed the general problem of representing and reasoning about probabilistic temporal processes. The main points are as follows:

- The changing state of the world is handled by using a set of random variables to represent the state at each point in time.  
- Representations can be designed to (roughly) satisfy the Markov property, so that the future is independent of the past given the present. Combined with the assumption that the process is time-homogeneous, this greatly simplifies the representation.
- A temporal probability model can be thought of as containing a transition model describing the state evolution and a sensor model describing the observation process. The principal inference tasks in temporal models are filtering (state estimation), prediction, smoothing, and computing the most likely explanation. Each of these tasks can be achieved using simple, recursive algorithms whose run time is linear in the length of the sequence.  
- Three families of temporal models were studied in more depth: hidden Markov models, Kalman filters, and dynamic Bayesian networks (which include the other two as special cases).  
- Unless special assumptions are made, as in Kalman filters, exact inference with many state variables is intractable. In practice, the particle filtering algorithm and its descendants are an effective family of approximation algorithms.