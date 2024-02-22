# Towards D of M C A

ref impl: https://GitHub.com/ServiceWeaver

## notes on paper

couple of interesting ideas in this one

- defining hard network boundaries between applications almost always means you'll end up underutilizing application hosts
- delegating the boundary between method calls and RPCs to an automated framework
- if you can guarantee that different versions of a single application NEVER interact, you can send raw structs over the wire. no need for intermediate data formats, nor serialization / deserialization

interestingly, the model proposed in the paper doesn't support streaming methods, makes little/no mention of async pub/sub, and prioritizes regular params/return methods. its reference implementation is Go, but channels aren't supported

## musing about weaknesses

there's a bit of weirdness IMHO given that the runtime can turn practically any simple method call into an RPC. your application's performance can be subject to poor judgement calls by the runtime framework. with the framework, should you make all method calls (at least the inter-component ones, which are subject to placement on another host) async, move them to be as early as possible, await their results only when needed? do you not worry about it and hope the runtime always makes good decisions about frequent vs infrequent inter-component method calls?

another weakness with this model is that you can easily fall into poor architecture pitfalls. one advantage of distributed application models which use message brokers (Rabbit, Kafka, etc), is the idea that producers and consumers can deliver mupltiple messages simultaneously via batching, which can help make sure that network packet frames are being filled to the brim, reducing network overhead on a per-packet basis.

## takeaways

- Pack more functionality into each service. don't go crazy with microservices. don't get trapped into a monolith model
- I need to look into NATS