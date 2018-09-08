# Container Practice

## Quickstart

```bash
docker container run -d --publish 80:80 nginx:latest
```

Every time you run, docker will create a new container, as long as the command
is valid and the arguments do not conflict with an existing container. Some
useful anatomy of this command:

- `docker container run` specifies that you want to start a new container from a
  specified base image
- `--publish 80:80` specifies that you want port 80 on the container to be
  mapped to port 80 on the host machine.
- `-d` specifies that the container should run in the background. By default,
  the run command will attach the current shell to the std output of the
  container. If you detach, you can always attach later.
- `nginx` is the image, which will be pulled from the docker hub if the latest
  (or specified) version is not already downloaded.
- `:latest` is optional, but shows that you can pull different versions of an
  image.

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
