# Building Images from Dockerfiles

```bash
docker image build -t whateverimagenamethatyouwantsinceyoucanretagitlater .
```

Builds an image with the repository name of
`whateverimagenamethatyouwantsinceyoucanretagitlater`, using the build context
of `.`, the current directory. Only works if there is a file named `Dockerfile`
in the current directory. If your dockerfile has a fancy name like "wehavetosupportWindows😧.Dockerfile", then you can refer to this file with the `--file` or `-f` flag on the build command.

```bash
docker image build \
    -t "whateverimagenamethatyouwantsinceyoucanretagitlater" \
    -f "wehavetosupportWindows😧.Dockerfile" \ 
    .
```

There are a lot of space-saving considerations made when building images, due to
how image layering works within the Docker engine.

## Dockerfile Build Tips

### Stanza Ordering

Make sure that the order of steps in your dockerfile is directly related to how
often the subject of the stanza will change. For example, if you're building a
web app, make sure that copying your source code into the image is performed
closer to the bottom, because all of the steps after the code is copied in will
have to be re-executed, every time you change your code and rebuild the
application.

### When Installing Programs

Make a multi-line RUN stanza when installing lots of programs using the default
package manager, especially when you need to add keys and run the update
command. When you use RUN, an temporary container has to be run, using the
previous image layer. If you have multiple RUNs, the image will be started and
stopped multiple times.

## Extending Official Images

Any image can be used as the subject of the `FROM` command. This will allow you
to create customized images that are built on top of a base application. You
don't need to specify any of the required stanzas when specifying an existing,
non-scratch base image, since they will be inherited from the base image.

```Dockerfile
FROM nginx:latest

# Best practice for changing directories in Dockerfiles
# Don't use `cd`, please
WORKDIR /usr/share/nginx/html

COPY index.html index.html
```

There is no need for a Dockerfile like this:

```Dockerfile
FROM nginx:latest
```

because you can always retag an image without running a build.
