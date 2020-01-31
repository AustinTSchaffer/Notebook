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

## 
