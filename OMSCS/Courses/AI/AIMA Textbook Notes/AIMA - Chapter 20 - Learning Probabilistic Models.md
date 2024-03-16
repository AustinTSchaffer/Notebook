---
tags:
  - OMSCS
  - AI
  - AIMA
  - ML
---
# AIMA - Chapter 20 - Learning Probabilistic Models

## 20.1 Statistical Learning
Key terms and section headers
- data
- hypotheses
- evidence
- bayesian learning
- hypothesis prior
- likelihood
- maximum a posteriori (MAP, pronounced M-A-P)
- minimum description length (MDL)
- uniform
- maximum-likelihood hypothesis ($h_{ML}$)

## 20.2 Learning with Complete Data
key terms and section headers
- density estimation
- complete data
- parameter learning
- maximum-likelihood parameter learning : discrete models
	- log likelihood
- Naive Bayes Models
- generative and discriminative models
	- generative model
	- discriminative model
- maximum-likelihood parameter learning : continuous models
	- linear-Gaussian
	- linear regression
- Bayesian parameter learning
	- beta distributions
	- hyperparameters
	- virtual counts
	- parameter independence
- Bayesian linear regression
	- uninformative prior
- learning Bayes net structures
- Density estimation with nonparametric models
	- nonparametric density estimation
	- k-nearest-neighbors
	- kernel functions

## 20.3 Learning with Hidden Variables: The EM Algorithm
Key terms and section headers

- hidden variables (latent variables)
- expectation-maximization
- unsupervised clustering: learning mixtures of gaussians
	- unsupervised clustering
	- mixture distribution
	- components
	- mixture of gaussians
	- E-STEP
	- M-STEP
	- indicator variables
- learning bayes net parameter values for hidden variables
	- naive Bayes
	- indentifiable / identifiability
- learning hidden markov models
	- HMMs
	- forward-backward algorithm
	- smoothing
	- filtering
- The general form of the EM algorithm
- learning bayes net structures with hidden variables
	- structural EM

## Summary
- Bayesian learning methods formulate learning as a form of probabilistic inference, using the observations to update a prior distribution over hypotheses. This approach provides a good way to implement Ockham’s razor, but quickly becomes intractable for complex hypothesis spaces.  
- Maximum a posteriori (MAP) learning selects a single most likely hypothesis given the data. The hypothesis prior is still used and the method is often more tractable than full Bayesian learning.  
- Maximum-likelihood learning simply selects the hypothesis that maximizes the likelihood of the data; it is equivalent to MAP learning with a uniform prior. In simple cases such as linear regression and fully observable Bayesian networks, maximum- likelihood solutions can be found easily in closed form. Naive Bayes learning is a particularly effective technique that scales well.  
- When some variables are hidden, local maximum likelihood solutions can be found using the expectation maximization (EM) algorithm. Applications include unsupervised clustering using mixtures of Gaussians, learning Bayesian networks, and learning hidden Markov models.  
- Learning the structure of Bayesian networks is an example of model selection. This usually involves a discrete search in the space of structures. Some method is required for trading off model complexity against degree of fit.  
- Nonparametric models represent a distribution using the collection of data points. Thus, the number of parameters grows with the training set. Nearest-neighbors methods look at the examples nearest to the point in question, whereas kernel methods form a distance-weighted combination of all the examples.

> Statistical learning continues to be a very active area of research. Enormous strides have been made in both theory and practice, to the point where it is possible to learn almost any model for which exact or approximate inference is feasible.