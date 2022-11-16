---
tags: OMSCS, GIOS, RPC
---
# P4L1: Remote Procedure Calls (RPC)

## Overview
- Remote Procedure Calls (RPC)
- Supplemental paper: [[P4L1 Implementing Remote Procedure Calls.pdf]]

## Why RPC?
> Why do anything?

### Example Application: GetFile App
- Defines client and server functionality
- clients and servers have to
	- create/init sockets
	- allocate and populate buffers
	- include protocol information
		- GetFile
		- size
	- copy data into buffers

### Example Application: ModImage App
- client-server
- clients and servers have to
	- create/init sockets
	- allocate and populate buffers
	- include protocol information
		- algorithm
		- parameters
	- copy data into buffers

### Applications in General
- There's common steps related to IPC
- A lot of these steps could be encapsulated into a set of functionality (RPC)

## RPC Fundamentals
### RPC: Benefits
- RPC is intended to simplify the development of cross-address space and cross-machine interactions
- RPC offers a higher-level interface for data movement and communication
- RPC allows for code sharing related to error handling
- RPC hides complexities of cross-machine interactions

### RPC: Requirements
In general, RPC systems need to facilitate interactions between different processes running on potentially different hardware, different OSes, while also hiding complexity from the programmer.

1. Client/Server Interactions
2. Procedure Call Interface (RPC)
	- synchronous call semantics
3. Type Checking
	- error handling
	- packet bytes interpretation
	- optimizes runtime behavior
4. Cross-Machine Conversion
	- e.g. big/little endian
5. Higher-level protocol
	- access control, fault tolerance
	- support different transport protocols

![[Pasted image 20221113153614.png]]

### RPC: Addition Server Example
- Client doesn't have the code to add 2 numbers.
- A server does, and exposes the add instruction as an RPC
- RPC package has stubs which allows the client and server to interact predictably.
- Client is able to reference the `add(i, j)` stub as if it's just a regular function that may exist locally
- RPC package on the client is able to pack the request in a predictable format that the server RPC package can unpack
- RPC package on the server is able to unpack the request
- Server uses the parameters to perform the requested operation
- Results are passed back down to the client the same way that the request was passed to the server

![[Pasted image 20221113155043.png]]

### RPC: Steps
Server must register its functionality
- procedure
- argument types
- location

0. **bind:** client finds and **binds** to the desired server
1. **call:** client makes RPC call
	1. control passed to stub
	2. client code blocks
2. **marshal:** client stub marshals arguments (serializes arguments into a buffer)
3. **send:** client sends the message to the server
4. **receive:** server receives the message
	1. passes message to server stub
	2. access control
5. **unmarshal:** server stub unmarshals the arguments
	1. extracts arguments
	2. creates data structures
6. **actual call:** server stub calls the local procedure implementation
7. **result:** server performs operation and computes the result

Similar steps occur when returning the result from the server to the client.

## Interface Definition Language (IDL)
- WHAT can the server do?
- WHAT arguments are required for the various operations?
- WHY
	- client-side bind decision
	- runtime to automate stub generation

IDLs are an agreement for how the protocols will be expressed.

### Specifying an IDL
- An IDL is used to describe the interface that the server exports
	- procedure names
	- arguments
	- result types
	- version number. Used to determine the most up-to-date server implementation. Also used to facilitate asychronous/incremental upgrades
- RPC can use IDL that is language-agnostic
	- XDR in SunRPC
	- protobuffers (protobuf / `.proto`) in gRPC
- RPC can use language-specific IDL
	- Java in JavaRMI

Example XDR IDL:
![[Pasted image 20221113155924.png]]

Remember, IDLs are just the interface! They don't define the implementation!

## Marshalling
- Have arguments somewhere in the address space of a process. Those arguments are likely not contiguous in memory.
- The process needs to call the RPC stub with those arguments.
- Those arguments need to be serialized into a contiguous memory location (a buffer)
- That buffer will be sent via a `socket_send` or some other network-related system call.

Marshalling is the process of serializing the arguments into a predictable and agreed-upon format, such that the result of the serialization can be sent via a network call, and such that the result can be correctly deserialized/unmarshalled on the receiving end.

