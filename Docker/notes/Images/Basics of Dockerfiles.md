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
