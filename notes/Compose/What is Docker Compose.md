# What is Docker Compose?

- Single YAML file for multiple containers
- Configuring relationships between multiple containers
- Specify images, containers, volumes, networks, environment variables, most
  other container run options are supported.

## docker-compose.yml

YAML is a really easy and forgiving markup language, so don't worry about that
being a barrier to entry. The file can be used on the command line for local
Docker automation and testing. Also, Docker itself can use compose files
directly, thanks to Swarm (Docker version 1.13).

`docker-compose.yml` is the default file name for this file, but any file name, as long as it points to a valid YML file can 

### Version

Docker compose files have a version, usually the first option in the file. If
you do not specify a version, version 1 is assumed, so ALWAYS specify the
version number. Use 2 at a minimum, but it's recommended to start trying out
features from version 3.

### Services

This section is where you specify all of the "services" that Docker compose will
spin up. These are your containers, but they're called services, because you
could use it to spin up 1 or MORE containers for a single service. A single
service is just a set of configurations for a single container (like a list of
options for a repeatable `docker container run`)

### Volumes

The best part about working with Docker-Compose for bind mounts: the
`docker-compose.yml` file can use relative file paths.

## Sample Wordpress Site Compose File

```yml
version: '2'

services:
  wordpress:
    image: wordpress
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_PASSWORD: example
      TEST_ENV_VAR: this_wont_be_used
    volumes:
      - ./wordpress-site:/var/www/html
  db:
    image: mariadb
    environment:
      MYSQL_ROOT_PASSWORD: example
    volumes:
      - ./mysql-data:/var/lib/mysql
```

1. Sets a wordpress service
    1. Uses the official `wordpress` image
    2. Exposes port 80 on the host as port 8080
    3. Specifies some environment variables
    4. Uses local resources for the `/var/www/html`
2. Sets up a database service
    1. Uses the official `mariadb` image
    2. Specifies some environment variables
    3. Saves the mysql data to a local mount

What you don't see, is any network configuration. By default, compose will sets
up a network with default new-network configurations, and will connect both
services to that network. That's why you don't see any port mappings for the
`db` service. The wordpress app can connect to the container(s) that is/are
configured by the `db` service, using `mysql://db:3306`. This helps harden your
server. No visible attack surface for the `db` containers.
