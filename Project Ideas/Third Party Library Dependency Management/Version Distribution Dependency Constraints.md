---
tags:
---
# Version Distribution Dependency Constraints

The structure of a package on PyPI is as follows.

- Package Name
- List of published versions, for each version:
	- List of "URLs". For each URL
		- Platform compatibility information.
		- Date published.
		- For wheels, a `.metadata` file describing the distribution's dependencies. For each dependency:
			- Dependency name (always present)
			- Version constraint information against the dependency (common, recommended)
			- Extras for the package (uncommon)
			- Extras for the dependency (uncommon)

Given this hierarchical structure, there is a layer of indirection, the "version distribution" (VD) layer, between a package-version (PV) pair and the list of packages that the PV pair depends on.

## Building a Naive Linking Index

For building an naive index on top of this, you can check all of the VDs of a specific PV pair to see if there is any variation between the deps of all VDs of the PV. If there aren't, you can just naively build a linking model that directly links a PV pair to a set of dependency information, without including any platform information, skipping over the VD layer. That model would look something like:

- package info
	- if using current DB schema over in the project
		- package known version ID (UUID)
	- otherwise:
		- package name
		- package version
- package extras
- dependency name
- dependency extras
- dependency version constraints

Using a unique constraint against package info, package extras, dependency name, and dependency extras results in a schema that can enumerate all of the dependencies for all versions of packages which have the property described above.

However, this doesn't work for some packages. A decent number of PVs have VDs with heterogeneous dependency requirements. These serve as counterexamples that the above model cannot represent.

## Examples
Before getting into counterexamples, here are some of the more complicated examples that can be modeled using the naive linking index model.

### Example 1: `modin==0.7.3`

Below is an example of a PV pair, with 3 different extras, and 5 wheel VDs. There are no conflicts between the version constraint requirements for each extra of `modin`.

![[Pasted image 20240524144017.png]]

## Counterexamples
### Counterexample 1: `tensorflow-gpu==0.12.0`

Here's a screenshot of a debugging session showing that `tensorflow-gpu` version `0.12.0` depends on `wheel>=0.26` in 4 of its VDs and `wheel`, with no version constraint information, on 2 of its VDs.

![[Pasted image 20240524140659.png]]

### Counterexample 2: `market-generic==0.0.0` vs `market-generic==0.0`

Here's another example. `market-generic` version `0.0.0` has 11 dependencies. `markget-generic` version `0.0` has 4 additional dependencies. There are no dependency version constraint conflicts in this set of dependencies.

![[Pasted image 20240524143050.png]]

### Counterexample 3: `sphinx==1.2.1`

In the screenshot below, `sphinx` version `1.2.1` has 3 dependencies, `jinja2`, `docutils`, and `pygments`. This PV pair has 4 VDs which are wheels.

- `pygments`
	- All 4 VDs depend on `pygments>=1.2`
- `docutils`
	- 3 VDs depend on `docutils>=0.7`
	- 1 VD depends on `docutils>=0.10`
- `jinja2`
	- 3 VDs depend on `jinja>=2.3`
	- 1 VD depends on `jinja>=2.3,<2.7`

![[Pasted image 20240524143310.png]]

### Counterexample 4: `tensorflow-addons==0.5.1`
There are 8 wheel VDs of this PV pair. The list of dependencies for each makes it clear that the package doesn't have support for GPU acceleration when running on MacOS. That requires a separate package (`tensorflow-gpu` vs `tensorflow`).

![[Pasted image 20240524145931.png]]

### Counterexample 5: `onnxruntime-directml==1.17.0`

There are 5 VDs of this PV pair, and 3 different version constraints for `numpy`.

![[Pasted image 20240524150947.png]]

### Counterexample 6: `matercard-vending==1.0.1`
The `py2.py3` VD depends on one version range of `mastercard-api-core`. The `py2` VD depends on a different version range of `mastercard-api-core`. There are no overlaps between these ranges.

![[Pasted image 20240524151730.png]]

## Improving the Naive Linking Index
What do we do to support the counterexamples?

- What do we do for conflicting version constraints between different VDs? Take the intersection of the version constraint information?
- What do we do when different VDs have different lists packages that they depend on? Do we take a union set of all packages that all VDs of a PV depend on?

Do we simply add more columns to the linking index to notate platform-compatibility information when necessary? That might look like:

- package info
	- if using current DB schema over in the project
		- package known version ID (UUID)
	- otherwise:
		- package name
		- package version
- platform info
	- python version(s)
	- OS
	- CPU architecture
	- setuptools info
	- etc?
- package extras
- dependency name
- dependency extras
- dependency version constraints

## How many platforms are there?
To help normalize the schema, if desired, we could potentially add a separate schema for platform info and link it back to the model from the previous section. This may also make it easier to produce a view over the linking index, when attempting to resolve dependencies for a specific platform.

- linking index
	- package info
		- if using current DB schema over in the project
			- package known version ID (UUID)
		- otherwise:
			- package name
			- package version
	- platform info ID (UUID)
	- package extras
	- dependency name
	- dependency extras
	- dependency version constraints
- platform info
	- platform info ID (UUID)
	- python version(s)
	- OS
	- CPU architecture
	- setuptools compatibility info \*
	- anything else

\* or whatever `manylinux1` refers to.

With this, is there a platform hierarchy? For example, are there any packages that have a generic OSX distribution, and then distributions for specific versions of OSX? Effectively, how does `pip` and/or [`resolvelib`](https://pypi.org/project/resolvelib/) decide which wheels to download?

## PV Pair Backlinks
One of the existing problems with the current $\text{pip} \leftarrow \text{PyPI}$ scheme is the "backtracking" algorithm. Essentially, if Package A depends on Package B, and Package C depends on Package A (any version) and Package B (an old version), pip has to backtrack on 

- package info
	- if using current DB schema over in the project
		- package known version ID (UUID)
	- otherwise:
		- package name
		- package version
- package extras
- dependency name
- dependency extras
- dependency version (was previously: "dependency version constraints")

Essentially what we've done here is taken the naive linking index and exploded out the "dependency version constraints" into discrete version numbers, based on the known versions of the dependency which fall within the specified "dependency version constraints". Putting a unique constraint across all of these fields results in a bidirectional linking model.

- If you have some version of Package A and want to find all of the PV pairs that A depends on, you can get that information.
- If you have some version of Package B and want to find all of the PV pairs that depend on B, you can get that information.

There are 2 main problems with this approach.

- Any inefficiencies related to duplication and duplicated yet again.
- Keeping the links up to date as new versions are published and later discovered by this system.
	- Any newly discovered VDs will have to be checked to see if there are any conflicts with existing VDs.
	- The version constraint information of a direct dependency of a VD will need to be compared against all of the known versions of a specific dependency name, in order to explode the constraint information into discrete version strings.
	- Any newly discovered PV pairs will need to be compared against a registry of dependency name / dependency version constraint information in order to explode more records into this linking index.

This has potential to put the database into a terabyte-scale project, but might be necessary for implementing a more efficient dependency resolution algorithm.

## Don't forget about "yanked"
> Or maybe do forget about "yanked"

We probably don't want yanked PV pairs to show up in this linking index. They are rare, so we can probably ignore the property, but they can be ignored when feeding potential package manifests to the solver.

## Putting it all Together
TODO: Combine the schemas from "Improving the Naive Linking Index" and "PV Pair Backlinks"