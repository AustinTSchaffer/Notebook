# Container Practice


## Quickstart

```bash
docker container run -d -p 80:80 nginx:latest nginx -T
```

Every time you run, docker will create a new container, as long as the command
is valid and the arguments do not conflict with an existing container. Some
useful anatomy of this command:

- `docker container run` specifies that you want to start a new container from a
  specified base image. If no errors, the command will ALWAYS create a new
  container. Does not reuse any previously created containers.
- `-p 80:80` specifies that you want port 80 on the container to be mapped to
  port 80 on the host machine. Shorthand for `--publish 80:80`
- `-d` specifies that the container should run in the background. By default,
  the run command will attach the current shell to the std output of the
  container. If you detach, you can always attach later.
- `nginx` is the image, which will be pulled from the docker hub if the latest
  (or specified) version is not already downloaded.
- `:latest` is optional, but shows that you can pull different versions of an
  image. For example `nginx:alpine` or `bginx:1.11`.
- `nginx -T` specifies what command the container should run when it starts up.
  Docker images typically have an already specified command that it runs when
  the container starts up, but this can be changed by putting any text after the
  image name in the `docker container run` command. If this specified command
  finishes execution, or stops running for any other reason, the Docker
  container will also stop.

After you docker run, you'll get back an identifier, which uniquely identifies
the container. All containers also get a randomly generated name, if no unique
name is specified.

```bash
docker container ls
docker container stop "<name or id>"
docker container rm "<name or id>"
```


## Naming a Container

```bash
docker container run --publish 80:80 -d --name webhost nginx
```

`--name` specifies the name of the container, which will prevent Docker from
randomly generating a name for the container. This will fail if run a second
time, since the name (and port) will already be in use.


## Stop/Remove 1 Container or Many Containers

Some Docker commands can accept multiple forms of input, as well as multiple
inputs. For example, the stop and rm container commands can take either the name
or the unique IDs of containers as inputs, as well as take that information for
multiple containers.

```bash
docker container run -d --name nginx_1 nginx
docker container run -d --name nginx_2 nginx
docker container run -d --name nginx_3 nginx
docker container run -d --name nginx_4 nginx
docker container stop nginx_1 nginx_2 nginx_3 nginx_4
docker container rm nginx_1 nginx_2 nginx_3 nginx_4

# Alternatively
docker container run -d --name nginx_1 nginx
docker container run -d --name nginx_2 nginx
docker container run -d --name nginx_3 nginx
docker container run -d --name nginx_4 nginx
docker container rm -f nginx_1 nginx_2 nginx_3 nginx_4
```


## What's Happening When You Docker Container Run?

1. Check for the image in the local cache
  1. If there, use it
  2. Download the image from the Docker Hub, or any other configured Docker
     image repositories, and store it in the cache
2. Creates a new container based on the image. This does not copy the image, but
   instead starts a new layer of changes on top of that image.
4. Creates a virtual IP address and opens up the specified ports. Other
   networking things can happen, like if a virtual network is specified.
5. Starts the container using the command specified in the Dockerfile, or using
   the override command specified in the Docker run command.


