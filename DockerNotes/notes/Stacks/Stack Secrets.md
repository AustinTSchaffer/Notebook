# Secrets for Stacks and Swarms

- Easiest "secure" solution for storing secrets in Swarm
    - Encrypted on Disk
    - Encrypted in Transit
    - Only sent to nodes that "need to know"

- What is a Secret?
    - Usernames and Passwords
    - TLS certificates and keys
    - SSH keys
    - Any unique-data you want to keep PRIVATE.

- Can store anything up to 500kB in size

- Doesn't require you to rewrite your apps

## Raft

- As of 1.13, Swarm Raft DB is encrypted on disk. By default.

- Only stored on manager nodes

- Default is Managers and Works "control plane" is TLS + Mutual Auth

- Secrets are first stored in Swarm, then assigned to a service(s). "Who's
  allowed to use this secret?"

- Only containers in assigned Serice(s) can see the contents of the secret.

- Look like files in container, but are actually in-memory fs
    - `/run/secrets/<secret_name>`
    - `/run/secrets/<secret_alias>` (different name, same key)

- docker-compose can use file-based secrets, but it's not actually secure
  (yolo). DONT USE COMPOSE IN PRODUCTION. OMG STOP ASKING IF YOU CAN. Secrets
  are a "Swarm Only Thing". Compose just mounts the secrets into the container.
