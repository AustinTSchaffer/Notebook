# Scaling Out with Routing Mesh

The "magic" of swarm is thanks to the routing mesh. The mesh routes ingress
(incoming) packets for a Service to proper Task. Spans all nodes in the Swarm.
This uses IPVS from the Linux Kernel. Load balances Swarm Services across their
Tasks. Continer-to-container in Overlay network uses Virtual IP (VIP). Swarm
puts a private VIP in front of all services. Private IP inside virtual network
of a Swarm.

1 Service, 10 different containers, no need for a load balancer, Swarm takes
care of load balancing. External traffic incoming to published ports (all nodes
listen). When deploying containers in a swarm, no need to care which nodes are
used. Swarm manages all of that. Swarm will take all incoming requests and
reroute them.

## Example Using Elastic Search

```bash
docker service create \
    --name search \
    --replicas 3 \
    -p 9200:9200 \
    elasticsearch:2

watch curl localhost:9200 | jq '.name'
```

## Tech Works

- Stateless load balancing
- If you have to use session cookies in your application, then you may need to
  add additional layers
- This Load Balancer is at OSI Layer 3 (TCP), not Layer 4 (DNS). Still will need
  another puzzle piece, if you're running multiple websites on the same port on
  the same swarm.
- Both limitations can be overcome with:
    - Nginx or HAProxy LB proxy (stateful load balancers)
    - Docker Enterprise Edition, comes with built-in L4 web proxy. Allows you to
      configure the web.config so "everything just works".
