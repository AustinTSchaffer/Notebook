---
tags:
  - SRE
---
# Foreword and Preface
## Attribution
> _Site Reliability Engineering_, edited by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (O’Reilly). Copyright 2016 Google, Inc., 978-1-491-92912-4.

## Foreword
> The book is a collection of essays by one company, with a single common vision.

> The articles are not rigorous, academic pieces; they are personal accounts \[...\]

## Preface
- estimates on the cost of software
	- 10% - 60% are the initial implementation
	- 40% - 90% are the continued maintenance
- Your average engineer only talks about the initial implementation, not the maintenance, which is the most expensive part of the process.
- SRE is the role which focuses on the whole SDLC, not just the implementation, but also the continued maintenance.

- SREs are engineers
	- apply principles of CS and engineering to design and development of computer systems
		- writing software for systems alongside SDEs
		- building additional pieces
			- backups
			- load balancing
		- reusable infrastructure components
		- how to apply existing solutions to new problems
	- focus on reliability. Some claim that reliability is the most important feature of a computing system.
	- when systems are "reliable enough", SREs pivot to adding features or building new products
	- focus on operating "services" built on distributed computing systems
	- the "site" originally referred to keeping `google.com` up, but now the focus is on service-level infrastructure: bigtable, GCP, etc

