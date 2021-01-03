# Containers vs VMs

Containers and VMs are similar, but Containers are not VMs. 

- A container is just a process. 
- Containers stop when their process stops.
- Containers are limited to the resources of the host machine.
- Containers provide execution isolation, not hardware emulation.

```bash
docker container run --name mongo -d mongo

# Show the processes running in the container
docker container top mongo

# Show all the processes on the host machine. ALL of the processes from
# docker container top mongo will also show in this list.
ps aux

# Stop the container, mongod no longer shows
docker container stop mongo
ps aux

# Start the container, mongod is back
docker container start mongo
ps aux
```
