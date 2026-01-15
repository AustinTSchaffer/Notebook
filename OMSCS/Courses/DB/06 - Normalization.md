---
tags:
  - OMSCS
  - DB
---
# 06 - Normalization
- Databases are forever
- EER Diagrams go missing
- Experts, idiots, compromises

## What's it all about?
Given a relation and a set of functional dependencies, like these
- Email -> {BirthYear, CurrentCity, Salary}
- {Email, Interest} -> SingeAge
- BirthYear -> Salary

How do we normalize the relation without information loss and so that the functional dependencies can be enforced?

## The Rules
1. No redundancy of facts
2. No cluttering of facts
3. Must preserve information
4. Must preserve functional dependencies

## Not a Relation - Non-First Normal Form (NFNF, $NF^2$)
![[Pasted image 20251126214804.png]]

- This table contains multi-values
- Not atomic

## Relation with Problems
![[Pasted image 20251126214931.png]]

### Redundancy
![[Pasted image 20251126215023.png]]

- Redundancy leads to inconsistency

### Insertion Anomaly
![[Pasted image 20251126215102.png]]

### Deletion Anomaly
![[Pasted image 20251126215140.png]]

### Update Anomaly
![[Pasted image 20251126215203.png]]

## Information Loss
If we decompose a table into 2 relations, then we could get too many rows back when we recombine them. Need to be careful with how a table is decomposed.
## Dependency Loss
If we decompose a table into 2 relations, then we cannot enforce the functional dependencies that are split between the 2 relations.
## Perfect
![[Pasted image 20251126215627.png]]

## Functional Dependencies
- Let X and Y be sets of attributes in R
- Y is functionally dependent on X in R iff for each x in R.X, there is precisely one y in R.Y

![[Pasted image 20251126215803.png]]

### Full Functional Dependencies
- Let X and Y be sets of attributes in R
- Y is fully functionally dependent on X in R iff Y is functionally dependent on X and Y is not functionally dependent on any proper subset of X

- {CurrentCity} is functionally dependent on {Email, BirthYear}
- {CurrentCity} is fully functionally dependent on {Email}

### Functional Dependencies and Keys
- We use keys to enforce full functional dependencies
- in a relation, the values of the key are unique
- that's why it enforces a function

![[Pasted image 20251126220138.png]]

## Normal Forms

### Overview
- Non First Normal Form (NFNF, $NF^2$)
- First normal form (1NF)
	- R is in 1NF iff all domain values are atomic
- Second normal form (2NF)
	- R is in 2NF iff R is in 1NF and every non-key attribute is fully dependent on the key
- Third normal form (3NF)
	- R is in 3NF iff R is in 2NF and every non-key attribute is non-transitively dependent on the key
- Boyce-Codd Normal Form (BCNF)
	- R is in BCNF iff every determinant is a candidate key
- Determinant
	- a set of attributes on which some other attribute is fully functionally dependent

### Decomposition Example
![[Pasted image 20251126220851.png]]

## How to compute with functional dependencies
> Armstrong's Rules

- **reflexivity**: if Y is part of X, then X->Y
- **augmentation**: if X->Y, then WX->Y and WX->WY
- **transitivity**: if X->Y and Y->Z, then X->Z
	- Email -> BirthYear and BirthYear -> Salary, then Email -> Salary

## How to guarantee lossless joins?
The join field must be a key in at least one of the relations.

## How to guarantee preservation of FDs?
The meaning implied by the remaining functional dependencies must be the same.

![[Pasted image 20251126221244.png]]

## 3NF and BCNF
- There are relations which can be decomposed to 3NF, but not to BCNF, while being lossless and dependency preserving
- It can only happen when the relation has overlapping keys.
- This never happens in practice.

![[Pasted image 20251126221550.png]]

