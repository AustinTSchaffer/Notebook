# Intro to Stacks

In 1.13, Docker added a new abstraction layer to Swarm called Stacks.

Stacks accept DockerCompose files as their declarative definition for
  services, networks, and volumes. Same service-level syntax, some differences.

We use `docker stack deploy` rather than `docker service create` and
`docker-compose up`

Stacks manage all of the networks and volumes, similar to DockerCompose. The
Swarm Stack can use "external", which allows the stack to use networks and
volumes that were defined/created externally to the Stack.

New key to compose file `deploy:`. DockerCompose ignores this key, but lets you
know that you're doing it wrong.

Can no longer use `build:` key (yet, might never happen). Building should happen
in CI, but NOT ON the Swarm node (limited storage space on cloud VMs). Swarm
ignores this key, but lets you know that you're doing it wrong.

`docker-compose` cli is not needed on Swarm server. It's just the file syntax
that is the same. `docker-compose` is not meant for production anyway. It's a
local automation tool, for dev purposes only. Feels more like a toy every day.

Check out the diagram in this same folder. It's missing "secrets", but that will
be covered later.
