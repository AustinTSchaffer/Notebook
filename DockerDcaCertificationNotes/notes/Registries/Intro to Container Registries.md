# Intro to Container Registries

An image registry needs to be part of your container plan. You can technically
distribute images as zip files, but there are a lot better tools.

## Docker Hub (hub.docker.com)

- default, and most popular public docker image registry
- Docker Registry plus lightweight image building
- You can link GitHub/BitBucket to Hub and auto-build images on commit
- You can chain image building
- has webhooks for sending web requests when an image is pushed
- has organization-level docker hub accounts

If you're trying to set up automated builds for a GitHub repository sending the
images to docker hub, use the "Create Automated Build" option. Automated builds
on Docker Hub have a few neat tools.

- Link a GitHub or BitBucket repository
- Automated builds from branches, auto tagging of multiple builds
- Travis CI hooks
- Automated rebuilding whenever a specific tag of a different repository is
  changed.

## Docker Store

The Docker Store (ca. 2016) for downloading different editions of Docker, and
helps you find certified images and certified Docker/Swarm plugins. Official
software only shows up here when Docker partners with commercial/industry
entities, which verifies that the images follow Docker image "best-practices"
and are truly registered to the entity whose name is attached to the image.

The "docker hub" is like the GitHub of docker images, while the "docker store"
is like an app store for docker images (booo).

## Docker Cloud

Web based Docker Swarm creation/management (is this valid anymore?). I think all
of the features of Docker Cloud have been rolled into Docker Hub.
