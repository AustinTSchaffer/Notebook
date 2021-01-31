---
tags: Docker, Images, NodeJS, Assignment
---

# Assignment 4 - Create Your Own Image

Dockerize an existing node.js app.

## Objectives

- Take an existing node.js app and Dockerize it
- Make a Dockerfile for the node.js application.
- Details are in the Dockerfile of the application
- Use the alpine version of Node 6.X as a base image
- Expected resulting website is http://localhost (need to expose port 80, so
  port-forwarding can be enabled)
- Push the completed image to a repository in the Docker
  Hub.
- Remove the local images and run the image, which should pull the image down
  from the Hub.

## Node App

The node app was provided by

- Repo: https://github.com/BretFisher/udemy-docker-mastery
- Directory: `dockerfile-assignment-1/`

**Note:** If you're cloning this repo, there should be a symbolic link from the
"node-app" of this directory, to the `dockerfile-assignment-1/` directory of the
git submodule, that points to the repo specified above. If it did not work, copy
the directory from the submodule as a subdirectory of this directory, with the
dir name of "node-app/". Destroy the symlink if you have to.

## Difficulties

1. Having a hard time running the `apk add tini` when building the image, when
   connected to public wifi. This is causing the `docker image build` to fail.
   Getting errors when it is trying to fetch the APKINDEX. It is possible to
   download the .tar.gz files onto my host machine with no issue.

    Step 2/9 : RUN apk add --update tini
    ---> Running in 5eae06851684
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/APKINDEX.tar.gz
    ERROR: http://dl-cdn.alpinelinux.org/alpine/v3.4/main: temporary error (try again later)
    WARNING: Ignoring APKINDEX.167438ca.tar.gz: No such file or directory
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.4/community/x86_64/APKINDEX.tar.gz
    ERROR: http://dl-cdn.alpinelinux.org/alpine/v3.4/community: temporary error (try again later)
    WARNING: Ignoring APKINDEX.a2e6dac0.tar.gz: No such file or directory
    ERROR: unsatisfiable constraints:
    tini (missing):
        required by: world[tini]


