# Dependency Hell

Any project that makes it easier to figure out how to upgrade software package dependencies would be a $$$ idea.

My current issue at work is trying to figure out how to upgrade a bunch of dependencies that are _currently_ compatible with each other and my group's source code. My ticket is a bit open ended, but essentially, we need to get Pandas and Snowflake up to date. This will 100% introduce regressions and breaking changes in our source code, but that's just the nature of it.

Ok, also, just dealing with dependencies in general is kind of a madhouse.

So essentially, what if you could generate a graph database of all package/version pairs with relations to the package/version pairs they require and are compatible with? Would that make it easier to drag a package version into the future? A couple of package versions? How do you minimize breaking changes in your source code? Is this even worth doing once you hit a critical mass of dependencies?

So many questions.

I think I'll have another drink.

## Related

In this same vein, Python's most popular package installation systems are essentially arbitrary code execution. We've already seen that pypi.org doesn't have to explicitly (and in many cases doesn't) list the packages that a package requires before you download it. Any benefits of having a system that makes dependency chains easier to navigate can be completely undone by aggressively poorly behaved packages.

So what would an aggressively poorly behaved package look like? Mine dogecoin while you wait? Send hardware info off to a random IP address? Specify random version ranges of random packages? Always installs incompatible versions of different packages?
