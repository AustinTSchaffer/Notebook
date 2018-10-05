# Persistent Data using Docker Volumes

## In the Dockerfile

Some `Dockerfile`s use the `VOLUME` stanza. This creates a volume for the
container on startup. In the example below, the Dockerfile defines

```Dockerfile
FROM alpine:latest
VOLUME /
```

```bash
# On a fresh machine
docker volume prune
cat ./Dockerfile
```
