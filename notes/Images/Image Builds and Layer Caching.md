# Image Builds and Layer Caching

## TL;DR

Sometimes you don't want to use the layer cache. Enjoy your coffee.

## On With It Then...

This is not strictly related to a certification, but CircleCI is starting to put
out advertisements that are also tutorials on how to configure layer caching for
your Docker image builds, running within CircleCI. That got me thinking about
the ways that a layer cache can make you miss critical bug fixes or security
updates.

One of the best thing about building images is the layering system, which allows
you to reuse layers when building a new tag of an image. In a nutshell, that's
how the `FROM` stanza works. It allows the developer to specify a set of layers
as the base for their application container, which keeps the developer from
having to install a Linux distro every time they make changes to their app.

Could you imagine?

```bash
git diff  # Please always verify your git adds
git add .
git commit -m 'Fixed a null check'

time docker image build . -t myapp:latest
# ...
# real    forever
# user    aeon
# sys     eternity
```

The cool part about this, in my opinion, is that this same principle applies
whenever you build images that have multiple layers. Suppose that

1. you make a change that affects a layer that is later in the process
2. none of the proceeding layers have been changed, including the base image
3. all of the untagged, intermediate layers are still available locally and
   haven't been pruned

If these conditions case, you can avoid rerunning tons of work.

```Dockerfile
FROM debian:9

# Install all packages available for Debian 9 (doesn't actually work, luckily)
RUN apt-get update && apt-get install -y $(apt-cache pkgnames)

# Copy our app into the container
COPY . .
```

If the `apt-get install everything` actually manages to run, then it will save
the layer to the file system and give it a hash as an identifier. Then it will
copy the application's code into the container and give that a hash as an
identifier.

## So What's The Issue?

The issue here is if you are caching layers when you don't know if a proceeding
layer has changed in a meaningful way. In the case above suppose one of the
programs that are installed via `apt-get` was at one point extremely broken with
wide open vulnerabilities that put your application at risk. Coincidentally, the
program was super broken and pushed to the package feeds during the time when an
image was built from the Dockerfile. If you are always using the cache when
building images from this particular Dockerfile, then you will NEVER get the
security fix.

This same principle applies in a lot of situations. I've generated a few
examples below.

- Part of your build process involves getting a resource from an API, that could
  change periodically
- The code libraries that your application depends on are specified using a
  range of values, instead of an explicit point release
- Your application generates a local timestamp that you're using later for some
  reason

In Short: Docker cannot automatically invalidate the cache for any changes that
are external to the context of the directory that contains your application's
source code.

ELI5: If it's not in the folder, Docker can't see it.

## Sounds Pretty Annoying Doesn't It?

Yeah, well that's the price we all pay for efficiency. Don't they say that cache
invalidation is one of the hardest problems in computer science? Right up there
with naming things?

Part of being a product owner is keeping track of all of the dependencies of the
application that you, well, own. If one of your dependencies gets a set of bug
fixes and security updates within the major version that you depend on, you
should be aware of it, and turn on `--no-cache` and `--pull`.

The alternative that I see would be to always pin the versions of the
dependencies that you are using to a specific point release and build. That way,
your cache becomes invalidated, because you have to change a file to indicate a
new version of the dependencies. However, this only applies in situations where
you can explicitly pin the versions in a configuration file. It's much more
common to do this for packaged code libraries than it is for the things that you
install via a package manager. Typically, that's the reason for using base
images that are based on Linux distributions. The distributions manage and keep
track of packages that have breaking changes.

At any rate, do future-you a favor. Reduce your dependencies, upgrade them
periodically, keep track of breaking changes, and turn off the cache when you
have to.
