---
tags:
  - OMSCS
  - AI
---
# Module 02 - Simulated Annealing

> Do the stupid thing first, then add intelligence until you solve the problem.

This module goes over the N-Queens problem a lot. On small boards, you can arrange the queens randomly, then move the queen with the most number of queens that it can attack to a space which minimizes that number. This works pretty well on some inputs, but stops working as N increases.

This is effectively a hill climbing approach, in which the solution can get stuck in a local minimum. Options for improving this:

- Randomly restart from another state. Keep track of the best solution.
- Simulated annealing. Start with a large step size, but decrease it over time.

Other issues with hill climbing:
- step size too small
	- Hitting "shoulders"
	- Taking too long to reach a maximum
- Step size too large
	- Skipping over the local/global maximum
- only searching immediate surrounding pixels

## Simulated Annealing
![[Pasted image 20240116182506.png]]

## Local Beam Search
- "Keep track of $K$ particles"
- Randomly generate $K$ particles
- Iterate
	- Randomly generate $N$ neighbors of each particle
	- Keep the $K$ best particles of the $K \times N$ existing particles
- Stochastic beam search works the same, except $K$ "best" is determined probabilistically. Sometimes you pick a bad one just for fun.

## Genetic Algorithms
- simulating evolution and mating
	- Randomly generate starting members of the population.
	- Define a fitness function
	- Define a method for selecting parents based on fitness
	- Define a method for producing offspring from 2+ parents plus fitness
	- Define a method for randomly mutating offspring to introduce new information.
	- Carry over the best $N$ parents from the past generation for the next iteration so you don't lose useful information.
- super cool in principle
- super fun to implement
- probably not a super pragmatic method for most optimization problems
- "It's a fancy version of stochastic beam search which makes a nice analogy to biology."
- "Some people call genetic algorithms the 2nd-best solution to any problem."

