---
tags: OMSCS, AIES
---
# Lesson 05 - Fairness and Bias

## What is Bias

Algorithmic bias concepts
- Motivation and examples
- Sources of algorithmic bias
- Types of bias
- Measures of bias

Biases are related to:
- Stereotypes
- Prejudice
- Discrimination

## An incorrect assumption about AI
- Discrimination is prohibited based on the basis of membership in a protected class group
- Law prohibits this
- People's decisions include objective and subjective elements, therefore they can be biased
- If algorithmic inputs only include objective elements, therefore the should not be biased (THIS IS A FALLACY)

#COMPAS

![[Pasted image 20230530160741.png]]

![[Pasted image 20230530160815.png]]

- AdFisher:
	- https://github.com/tadatitam/info-flow-experiments
	- A tool for running automated experiments on personalized ad settings
	- Used to demonstrate that settings gender=female results in less ads for high-paying jobs on job-related websites

## Algorithmic Bias
Training models on biased data sets results in biased models.

![[Pasted image 20230530161026.png]]

Self-fulfilling prophecy, "the spiral"

![[Pasted image 20230530161052.png]]

Confounding matters
- Algorithms are black boxes
- considered proprietary
- outside of the jurisdiction of regulation
- Bias within algs becomes obscured
- Mitigation is more difficult

## Biases in Data
![[Pasted image 20230530161336.png]]

![[Pasted image 20230530161520.png]]

![[Pasted image 20230530161551.png]]

**Problem:** It is difficult to identify which specific group the algorithm might be biased against.

![[Pasted image 20230530163130.png]]

## Fairness
![[Pasted image 20230530163625.png]]

![[Pasted image 20230530163652.png]]

![[Pasted image 20230530163743.png]]

![[Pasted image 20230530163820.png]]

## Quantifying Fairness
![[Pasted image 20230530163928.png]]

![[Pasted image 20230530164026.png]]

