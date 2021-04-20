# Testing with Retrying

I'm currently testing some edge cases with the `retrying` package, which is a dependency of Plotly that I found interesting at the time. The current (Apr 2021) version of this package is `1.3.3`. `retrying==1.3.3` of this package depends on `six>=1.7.0`. PyPI does not seem to have this information available.

```bash
$ curl -s https://pypi.org/pypi/retrying/1.3.3/json | jq '.info.requires_dist'
# null
```

I'm currently playing with trying to gather information on this package without performing a _complete_ installation. `pip check` seems to know the version ranges when a conflict arises, but doesn't display that information unless there's a conflict.

```bash
$ pip install --no-deps retrying
# Processing /home/austin/.cache/pip/wheels/c4/a7/48/0a434133f6d56e878ca511c0e6c38326907c0792f67b476e56/retrying-1.3.3-py3-none-any.whl
# Installing collected packages: retrying
# Successfully installed retrying-1.3.3

$ pip check
# retrying 1.3.3 requires six, which is not installed.

$ pip install six==0.9.0
# Processing /home/austin/.cache/pip/wheels/c5/cf/43/143470523d8f4ba5c19c900973e78adf7a6ff2a0661d32800d/six-0.9.0-py3-none-any.whl
# ERROR: retrying 1.3.3 has requirement six>=1.7.0, but you'll have six 0.9.0 which is incompatible.
# Installing collected packages: six
# Successfully installed six-0.9.0

$ pip check
# retrying 1.3.3 has requirement six>=1.7.0, but you have six 0.9.0.
```
