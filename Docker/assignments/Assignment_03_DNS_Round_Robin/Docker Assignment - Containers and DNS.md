---
tags: Docker, Assignment, DNS, Networking
---

# Assignment 3 - Containers and DNS

This assignment is to test linking between containers within a Docker virtual
network.

## Prerequisites

- Know how to use -it to get shell in a container
- Understand the basics of a Linux Distro
- Docker Container management (run, rm, inspect, port)
- Basics of DNS records

## Objectives

DNS Round Robin. 2 different hosts with 2 different aliases, that respond to the
same name. Multiple IP address and DNS records behind the name that you're
using. For example, the google.com DNS name 100% has more than 1 server that you
can connect to.

Since Docker Engine 1.11, you can assign aliases so that multiple containers
respond to the same DNS address. You can add as many containers that you want
under the same net alias.

## Task

- Create a new virtual network
- Create 2 `elasticsearch:2` containers.
- Research and use `--net-alias search` when creating them to give them an
  additional DNS name to respond to.
- Run `alpine nslookup search` with `--net` to see the 2 containers for the same
  DNS name.
- Run `centos curl -s search:9200` with `--net` multiple times to see the round
  robin in action.

## Solution

```bash
docker container run -d --name es1 elasticsearch:2
docker container run -d --name es2 elasticsearch:2
docker container run -d --name es3 elasticsearch:2

docker network create elasticsearch_net

docker network connect --alias search elasticsearch_net es1
docker network connect --alias search elasticsearch_net es2
docker network connect --alias search elasticsearch_net es3

docker container run --name alpine alpine:3.8 nslookup search 
# nslookup: can't resolve '(null)': Name does not resolve
# Name:      search
# Address 1: 137.155.254.55

docker network connect elasticsearch_net alpine

docker container start -ia alpine 
# nslookup: can't resolve '(null)': Name does not resolve
# Name:      search
# Address 1: 172.19.0.4 es3.elasticsearch_net
# Address 2: 172.19.0.2 es1.elasticsearch_net
# Address 3: 172.19.0.3 es2.elasticsearch_net

docker container run -it --name centos --rm --network elasticsearch_net centos:7 /bin/bash
yum install -y bind-utils
nslookup search
# Server: 127.0.0.11
# Address: 127.0.0.11#53
# 
# Non-authoritative answer:
# Name: search
# Address: 172.19.0.2
# Name: search
# Address: 172.19.0.3
# Name: search
# Address: 172.19.0.4

curl search:9200 # { name: "Mop Man", ... }
curl search:9200 # { name: "Mop Man", ... }
curl search:9200 # { name: "Mister One", ... }
curl search:9200 # { name: "Bishop", ... }
curl search:9200 # { name: "Mop Man", ... }
# etc
exit

docker container rm -f es1 es2 es3 alpine
```

## Notes

Please note that DNS-round-robin is not an acceptable stand-in for a genuine
load balancer.

If you keep retrying the connection to the search service, you'll notice that
the machine that is chosen is a bit random every time.
