---
tags:
  - OMSCS
  - DB
---
# 04 - Relational Algebra and Calculus
## Relational Algebra
### Operators
![[Pasted image 20251011223604.png]]

![[Pasted image 20251011223648.png]]

![[Pasted image 20251011223658.png]]

![[Pasted image 20251011223730.png]]

- All operators return sets of tuples.
- All operations can only return unique tuples.
- Relations are sets!!!

### Select
- Filter a Relation or Set

![[Pasted image 20251011224809.png]]

![[Pasted image 20251011224838.png]]

### Projection
- Remove attributes from a relation or set

![[Pasted image 20251011224921.png]]

### Union
![[Pasted image 20251011225256.png]]

### Intersection
![[Pasted image 20251011225334.png]]

### Set Difference
![[Pasted image 20251011225625.png]]

### Natural Join
- Matches values of attributes with same names
- keeps only one copy of the join attributes
- is an "inner" join

![[Pasted image 20251011225759.png]]

### Theta Join
- theta: comparison expression
- all attributes are preserved
- also an inner join

![[Pasted image 20251011225931.png]]

### Left Outer Join
![[Pasted image 20251011230150.png]]

- variations
	- natural (left) outer join (as here)
	- a special case of a theta-join

### Cartesian Product
![[Pasted image 20251011230242.png]]

![[Pasted image 20251011230420.png]]

### Divide By
- Universal quantification

![[Pasted image 20251011230632.png]]

![[Pasted image 20251011230640.png]]

![[Pasted image 20251011230706.png]]

### Rename
- useful to control natural join / theta join / etc

![[Pasted image 20251011230753.png]]

## Relational Calculus
![[Pasted image 20251011230843.png]]

### Selection
![[Pasted image 20251011231011.png]]

![[Pasted image 20251011231032.png]]

### Projection
![[Pasted image 20251011231057.png]]

### Union
![[Pasted image 20251011231119.png]]

### Intersection
![[Pasted image 20251011231142.png]]

### Set Difference
![[Pasted image 20251011231203.png]]

### Natural Join
![[Pasted image 20251011231223.png]]

### Cartesian Product
![[Pasted image 20251011231303.png]]

![[Pasted image 20251011231400.png]]

### Divide By
![[Pasted image 20251011231421.png]]

