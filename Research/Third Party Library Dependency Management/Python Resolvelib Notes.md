# Python Resolvelib Notes
This is the library that performs dependency resolution for `pip`.

## Terminology
- Identifier
- Package
	- "A thing that can be installed. A Package can have one or more versions available for installation."
- Version
	- "A string, usually in a number form, describing a snapshot of a Package. This number should increase when a Package posts a new snapshot, i.e a higher number means a more up-to-date snapshot."
- Specifier
	- A specifier is a collection of versions
	- Wildcard versions exist (`*`), which indicate that any version of a package works
- Requirement
	- A requirement is a package / specifier pair
- Candidate
	- "A combination of a Package and a Version, i.e. a “concrete requirement”. Python people sometimes call this a “locked” or “pinned” dependency. Both of “requirement” and “dependency”, however, SHOULD NOT be used when describing a Candidate, to avoid confusion."
	- "Some resolver architectures refer this as a “specification”, but it is not used here to avoid confusion with a _Specifier_."
- Resolver
	- The provided "Resolver" class includes dependency resolution logic
- Provider
- Reporter
- Result

## Notes
- It appears that `resolvelib` does not contain any of the code that interacts with `pypi.org`
- In the pip project, the `RequirementCommand` class (from `src/pip/_internal/cli/req_command.py`) contains the code which initializes the resolvelib resolver, and its many dependencies.
	- `make_requirement_preparer`
	- `make_resolver`
	- `get_requirements` parses CLI options
- Where do we hook into the process?

## Pip Download with Debug On
For this section, I'll be referring to `pip` and `resolvelib` interchangeably. Pip contains all of the logic for downloading packages and interpreting their requirements. Resolvelib contains the framework for resolving requirements in an iterative process.

### Unrestricted Boto3, Restricted Botocore
Command: `PIP_RESOLVER_DEBUG=1 pip download boto3 "botocore==1.23.54" -d $(mktemp -d)`

- The first ting that pip does is download wheels for the 2 specified requirements.
- During round 0, resolvelib 
