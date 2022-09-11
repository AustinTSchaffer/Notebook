---
tags: C, Sockets, GIOS, OMSCS, TLPI
---

# C and Sockets

These notes were taken from "The Linux Programming Interface: Chapter 56: Sockets". Some of these notes were also taken from Beej's network guide.

Applications communicate over networks by binding to "sockets". Sockets are created using the `socket()` system call:

```c
int fd = socket(domain, type, protocol);
```

## Protocol
TLPI recommends setting `protocol` to `0` for all example applications.

## Domain
Each socket exists in a "communication domain", which determines

- How to identify the socket, basically, what is the format of the socket's "address"
- The range of communication. This determines whether the socket allows communication between applications on the same host or applications on different hosts, connected by a network.

Modern OSes support at least these domains
- `AF_UNIX`
	- Allows communication between applications on the same host. This communication happens "within the kernel".
	- `AF_LOCAL` can be a synonym for this, but it's not universally supported.
	- The address format is the path name.
	- Address structure: `sock-addr_un`
- `AF_INET`
	- Allows communication between applications on network connected hosts using IPv4.
	- The address format is a 32-bit IPv4 address and a 16-bit port number.
	- Address structure: `sock-addr_in`
- `AF_INET6`
	- is the IPv6 variant of `AF_INET`.
	- The address format is a 128-bit IPv6 address and a 16-bit port number.
	- Address structure: `sock-addr_in6`

## Socket Types

Every socket implementation provides at least 2 types of socket: **stream** and **datagram**.

