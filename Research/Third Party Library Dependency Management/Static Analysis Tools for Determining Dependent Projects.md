---
tags:
---
# Static Analysis Tools for Determining Effective Dependent Project Interface

The idea here synthesizes a few different lines of research
- Given a package, and a changeset, we can determine the list of classes/functions/properties/structs/etc which have received a breaking change, if any.
	- [[Automatic Semantic Versioning]]
- Given a range of versions of a project, determine the range of packages that the project depends on
	- [[Python Packaging Deep Dive]]
	- [[Global Python Packaging Dependency Relationships]]
- Given a specific version of a project, determine which function calls/imports/etc are dependent on a third-party library
	- Static analysis of the code, to determine which specific function calls that project $A$ version $V_A$ requires from project $B$ version $V_B$.
	- This will be highly dependent on the project not using tons of metaprogramming
	- Likely should require mypy to enforce type-hints on method definitions

Given these lines of research, we can build a comprehensive dataset mapping to determine whether project $A$ version $V_A$ can upgrade its project $B$ version $V_B$ to $V_B'$ without encountering obvious breaking changes, producing a new version of project $A$ ($V_A'$).

Given these lines of research, the maintainers of project $B$ could use the same database of interrelated projects to determine if any downstream projects depend on a set of function calls that they'd like to remove.