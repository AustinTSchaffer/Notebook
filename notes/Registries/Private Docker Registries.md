# Private Docker Registries

Source code for private docker regitries can be found at [docker/distribution on GitHub](https://github.com/docker/distribution).
There is an older version of the software, but that version is marked as
"legacy". The new version is implemented in go.

```bash
docker pull registry
```

- de-facto private container registries
- Not full featured, no web UI, basic auth only, no user roles, just access and
  no-access
- At its core, it's just a web API and a storage system, written in go
- Storage supports local, S3/Azure/Alibab/Google Could, and OpenStack Swift

## Private Docker Registry Considerations

- You can secure your Registry using TLS
- Storage cleanup via Garbage Collection
- Hub caching via "--registry-mirror". Docker daemons will cache images in that
  registry. Provides some failover
- out of the box, docker will not talk to registries that aren't using HTTPS.
  "Secure by Default". For remote self-signed TLS, enable "insecure-registry" in engine (not recommended).

## Run a Private Docker Registry

The registry runs on port 5000.

```bash
docker run -d --rm \
    --name myregistry \
    -p 5000:5000 \
    registry

docker run hello-world

docker tag hello-world 127.0.0.1:5000/my-hello-world

docker push 127.0.0.1:5000/my-hello-world
```
