#!/bin/sh

# Set up the frontend and backend VNets

docker network create \
    --driver overlay \
    frontend

docker network create \
    --driver overlay \
    backend

# DB Structures (No ports external to overlay VNets)

docker service create \
    --replicas 1 \
    --network frontend \
    --name redis \
    redis:3.2

docker service create \
    --replicas 1 \
    --mount type=volume,source=db-data,target=/var/lib/postgresql/data \
    --network backend \
    --name db \
    postgres:9.4

# Backend Worker (No ports external to overlay VNets)
# Detach, since no dependencies

docker service create -d \
    --replicas 1 \
    --network frontend \
    --network backend \
    --name worker \
    dockersamples/examplevotingapp_worker

# Admin Interface (Could be IP / Logon Restricted, or a proxy)
# Detach, since no dependencies

docker service create -d \
    --replicas 1 \
    --network backend \
    -p 8080:80 \
    --name result \
    dockersamples/examplevotingapp_result:before

# Public Interface (HTTP Port 80)
# Detach, since no dependencies

docker service create -d \
    --replicas 3 \
    --network frontend \
    -p 80:80 \
    --name vote \
    dockersamples/examplevotingapp_vote:before
