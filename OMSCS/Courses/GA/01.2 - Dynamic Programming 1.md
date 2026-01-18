---
tags:
  - OMSCS
  - Algorithms
---
# 01 - Dynamic Programming 1
> FIB - LIS - LCS

## Overview

- Fibonacci Numbers (FIB)
- Longest increasing subsequence (LIS)
- Longest common subsequence (LCS)
- Knapsack
- Chain matrix multiplication
- Shortest path algorithms

## Toy Example - Fibonacci Numbers

- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
- $F_0=0$
- $F_1=1$
- $F_n=F_{n-1}+F_{n-2}$
- Input: integer n >= 0
- Output: n-th fibonacci number

### Attempt 1 - Basic Recursion
```py
Fib1(n):
	input: integer n>=0
	output: F_n
	if n = 0, return (0)
	if n = 1, return (1)
	return (Fib1(n-1) + Fib1(n-2))
```

Let $T(n)$ = the number of steps for $Fib1(n)$
- $T(n) \le O(1) + T(n-1) + T(n-2)$
- $T(n) \ge F_n \approx \frac{\phi^n}{\sqrt{5}}$
- $\phi=\frac{1+\sqrt{5}}{2}$ (the golden ratio)
- Exponential runtime

### Attempt 2 - Dynamic Programming Approach
```py
Fib2(n):
	F[0] = 0
	F[1] = 1
	for i = 2 -> n:
		F[i] = F[i-1] + F[i-2]
	return (F[n])
```

- No recursion (No unnecessary stack frames)
- Memoization
	- We don't use this in the course
	- The goal of this unit is to learn DP. Using Memoization hides implementation details.
	- DP has advantages
		- Faster (no hash lookups)
		- Simpler to analyze the runtime
	- DP algorithms start to look similar to each other after enough practice

## Longest Increasing Subsequence (LIS)

- Input: $n$ numbers $A=a_1, a_2, ..., a_n$
- Goal: find the length of the LIS in $A$
- Example: $A=[5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]$
- Substring = set of consecutive elements
- Subsequence = subset of elements in order (can skip)
- In this example: $LIS=[-3,1,4,5,8,9]$

- 1st step: define subproblem in words
	- FIB: $F[i]$ = $i$-th fibonacci number
	- LIS: Let $L(i)$ = length of LIS on $a_1,...,a_i$
- 2nd step: state a recursive relation
	- FIB: express $F(i)$ in terms of $F(1),...,F(i-1)$
	- LIS: express $L(i)$ in terms of $L(1),...,L(i-1)$

LIS: express $L(i)$ in terms of $L(1),...,L(i-1)$

> Let $L(i)$ = the length of the LIS on $[a_1, a_2, ..., a_i]$

- $A=[5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]$
- $L=[1,2,2,2,3,3,4,4,4,???]$
- This was taking $5$ as the "current", then incrementing the counter whenever we found an integer larger that was larger then the current, then resetting the current.
- At point $???$, we need to switch to the LIS starting with $-3$. At $i=9$, how do we get $L(9)$ using $[L(1),...,L(8)]$?
- As we iterate through the array, we need to keep track of the LIS with the ***minimum*** ending character in LIS solution.
- At $i=7$
	- $[5,7,9,10]$ is the LIS
	- $[-3,1,4]$ is a suboptimal solution
- At $i=8$
	- $[5,7,9,10]$ and $[-3,1,4,5]$ are tied for length
	- $[-3,1,4,5]$ should win the tie due to having the lowest ending integer
- For each element in $A$, we need to maintain a parallel list $L$ where $L[i]$ contains the length of the LIS that ends with that character.
- What are the possible ending characters? The possible ending characters are ALL possible earlier characters.

> Let $L(i)$ = the length of the LIS on $[a_1, a_2, ..., a_i]$ **which includes $a_i$**

```
A = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
L = [1, 2, 1,  1, 3, 2,  4, 3, 4, 5, 6, 3]
     ^  ^  ^   ^  ^  ^   ^  ^  ^  ^  ^  ^
     5  5  4  -3  5 -3   5 -3 -3 -3 -3 -3
        7         7  1   7  1  1  1  1  1
                  9      9  4  4  4  4  3
                        10     5  5  5
                                  8  8
                                     9
```

> Recurrence relation: $L(i)=1+max_j\space\{L(j):a_j<a_i \space\&\space j<i\}$

```py
LIS(A):
  for i=1 -> n:
    L[i] = 1
    for i=1 -> i-1:
      if A[j] < A[i] && L[i] < 1+L[j]
	    then L[i] = 1 + L[j]

  idx_max = 1
  for i=2 -> n:
    if L[i] > L[idx_max] then idx_max=i

  return L[idx_max]
```

## Longest Common Subsequence (LCS)
- Input: 2 strings X and Y (same length N)
- Goal: find the length of the longest string which is a subsequence of both X and Y

### Example
- $X=BCDBCDA$
- $Y=ABECBAB$
- A is in both X and Y
- BC is in both X and Y
- BCB is in both X and Y
- BCBA is in both X and Y
- Y has no D's, so X can be rewritten as BCBCA
- X has no E's, so Y can be rewritten as ABCBAB
- BCBA is the LCS, therefore len(LCS) is 4.

> Illustrates a slightly different flavor of dynamic programming problem. It's used in unix's `diff`.

