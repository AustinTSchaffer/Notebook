---
tags:
---
# Kora - A cloud-native event streaming platform for Kafka

Notes on paper: [[Kora - A cloud-native event streaming platform for Kafka.pdf]]

## Abstract
- Confluent Cloud is running 10s of thousands of Kafka clusters across AWS, Google Cloud, and Azure (multi-cloud service provider)
- "Kora is the cloud-native platform for Apache Kafka which is that the core of Confluent Cloud."

## Introduction
- event streaming is a super popular paradigm for microservice/eventing architectures
- Kafka predates the cloud's prevalence and still shows signs of that history. Example, its single tiered storage layer means making the cluster larger requires a ton of data to be moved.
- Where Kora fits in
	- abstracts low-level resources, such as Kafka brokers
	- hides operational complexity, such as system upgrades
	- supports a pay-as-you-go model, end users only pay for their data usage, and don't need to provision an entire cluster
- Kora has many abstractions which allows end users to worry about application requirements instead of their Kafka deployment.

## Conclusion
- designed as a elastic, scalable, manageable, and cost-efficient streaming backend
- tiered storage layer to improve cost and performance
- elastic and consistent performance through incremental load balancing
- cost effective multi-tenant system
	- dynamic quota management
	- cell-based isolation
- continuous monitoring of system health and data integrity
- clean abstraction with standard Kafka protocols to hide underlying resources
- Definitely an attractive offering for hosting Kafka.