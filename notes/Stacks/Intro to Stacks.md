# Intro to Stacks

In 1.13, Docker added a new abstraction layer to Swarm called Stacks.

Stacks accept DockerCompose files as their declarative definition for
  services, networks, and volumes. Same service-level syntax, some differences.

We use `docker stack deploy` rather than `docker service create` and
`docker-compose up`

## Is it Compose? Kinda?

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

## Running It

`docker stack deploy -c some-stack-composefile.yml appname`

This will spit out a lot of info really fast. "Creating 'object type' 'name'".
Keep in mind, this does not show that the services are done spinning up. This
just creates the network / volume / service objects, which the scheduler then
uses to create tasks, which then create the containers.

Networks are created immediately, along with a default network.

## Docker Stack Commands

- deploy (Deploys a stack from a file)
- ls (Shows all of your stacks)
- ps (Shows all of the tasks for a stack (not the containers))
- rm (Remove a stack (kill all services))
- services (Shows all of the services in a stack, similar to service ls, except
  limits to the specified stack)

Most important are ls, ps, and services.
