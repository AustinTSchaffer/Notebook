# Domain 1: Orchestration (25% of exam)

## Complete the setup of a swarm mode cluster, with managers and worker nodes

The first node in a swarm mode cluster must perform do a `docker swarm init`.
This will initialize a Docker swarm, and will spit out a token, allowing worker
nodes to join the swarm. You can also add manager nodes to this swarm, using the
manager join token. You can access both of these tokens from any manager node in
the swarm, using `docker swarm join-token`.

```bash
$ docker swarm init
$ docker swarm join-token manager
$ docker swarm join-token worker
```

Once the first node in a swarm has been initialized, and you have grabbed the
join tokens, you can add any number of managers and workers to the swarm by
running the

A couple of important things to note, Docker hosts that have multiple configured
IP addresses will often ask which IP should be used to broadcast. This will
configure the IP address that will be used to populate the join-tokens. This IP
should also be the IP that is connected to the domain name for the host machine
and/or should be an IP that is accessible to all of the other machines in the
swarm. Also, swarm mode requires a few TCP and UDP ports.

> The following ports must be available. On some systems, these ports are open
> by default.
>
> - TCP port 2377 for cluster management communications
> - TCP and UDP port 7946 for communication among nodes
> - UDP port 4789 for overlay network traffic
>
> If you plan on creating an overlay network with encryption (--opt encrypted),
> you also need to ensure ip protocol 50 (ESP) traffic is allowed.

## State the differences between running a container vs running a service

Instead of `docker container run`, services can be created using
`docker service create`. The syntax of these 2 commands is mostly the same,
except one creates a service, and the other only creates a single container. A
service is not a container. A service defines a configuration for a container.
**dockerd** will then have to pick up the service and generate tasks for the
service. These tasks will then create/update/destroy containers for the service.

Each `docker container run` command can only create a single container. The
`docker service create` command allows you do define services with multiple
"replicas", which will allow the dockerd to create the specified number of
containers that all have the same configuration. Also, a single service with
multiple replicas can be replicated across all of the nodes in the swarm.

## Demonstrate steps to lock a swarm cluster

Docker swarm locking procedures

- On swarm init, you can set `--autolock`, which will require a key to unlock
  stopped swarm managers before starting them again.
- On swarm init, you can use `--cert-expiry duration` to specify the lifetime of
  swarm certificates. In docker `18.09`, this duration defaults to 90 days.
- On swarm init, you can use `--external-ca external-ca` to specify an external
  certificate authority.
- You can specify overlay networks that allow communication between containers
  running in the swarm. This network can be setup so that all traffic is
  encrypted.

## Extend the instructions to run individual containers into running services under swarm

Instead of using `docker container run`, you have to use
`docker service create`. The syntax of these 2 commands is mostly the same,
except one creates a service, and the other only creates a single container.

There are some options that are exclusive to each command, which are fully
explained in the documentation for each command, but other than differing
options, these commands work almost identically.

```bash
# Create a container
$ docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

# Create a service
$ docker service create [OPTIONS] IMAGE [COMMAND] [ARG...]
```

## Interpret the output of "docker inspect" commands

`docker inspect` allows you to dump information about the configuration and the
current state of any object currently running in Docker. You can use the name of
the object, but if there is any ambiguity with that name, like a case where a
container and a network share a name, you can use the object's unique ID.

The output of this command will be formatted as JSON.

## Convert an application deployment into a stack file using a YAML compose file with "docker stack deploy"

## Manipulate a running stack of services

If you used `docker stack deploy` to specify your stack of services, you can
modify the stack configuration through the YAML configuration file, and then
redeploy the stack with `docker stack deploy`.

If you manually performed a `docker service create` for each of the services in
your stack, you can change any of the properties of that service using
`docker service update`.

You may also be able to modify a service that was created by
`docker stack deploy` using `docker service update`, but that is not
recommended, because then the state of the service will not match the
configuration recorded in the YAML file.

## Increase # of replicas

```bash
# Create a service with a single replica (default number of replicas)
docker service create --name someservice alpine ping 8.8.8.8

# Set the replicas to 10 for that service
docker service update --replicas=10 someservice

# Clean up
docker service rm someservice
```

## Add networks, publish ports

## Mount volumes

## Illustrate running a replicated vs global service

## Identify the steps needed to troubleshoot a service not deploying

## Apply node labels to demonstrate placement of tasks

## Sketch how a Dockerized application communicates with legacy systems

## Paraphrase the importance of quorum in a swarm cluster

## Demonstrate the usage of templates with "docker service create"
