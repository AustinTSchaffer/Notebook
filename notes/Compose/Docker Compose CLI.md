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
