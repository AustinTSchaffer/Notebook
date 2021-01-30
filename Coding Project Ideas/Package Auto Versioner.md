---
tags: Ideas, Programming, SemanticVersioning
---

# Auto-Versioning Python Packages

## Semantic Versioning

Semantic Versioning 2.0.0, as described by https://semver.org defines the following rules for semantic versions:

> Given a version number `MAJOR.MINOR.PATCH`, increment the:
>
> 1. `MAJOR` version when you make incompatible API changes,
> 2. `MINOR` version when you add functionality in a backwards compatible manner, and
> 3. `PATCH` version when you make backwards compatible bug fixes.
>
> Additional labels for prerelease and build metadata are available as extensions to the `MAJOR.MINOR.PATCH` format.

Minor note, Microsoft uses an additional component to describe the `BUILD` number, since MS has so many slow-moving gears, they need an additional version number just to help manage their release cycle.

One problem that always seems to trip up package maintainers is when and how to change the semantic version of their packages. There also seems to be varying methodologies on when to change a package version when there's a breaking change (Looking at you two, `urllib3` and `requests`).

## Existing Tools

I've used tools like [`versioneer.py`](https://github.com/python-versioneer/python-versioneer) in the past, which are great at unifying your `git` tags with your package versions. .NET has a similar tool called [GitVersion](https://github.com/GitTools/GitVersion). [Here's another written entirely in shell](https://github.com/markchalloner/git-semver). All of these tools require manual intervention to create/update git tags and/or and enforcement of stylized git commit messages to determine what the new semantic version should be.

I've yet to see a tool that checks the previous version of a library with the current version of a library to see the difference between the 2, as far as the public interface of that library is concerned, and make a determination of what the new version number should be. It should be possible. Some links that elude to what I'm getting at:

- https://github.com/semantic-release/cracks
- https://docs.buf.build/breaking-overview/
- https://softwarerecs.stackexchange.com/questions/34224/detect-changes-in-a-python-librarys-api

## Considerations

- Changes*/removals to existing features provided by a library should be considered `MAJOR` i.e. "breaking" changes. (The exception to "changes" is if the interface of a function/method changes in a way that does not violate the complexities of this [covariance vs contravariance](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)) article that I haven't yet fully wrapped my head around on an academic level.)
- Additions to the public interface should be considered `MINOR` changes. There's probably a discussion be had about whether an additional constant should count as a `MINOR` or `PATCH` change.
- If the public interface of the library appears to not change, then it's more than likely a `PATCH` change, i.e. bugfix.
- Comparisons between a tagged and untagged version of a library only make sense if you're comparing the untagged version with a the most recently tagged version. Example, if you're comparing `v4.0.1` against `v1.32.1`, any such auto-detection tool would most likely just say `v2`. This should also be observed when generating a hotfix.

## Features

- The considerations outlined above are idealistic. Teams may want to adjust what is considered major, minor, and patch changes.
- There should be configuration options to select what files should be considered part of the public interface of a package. Python conventions dictate that a leading `_` means "use at your own risk".
- Any such tool should be able to fetch the old version and new version of a package when making a determination. There should be a way to serialize the public interface of a package so it can be sorted, and visually compared. One such idea in the Python universe is auto-generating [stubs files](https://pypi.org/project/pygenstub/1.0a6/), which are essentially header files.
- Additional kwargs and/or optional arguments should be considered minor changes.
