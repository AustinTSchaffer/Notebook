# Python Packaging Deep Dive

## The Problem

For each package on PyPI:

- What versions of that package are available on PyPI?
- Which Python version(s) does the package have a native installer for?
- Which platforms does the package have a native installer for?
- Which architectures does the package have a native installer for?
- Which "extras" are available for that version of the package?

Given all combinations of the above bullet points, which versions of which packages does the package depend on?

We should be able to look at https://pypi.org/simple to determine most of these questions and iterate over all of the download links. The biggest complication in this list is the "extras" bullet, which will require some combinatorics.

## Complications

The more I look into this problem, the more I realize that I'm probably going to have to install every version of every package on PyPI. There's PEP 517 that looks to improve this system across the board, but it's been in review since 2015 at least. (https://www.python.org/dev/peps/pep-0517/)

Remembering that many Python packages rely on arbitrary code execution when they're installed, there's no limit to the number of factors that can affect the dependencies of a package. For this project we have to draw the line somewhere.

- platform
- architecture
- Python version
- package "extras"

Some additional notes on these categories:

Some PyPI packages, such as Pandas, are platform dependent. You can see references to Linux, Mac, and Windows just in Pandas's PyPI listing (https://pypi.org/simple/pandas/). There's even multiple versions of `manylinux` in the listing, including `2010`, `2014`, and `1` https://www.python.org/dev/peps/pep-0599/. If we're just using Linux hosts for the program that performs this full data scrape of PyPI, we will probably only be able to determine the full set of Python packages that are either dependent on Linux or are otherwise platform independent. Some packages could require different packages based on platform, and there's almost no way to be sure unless you install the package on the specified platform.

Some PyPI packages, such as Numpy, are architecture dependent. Numpy lists a few options on PyPI. There's no reason that a package could require different packages depending on platform.

Both Pandas and Numpy provide different installers based on the Python version, which you also can see in their simple index pages. The same rules apply here as well.

Just look at the download options for Numpy `1.20.1`.

```
numpy-1.20.1-cp37-cp37m-macosx_10_9_x86_64.whl
numpy-1.20.1-cp37-cp37m-manylinux1_i686.whl
numpy-1.20.1-cp37-cp37m-manylinux1_x86_64.whl
numpy-1.20.1-cp37-cp37m-manylinux2010_i686.whl
numpy-1.20.1-cp37-cp37m-manylinux2010_x86_64.whl
numpy-1.20.1-cp37-cp37m-manylinux2014_aarch64.whl
numpy-1.20.1-cp37-cp37m-win32.whl
numpy-1.20.1-cp37-cp37m-win_amd64.whl
numpy-1.20.1-cp38-cp38-macosx_10_9_x86_64.whl
numpy-1.20.1-cp38-cp38-manylinux1_i686.whl
numpy-1.20.1-cp38-cp38-manylinux1_x86_64.whl
numpy-1.20.1-cp38-cp38-manylinux2010_i686.whl
numpy-1.20.1-cp38-cp38-manylinux2010_x86_64.whl
numpy-1.20.1-cp38-cp38-manylinux2014_aarch64.whl
numpy-1.20.1-cp38-cp38-win32.whl
numpy-1.20.1-cp38-cp38-win_amd64.whl
numpy-1.20.1-cp39-cp39-macosx_10_9_x86_64.whl
numpy-1.20.1-cp39-cp39-manylinux2010_i686.whl
numpy-1.20.1-cp39-cp39-manylinux2010_x86_64.whl
numpy-1.20.1-cp39-cp39-manylinux2014_aarch64.whl
numpy-1.20.1-cp39-cp39-win32.whl
numpy-1.20.1-cp39-cp39-win_amd64.whl
numpy-1.20.1-pp37-pypy37_pp73-manylinux2010_x86_64.whl
numpy-1.20.1.zip
```

Given the above 3 categories, you then have to also consider every combination of the package's provided "extra requirements" lists. Typically you'll see extras for "dev" and "test". As an atypical example, where the extras likely affects a production deployment/installation of boto3/botocore, `botocore` has an extra named `"crt"`, which adds the `awscrt` to the list of required packages.

```bash
johnnydep botocore -o json --fields name requires --no-deps
# [
#   {
#     "name": "botocore",
#     "requires": [
#       "jmespath<1.0.0,>=0.7.1",
#       "python-dateutil<3.0.0,>=2.1",
#       "urllib3<1.27,>=1.25.4"
#     ]
#   }
# ]

johnnydep botocore[crt] -o json --fields name requires --no-deps
# [
#   {
#     "name": "botocore",
#     "requires": [
#       "awscrt==0.11.11",
#       "jmespath<1.0.0,>=0.7.1",
#       "python-dateutil<3.0.0,>=2.1",
#       "urllib3<1.27,>=1.25.4"
#     ]
#   }
# ]
```

## Note on `manylinux`

`manylinux` seems to be an infix that controls what version of `pip` is supported by the package's distribution.

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

