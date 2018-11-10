# Health Checks in Dockerfiles

The `HEALTHCHECK` stanza was added in Docker 1.12. It is supported in
Dockerfiles, Compose YAML, docker run, and Swarm Services.

The Docker Engine with run command as an `exec` inside of the container (for
example, curl localhost). `exit 0` is OK, `exit 1` is an Error. Three container
states: "starting", "healthy", "unhealthy".

This helps monitor your application's status, but is not a monitoring
replacement. This is just to help docker determine how its containers are doing,
and whether it needs to recreate the container.

Healthcheck statuses show up in `docker container ls`. The last 5 healthchecks
show in `docker container inspect`. Docker run does nothing with healthchecks.
Services will replace tasks if they fail healthchecks. Service updates wait for
them before continuing.

## Example using `docker run`

The `|| false` makes sure that the return code of the healthcheck is either 0 or
1.

```bash
docker run \
    --health-cmd="curl -f localhost:9200/_cluster/health || false" \
    --health-interval=5s \
    --health-retries=3 \
    --health-timeout=2s \
    --health-start-period=15s \
    elasticsearch:2
```

## Using `Dockerfile`

Options for the healthcheck command

- `--interval=DURATION` (default: 30s)
- `--timeout=DURATION` (default: 30s)
- `--start-period=DURATION` (default: 0s) (19.09+)
- `--retries=N` (default: 3)

### Nginx Example

The `|| exit 1` does the exact same thing as `|| false`.

```Dockerfile
FROM nginx:1.13

HEALTHCHECK \
    --timeout=3s \
    --interval=30s \
    --retries=3 \
    CMD curl -f http://localhost/ || exit 1
```

A more sophisticated healthcheck for Nginx would be to

### Postgres Example

```Dockerfile
FROM postgres

# specify a real user with -U to prevent errors in PostGres log

HEALTHCHECK \
    --interval=5s \
    --timeout=3s \
    CMD pg_isready -U postgres || exit 1
```

### Compose or Stack YAML Example

Your compose file version must be at least 2.1 in order to start using
healthchecks within your YAML configs. In order to use the Start
Period option, you need to use compose file version 3.4, minimum.

```yml
version: "3.4"

services:
  web:
    image: nginx
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost", "||", "false"]
      interval: 1m30s
      timeout: 10s
      retries: 3
      start_period: 1m
```
