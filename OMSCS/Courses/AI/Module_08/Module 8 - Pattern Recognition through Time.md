---
tags:
  - OMSCS
  - AI
---
# Module 8 - Pattern Recognition through Time

This module follows chapter 14 from AIMA: [[AIMA - Chapter 14 - Probabilistic Reasoning over Time]]

## Warping
- For detecting patterns which might have different y-intercepts, encode the changes in the signal's values, rather than the signal's raw values
- For detecting patterns which might stretch and compress, do some time warping

![[Pasted image 20240325101744.png]]

![[Pasted image 20240325101813.png]]

![[Pasted image 20240325101847.png]]

## Dynamic Time Warp

![[Pasted image 20240325101959.png]]

Try to match values between sequences, but try to keep to the diagonal when possible.

Distance in this example is $\sqrt{34}$, much lower compared to the euclidean distance of $\sqrt{170}$.

## Sakoe Chiba Bounds
![[Pasted image 20240325102302.png]]

Similar to the previous algorithm, but we don't allow the dynamic warping to deviate from some bounds around the diagonal.

## Hidden Markov Models
- module focuses on 1st order HMMs

![[Pasted image 20240325121112.png]]

### HMMs: I vs We
![[Pasted image 20240325121514.png]]

![[Pasted image 20240325121551.png]]

### Viterbi Trellis
![[Pasted image 20240325122002.png]]

![[Pasted image 20240325122317.png]]

![[Pasted image 20240325122630.png]]

- This is the part from the textbook chapter

### New Observation for "I"
![[Pasted image 20240325130548.png]]

## New Observation for "We"
![[Pasted image 20240325130609.png]]

