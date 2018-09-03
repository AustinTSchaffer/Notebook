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


## Add Users to the Docker Group (Optional)

```bash
sudo usermod -aG docker your_username

# If not in a root shell...
sudo usermod -aG docker $(whoami)
```

Docker needs root permissions in order to perform some of the operations that
it needs to perform, since Docker affects processes on the machine level. On some
variants of Linux, you can add this permission to help prevent requiring sudo for
every single Docker action.

This does not work for Red Hat variants of Linux, like CentOS. Those OS will
require users to type sudo for every single actionable Docker command.


## Docker Compose and Docker Machine

Docker Compose and Docker Machine are 2 other good components to have.
Unfortunately, Docker machine appears to be in maintenance mode.
Docker Compose is great for getting started with muli-container environments.

