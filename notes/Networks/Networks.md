# Docker Networks

## CLI

```bash
# Show all networks
docker network ls

# Inspect a specific network
docker network inspect

# Create a new Docker network (virtual network)
docker network create --driver

# Adding/Removing containers from networks
docker network connect
docker network remove
```


## Docker Default Networks

Docker has 3 default networks that are always available.

### Bridge

The default Docker virtual network is its `bridge` network. This is the default
network that containers connect to when they are started or created if no other
networking commands are specified.

Features of the Docker bridge network:

- Default Docker virtual network
- NAT'ed behind the Host IP

To see all of the containers that are connected to this network, or any other
Docker virtual network, use `docker network inspect [network_name]`.

### Host

This Docker network is a special network that skips is the virtual networking of
Docker, allowing containers to attach themselves directly to the network that
the host machine is connected to. This is good for performance reasons, but
sacrifices the security of the container model. Breaks the security boundary.

### None

Removes the eth0 network interface from the container, leaving the container
with the localhost interface only.


## Creating and Using a New Network

```bash
docker network create my_app_net
```

If no driver is specified, the bridge driver is the default. You can see this
when you ls your networks after creating a new one with default settings:

    NETWORK ID          NAME                DRIVER              SCOPE
    b1905c518dc8        bridge              bridge              local
    3e36325a449a        host                host                local
    bc72232bae69        my_app_net          bridge              local
    0f01cce9bc8e        none                null                local

There are only a few built-in network drivers, but you can use lots of 3rd party
network drivers, like overlay networks.


## Attaching Containers to a Network

### On Container Creation

You can attach a container to a network on container creation using the run
option `--network`.

```bash
docker network rm my_app_net
docker network create my_app_net --driver bridge
docker container run -d --name new_nginx --network my_app_net nginx
docker network inspect my_app_net
```

Relevant output of inspect:

    [
        {
            "Name": "my_app_net",
            "Driver": "bridge",
            "Containers": {
                "c7a59487d5004b6a55b18ecc8e57930718893aba2e012adccafb982c2c076aa6": {
                    "Name": "new_nginx",
                    "EndpointID": "f69c083e781e367501749cc40195494c2b20d69f5149beceeb9e1a5cdac39b2e",
                    "MacAddress": "02:42:ac:14:00:02",
                    "IPv4Address": "172.20.0.2/16",
                    "IPv6Address": ""
                }
            }
        }
    ]

### Using `docker network connect`

You can attach a running container to a network using `docker network connect`.

```bash
docker network create my_app_net2
docker network connect my_app_net2 new_nginx
docker network inspect my_app_net2
docker container inspect new_nginx
```

Relevant portions of the network inspect:

    [
        {
            "Name": "my_app_net2",
            "Driver": "bridge",
                "c7a59487d5004b6a55b18ecc8e57930718893aba2e012adccafb982c2c076aa6": {
                    "Name": "new_nginx",
                    "EndpointID": "e2bb4f460e562b7269161d92f8f11d58840ce8b0fbb76d28183838f7a6da12d5",
                    "MacAddress": "02:42:ac:15:00:02",
                    "IPv4Address": "172.21.0.2/16",
                    "IPv6Address": ""
                }
            }
        }
    ]

Relevant Portions of the container inspect:

    [
        {
            "Name": "/new_nginx",
            "NetworkSettings": {
                "Networks": {
                    "my_app_net": {
                        "Gateway": "172.20.0.1",
                        "IPAddress": "172.20.0.2",
                        "IPPrefixLen": 16                    },
                    "my_app_net2": {
                        "Gateway": "172.21.0.1",
                        "IPAddress": "172.21.0.2",
                        "IPPrefixLen": 16
                    }
                }
            }
        }
    ]

Bonus:

```bash
docker container exec new_nginx apt update
docker container exec new_nginx apt install net-tools
docker container exec new_nginx ifconfig
```

Results:

    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.20.0.2  netmask 255.255.0.0  broadcast 172.20.255.255
        ...

    eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.21.0.2  netmask 255.255.0.0  broadcast 172.21.255.255
        ...

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        ...


### Removing a Container from a Network

Use `docker container disconnect`, which uses the same syntax as docker
container connect.

```bash
docker container disconnect my_app_net2 new_nginx
docker container exec new_nginx ifconfig
```

Results:

    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.20.0.2  netmask 255.255.0.0  broadcast 172.20.255.255
        ...

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        ...
