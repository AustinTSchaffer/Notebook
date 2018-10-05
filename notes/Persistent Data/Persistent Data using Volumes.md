# Persistent Data using Docker Volumes

## In the Dockerfile

Some `Dockerfile`s use the `VOLUME` stanza. This creates a volume for the
container on startup. In the example below, the Dockerfile defines a volume,
which creates a volume for the container whenever the

```Dockerfile
FROM alpine:latest
VOLUME /test
```

Using the image:

```bash
# On a fresh machine
docker volume prune
docker image build . -t volumetest 

docker container run \
    --name myalpine volumetest \
    touch /test/dont_lose_me.data

docker container run \
    --volumes-from myalpine \
    --name myalpine2 volumetest \
    ls /test
    
# dont_lose_me.data

docker container prune
docker image rm volumetest
docker image prune
docker volume prune
```

If you use Docker (container|volume) inspect, you can see 

1. Which volume(s) hold the container's data
2. Where those volumes are stored on the host machine

If you're on Linux, you can `cd` to that directory on the host machine and `ls`
the volume directories. The UFS is not encrypted and not compressed.

## How Safe is the Data?

Even if you remove all of containers that use a volume, the volume will remain
on the host machine, and can be managed using the Docker volume commands, and
even attached to a new container, or backed up on the host machine.

There is a special flag in `docker container rm` and `docker-compose down` that
will remove the volume(s) along with the associated container(s). That flag is
`-v`, so be careful if you like using "verbose" mode.

**MySQL Example:**

```bash
docker container run -d \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=True \
    --name mysql mysql

docker container inspect mysql # Look for the Name property of Mounts
docker volume inspect $THE_VOLUME_NAME_OR_ID # Use the Name property from the above
docker container rm -f mysql # Destroy the container, just like you would in production
docker volume inspect $THE_VOLUME_NAME_OR_ID # Still works
```
