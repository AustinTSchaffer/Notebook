---
tags:
---
# Global Python Packaging Dependency Relationships

## Prior Art
- Jing Wang, Qingbo Wu, Yusong Tan, Jing Xu and Xiaoli Sun, "A graph method of package dependency analysis on Linux Operating system," _2015 4th International Conference on Computer Science and Network Technology (ICCSNT)_, Harbin, 2015, pp. 412-415, doi: 10.1109/ICCSNT.2015.7490780.
	- "Current package managers only provide a local view of the dependency relationship"
	- "In this paper we present our research that target to bridge this gap: we propose a graph method to establish entire distribution package dependency relationship and analyze the complicated relationship graph with relevant properties."
	- Global view was for Ubuntu Kylin 14.04
- A. Decan, T. Mens, M. Claes and P. Grosjean, "When GitHub Meets CRAN: An Analysis of Inter-Repository Package Dependency Problems," _2016 IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER)_, Osaka, Japan, 2016, pp. 493-504, doi: 10.1109/SANER.2016.12.

## Example Failure Case - Boto3/Botocore

`pip install boto3<=1.34.97 botocore==1.23.54`

The issue with this command is that the boto3 dependency is largely unrestricted, but the boto3 depends on a minimum version of botocore, while the pip install command references a specific version of botocore. Pip then has to walk through versions of boto3 in descending order in order to find a version that depends on a valid version of botocore. This looks something like this:

```
Collecting botocore==1.23.54
  Obtaining dependency information for botocore==1.23.54 from https://files.pythonhosted.org/packages/a6/08/3cc6858a2d9fee8538f212944cff08df325828fbfe17801974c95f51f338/botocore-1.23.54-py3-none-any.whl.metadata
  Using cached botocore-1.23.54-py3-none-any.whl.metadata (5.8 kB)
Collecting jmespath<1.0.0,>=0.7.1 (from botocore==1.23.54)
  Obtaining dependency information for jmespath<1.0.0,>=0.7.1 from https://files.pythonhosted.org/packages/07/cb/5f001272b6faeb23c1c9e0acc04d48eaaf5c862c17709d20e3469c6e0139/jmespath-0.10.0-py2.py3-none-any.whl.metadata
  Using cached jmespath-0.10.0-py2.py3-none-any.whl.metadata (8.0 kB)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in ./venv/lib/python3.12/site-packages (from botocore==1.23.54) (2.3)
Collecting urllib3<1.27,>=1.25.4 (from botocore==1.23.54)
  Obtaining dependency information for urllib3<1.27,>=1.25.4 from https://files.pythonhosted.org/packages/b0/53/aa91e163dcfd1e5b82d8a890ecf13314e3e149c05270cc644581f77f17fd/urllib3-1.26.18-py2.py3-none-any.whl.metadata
  Using cached urllib3-1.26.18-py2.py3-none-any.whl.metadata (48 kB)
INFO: pip is looking at multiple versions of boto3 to determine which version is compatible with other requirements. This could take a while.
Collecting boto3
  Obtaining dependency information for boto3 from https://files.pythonhosted.org/packages/09/18/6b9e0bbdc28a11c1f953160934cd10c938811345d80c3d9c5719c18fe522/boto3-1.34.97-py3-none-any.whl.metadata
  Using cached boto3-1.34.97-py3-none-any.whl.metadata (6.6 kB)
  Obtaining dependency information for boto3 from https://files.pythonhosted.org/packages/fe/8d/068288124764cf218a34f8a6e234a7586e0175a8c09a9fc9cf9d8a1be7d1/boto3-1.34.96-py3-none-any.whl.metadata
  Using cached boto3-1.34.96-py3-none-any.whl.metadata (6.6 kB)
  Obtaining dependency information for boto3 from https://files.pythonhosted.org/packages/b0/2b/c5ace773570a839ff869b4482480e805f36b4b01a16fc2cbccb8d3f462fd/boto3-1.34.95-py3-none-any.whl.metadata
  Using cached boto3-1.34.95-py3-none-any.whl.metadata (6.6 kB)
  Obtaining dependency information for boto3 from https://files.pythonhosted.org/packages/9f/3b/5a7a68db7cf2ce25d12224cd73e4aa710fb2d5e938ed455da55705ea5531/boto3-1.34.94-py3-none-any.whl.metadata

...
```

Pip is smart enough to check PyPI for boto3's metadata file, allowing pip to check the dependencies of different versions of boto3 against the installation constraints. However, it has to walk backward through time. It does this so it can find the latest possible packages given the constraints.

If we had access to a graph of $(P_A, V_A) \rightarrow (P_B, V_B)$ tuples, pip could take the constraints and generate a reverse graph as well to find the valid $(P_A, V_A)$ tuples which satisfy the installation constraints, given a pinned version of $(P_B, V_B)$

## Example Failure Case - Z3-Solver and Crosshair-Tool

This one is WAY worse than the boto3/botocore example.

`pip install 'z3-solver<4.11' crosshair-tool`
