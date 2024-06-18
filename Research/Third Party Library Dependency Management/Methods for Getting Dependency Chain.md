# Methods for Getting Dependency Chain
## PyPI APIs
- https://pypi.org/simple/ - Get the list of app packages (HTML)
	- `https://pypi.org/simple/<project>` - Get the list of links available for one project, by name
- `https://pypi.org/simple/<project>/json` - Get information about a project in JSON format, including all links URLs across all versions of the project.
- `curl -H "Accept: application/json" https://pypi.org/stats/` - Get the size of the problem (currently about 20TB)
- https://stackoverflow.com/questions/30188158/how-to-read-python-package-metadata-without-installation - You can use `pkginfo` to get information about a wheel (`.whl`) or source-dist (`.tar.gz`) without installing the package.

## Metadata File

PyPI exposes the metadata file for various packages without requiring that you download the entire wheel. An example URL for Boto3:

https://files.pythonhosted.org/packages/76/83/1dee8818c499efda9632be228bb7dcbb25e2d8ba8db6410e50d088e255d5/boto3-1.26.35-py3-none-any.whl.metadata

```bash
curl https://files.pythonhosted.org/packages/76/83/1dee8818c499efda9632be228bb7dcbb25e2d8ba8db6410e50d088e255d5/boto3-1.26.35-py3-none-any.whl.metadata 2>&1 | grep '^Provides-Extra'
# Provides-Extra: crt

curl https://files.pythonhosted.org/packages/76/83/1dee8818c499efda9632be228bb7dcbb25e2d8ba8db6410e50d088e255d5/boto3-1.26.35-py3-none-any.whl.metadata 2>&1 | grep '^Requires-Dist'
# Requires-Dist: botocore (<1.30.0,>=1.29.35)
# Requires-Dist: jmespath (<2.0.0,>=0.7.1)
# Requires-Dist: s3transfer (<0.7.0,>=0.6.0)
# Requires-Dist: botocore[crt] (<2.0a0,>=1.21.0) ; extra == 'crt'
```

- Doesn't require full package download
- Shows the exact list of dependencies we care about for each package
- Likely that not all packages will expose this.
	- Doesn't appear to be discoverable from the pypi simple index (https://pypi.org/simple/boto3/ for example)
	- Doesn't appear to be directly discoverable from the pypi JSON API (https://pypi.org/pypi/boto3/json for example)
	- Tack on `.metadata` to the end of the `.whl` link to retrieve it. This may only work for bdist/wheel download links.
- 

## Johnny Dep

https://pypi.org/project/johnnydep

The package `johnnydep` scrapes pip/pypi/wheel/whatever for the depth of information that I need for this project. Digging through its source, it looks like it downloads `.whl`s and `.tar.gz`s in order to scrape information about package dependencies. Though, it unfortunately also looks like it scrapes console output for information about a package's available versions, as opposed to using the https://pypi.org/pypi/package/version/json API. I'm not sure which method of getting available package versions would be more reliable and more efficient.

Relevant: https://github.com/pypa/warehouse/issues/8966

### Example
Given `johnnydep boto3 -o json --fields name specifier`, this program outputs:

```json
[
  {
    "name": "boto3",
    "specifier": ""
  },
  {
    "name": "botocore",
    "specifier": "<1.35.0,>=1.34.98"
  },
  {
    "name": "jmespath",
    "specifier": "<2.0.0,>=0.7.1"
  },
  {
    "name": "s3transfer",
    "specifier": "<0.11.0,>=0.10.0"
  },
  {
    "name": "python-dateutil",
    "specifier": "<3.0.0,>=2.1"
  },
  {
    "name": "urllib3",
    "specifier": "!=2.2.0,<3,>=1.25.4"
  },
  {
    "name": "six",
    "specifier": ">=1.5"
  }
]
```

### Issue 0: The Name
Title.

## Issue 1: No Search Depth Config

Here's the `pipdeptree` output of the same version of `boto3` used in the example. You can see that the specifiers of each package line up with the `johnnydep`.

```
boto3==1.34.98
├── botocore [required: >=1.34.98,<1.35.0, installed: 1.34.98]
│   ├── jmespath [required: >=0.7.1,<2.0.0, installed: 1.0.1]
│   ├── python-dateutil [required: >=2.1,<3.0.0, installed: 2.9.0.post0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   └── urllib3 [required: >=1.25.4,<3,!=2.2.0, installed: 2.2.1]
├── jmespath [required: >=0.7.1,<2.0.0, installed: 1.0.1]
└── s3transfer [required: >=0.10.0,<0.11.0, installed: 0.10.1]
    └── botocore [required: >=1.33.2,<2.0a.0, installed: 1.34.98]
        ├── jmespath [required: >=0.7.1,<2.0.0, installed: 1.0.1]
        ├── python-dateutil [required: >=2.1,<3.0.0, installed: 2.9.0.post0]
        │   └── six [required: >=1.5, installed: 1.16.0]
        └── urllib3 [required: >=1.25.4,<3,!=2.2.0, installed: 2.2.1]
```

The issue with JD is you currently can't specify a search depth, so the JD output is based on cascading constraints of the latest selected package of each top-level constraint. This isn't quite what I'm looking for.

### Issue 2: Performance
Getting the dependency information for `boto3` took 22 seconds total. This is just for one version of boto3 (of thousands).

```bash
time johnnydep boto3 -o json --fields name specifier
# 
# ... debug logs ...
#`
# ... the output ...
# 
# 16.45s user 1.87s system 83% cpu 21.995 total
```
