# AWS Workshop Day 2

Jan 30, 2020

This workshop covered containers in the context of AWS, as well as other AWS
services that could be used to support containers within the context of AWS.

Docker is the underlying technology that powers most of AWS's services. Most of
AWS's application layer runs as containers that are executed within a Docker
runtime.

## Speaker Credentials

Brinton Sherwood - Principal Cloud Architect

VSO - Virtual Service Operations

## Common Container User Cases

- Batch Processing
- Machine Learning
- Hybrid Applications
- Application Migration to the Cloud
- Platform as a Service

## History: `chroot` Jail

Old UNIX term. You could put an application into what was called a "chroot
jail". Whenever an application requested a system resource, the system would
copy the resource for the application and the application was not allowed to
write resources to the actual system since it lived in its own personal jail
from which it could not break out.

It was manual work. You had to install and configure it manually.

Docker wrote a management tool around the old chroot jail. Might not be how they
do it now. They've come a long way.

## AWS Fargate

Fargate is an AWS-only offering for container orchestration.

Benefits

- Deploy and manage applications, not infrastructure
- Secure isolation by design. Individual ECS tasks or EKS pods each run in their
  own dedicated kernel runtime environment and do not share CPU, memory,
  storage, or network resources with other tasks and pods.
- Right-sized resources with flexible pricing options. You don't pay for a
  dedicated cluster.

Biggest advantage of Fargate over other container hosting/orchestration services
is that you don't pay for dedicated hardware. Otherwise it's fundamentally the
same.

It apparently also converts Python calls to lambda functions.

## Paradigm?

Paradigm! Paradigm, paradigm paradigm paradigm. Paradigm.

Network is at the core of the cloud. None of it makes any sense without really
smart networking.

> Nobody:
>
> Mainframe:
> ![](bender-im-back-baby.jpg)

## Message Queues

Software application interactions are programmed in 3 main ways

**Direct code call**

This is IPC

**API call**

This is an RPC call on the same machine. A remote procedure call (RPC) is an
internal procedure call (IPC) with an IP address.

> Take some Kernel classes.
> 
> - Brinton Sherwood

**Messaging**

In messaging, the call and payload are contained in a "message" that persists on
a message server. There is a central broker that never sleeps.

All three types can be synchronous or asynchronous.

## Why Messaging

- Central broker can handle messages without doing much compute.
- Many senders, many receivers.
- Increased reliability. Queues can persist your data and reduce the errors that
  happen when different parts of your system go offline. Messages sent to a dead
  service will wait until the service comes back online.
- Granular scalability. When workloads peak, multiple instances of your
  application can all add requests to the queue without risk of collision. As
  your queues get longer, you can increase the number of consumers.
- Simplified decoupling. Message queues remove dependencies between components
  and significantly simplify the coding of decoupled applications.

> Blast Radius: If something happens, what's the worst thing that could happen?

In AWS, each user's "blast radius" is their account. If someone compromises an
S3 role, the "blast radius" is all of the S3s associated with that role.

If you're using a single message broker and it goes down, the blast radius is
everything.

## AWS Simple Queue Service

AWS SQS was the 2nd service that AWS added. (The first was S3.)

SQS is a queue-based message pipe.

SQS is a fully managed message queueing service that enables you to decouple and
scale microservices, distributed systems, and serverless applications.

SQS eliminates the complexity and overhead associated with managing and
operating message-oriented middleware, and empowers developers to focus on
differentiating work.

SQS has 2 types of queues

- Standard queues offer maximum throughput, best-effort ordering, and
  at-least-once delivery.
- SQS FIFO queues are designed to guarantee that messages are processed exactly
  once, in the exact order that they are sent. They are synchronous. The message
  at the tip of the queue will block the queue if the consumers can't process
  it. You might want that.

SQS is built for performance, sacrificing "bells and whistle" features. But who
needs features? It's a queue. It's queues.

## AWS SQS Benefits

It's a managed queue. Don't need to stand-up servers to hold applications that
do basically do the same thing.

> It's a distributed broker. The big selling point is that AWS manages that
> complexity for you. (Unless you're using a FIFO.)

Make sure you minimize your FIFO points.

## Facts Sheet

**Standard Queues**

- Unlimited Throughput: Support a practically unlimited number of transactions
  per second (TPS) per API action.
- At-Least-Once Delivery
- Best-Effort Ordering

**FIFO Queues**

- ~300 TPS, but you can batch up to 10 messages to achieve ~3000 TPS. You can
  file a support request to increase this/these limit(s).
- Exactly-Once Processing
- First-In-First-Out Delivery

## SNS

SNS is designed for more public-facing messages and should not be used as a
stand-in for SQS. That's just silly.

## Notes on Architecture

You need more queues than you think.

If something is timing out, you haven't decoupled properly.

Make sure that your errors are coming from the thing that caused it.

## AWS Athena

Interactive query service that makes it easy to analyze data in Amazon S3 using
standard SQL. Think of it as a managed ETL service that interacts with any data
written to AWS S3.

Athena is easy to use. Simply point to your data in Amazon S3, define the
schema, and start querying using standard SQL.

With Athena, there's no need for complex ETL jobs to prepare you data for
analysis. This makes it easy for anyone with SQL skills to quickly analyze
large-scale datasets.

Athena is out-of-the-box integrated with
[AWS Glue](https://aws.amazon.com/glue/) Data Catalog, allowing you to create a
unified metadata repo across various services, crawl data sources to discover
schemas and populate your Catalog with new and modified table and partition
definition, and maintain schema versioning.

## Closing Quotes

> No-SQL: I don't care, here's your data. Have a nice day or don't.

> Athena is a SQL-compliant ETL.

> - ETL is for relational databases.
> 
> - Map-Reduce is for No-SQL databases.

> All a data-lake is is a place to store all of your crap.