Unmarshalling is the process of reversing the marshalling process.

RPC systems include a compiler which automatically write the marshal and unmarshal code.

## Binding
The client determines
- WHICH server it should connect to
	- service name
	- version number
- HOW will it connect to that server
	- IP address
	- network protocol

## Registry
The registry is a database of available services
- search for service name to fine the service (which) and contact details (how)
- distributed
	- any RPC service can register
	- well-known addresses that services can use to register and clients can use to lookup services
- machine-specific
	- for services running on the same machine
	- clients must know machine address
	- registry provides port number needed for connection

Regardless of type, registries require naming conventions / naming protocols.

## Pointers in RPC
You can't really pass pointers to remote servers, because they're an address that can only be retrieved on the same system.

![[Pasted image 20221113172115.png]]

RPC systems can make one of 2 decisions
- No pointers allowed!
- Serialize pointers, copy referenced "pointed to" data structure to send buffer

## Handling Partial Failures
> When a client hangs... what's the problem?

- server down?
- service down?
- network down?
- message lost?
- Auto timeout and retry? No guarantees that the issue will be resolved.

RPC systems typically have special error notifications. (signal, exception, ...). These attempt to catch all the possible ways in which the RPC call can (partially) fail.

## RPC Design Choice Summary
- Binding: how to find the server
- IDL: how to talk to the server, how to serialize/marshal data
- pointers: pointers allowed as arguments? disallow or copy data?
- Partial failures: special error notifications provided to client

Many choices can be made in all of these domains.

Some examples include: SOAP, Sun RPC, Java (Remove Method Invocation) RMI, gRPC

REST is technically not RPC.

## Sun RPC
Developed in 80s by Sun for UNIX. Now widely available on other platforms.

### Design Choices
- Binding
	- per-machine registry daemon
- IDL
	- XDR (for interface specification and for encoding)
- Pointers
	- allowed and serialized
- Failures
	- retries
	- returns as much info as possible

### Overview
- client and server interact via prcedure call
- interface specified via XDR (`.x` files)
- `rpcgen` compiler converts `.x` files to language specific stubs
- Server registers with local registry daemons
- registry (per-machine)
	- name of service
	- version
	- protocol(s)
	- port number
- binding creates handle
	- client uses handle in calls
	- RPC runtime uses handle to track per-client RPC state
- client and server can be on the same or on different machines
- documentation, tutorials, and examples are now maintained by Oracle
- TI-RPC: Transport-Independent Sun RPC
- provides Sun RPC / XDR documentation and code samples
- older online references are still relevant
- Linux man pages via `man rpc`

![[Pasted image 20221115192708.png]]

### Example

- Client: `send x`
- Server: `return x^2`

```c
struct square_in {
	int arg1;
};

struct square_out {
	int res1;
};

program SQUARE_PROG { /* RPC service name */
	version SQUARE_VERS {
		square_out SQUARE_PROC(square_in) = 1; /* proc1 */
	} = 1; /* version1 */
} = 0x31230000; /* Service ID */
```

### XDR `.x` file
Describes
- data types
- procedures (name, version, ...)
- Service ID

It's basically a header file, or an interface

The version numbers are not used by the client code, they're used by the client-side RPC library to determine the service(s) that it can and wants to connect to.

Service ID Conventions
- `0x 0000 0000` - `0x 1fff ffff`: Defined by Sun
- `0x 2000 0000` - `0x 3fff ffff`: Range that you can use
- `0x 4000 0000` - `0x 5fff ffff`: transient
- `0x 6000 0000` - `0x ffff ffff`: reserved

### Compiling XDR
- `rpcgen` compiler
- `rpcgen -c square.x`: Generates C code
	- `square.h`: data types and function definitions
	- `square_svc.c`: server stub and skelethon (main)
	- `square_clnt.c`: client stub
	- `square_xdr.c`: common marshalling routines
	- **Default implementation is not thread safe!**
	- Using `-M` makes the code threadsafe

`square_svc.c`: Server stub and skelethon
- `main`: registration and housekeeping
- `square_prog_1`
	- internal code, request parsing, arg marshalling
	- `_1`: version 1
