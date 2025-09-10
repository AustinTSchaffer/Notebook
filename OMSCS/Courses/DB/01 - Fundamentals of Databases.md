---
tags:
  - OMSCS
  - DB
---
# 01 - Fundamentals of Databases

- high level overview of what a DB is
- it's a "model of reality"
- why use models at all?
- when to use a Database Management System (DBMS)

## Models of Reality
- a model is a means of communication
- users of a model must have a certain amount of knowledge in common
- a model
	- only emphasizes selected aspects
	- is described in some language
	- can be erroneous
	- may have features that do not exist in reality

## To use or not to use a DBMS
### To Use
- data-intensive applications
- persistent storage of data
- centralized control of data
- control of redundancy
- control of consistency and integrity
	- consistency = whether you can derive contradictions from within the DB itself
- multiple user support
	- flight reservation
	- point of sale transactions
- sharing of data
- data documentation
- data independence
- control of access and security
- backup and recovery
### Not To Use
- the initial investment in hardware, software, and training is too high
- the generality is not needed
	- overhead for security, concurrency, and recovery is too high
- data and apps are simple and stable
- real-time requirements cannot be met by it
- multiple user access is not needed

## Outline of Major Topics
- data modeling
- process modeling
- database efficiency

## Data Modeling
![[Pasted image 20250831114949.png]]

- the model represents a perception of structures of reality
- the data modeling process is to fix a perception of structures of reality and represent this perception
- in the data modeling process, we select aspects and abstract

## Process Modeling
![[Pasted image 20250831114933.png]]

- the use of the model reflects processes of reality
- processes may be represented
	- embedded in program code
	- executed ad-hoc

![[Pasted image 20250831114914.png]]

## Data Models
- data structures
- constraints
- operations
- keys / identifiers
- integrity / consistency
- null values
- surrogates

## Architecture
- database 
	- ANSI/SPARC 3-Level DB Architecture
	- data independence
- DBMS

## Metadata

## Example of Data Models
> A data model is not the same as a model of data.

- Entity-Relationship Model
- Relational Model
- Hierarchical Model (legacy, IBM IMS, XML)


### Relational Model
#### Data Structures
- data is represented in tables
- tables have a name
- tables have columns
- columns have a data type
- tables have rows
- schema represents aspects of the data (the structure)
- The schema is not expected to change (much)
#### Constraints
- constraints express rules that cannot be expressed by the data structures alone (more than just type constraints)
- validation rules
- foreign key relations
- unique constraints
- > dates must be after "1900-01-01"
#### Operations
- operations support change and retrieval of data
- CRUD operations
- list operation
- filtering
- etc

## Keys and Identifiers
- keys are uniqueness constraints
- keys are used for reference and lookup of rows

## Integrity and Consistency
- **integrity**: Does the DB reflect reality well?
- **consistency**: Is the DB without internal conflicts?

## Null Values
- it's "advanced 0"
- represents the lack of a value, not a value itself
- also represents values which are "inapplicable" to the specific row ("catch-all" forms)

## Surrogates - Things and Names
- "Leo"
- "GTO1"
- "49"
- **name-based**: a thing is what we know about it
- surrogates are system-generated, unique, internal identifiers

![[Pasted image 20250831120057.png]]

![[Pasted image 20250831120320.png]]


## ANSI/SPARC 3-Level DB Architecture
### Separating Concerns
- a DB is divided into schema and data
- the schema describes the intention (types)
- the data describes the extension (data)

![[Pasted image 20250901150105.png]]

- benefits include
	- it's possible to change how data is stored without changing the application which uses the data
- physical data independence is a measure of how much the internal schema can change without affecting the application programs
- logical data independence is a measure of how much the conceptual schema can change without affecting the application programs
### Conceptual Schema
- describes conceptually relevant, general, time-invariant structural aspects of reality
- excludes aspects of data representation, physical organization, and access
- applications can only "see" these structures
### External Schema
- describes parts of the information in the conceptual schema in a form convenient to a particular user group's view
- is derived from the conceptual schema
### Internal Schema
- describes how the information described in the conceptual schema is physically represented to provide the overall best performance
- includes indexes

## ANSI/SPARC DBMS Framework
![[Pasted image 20250901150809.png]]

- hexagons are different people/roles
- triangle is where schema definitions are stored
- squares are processors
- 2 main parts
	- schema compiler
	- query transformer

## Metadata
- system metadata
	- where data came from
	- how data is changed
	- how data is stored
	- how data is mapped
	- who owns data
	- who can access data
	- data usage history
	- data usage statistics
- business metadata
	- what data is available
	- where data is located
	- what the data means
	- how to access data
	- predefined reports
	- predefined queries
	- how current the data is 
- importance
	- system metadata is critical in a DBMS
	- business metadata is critical in a data warehouse
