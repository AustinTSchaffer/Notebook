# Docker-Compose CLI

Docker-Compose just wraps the Docker CLI, attempting to wrap common
functionality of the Docker Service API, applying it to multiple containers.

`docker-compose up` Creates and starts containers for all of the services in the
"docker-compose.yml" file in the current directory. Attaches to the containers
once they are running.

`docker-compose up -d` Same as `docker-compose up`, except the containers run in
the background.

`docker-compose -f <some-yml-file> <command>` Uses a specified YML file for the
configurations for docker-compose.

`docker-compose logs` prints the logs for the containers.

`docker-compose top` Same as `docker container top`, except for all services.

## Default Behavior

- the compose CLI checks to see if there is a docker-compose.yml file in the pwd, if there was no file specified.
- Containers, networks, built images, etc are all named with the name of the
  parent directory, as a namespacing consideration, to help prevent name
  conflicts. This can be overridden with the `-p` (project) option.
