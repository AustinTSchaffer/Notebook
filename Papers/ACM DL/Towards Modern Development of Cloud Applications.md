# Towards Modern Development of Cloud Applications

Notes on [[Towards Modern Development of Cloud Applications]]

> Sanjay Ghemawat, Robert Grandl, Srdjan Petrovic, Michael Whittaker, Parveen Patel, Ivan Posva, and Amin Vahdat. 2023. Towards Modern Development of Cloud Applications. In Proceedings of the 19th Workshop on Hot Topics in Operating Systems (HOTOS '23). Association for Computing Machinery, New York, NY, USA, 110–117. https://doi.org/10.1145/3593856.3595909

Reference Implementation: https://GitHub.com/ServiceWeaver

Grammar and capitalization are rough in this note as it was written on an Android keyboard using the GitHub app.

## notes

couple of interesting ideas in this one

- defining hard network boundaries between applications almost always means you'll end up underutilizing application hosts
- delegating the boundary between method calls and RPCs to an automated framework
- if you can guarantee that different versions of a single application NEVER interact, you can send raw structs over the wire. no need for intermediate data formats, nor serialization / deserialization.
	- Jack made the point that the endianness of different hosts could differ. The runtime could be aware of that and could translate the structs prior to sending (if necessary). Still, there would be no need to serialize the data to protobuf/json

interestingly, the model proposed in the paper doesn't support streaming methods, makes little/no mention of async pub/sub, and prioritizes regular params/return methods. its reference implementation is Go, but channels aren't supported

## potential weaknesses of approach

as a software developer, there's a bit of weirdness given that the runtime can turn any simple method call into an RPC. An application's overall performance would be subject to poor judgement calls by the runtime framework. with the framework, should you make all method calls (at least the inter-component ones, which are subject to placement on another host) async, move them to be as early as possible, await their results only when needed? do you not worry about it and hope the runtime always makes good decisions about frequent vs infrequent inter-component method calls?

another weakness with this model is that you can easily fall into poor architecture pitfalls. one advantage of distributed application models which use messaging/queueing brokers (RabbitMQ, Kafka, etc), is the idea that producers and consumers can deliver mupltiple messages simultaneously via batching, which can help make sure that network packet frames are being filled to the brim, reducing network overhead on a per-packet basis. message queueing also helps overall process reliability, allowing intermediate results to be unACKed by downstream consumers, in various failure conditions

- external resource not available
- programming errors
- feature not yet enabled by external team
- etc

## security

Even the feds agree that all systems should follow a 0-trust model, in which all applications on the same network should be able to cryptography verify the authenticity and authorization of all requests, especially network requests. Under this model, the runtime should/must support adding layers of security to a application making a network request to itself. Surely it must and surely the reference implementation already does. I bring this up to illustrate that the runtime's method call to RPC translator can't simply make unathenticated calls to another instance of itself. This invariably adds overhead. For instances on the same host machine, it's probably fine to leave the calls unauthenticated.

## takeaways

- Pack more functionality into each service. don't go crazy with microservices. don't get trapped into a monolith model
- I need to look into NATS