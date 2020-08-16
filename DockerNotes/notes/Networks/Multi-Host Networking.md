# Multi Host Networking

This note applies to both Docker Networks and Docker Swarm.

- `--driver overlay` when creating a virtual network
- For container-to-container comms inside a single Swarm
- Optional IPSec (AES) encryption on network creation. Provides encryption for
  all network traffic.
- Each service can be connected to multiple networks (frontend, backend)

## Example

```bash
# Swarm already configured with > 1 nodes
    docker network create --driver overlay mydrupal

    docker service create \
        --name psql \
        --network mydrupal \
        -e POSTGRES_PASSWORD=mypass \
        postgres

    docker service ps psql

    docker service create \
        --name drupal \
        --network mydrupal \
        -p 80:80 \
        drupal
```
