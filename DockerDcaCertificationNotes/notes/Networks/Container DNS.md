# Docker Networks and DNS

The IP addresses of Docker containers are predictable, but you can't rely on them when setting up applications using containers, especially for multi-container applications. The DNS is the key to inter-container communication, since configurations are so dynamic.

## Naming

Can't rely on IP addresses for connecting from one container to another. The Docker solution for this, is that the Docker daemon uses a built-in DNS server that containers can use. This DNS allows containers to talk to each other by referencing each other by the same name.

If you spin up a new container in a new network, this allows the container to utilize the built in DNS. If you spin up another container in that same network, the 2 containers can reference each other.

The DNS defaults the hostname of each container to the name of the container, but it is possible to set up aliases for each container.

### Example

```bash
# Starting from a blank slate
docker network create my_app_net

docker container run -d \
    --name nginx_1 \
    --network my_app_net \
    nginx

docker container run -d \
    --name nginx_2 \
    --network my_app_net \
    nginx

# Set up an instance of alpine, download and install curl,
# then connect it to the network.
docker container run -d \
    --name my_alpine \
    alpine tail -f /dev/null

docker container exec my_alpine apk add curl
docker network connect my_app_net my_alpine

# Try some test curls.
docker container exec my_alpine curl nginx_1 
docker container exec my_alpine curl nginx_2
```

Both of the execution of curl above are able to successfully connect to the different nginx servers, resulting in the landing page of both being downloaded and displayed in the terminal. If we add a 3rd nginx container, connected to the bridge network, this behavior does not work.

```bash
docker container run -d \
    --name nginx_3 \
    nginx

docker network connect bridge my_nginx

# Show that nginx_3 and my_alpine are connected to bridge
docker network inspect bridge 

docker container exec -it my_alpine curl nginx_1 # Still Works
docker container exec -it my_alpine curl nginx_2 # Still Works
docker container exec -it my_alpine curl nginx_3 # No Connection
```

### Link

If you have a 2 container application, where 1 container needs resources from another container, it is possible to handle DNS name resolution by using the `--link` option in Docker container run. The link argument takes a name, or a list of names, each being the name of ID of another container. This allows containers to reference each other without a network.

Using a docker network is still much easier, since you do not have to specify the link every time the container is run or started. Also, tools like docker-compose can manage network naming and name resolution automatically.

### Analysis

The back-end of an application can be built out of a swarm of distinct containers, each that manage their own application and their own file systems. If all of those containers connect to the same non-default network, then they can reference each other by name. No code that determines the current IP address of each container is needed. The configuration files for the different application components can just use Docker's built-in DNS. For example, a web app that uses some form of DB can just name its database container "db" or "my_app_db" or "my_app_db_1". Any containers that connect to this DB just have to reference this container using that string.

In fact, the DNS is a must-have, because keeping track of IP addresses is nearly impossible, especially in environments where containers are spun up to accomplish a specific task before shutting down again. Container names are static for the entire life of the container, even when it is stopped.

