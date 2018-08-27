# Installing Docker on Linux

Installing Docker on linux is the best, native experience of the platform.
Unlike Docker for Windows and Docker for Mac, Docker on Linux does not
require any hardware emulation for running the Docker Daemon itself.

Three primary ways to install Docker on Linux

- Install script
- Docker store
- `docker-machine`

## Install Script

Preferred way, easiest setup, uses the edge releases.

```bash
curl -sSL httls://get.docker.com/ | sh
```

## Docker Store

If you have any issues with the script, like if you're running on
Linux Mint, you should go check out the Docker Store and read through
the install instructions for the OS that most closely resembles your setup.

As long as you're running a Debian or Fedora/Red Hat based Linux (a free 
version), there should be a way to install Docker CE. RHEL only supports
Docker EE, but installing the CentOS version of Docker CE should also work
(for now).

Please note that there loads of Linux distros, and if your version is unlisted,
then Docker may not work for you. Amazon Linux, Linode Linux, Red Star Linux, 
etc. Less common and vendor specific platforms are hard to develop for.

Most imprtantly, don't use pre-installed Docker setups if you can avoid it.
The vendor may not be up-to-date on Docker.


