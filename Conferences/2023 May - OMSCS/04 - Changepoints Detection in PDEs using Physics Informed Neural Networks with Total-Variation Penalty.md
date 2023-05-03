# Changepoints Detection in PDEs using Physics Informed Neural Networks with Total-Variation Penalty
*by Zhikang Dong*

Paper Link: https://arxiv.org/abs/2208.08626

- 2 step estimation algorithm
	- estimate potential changepoints
	- use dynamic programming

- 3 components of loss function
	- LFD: Discrepancy between ground truth and estimation
	- Boundary Loss: Plug in boundary info into loss function
	- PDE Loss: Force NN to learn physical law

Several extensions of PINNs
- Bayesian PINNs (B-PINN)
- B-PINNs use the Hamiltonian Monte Carlo (HMC)

![[Pasted image 20230503111257.png]]
