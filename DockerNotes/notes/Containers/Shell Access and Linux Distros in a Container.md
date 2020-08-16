# Shell Access, Linux Distros, and Linux Containers

## Shell Access

There is no need to install SSH on the containers themselves, if you have access
to the host machine.

```bash
# Run a new container, detach output, but start an interactive session instead
docker container run -it [other options] [image] [command]

# Executing a command/program on a container, interactively, such as bash
docker container exec -it [other options] [container name] [command]

# Start a stopped container, 
docker container start -ai [other options] [container name]
```

The `i` option stands for "interactive", while the `t` option stands for
"pseudo-tty". When you use the `run` syntax, you have to specify a new command.
Typically, it's best to start the container and connect to it later using the
`exec` syntax.


## CentOS Distro Example

You can grab a .ISO for most linux distributions for free for installation on a
physical machine or a VM. Docker also has a lot of the distros available to
download as Docker images. The full ISOs provided by the manufacturer typically
have a lot of software installed that are not really necessary for running the
OS, so the Docker containers typically omit a lot of that software. This means
that you can use OS images as a base image for you application, in case the
application is designed to run on a specific OS. You can also use the
application's Docker file to install additional programs.

Let's not get too complicated at this stage and just run some OS as a Docker
container.

```bash
docker run -it --name centos centos
```

This will (download the latest CentOS image and) start a container based on the
latest CentOS image. Using the `-it` options, it'll start the container and drop
you into a shell. Fom here, you can install programs or do anything else that
you can do just like how it works when running the OS in a VM or on a physical
machine.


## What is Alpine?

It's a small security-focused Linux distribution. VERY small. It's only 5MB in
size and is becoming a very popular base image due to its size.

```bash
docker image pull alpine
date && docker image ls alpine
# Sat Sep  8 16:47:03 EDT 2018
# REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
# alpine              latest              11cd0b38bc3c        2 months ago        4.41MB
```

Alpine is super small, so don't be surprised if it feels like another planet.
For example, even if your host machine has `bash`, Alpine does not. Alpine has
`sh`. Alpine uses `apk`, which you can use to install any of the additional
programs that you need.

```bash
docker container run -it alpine bash # No
docker container run -it alpine # Better
docker container run -it alpine sh # Best
```
