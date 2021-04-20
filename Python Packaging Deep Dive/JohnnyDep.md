# Johnny Dep

The package `johnnydep` scrapes pip/pypi/wheel/whatever for the depth of information that I need for this project. Digging through its source, it looks like it downloads `.whl`s and `.tar.gz`s in order to scrape information about package dependencies. Though, it unfortunately also looks like it scrapes console output for information about a package's available versions, as opposed to using the https://pypi.org/pypi/package/version/json API. I'm not sure which method of getting available package versions would be more reliable and more efficient.
