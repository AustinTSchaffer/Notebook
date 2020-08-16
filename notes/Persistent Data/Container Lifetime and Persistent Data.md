# Container Lifetime and Persistent Data

Key Concepts

- immutable and ephemeral
- Volumes and how they work
- Bind mounts for volumes

## "Immutable" and "Ephemeral"

Containers are meant to be immutable and ephemeral. This is fancy talk for
"containers should not change too much" and "containers probably shouldn't stick
around for too long." This does not mean that containers can't be used as
Daemons, but that's up to you to decide. 

This helps define an "immutable infrastructure", which allows containers to be
easily redeployed. This also helps when upgrading your infrastructure, because
you don't need to migrate individual files from a container when bumping up the
version number on the base image.

Again, this is ideal. Programs are messy, and most read and write logs and other
unique data, referred to as "persistent data". Docker's volumes feature allows
your containers to preserve this data, while also decoupling the data from the
runtime that is a container.

If a container has persistent data that isn't in a volume, it will remain in the
Union File System (UFS) until the container is **removed**. If a container is
just stopped, it is possible to pull data off of the container. Once the
container is removed however, all of that data is gone.

## Volumes 

Creates a special location outside of the UFS, that allows data to be stored and
tracked by the Docker engine.

## Bind Mounts

Link a container path and a host path, allowing a container to read and write
files on the host machine.
