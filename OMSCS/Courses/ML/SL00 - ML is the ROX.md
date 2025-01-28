---
tags:
  - OMSCS
  - ML
---
# SL00 - ML is the ROX
> ML is just applied statistics.

About a broader notion of computational artifacts that learn over time. ML is about the math, science, and computer engineering required to apply statistical models to data.

## Supervised Learning
- take labeled data sets
- generate a model based on that labeled data set
- apply labels to data that it wasn't trained on
- it's "function approximation"

## Induction and Deduction
- Assumptions include
	- data is good
	- function is well-behaved
- bias and inductive bias
- supervised learning is all about induction
- deduction is about going from general rules to specific instances. Classical AI is based almost purely on deduction.
- induction is more about probabilities

## Unsupervised Learning
- no examples
- just inputs
- derive structure from the relationship between the datapoints themselves
- "all 4 legged animals are dogs"
- supervised learning is approximation
- unsupervised learning is description / summarization

## Reinforcement Learning
- "learning from delayed reward"
- Where were the mistakes made?
- Which moves mattered?

## Comparison
- "all of these problems are sort of the same problem"
- "all of these problems are some form of optimization"
	- SL: "model labels data well"
	- RL: "model's behavior scores well"
	- UL: "model's clusters score well"
- Data is king in ML
- Data is central. The algorithms are not central.
