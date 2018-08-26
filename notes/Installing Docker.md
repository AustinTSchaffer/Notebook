# Installing Docker (Linux Mint 19)

## Installing on Windows 10

This is the best experience on Windows, but due to OS feature requirements, it only works on the Pro and Enterprise editions of Windows 10 (with latest update rollups). You need to install "Docker for Windows" from the Docker Store.

With this Edition it's recommend to use PowerShell for the best CLI experience.

## Installing on Windows 7, 8, or 10 Home Edition

Unfortunately, Microsoft's OS features for Docker and Hyper-V don't work in these older versions, and "Windows 10 Home" edition doesn't have Hyper-V, so you'll need to install the Docker Toolbox, which is a slightly different approach to using Docker with a VirtualBox VM. This means Docker will be running in a Virtual Machine that sits behind the IP of your OS, and uses NAT to access the internet.

## Docker for Mac

You'll want to install Docker for Mac, which is great. If you're on an older Mac with less than OSX Yosemite 10.10.3, you'll need to install the Docker Toolbox instead.

## Docker Community Edition on Linux

Do *not* use your built in default packages like apt/yum install docker.io  because those packages are old and not the Official Docker-Built packages. 

It is recommended to use Docker's automated script to add their repository and install all dependencies: `curl -sSL https://get.docker.com/ | sh`,  but you can also install manually by following specific instructions on the Docker Store for your distribution.

## If None of These Work

Maybe you don't have local admin, or maybe your machine doesn't have enough resources. The best free option here is to [PWD](http://use play-with-docker.com), which will run one or more Docker instances inside your browser, and give you a terminal to use it with. You can actually create multiple machines on it, and even use the URL to share the session with others in a sort of collaborative experience.


