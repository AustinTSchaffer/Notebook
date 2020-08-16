# Docker Network Concepts

More concepts regarding docker networking.


## Defaults

All containers attach to a network. The default network is bridge. All Docker
networks route through a NAT firewall on the host IP.

Inside a Docker virtual network, there is no need to map ports on the container
to ports on the host machine. Inside the virtual network, all containers on the
network are able to reference each other's exposed ports, using just the DNS
name of the container, through the DNS server for the virtual network.

All of these defaults are configurable. "Batteries included, but removable."

- Make new virtual networks
- Map a container to multiple networks, or 0 networks (the "none" network)
- Skip virtual networks, use host IP (--net=host).
- Docker network drivers extends the capabilities of Docker, usually used for
  interfacing with 3rd party tools.


## Some Command Line Stuff

```bash
docker container run -p 80:80 --name webhost -d nginx
docker container port webhost 
# 80/tcp -> 0.0.0.0:80
docker container inspect webhost --format '{{.NetworkSettings.IPAddress}}'
# 172.17.0.2
```

## Diagram

    Bridge Network (bridge / docker0)
    [
        C1 (exposed port 80, also -p 80:80)
        C2 (exposed port 80)
    ]

    My App Network
    [
        httpd (exposed port 80, also -p 8080:80)
        mysql (exposed port 3306)
    ]

**Notes**

- Port 80 of C1 is connected to port 80 on the externally
  facing network interface of the host machine. Any traffic that hits this port
  on the host machine will be routed through the default virtual network, and
  directed toward C1

- httpd and mysql can talk freely to each other, without using the
  externally-facing network interfaces on the host machine.

- Port 80 of httpd is connected to port 8080 on the externally facing network
  interface of the host machine. Any traffic that hits this port on the host
  machine will be routed through the custom virtual network, and directed toward
  C1.

- httpd and C1 can talk to each other freely, but have to use the externally
  facing interface on the host machine.

**Remarks**

Always use explicit networks when setting up multi-container applications, and
separate them based on which services need to talk to which other services.
Always remember that you can attach 1 container to multiple networks.
