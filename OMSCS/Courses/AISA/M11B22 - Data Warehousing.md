---
tags: OMSCS, AISA
---
# M11B22 - Data Warehousing

> Q: What is data warehousing?
>
> A: A process of transforming data into information, and making it available to users in a timely enough manner to make a difference.

It's a single, consistent, and complete store of data obtained from a variety of different sources, and made available to end users in a way they can understand and use in a business context.

- provides the enterprise with a consolidated and summarized memory
- data minding provides the enterprise with prediction intelligence

![[Pasted image 20230316220445.png]]

- subject oriented
- integrated
- time-varying
- non-volatile
- a collection of data that is used primarily in organizational decision making

- a popular, data summarization enhanced database technology in the business world
- holds the potential to unlock some trend analysis in science and engineering fields

![[Pasted image 20230316220659.png]]

## Data Warehouse vs Operational DBMS

Online transaction processing (OLTP)
- major task of traditional relational DBMS
- Day to day operations
	- purchasing
	- inventory
	- banking
	- manufacturing
	- payroll
	- registration
	- accounting
- describes processing at operational sites

Online Analytical Processing (OLAP)
- major task of data warehouse system
- data analysis and decision making
- describes processing at warehouse

Examples of OLAP
![[Pasted image 20230316221101.png]]

## Architectures
![[Pasted image 20230316221135.png]]

![[Pasted image 20230316221147.png]]

![[Pasted image 20230316221207.png]]

![[Pasted image 20230316221222.png]]

![[Pasted image 20230316221240.png]]

![[Pasted image 20230316221248.png]]

![[Pasted image 20230316221324.png]]

![[Pasted image 20230316221409.png]]

![[Pasted image 20230316221509.png]]

## Design
![[Pasted image 20230316221546.png]]

![[Pasted image 20230316221637.png]]

![[Pasted image 20230316221741.png]]

![[Pasted image 20230316221814.png]]

![[Pasted image 20230316221822.png]]

![[Pasted image 20230316221851.png]]

![[Pasted image 20230316221934.png]]

![[Pasted image 20230316221948.png]]

![[Pasted image 20230316222020.png]]

![[Pasted image 20230316222038.png]]

![[Pasted image 20230316222127.png]]

![[Pasted image 20230316222134.png]]

![[Pasted image 20230316222155.png]]

![[Pasted image 20230316222238.png]]

![[Pasted image 20230316222324.png]]

![[Pasted image 20230316222333.png]]

![[Pasted image 20230316222412.png]]

## Models
Modeling data warehouses: dimensions and measures
- **Star schema:** a fact table in the middle connected to a set of dimension tables
- **Snowflake schema:** a refinement of star schema where some dimensional hierarchy is normalized into a set of smaller dimension tables, forming a shape similar to a snowflake
- **Fact constellations:** multiple fact tables share dimension tables, viewed as a collection of stars, therefore called galaxy schema or fact constellation

![[Pasted image 20230316222656.png]]

![[Pasted image 20230316222849.png]]

![[Pasted image 20230316222833.png]]

## Defining Schemas
![[Pasted image 20230316223144.png]]

![[Pasted image 20230316223155.png]]

![[Pasted image 20230316223207.png]]

## Operations
> Common usage patterns/operations performed against data warehouses

![[Pasted image 20230316223242.png]]

![[Pasted image 20230316223308.png]]

![[Pasted image 20230316223318.png]]

![[Pasted image 20230316223329.png]]

![[Pasted image 20230316223338.png]]

![[Pasted image 20230316223346.png]]

![[Pasted image 20230316223355.png]]

![[Pasted image 20230316223415.png]]

## Implementation and Optimization
![[Pasted image 20230316223437.png]]

![[Pasted image 20230316223508.png]]

### Indexing
![[Pasted image 20230316223552.png]]

![[Pasted image 20230316223609.png]]

### Materialized views
![[Pasted image 20230316223616.png]]

![[Pasted image 20230316223628.png]]

![[Pasted image 20230316223651.png]]

![[Pasted image 20230316223718.png]]

![[Pasted image 20230316223727.png]]

![[Pasted image 20230316223744.png]]

