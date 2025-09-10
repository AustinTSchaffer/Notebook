---
tags:
  - OMSCS
  - DB
---
# 02 - Extended Entity-Relationship (EER) Model
> In order to do data modeling, we need data models.

## Entity Type and Entity Surrogates
![[Pasted image 20250901153806.png]]

- entity types are represented as rectangles
- entity type names must be unique

## Single Valued Properties
- sv props are represented as ellipses
- these ellipses are linked to an entity type
- prop values are 
	- lexical, visible, audible
	- they are things which name other things
- properties identify another property if they are "underlined"
	- for each identifying prop value, there is at most one instance of the identified entity
	- each entity must be uniquely referenceable

## Composite Properties
- composite props are represented as ellipses
- these ellipses are linked to another property
- the "name" property is a composite property, composed of firstname and lastname

![[Pasted image 20250901154125.png]]

## Multi-Valued Property
- double ellipses

![[Pasted image 20250901154158.png]]

## Relationships
- relationships are represented as diamonds
- the names of multiple relationship types between the same two entity types must be unique
### 1-1 relationship types
![[Pasted image 20250901154343.png]]
- partial function
### 1-many relationship types
![[Pasted image 20250901154509.png]]
- partial function
### mandatory 1-N relationship types
![[Pasted image 20250901154637.png]]
- total function
### N-M relationship types
![[Pasted image 20250901154728.png]]
### N-ary relationship types
![[Pasted image 20250901154836.png]]
- relationships can link 2 or more entities
### Many relationship types
> Many ternary relationship types cannot be reduced to a conjunction of binary relationship types.

![[Pasted image 20250901154955.png]]

### Identifying relationships / weak entity types
![[Pasted image 20250909204641.png]]

- StatusUpdate is identified by the email of the user and the date/time it was posted.
	- Cannot exist without RegularUser
	- Cannot be identified without RegularUser (ID: (Email, DateAndTime) tuple)
- StatusUpdate is a weak identity because its ID has to go "through" the RegularUser entity

### Recursive Relationship Types
![[Pasted image 20250909204929.png]]

- Creates a graph or tree structure within a single entity type (or a set of entity types)

## Supertypes and subtypes
### "is-a" relationship types
![[Pasted image 20250909205033.png]]

- "d" is "disjoint"
- "o" is "overlap"
### Inheritance
![[Pasted image 20250909205209.png]]

## Union Entity Types
![[Pasted image 20250909205410.png]]

- example above, employer can be Company or GovtAgency
- $Employer \subseteq Company \cup GovtAgency$
- $Compay \cap GovtAgency = \emptyset$

## Are Relationships Entities?
> Or are they just glue?

![[Pasted image 20250909205920.png]]

- relationships may have attributes
- for 1-N relationships, attributes may be moved to the entity on the "many-side".
- for 1-1 relationships, attributes may exist on either entity

![[Pasted image 20250909210121.png]]

- The example above is an "objectified relationship type"

## Fun Example
![[Pasted image 20250909210451.png]]

## What can the EER do?
- Classification
- Generalization
- Does not do aggregation
	- You can't model a drive train in an EER model

## What is the result type of a query?
![[Pasted image 20250909210853.png]]

- list of properties are not entity types
- there is no "type"
- DBMSes are not based on EER

## Relational Model
- Data structures
- Constraints
- Operations
	- Relational Algebra
	- Relational Calculus
		- Tuple Calculus (SQL)
		- Domain Calculus (QBE)
### Data Structures
- There is only one structure (relations)
- a domain $D$ is a set of atomic values
- a relation $R$ is a subset of the set of ordered n-tuples
- ![[Pasted image 20250909211306.png]]
- an attribute $A$ is a unique name given to a domain in a relation helping us interpret domain values

> We illustrate domains by tables.

![[Pasted image 20250909211330.png]]

> The value of a relation is independent of attribute order and tuple order.

### Constraints
- Keys
- Primary Keys
- Entity integrity
- Referential integrity

