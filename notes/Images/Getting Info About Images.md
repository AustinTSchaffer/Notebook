# Getting Info About Images

Sometimes the documentation of an image is lacking, so it can be hard to
determine how to use the image, and how it works.

One way to gather information is to go find the Dockerfile that was used to
build the image tag that you're looking at. If that Dockerfile is missing the information that you're looking for, for example:

- Exposed Ports (EXPOSE)
- Any Volumes
- CMD
- ENTRYPOINT
- WORKDIR

You can try to look at the base image, from the FROM stanza, to see if that
image has the info that you're looking for.

Another good way, is to pull the image, and use the `docker image inspect`
command. This will show all of the image's metadata that is used to start a new instance of the image, such as:

- default environment variables
- CMD and ENTRYPOINT
- Any volumes that are generated on container start
- Which ports are exposed and can be mapped to the host or accessed from within
  a virtual network.


