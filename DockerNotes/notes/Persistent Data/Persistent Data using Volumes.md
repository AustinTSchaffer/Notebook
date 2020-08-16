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

# Look for the Name property of .Mounts
docker container inspect mysql 

# Use the Name property from the above
docker volume inspect $THE_VOLUME_NAME_OR_ID

# Destroy the container, just like you would in production 😉
docker container rm -f mysql

# Still works
docker volume inspect $THE_VOLUME_NAME_OR_ID 

# Creates a new volume for the /var/lib/mysql directory of the container
docker container run -d \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=True \
    -v /var/lib/mysql \
    --name mysql mysql
docker container rm -f mysql

# Creates a "Named Volume", a volume named "mysql-db". More user friendly. 
docker container run -d \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=True \
    -v mysql-db:/var/lib/mysql
    --name mysql mysql
docker container rm -f mysql

# Uses the Named Volume from before.
docker container run -d \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=True \
    -v mysql-db:/var/lib/mysql
    --name mysql mysql
# docker container rm -f mysql
docker container stop mysql

# Mounts the volumes that the "mysql" container is using.
docker container run -d \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=True \
    --volumes-from mysql
    --name mysql2 mysql

docker container rm -f mysql mysql2

# Look at the mess we made.
docker volume ls

# Ok clean it up
docker volume prune
```