### Step 1: Define subproblem in words.
> Try the same problem on prefix of input.

```
For i where 0 <= i <= n,
let L(i) = length of LCS in X and Y.
```

### Step 2: Define the recurrence (Attempt 1)

Express $L(i)$ in terms of $L(1), ..., L(i-1)$

> For i where $0 \le i \le n$
> let $L(i)$ = length of LCS in $X_{1..i}$ and $Y_{1..i}$

The last character in $X$ and $Y$ must be either the same or different.
- If they're the same ($X_i = Y_i$), we can
	- recurse into the prefix of the 2 lists $\{X_{1..(i-1)}, Y_{1..(i-1)}\}$
	- find the LCS of those prefixes
	- add 1 to their result
- If the last characters are different ($X_i \ne Y_i$)
	- The last character of the LCS can either be $X_i$ or $Y_i$ or neither. Therefore, the LCS does not include $X_i$ and/or $Y_i$.
	- If both are dropped, we can simply find the LCS in $\{X_{1..(i-1)}, Y_{1..(i-1)}\}$
	- However, if we take $X_i$ and drop $Y_i$, the prefixes become different lengths, and **therefore the solution to the subproblem does not exist within the recurrence relation.**

This definition ($L(i)$) did not work, but it gave us more insight into what is a good subproblem.

The difficulty here is that the prefixes X and Y are the same length, which does not work for all problems. Therefore, we need to redefine L with a pair of parameters, i and j ($L(i,j)$)

### Step 2: Define the recurrence (Attempt 2)
- We need a prefix of X of length i, and a prefix of Y of length j.
- This will result in a 2D table within the DP implementation, where previous DP examples only had 1D tables.

Subproblem definition.

> For $i$ and $j$, where $0 \le i \le n$ and $0 \le j \le n$
> let $L(i,j)=$ the length of LCS in $X_{1..i}$ ($\{X_1,...,X_i\}$) and $Y_{1..j}$ ($\{Y_1,...,Y_j\}$)

- $L(i,0)=0$
- $L(0,j)=0$

#### Example 1
- $X=BCDBCDA$
- $Y=ABECBABD$
- Notes
	- If the LCS ends in $A$, then $Y_8$ and $Y_7$ are not included in the LCS.
	- If the LCS ends in $D$, then $X_7$ is not included in the LCS.
	- The LCS might not end with $A$ or $D$.
- if $X_i \ne Y_j$
	- if drop $X_i$ then $L(i,j)=L(i-1,j)$
	- if drop $Y_j$ then $L(i,j)=L(i,j-1)$
	- general case: $L(i,j)=max\{L(i-1,j),L(i,j-1)\}$

#### Example 2
- $X=BCDBCDA$
- $Y=ABECBA$
- if $X_i=Y_j$
	- The optimal solution includes $X_i$ and $Y_j$
	- $L(i,j)=1+L(i-1,j-1)$
- There's a lot of reasoning you can walk through to show that you don't need to apply $max$ over additional recursive cases.

#### The Recursive Algorithm
![[Pasted image 20260113204226.png]]

#### The DP Algorithm
- $L$ is a 2D array.
- We fill it up row by row, i.e. we start with $L(0,0)$, then get $L(0,1)$, etc.

```py
LCS(X, Y):
	for i=0 -> len(X), L[i][0]=0
	for j=0 -> len(Y), L[0][j]=0
	for i=1 -> len(X)
		for j=1 -> len(Y)
			if X[i] = Y[j] then L[i][j] = 1 + L[i-1][j-1]
			else L[i][j] = max( L[i][j-1], L[i-1][j] )

	return (L[len(X)][len(Y)])
```

#### Example
|     | j   | 0   | 1   | 2   | 3   | 4   | 5   | 6     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| i   |     |     | A   | B   | E   | C   | B   | A     |
| 0   |     | 0   | 0   | 0   | 0   | 0   | 0   | 0     |
| 1   | B   | 0   | 0   | 1   | 1   | 1   | 1   | 1     |
| 2   | C   | 0   | 0   | 1   | 1   | 2   | 2   | 2     |
| 3   | D   | 0   | 0   | 1   | 1   | 2   | 2   | 2     |
| 4   | B   | 0   | 0   | 2   | 2   | 2   | 3   | 3     |
| 5   | C   | 0   | 0   | 2   | 2   | 3   | 3   | 3     |
| 6   | D   | 0   | 0   | 2   | 2   | 3   | 3   | 3     |
| 7   | A   | 0   | 1   | 2   | 2   | 3   | 3   | **4** |
- $LCS(ABECBA, BCDBCDA)=4$ 
- What is this sequence? Who knows. That's a different question.

## LCS Extract Sequence

Now that we have the table filled in, we can extract the LCS by following the table in reverse from the last matching cell. In this case, the last matching cell happened to be in the bottom right.

![[Pasted image 20260113205930.png]]

## Practice Problems
From the \[DPV\] book
- [[6.1 - Contiguous Subsequence]]
- [[6.2 - Hotel Stops]]
- [[6.3 - Yuck Donald's]]
- [[6.4 - String of Words]]
- [[6.11 - Longest Common Substring]]

General Approach:
- define the subproblem in words
	- use a prefix of the input
	- add a constraint, include last element
- Recurrence relation
	- define $T(i)$ in terms of $T(1), ..., T(i-1)$

