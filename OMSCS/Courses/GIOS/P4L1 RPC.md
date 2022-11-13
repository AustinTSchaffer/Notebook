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
// TODO: Pick this up next time.