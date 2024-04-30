---
tags:
---
# 01 - Machine Learning Potentials for Large-Scale Simulations
> By Geonu Kim - Staff Researcher - Samsung

https://omscs.gatech.edu/machine-learning-potentials-large-scale-simulations

- Paper: https://openreview.net/forum?id=hr9Bd1A9Un&referrer=%5Bthe%20profile%20of%20Yongdeok%20Kim%5D(%2Fprofile%3Fid%3D~Yongdeok_Kim1)
	- Title: Benchmark of Machine Learning Force Fields for Semiconductor Simulations: Datasets, Metrics, and Comparative Analysis
	- Authors: Geonu Kim and Byunggook Na and Gunhee Kim and Hyuntae Cho and Seungjin Kang and Hee Sun Lee and Saerom Choi and Heejae Kim and Seungwon Lee and Yongdeok Kim
	- Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track
	- 2023
	- https://openreview.net/forum?id=hr9Bd1A9Un
- Repo: https://github.com/SAITPublic/MLFF-Framework

![[Pasted image 20240430102814.png]]

Image Source: https://www.nature.com/articles/s41524-022-00765-z

## Accelerated Materials Discovery
- automated material characterization -> AI-guided design
- AI-guided design -> automated chemical synthesis
- automated chemical synthesis -> automated material characterization
- automated chemical synthesis -> **new advanced materials**

- Promising candidates $M^*$
- target property: $f(M)$
- $M^* = argmax_M \space f(M)$

## Density Functional Theory
Research is to use ML to simulate DFT, because DFT requires a lot of computation power above a certain size scale. DFT is comparable to an $O(n^3)$ algorithm.

## MLFF - Machine Learning Force Fields
predicts
- $\text{energy} E \in R$
- forces (equation on slide)

Algorithms for MLFF
- Artificial neural nets (ANNs)
- Kernel methods
- Linear fitting
- graph methods

## Eval Metrics
- EF metric - RMSE of per-atom energy + RMSE of forces

Dynamic indicators
- radial distribution function (RDF)
- angular " " (ADF)

## Summary
- no clear winning model for large-scale semiconductor MD simulations
- check the github repo

