# Images and Layers

Images are built out of images layers. This allows images to share components,
reducing the total storage space required by multiple versions of an image.
Docker accomplishes this by implementing images as a [Union File System](https://en.wikipedia.org/wiki/UnionFS).

## Layer Sharing in Action

When you `docker image pull`, you can see this in action. Starting from a fresh
Docker installation, if you pull down the `1.14` nginx image, you'll see a few
different layers download from the hub, followed by a final digest. When you
pull the `1.15` nginx image, you can see that the 2 images share a layer
(`802b00ed6f79`), which was only pulled once for the 2 of them.

```bash
docker image pull nginx:1.14
# 1.14: Pulling from library/nginx
# 802b00ed6f79: Pull complete
# ed418bf9bf60: Pull complete
# 94fedb7de3b4: Pull complete
# Digest: sha256:2fa968a4b4013c2521115f6dde277958cf03229b95f13a0c8df831d3eca1aa61
# Status: Downloaded newer image for nginx:1.14
docker image pull nginx:1.15
# 1.15: Pulling from library/nginx
# 802b00ed6f79: Already exists
# c16436dbc224: Pull complete
# 683eac851b28: Pull complete
# Digest: sha256:e8ab8d42e0c34c104ac60b43ba60b19af08e19a0e6d50396bdfd4cef0347ba83
# Status: Downloaded newer image for nginx:1.15
```

This sharing does not only work for a single application. If 2 entirely
different images (different name, different maintainer, different version tag)
both use the version of Ubuntu as the base image, you'll only have to pull down
that image layer once.

You can see the changes and the size of the changes made (in Bytes) using
`docker image history`. Notice how the 2 images have totally different
histories, but the very bottom 2 layers is the exact same.

```bash
docker image history nginx:latest
# IMAGE               CREATED             CREATED BY                                      SIZE
# 06144b287844        3 weeks ago         /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  STOPSIGNAL [SIGTERM]         0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  EXPOSE 80/tcp                0B
# <missing>           3 weeks ago         /bin/sh -c ln -sf /dev/stdout /var/log/nginx…   22B
# <missing>           3 weeks ago         /bin/sh -c set -x  && apt-get update  && apt…   53.8MB
# <missing>           3 weeks ago         /bin/sh -c #(nop)  ENV NJS_VERSION=1.15.3.0.…   0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  ENV NGINX_VERSION=1.15.3-…   0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  CMD ["bash"]                 0B
# <missing>           3 weeks ago         /bin/sh -c #(nop) ADD file:e6ca98733431f75e9…   55.3MB
docker image history mysql:latest
# IMAGE               CREATED             CREATED BY                                      SIZE
# 6a834f03bd02        3 weeks ago         /bin/sh -c #(nop)  CMD ["mysqld"]               0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  EXPOSE 3306/tcp 33060/tcp    0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  ENTRYPOINT ["docker-entry…   0B
# <missing>           3 weeks ago         /bin/sh -c ln -s usr/local/bin/docker-entryp…   34B
# <missing>           3 weeks ago         /bin/sh -c #(nop) COPY file:59647006b032bcb2…   6.53kB
# <missing>           3 weeks ago         /bin/sh -c #(nop) COPY dir:110dcf1221c1f9432…   1.22kB
# <missing>           3 weeks ago         /bin/sh -c #(nop)  VOLUME [/var/lib/mysql]      0B
# <missing>           3 weeks ago         /bin/sh -c {   echo mysql-community-server m…   369MB
# <missing>           3 weeks ago         /bin/sh -c echo "deb http://repo.mysql.com/a…   56B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  ENV MYSQL_VERSION=8.0.12-…   0B
# <missing>           3 weeks ago         /bin/sh -c #(nop)  ENV MYSQL_MAJOR=8.0          0B
# <missing>           3 weeks ago         /bin/sh -c set -ex;  key='A4A9406876FCBD3C45…   25kB
# <missing>           3 weeks ago         /bin/sh -c apt-get update && apt-get install…   44.7MB
# <missing>           3 weeks ago         /bin/sh -c mkdir /docker-entrypoint-initdb.d    0B
# <missing>           3 weeks ago         /bin/sh -c set -x  && apt-get update && apt-…   4.44MB
# <missing>           3 weeks ago         /bin/sh -c #(nop)  ENV GOSU_VERSION=1.7         0B
# <missing>           3 weeks ago         /bin/sh -c apt-get update && apt-get install…   10.2MB
# <missing>           3 weeks ago         /bin/sh -c groupadd -r mysql && useradd -r -…   329kB
# <missing>           3 weeks ago         /bin/sh -c #(nop)  CMD ["bash"]                 0B
# <missing>           3 weeks ago         /bin/sh -c #(nop) ADD file:e6ca98733431f75e9…   55.3MB
```

The `<missing>` tag is a misnomer, just means that there is no specific image
for the layer and does not indicate that something is broken.
