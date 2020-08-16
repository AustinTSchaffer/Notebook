# Why Docker Swarm?

- Containers everywhere = new problems
- Apps can run the same on any platform. ANY.
- How do we deploy or maintain thousands of containers across multiple servers?
- How do we automate container lifecycle?
- How do we easily scale out/in/up/down?
- How can we replace containers without downtime? (blue/green deploy)
- How do we control/track where containers get started?
- How can we create cross-node virtual networks?
- How can we ensure tht only trusted servers are running our containers?
- How can we store secrets, keys, passwords, and get them to the right
  containers, and only that container?

## Docker Swarm Mode is Built-In Orchestration

- Swarm Mode is server clustering solution built inside Docker.
- This is not related to Swarm "classic", pre-1.12 versions.
- Summer 2016, at Dockercon, SwarmKit toolkit was announced.

1.13, Stacks and Secrets were added

None of these features are available by default, in an attempt to prevent them
from interfering with previous docker functionality.

- docker swarm
- docker node
- docker service
- docker stack
- docker secret

## Swarm Terminology

- Raft consensus group
- Managers and Workers
- Managers are workers that have the ability to control the swarm
- Each server has to run Docker.

## Docker Service Command

Replaces the `docker run` command. A single service can have multiple
containers. Replicas. Manager nodes decide where in the swarm to run new
containers (which servers).

What happens when you `docker service create`?

### Manager Node

- "API" accepts command from client and creates a service object
- "Orchestrator" reconciliation loop for service objects and creates tasks
- "Allocator" Allocates IP addresses to tasks
- "Scheduler" Assigns nodes to tasks
- "Dispatcher" Checks in on workers

### Worker Node

- "Worker" Connects to dispatcher to check on assigned tasks
- "Executor" Executes the tasks assigned to worker node

