# Assignment: CLI App Testing

## Objectives

Check the `curl` version bundled on various Linux distros.

## Script

```bash
sudo docker container run -it --rm centos:7 curl --version

sudo docker container run -it --rm ubuntu:14.04 curl --version
# sudo apt update
# sudo apt install curl
# curl --version
# exit

sudo docker container run -it --rm alpine:3.8 /bin/sh
# apk add curl
# curl --version
```

## Results

| Linux OS	| Image Tag 	| CURL Version 	|
|-		|-		|-		|
| Centos 	| 7		| 7.29.0	|
| Ubuntu	| 14.04		| 7.35.0	|
| Alpine	| 3.8		| 7.61.1	|

