# Basics of Dockerfiles

Dockerfiles are recipes for building images. They looks like some sort of bash
script, except they aren't. Each command in the dockerfile specifies how to
build a new image layer, which can either add metadata for the image, or
actually change the filesystem of the image.

## Dockerfile Stanzas

There are a lot of commands or stanzas that can be used in a Dockerfile, but
references to what each do can be viewed in online documentation. There are a
few that will be mentioned in this repository, due to how commonly they are
used.

### FROM

The first line in any Dockerfile is always the `FROM` command, which specifies
the base image.

```Dockerfile
FROM debian:jessie
FROM alpine
FROM ubuntu:latest

# This last one is a neat one, specifies a completely empty file system.
# All you get is the kernel
FROM scratch
```

### ENV

Specifies environment variables used by the container when it is run or started
or restarted. Also specifies

```Dockerfile
ENV 
```

### RUN

The RUN command runs any bash commands that you specify. These commands can be
as long or as short as you want. For example, if you need to install a ton of
programs using Debian or Ubuntu as a base image.

```Dockerfile
RUN apt-key adv --keyserver ... --recv-keys ... \
    && echo "deb http://... ... ..." >> /etc/apt/sources.list
    && apt-get update
    && apt-get install a b c d e f g \
    && rm -rf /var/lib/apt/lists/*
```

## EXPOSE

By default, NO PORTS ARE OPENED ON A DOCKER CONTAINER. You have to expose ports
in the Dockerfile, if you want to use them in a virtual network, or expose them
on the host machine later.

```Dockerfile
EXPOSE 80 443 3306 8080 8081
```

## CMD

Required parameter (if the base image has no CMD specified). Specifies the
program that executes EVERY TIME the image is `docker container run`ed, or the
container is started or restarted.

## VOLUME

This Dockerfile command registers a file path in an image as a volume, which results in `docker container run` creating an anonymous volume for containers created from the image. I wrote this segment primarily because if this interesting Reddit question:

> When is VOLUME instruction in Dockerfile is useful? It just seem to create lots of useless anonymous volumes. I don't want anyone to include VOLUME in Dockerfile. It just leaves lots of useless anonymous volumes after stopping and removing containers.
> From: https://www.reddit.com/r/docker/comments/l7hbzd/when_is_volume_instruction_in_dockerfile_is/

Top response:

> Performance mainly. Writing to a container's writable layer is relatively slow compared to writing to a volume. Let's say you're a developer and know your application is going to write a large amount of data to /somedir. If you don't add /somedir as a VOLUME instruction and the end user also doesn't mount /somedir, all of those writes to /somedir end up in that container's writable layer slowing things down.
> By adding /somedir as a VOLUME instruction, you're ensuring your heavily written /somedir directory is bound to something with less of a performance hit. Hopefully the end user takes the effort to mount that same path to a named volume or bind mount, but even if they don't the container doesn't incur any real performance penalty from it.
> This does mean you'll end up some with a lot of dangling volumes over time, but that's what "docker system prune" is for.