- `square_prog_1_svc`
	- Actual procedure
	- must be implemented by the developer

`square_clnt.c`: client stub
- `squareproc_1`: wrapper for RPC call to `square_proc_1_svc`
- `y = squareproc_1(&x, ...)`

The last line is what makes RPC appealing. The library handles all of the not-so-fun parts of web dev
- configuration
- finding servers
- validating version constraints
- sockets, buffers, etc.

### Compilation Process
From `.x`, need to generate headers and stubs

Developer has to
- implement the server code
- develop the client and call the wrapper procedure when necessary
- `#include` the `.h`
- link with stub objects
- RPC Runtime does the rest

![[Pasted image 20221115194137.png]]

### Registry
- RPC daemon is called `portmapper`
- `/sbin/portmap` (need sudo privs)
- Query it with `rpcinfo -p`
	- `/usr/sbin/rpcinfo -p`
	- Shows program id, version, protocol (tcp or udp), socket port number, service name, ...
	- port mapper binds to port `111` using both tcp and udp

### XDR Data Types
- Default types
	- char
	- byte
	- int
	- float
- additional XDR data types
	- const (`#define`)
	- hyper (64-bit int)
	- quadruple (128-bit float)
	- opaque (~ C byte)
		- uninterpreted array of bits
- Fixed-length array
	- e.g. `int data[80]`
- Variable-length array
	- e.g. `int data<80>`
	- resulting translation contains a length and a value
	- It's a TLV
- Strings
	- `string line <80>`: C pointer to char
	- stored in memory as a normal null-terminated string
	- encoded (for transmission) as a pair of length and data

Specification: https://tools.ietf.org/html/rfc4506

- Example
	- `int data<5>`
	- When the array is full, on a 32-bit machine
	- `32*5` bits for the values
	- `32` bits for the length field
	- $32*6=192$ bits for the length and values
	- To represent the list on a C client, you also need an additional 4 bytes to represent the pointer to the array of integers.
	- Total transmit size: 24 bytes
	- Total size on client: 28 bytes

### XDR Routines
- Marshalling/Unmarshalling
	- found in `square_xdr.c`
- Clean up
	- `xdr_free()`
	- user-defined `_freeresult` procedure
	- e.g. `square_prog_1_freeresult`
	- called after results are returned

### Encoding
> What goes on the wire?

- Transport header
	- e.g. TCP, UDP
- RPC header
	- service procedure ID
	- version number
	- request ID
- Actual data
	- arguments or results
	- encoded into a bytestream depending on the data type

### XDR Encoding
- XDR: specifies the IDL and the encoding
	- i.e. specifies the binary representation of data "on-the-wire"
- XDR encoding rules
	- all data types are encoded in multiples of 4 bytes. If data types is less than 4 bytes, additional bytes are added as padding.
	- Big endian is the transmission standard.
	- two's complement is used to represent integers
	- IEEE format is used for floating point numbers

- An example
	- `string data<10>` (in `.x` file)
	- `data = "Hello"`
	- In a C client/server, this takes 6 bytes
		- `['H', 'e', 'l', 'l', 'o', '\0']`
	- In transmission buffer, this takes 12 bytes
		- 4 bytes for the length (length is 5, 32 bit ints)
		- 5 bytes for the characters
		- No null terminator
		- 3 additional bytes used for padding to make the number of bytes divisible by 4
- Another example
	- `int data<5>` defined in `.x` file
	- `data = [1, 2, 3, 4, 5]`
	- 32 bit ints
	- In transmission buffer
		- 4 bytes for the length
		- 4 bytes per int (20 bytes)
		- No padding needed
		- 24 bytes total

## Java RMI
> Java Remote Method Invocations (RMI)
- among address spaces in JVM(s)
- matches Java's OO semantics
- IDL is Java (language-specific RPC system)
- RMI Runtime
	- Remote Reference Layer
		- unicast
		- broadcast
		- return-first
		- response
		- return-if-all-match
	- Transport
		- TCP
		- UDP
			- shared memory if on same machine

![[Pasted image 20221115204135.png]]

Docs: https://docs.oracle.com/javase/tutorial/rmi/
