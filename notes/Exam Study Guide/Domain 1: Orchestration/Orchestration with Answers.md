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

Please see the notes section on Stacks for the usage of YAML files.

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

**Networks**

You can add networks to swarm services, if and only if the networks are using
some form of an "overlay" network, which specifies that the network works across
all of the nodes in a swarm.

On creation:

```bash
docker network create --driver overlay mynet

docker service create \
    --network mynet \
    --name myservice \
    nginx
```


On update:

```bash
docker service update --help | grep net
# --network-add network                Add a network
# --network-rm list                    Remove a network

docker network create --driver overlay newnet

docker service update \
    --network-add newnet \
    --network-rm mynet \
    myservice
```

**Ports**

On creation:

```bash
docker service create \
    -publish 8081:8081 \
    -p published=8080,target=80 \
    --name myservice \
    nginx
```

On update:

```bash
docker service update \
    --publish-add 8082:8080 \
    --publish-rm 8081 80 \
    myservice
```

## Mount volumes

When specifying volume options for services, you need to make sure that you are using the term "mount", instead of the term "volume". The relevant options are:

- `docker service create`
  - `--mount`
- `docker service update`
  - `--mount-add`
  - `--mount-rm`

If you are setting up a `bind` type mount on either creation or update, the
directory must exist on all docker hosts that might accept a container from the
service. If you are setting up a `volume` type mount, the new volumes will bes
either created or reused.

On creation: 

```bash
mkdir /root/mymount1

docker service create \
    --mount type=volume,source=a-new-volume,destination=/path/in/container \
    --mount type=bind,source=/root/mymount1,destination=/another/path/in/container \
    --name myservice \
    --replicas 3 \
    nginx:alpine
```

On update:

```bash
docker service update \
    --mount-add type=volume,source=another-new-volume,destination=/yet/another/path/in/container \
    --mount-rm /another/path/in/container \
    myservice
```

## Illustrate running a replicated vs global service

Using the `--mode` option flag, you can specify "replicated" vs "global".
"replicated" is the default, and allows you to specify a number of replications
for the service, which will be spread across all valid nodes in the swarm, more
or less evenly. "global" specifies that every active node should have a running
instance of the service.

```bash
docker service create \
    --mode global \
    --name my_redis_service  \
    redis:3.0.6

# vs

docker service create \
    --replicas 5 \
    --name my_redis_service \
    redis:3.0.6
```

There is no option to update mode after the service has already been created.
The mode must be specified on service creation.

## Identify the steps needed to troubleshoot a service not deploying

## Apply node labels to demonstrate placement of tasks

## Sketch how a Dockerized application communicates with legacy systems

## Paraphrase the importance of quorum in a swarm cluster

## Demonstrate the usage of templates with "docker service create"
