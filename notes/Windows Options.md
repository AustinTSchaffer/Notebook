# Windows Considerations and Options

## 2 Types of Containers

Supports both Linux containers and Windows containers. Linux containers were 
the default for all Docker containers up until (recently, late 2016), so it's
typical for people to refer to Linux Containers as just "containers", and to
specify "Windows" when required.

The only real difference is what's running in the container, and what binaries
the container is able to run.

## Docker for Windows

Running Docker on Windows requires a totally different version for Docker than
what is installed on virtually every other platform. Also, (currently, mid 
2018), Docker for Windows only works on Windows 10 Pro and Windows 10 
Enterprise. Also, it has compatibility issues with VirtulBox and VMWare, since
Docker for Windows uses HyperV. Along with Docker for Mac, d4Win has to set
up a Linux server in the background for running Docker.

Alternatively, the Docker Toolbox is an option that will allow you to run
Docker on older versions of Windows, and the Home version of Windows 10. This
may help with the VMWare issue, but comes with some additional considerations.
Doesn't have all the cool features of Docker for Windows.

Windows Server 2016 supports Docker for Windows, but it's bleeding edge, brand
new stuff (currently). Native Linux containers will be a thing soon, if not
already.

## Pro and Enterprise Users Only

You can grab it from http://store.docker.com. It has more features than just
a Linux VM. Docker for Windows help you develop and manage locally, so you
don't have to spin up a Linux machine if you do Windows development.


