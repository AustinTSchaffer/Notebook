---
tags:
  - OMSCS
  - ML
---
# No Free Lunch Theorem

- impossibility theorem
- a general purpose universal optimization strategy is impossible
- "the only way one strategy can outperform another is if it is specialized to the structure of the specific problem under consideration"

One can build a matrix where the rows are optimization algorithms and the columns are optimization problems. The cells of the matrix encode the effectiveness of each optimization algorithm on each optimization problem.

The paper posits that each row has the same average performance.

The effectiveness of one particular optimization algorithm is useless without considering the set of optimization problems that you hope to apply it to.

