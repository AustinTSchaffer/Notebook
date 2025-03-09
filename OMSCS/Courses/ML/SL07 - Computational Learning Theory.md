---
tags:
  - OMSCS
  - ML
---
# SL07 - Computational Learning Theory
How do we know if an algorithm will perform better than another algorithm? It helps to know what problem you're solving. It's not enough to say "this algorithm/model performs best compared to these other algorithms/models, so therefore the problem must match my algorithm/model". There may be a better algorithm that you haven't considered.

![[Pasted image 20250221223922.png]]

## Computational Learning Theory
- defining learning problems
- showing specific algorithms work
- show these problems are fundamentally hard
- algorithms in computing

Theory of computing analyzes how algorithms use resources: time, space. Big O notation. Theta, Omega, etc.

What resources matter in computational learning theory?
- time
- space
- samples, data, examples, data, etc.
- "Is this problem even solvable? Can we classify someone's favorite dog breed based on their diet?"
- ML algorithms aren't useful if it needs examples of every possible input. That's simply a solved problem.

## Learning from Examples
1. probability of successful training
	1. $\delta$ is the probability of failure
	2. $1-\delta$
2. number of examples to train on
	1. $m$
3. complexity of hypothesis class
	1. Not complex enough, can't model the data
	2. Too complex, overfitting
4. accuracy to which target concept is approximated
5. manner in which training examples presented
	1. batch
	2. online
6. manner in which training examples selected

### Selecting Training Examples
- learner / teacher
- learner asks questions of teacher: $C(X)?$
- teacher gives examples to help learner: $X=C(X)$
- Fixed distribution: $X$ chosen from $D$ based on probability of value within $D$
- Evil - worst distribution

### Teaching via 20 Questions
- H: set of possible people
- X: set of questions
- Teacher chooses h from H, and provides the questions.
	- If the teacher chooses x from X, the teacher can feed a question to the learner that's simply "Is H=h?"
	- the learner asks the question, teacher says "yes"
- Teacher chooses h from H, and provides no questions.
	- Learner needs $log_2|H|$ questions, each throwing out half of the remaining H.
	- The question chosen by the learner needs to give the learner the max amount of information.
	- This also assumes that the learner knows everything about H.

### Teacher with Constrained Queries
- $X:x_1,x_2,...,x_k$: k-bit input
- H: conjunctions of literals or negation
- Example hypothesis: $h=x_1 \space and \space x_3 \space and \space \neg{x_5}$

| $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $h$ |
| ----- | ----- | ----- | ----- | ----- | --- |
| 0     | 1     | 0     | 1     | 1     | 0   |
| 1     | 0     | 1     | 0     | 1     | 0   |
| 1     | 0     | 0     | 1     | 0     | 0   |
| 1     | 1     | 1     | 0     | 0     | 1   |

It's a truth table.

#### Example

| Sample | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $h$ |
| ------ | ----- | ----- | ----- | ----- | ----- | --- |
| 1      | 1     | 0     | 1     | 1     | 0     | 1   |
| 2      | 0     | 0     | 0     | 1     | 0     | 1   |
| 3      | 1     | 1     | 1     | 1     | 0     | 0   |
| 4      | 1     | 0     | 1     | 0     | 0     | 0   |
| 5      | 1     | 0     | 1     | 1     | 1     | 0   |

| Var   | Positive | Absent | Negative | Notes           |
| ----- | -------- | ------ | -------- | --------------- |
| $x_1$ |          | X      |          | Samples 1 and 2 |
| $x_2$ |          |        | X?       |                 |
| $x_3$ |          | X      |          | Samples 1 and 2 |
| $x_4$ | X?       |        |          |                 |
| $x_5$ |          |        | X?       |                 |

$h=\neg{x_2} \space and \space x_4 \space and \space \neg{x_5}$

Lessons learned
1. show what's irrelevant
2. show what's relevant

### Learner with Constrained Queries
![[Pasted image 20250221231210.png]]

The teacher can be mean and pick a hypothesis that has no absent variables. The learner then needs to ask all possible $\forall_{x \in X}$ to find $h$. The learner only gets information when $h(x)=1$
- $|H|=3^k$
- $|X|=2^k$

### Learner with Mistake Bounds
1. input arrives
2. learner guesses answer
3. wrong answer charged
4. repeat

bound the total number of mistakes

1. Assume it's possible each variable positive and negated
2. Given input, compute output
3. if wrong
	1. set all positive variables that were 0 to absent
	2. set all negative variables that were 1 to absent