In the internet domain:
- Stream sockets (usually) use Transmission Control Protocol ( #TCP ) 
- Datagram sockets use User Datagram Protocol ( #UDP )

### Stream Sockets (`SOCK_STREAM`)
Provides a reliable, bidirectional, byte-stream communication channel.

- Reliable delivery. Guaranteed that either the transmitted data will arrive intact and in full, or we'll receive an indication of a transmission failure.
- Bidirectional. Data can be transmitted in either direction between 2 sockets.
- Byte-stream. There is no concept of message boundaries.

A stream socket is similar to using a pair of pipes to allow bidirectional communication between 2 applications, except sockets permit communication over a network.

Stream sockets operate in connected pairs. This means they're described as "connection-oriented". Sockets have a concept of a "peer socket", which is the other end of the communication channel. The "peer socket" has a "peer address". The "peer socket" is owned by the "peer application". Stream sockets can only have 1 peer.

### Datagram Sockets (`SOCK_DGRAM`)
Allow data to be exchanged in the form of messages called "datagrams". Message boundaries are preserved, data transmission is not reliable. Messages arrive out of order, duplicated, and sometimes never.

Dgram sockets can be described as "connectionless" sockets. They don't have a concept of a peer.

## Socket System Calls

- `socket()` creates a new socket
- `bind()` binds the socket to an address. The server app can use this to bind its socket to a known address so clients can locate the socket.
- `listen()` allows a stream socket to accept incoming connections from other sockets.
- `accept()` accepts a connection from a peer application on a listening stream socket. Optionally returns the address of the peer.
- `connect()` establishes a connection with another socket.
- `close()` closes a socket. If multiple file descriptors point to the same socket, the connection is only terminated when all of the descriptors are closed.

On most Linux architectures, these system calls are implemented as library functions that all wrap `socketcall()`.

I/O can be performed using the conventional `read()` and `write()` syscalls, or by using socket-specific systems calls
- `send()`
- `recv()`
- `sendto()`
- `recvfrom()`

These syscalls generally block execution. Nonblocking I/O is also possible. It's more complicated.

On Linux, we can call `ioctl(fd, FIONREAD, &cnt)` to obtain the number of unread bytes available on TCP sockets, referred to by the file descriptor `fd` . For UDP sockets, this operation returns the number of bytes in the next unread datagram (which may be zero if the next datagram is of zero length), or zero if there are no pending datagrams.

## Using a Stream (TCP) Sockets
Here's a handy graph.

![[Pasted image 20220828151745.png]]

### `socket()`
Signature: `int socket(int domain, int type, int protocol);`

- `domain` specifies the communication domain, i.e. local-only or "internet".
- `type` is usually set to `SOCK_STREAM` or `SOCK_DGRAM`.
- `protocol` specifies the exact "protocol" used by the socket. We'll be setting this to `0`, which lets the Kernel choose the protocol.

On success, returns the file descriptor. On failure, returns `-1`.

Linux also allows nonstandard flags to be boolean ORed with the socket type.
- `SOCK_CLOEXEC` causes the kernel to enable close-on-exec flag (`FD_CLOEXEC`)
- `SOCK_NONBLOCK` causes the kernel to set the `O_NONBLOCK` flag on the open file description, which allows for nonblocking I/O operations.

### `bind()`
Signature: `int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);`

- `sockfd` is the file descriptor obtained from a previous call to `socket()`. 
- `addr` is a pointer to a structure specifying the address to which this socket is to be bound. The type of structure passed in this argument depends on the socket domain.
- `addrlen` specifies the size of the address structure. The `socklen_t` data type used for the `addrlen` argument is an integer type specified by SUSv3.

`struct sockaddr`

```c
struct sockaddr { 
	// Address family (AF_* constant)
	sa_family_t sa_family;
	// Socket address (size varies
	// according to socket domain)
	char        sa_data[14];
};
```

The only purpose for this type is to cast the various domain-specific address structures to a single type for use as arguments in the socket system calls. It would be a more convenient type if each socket domain had their own system calls. That would however make interchangeably interfacing with different socket domains more annoying.

### `listen()`
Signature: `int listen(int sockfd, int backlog);`

This syscall marks the stream socket refered to by the FD as "passive," indicating that the application is acting as the "server."

We can't apply `listen()` to a connected socket. Connected sockets
- have already had a `connect()` call successfully applied to them, and/or
- are returned by calls to `accept()`

- `sockfd` is the socket file descriptor
- `backlog` limits the number of pending connections to the socket. The kernel records information about pending connection requests, so that subsequent `accept` operations can be processed. Connection requests up to this limit succeed immediately.

### `accept()`
Signature: `int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);`

Returns FD on success, or -1 on err.

IMPORTANT, `accept` creates a _new_ socket. This new socket is connected to the peer socket that performed the `connect()`. An FD for the socket is returned as the function result of the `accept()` call. The listening socket `sockfd` remains open and can be used to accept further connections.

Typical server apps create one listening socket, binds it to an address, and handles all client requests by accepting connections via that socket.

The remaining args to `accept` return the address of the perr socket.
- `addr` points to a struct that returns the socket address. The type of this arg depends on the socket domain, just like `bind()`
- `addrlen` is a value-result arg. It points to an integer that must be initialized to the size of the buffer pointed to by `addr`. This lets the kernel know how much space is available to return the socket addr. After the `accept()` call, this integer indicates the number of bytes of data actually copied to the buffer.

If we're not interested in the peer socket's address, `addr` and `addrlen` can be set `NULL`. The info can be retrieved later via `getpeername()`, if required.

### `connect()`
Signature `int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);`

Returns 0 on success, -1 on error.

The `addr` and `addrlen` arguments are specified in the same way as the corresponding arguments to `bind()`.

If `connect()` fails and we wish to reattempt the connection
- close the socket
- create a new socket
- reattempt the connection with the new socket

### TCP I/O
![[Pasted image 20220828162536.png]]

We use `read()` and `write()` and/or `send()` and `recv()` to read/write data to/from sockets. 

### Example Server App

```c
#include <signal.h>
#include <syslog.h>
#include <sys/wait.h>
#include "become_daemon.h"
#include "inet_sockets.h"
#include "tlpi_hdr.h"

/* Name of TCP service */
#define SERVICE "echo"
#define BUF_SIZE 4096

/* SIGCHLD handler to reap dead child processes */
static void grimReaper(int sig)
{
	/* Save 'errno' in case changed here */
    int savedErrno;
    
    savedErrno = errno;
    while (waitpid(-1, NULL, WNOHANG) > 0)
        continue;
    errno = savedErrno;
}
 
/* Handle a client request: copy socket input back to socket */
static void handleRequest(int cfd)
{
    char buf[BUF_SIZE];
    ssize_t numRead;

    while ((numRead = read(cfd, buf, BUF_SIZE)) > 0) {
        if (write(cfd, buf, numRead) != numRead) {
            syslog(LOG_ERR, "write() failed: %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
    }
    
    if (numRead == -1) {
        syslog(LOG_ERR, "Error from read(): %s", strerror(errno));
        exit(EXIT_FAILURE);
    }
}

int main(int argc, char *argv[])  
{
	/* Listening and connected sockets */
    int lfd, cfd;
    struct sigaction sa;
  
    if (becomeDaemon(0) == -1)
        errExit("becomeDaemon");
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;
    sa.sa_handler = grimReaper;
    if (sigaction(SIGCHLD, &sa, NULL) == -1) {
        syslog(LOG_ERR, "Error from sigaction(): %s", strerror(errno));
        exit(EXIT_FAILURE);
    }

    lfd = inetListen(SERVICE, 10, NULL);
    if (lfd == -1) {
        syslog(LOG_ERR, "Could not create server socket (%s)", strerror(errno));
        exit(EXIT_FAILURE);
    }
  
    for (;;) {
	    /* Wait for connection */
        cfd = accept(lfd, NULL, NULL);
        if (cfd == -1) {
            syslog(LOG_ERR, "Failure in accept(): %s", strerror(errno));
            exit(EXIT_FAILURE);
        }
  
        /* Handle each client request in a new child process */
        switch (fork()) {
        case -1:
            syslog(LOG_ERR, "Can't create child (%s)", strerror(errno));
            /* Give up on this client */
            close(cfd);
            /* May be temporary; try next client */
            break;
        case 0:
	        /* Child */
	        /* Unneeded copy of listening socket */
            close(lfd);
            handleRequest(cfd);
            _exit(EXIT_SUCCESS);
        default:
	        /* Parent */
	        /* Unneeded copy of connected socket */
            close(cfd);
            /* Loop to accept next connection */
            break;
        }
    }
}
```

## Network Byte Order
C programmers have to worry about byte ordering a lot. C has a family of functions that allow us to convert between "network byte order" and "host byte order", where "host byte order" is the byte order on YOUR computer.

| Function | Description           | 
|----------|-----------------------|
| `htons()` | host to network short |
| `htonl()` | host to network long  |
| `ntohs()` | network to host short |
| `ntohl()` | network to host long  |

