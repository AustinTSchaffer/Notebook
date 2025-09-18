---
tags:
  - OMSCS
  - DB
---
# Methodology 1 - Analysis
## Assumptions
- business processes are well-designed
- documents are known
	- Anything input to or output from the application(s) that run(s) on the DB
- tasks are known
	- any processing that takes place using those documents
	- any processing that takes place which generates those documents
	- any processing that takes place which updates those documents
- system boundary is known
	- "Where does the application(s) end, and where do external stakeholders begin?"
- one database schema unifying all views can be designed
	- difficult: interests, goals, power, politics
	- problems with the methodology?
	- problems with the organization?
	- "organization: an entity created to pursue a shared set of goals"
	- "It is ALWAYS a problem with the organization."

## The Software Process
Waterfall
- business process (re-)design
- ***analysis***
- ***specification***
- ***design***
- ***implementation***
- testing
- operation
- maintenance

The "bol-talic-ized" terms are the subject of this course.

## Overview of the Methodology: Data First!
- In general software development processes, the process comes first.
- In DB development, it's data first. Once the data is designed, we hang the processes on where they fit.

![[Pasted image 20250917205917.png]]

## Example
[[GTPEgtonline_description.pdf]]

## Information Flow Diagram (IFD)
![[Pasted image 20250917210449.png]]

- boxes are document names
	- boxes can be input and/or output documents
- ovals are task names
	- tasks can interact with multiple documents
- arrows represent information flow
- broken line represents the system boundary
- the central feature is the database, represented as a box
- this is NOT a control flow diagram
	- never connect 2 documents
	- never connect 2 tasks

## Requirements (Example)
- Users must log into the system via the Login screen
	- inputs: email, password
	- buttons: register, login
	- purely an input document
- New users must register first
	- inputs: first name, last name, email, password, confirm password
	- buttons: cancel, register
	- purely an input document
- Users are able to edit their profile
	- Many different fields, many different types of fields
	- This is an input and output document
- User profiles contain professional information and educational information
	- DB maintains list of employers
	- DB maintains list of schools
- Rapid fire
	- search screen is an output document
	- "request new friend" screen is an input document
	- friend request status screen? input and output document
	- friend list form is an output document

## IFD (Example)
![[Pasted image 20250917211421.png]]

## Word of Advice
- START with the documents. 
- DON'T start with the TASKS.

## Specification
- EER Diagram
- Data Formats
- Constraints
- Task Decomposition

## Document Specification
- What goes into the database?
- What comes out of the database?
- These are mechanical steps to take the "art" out of database specification creation.
- Everything in the database must come from somewhere.
- Everything on the input documents must go somewhere.
- Everything in the database must be used for something.
- Everything on the output documents must come from somewhere.

