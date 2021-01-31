---
tags: Docker, Docker-Compose
---

# Image Building with Docker Compose

- You can build images at runtime
- Will build the app when you `docker-compose up`, if the app is not found in
  the cache
- App can be rebuilt using `docker-compose build` or `docker-compose up --build`

```yml
version: '2'
services:
  proxy:
    build:
      context: .
      dockerfile: nginx.Dockerfile
    image: nginx-custom
    ports:
      - 80:80
  web:
    image: httpd
    volumes:
      - ./html:/usr/local/apache2/htdocs/
```

Instead of specifying a default image for the service, the proxy service builds
an nginx image for from the nginx Dockerfile in the same directory. This is
great for rapid testing of apps that need to be built into images, but also
require lots of settings when `run`, or if they have dependencies on other
services.

The `build-images-sample/` in this directory demonstrates that behavior. This
sample was copied from `compose-sample-3` of the accompanying Bret Fisher
repository, included in this repository as a git module.