## Definitions
- **computational complexity:** How much comp effort is needed for a learner to converge to the best hypothesis in the hypothesis class?
- **sample complexity:** (batch) How many training examples are needed for a learner to create a successful hypothesis?
- **mistake bounds:** (online) How many misclassifications can a learner make over an infinite run?
- True hypothesis: $c \in H$ (concept in H)
- Candidate hypothesis: $h \in H$
- Training set: $S \subseteq X$ (subset)
- $c(x): \forall x \in S$
- Consistent learner: produces $c(x)=h(x)$ for $x \in S$
- Version space: $VS(S)=\{ h \space\text{such that (s.t.)}\space h \in H \space\text{consistent wrt}\space S \}$
- Hypotheses consistent with examples

## Terminology Quiz
![[Pasted image 20250221233031.png]]

Version space contains hypotheses:
- $c(X)=x_1$
- $c(X)=x_1 \oplus x_2$ (XOR)
- $c(X)=x_1 \vee x_2$ (OR)
- $c(X) = x_1 \neq x_2$
- $H=\{x_1, \space x_1 \oplus x_2, \space x_1 \vee x_2 \}$

## PAC Learning - Error of $h$
- **Training Error:** fraction of training examples misclassified by $h$.
- **True Error:** Fraction of examples that would be misclassified on sample drawn from $D$.
- $error_D(h)=P_{x \sim D}[c(x) \neq h(x)]$

> $c$ is PAC-learnable by $L$ using $H$ iff learner $L$ will, with probability $1-\delta$, outputs a hypothesis $h \in H$ such that $error_D(h) \leq \epsilon$ in time, and samples polynomial in $\epsilon^{-1}$, $\delta^{-1}$, and $n$.

- $c$: concept class
- $L$: learner
- $H$: hypothesis space
- $n$: $|H|$, size of $H$
- $D$: distribution over inputs
- $0 \leq \epsilon \leq \frac{1}{2}$: error goal
- $0 \leq \delta \leq \frac{1}{2}$: certainty goal
- PAC = Probably Approximately Correct
	- Probably: $1-\delta$
	- Approximately: $\epsilon$
	- Correct: $c(x) = h(x)$

### PAC-Learning Quiz
- $C=H=\{h_i(x)=x_i\}$
- K-bit inputs
- Is there an algorithm $L$ such that $c$ is PAC-learnable by $L$ using $H$? (yes)
	- Keep track of $VS(S,H)$
	- Pick one $h \in H$ uniformly
- $VS(S)$ is considered $\epsilon$-exhausted iff $\forall : h\in VS(S)$ has an $error_D(h) \leq \epsilon$

![[Pasted image 20250221235613.png]]

- ones in green are the training samples we've seen
- $VS(S)=\{ x_1, \space or, \space xor \}$
	- Due to $P(X=\{1, 1\})=0$: $error_D(x_1)=0.5$. Half the time it will be right (training data). Half the time it will be wrong ($X=\{0,1\}$).
	- $error_D(xor)=0$
	- $error_D(or)=0$
- $\epsilon = 0.5$

## Haussler Theorem - Bound True Error
- Let $error_D(h_1, h_2, ..., h_k \in H) \gt \epsilon$
- High true error. How much data do we need to "knock out" these hypotheses?
- $P_{x \sim D}(h_i(X)=c(X)) \le 1-\epsilon$
- $P(h_i \text{ consistent with } c \text{ on } m \text{ examples}) \le (1-\epsilon)^m$
- $P(\text{at least one of } h_1,...,k_k \text{ consistent with } c \text{ on } m \text{ examples})$
	- $\le k*(1-\epsilon)^m$
	- $\le |H|(1-\epsilon)^m$
- $(1-\epsilon)^m \le e^{-\epsilon m}$
- $-\epsilon \ge ln(1-\epsilon)$
- upper bound that version space not $\epsilon$-exhausted after $m$ samples: $\le |H| e^{-\epsilon m}$

If you know the size of your hypothesis space, then you know about how many samples you'll need.

![[Pasted image 20250222000943.png]]

You need 40.
- $m \ge \frac{1}{\epsilon} (ln 10 + ln \frac{1}{\delta})$
- $m \ge \frac{1}{0.1} (ln 10 + ln \frac{1}{0.2})$
- $m \ge 10 (ln 10 + ln 5)$
- $m \ge 39.12$

## Conclusion'
- It's possible to calculate the number of training samples you need.
- It's probably easier to check your learning curves.
- Concepts of teachers and students.
	- what is learnable?
	- similar to complexity theory for ML
