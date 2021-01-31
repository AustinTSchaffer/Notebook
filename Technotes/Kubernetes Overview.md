---
tags: Infrastructure, Kubernetes, Containers
---

# Kubernetes Overview

This document was written while watching [Kubernetes Explained in 100 Seconds](https://www.youtube.com/watch?v=PziYflu8cB8) by [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA)

At the highest-level, #Kubernetes is a tool for automating and orchestrating containerized workloads. It's become the de-facto standard for container orchestration in the cloud, providing more support and more features than Docker Swarm. It is also considerably more complex and more difficult to deploy compared to deploying Swarm and `docker-compose`. Part of Kubernetes ubiquity is due to it being open-source and also due to most cloud platforms providing managed Kubernetes instances.

Kubernetes is commonly deployed as a [**cluster**](https://kubernetes.io/docs/concepts/architecture/), where multiple compute nodes each run a Kubernetes runtime which all communicate together. Kubernetes distributes containers to each node in the cluster and is capable of auto-scaling the container jobs. Kubernetes is also capable of auto-healing, meaning it has the capability to replace compute nodes if one goes offline or becomes otherwise unhealthy.

The "brain" of Kubernetes is known as the **Control Plane**. The Control Plane exposes an API server, which handles both internal and external requests to manage the cluster. The Control Plane also manages its own key-value store to store data about the cluster. The Contol Plane uses `etcd` as its internal database. The control plane has a lot of components.

- https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
- https://kubernetes.io/docs/concepts/overview/kubernetes-api/
- https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/
- https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/
- https://kubernetes.io/docs/concepts/architecture/cloud-controller/

Each node in a Kubernetes cluster runs a [**Kubelet**](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/), which is the service that communicates back to the Control Plane. Each node also contains multiple [**Pods**](https://kubernetes.io/docs/concepts/workloads/pods/), which is the smallest deployable unit in a Kubernetes infrastructure.

> A Pod is a group of one or more containers, with shared storage/network resources, and a specification for how to run the containers. A Pod's contents are always co-located and co-scheduled, and run in a shared context.
>
> As well as application containers, a Pod can contain *init* containers that run during Pod startup. You can also inject ephemeral containers for debugging if your cluster offers this.
>
> https://kubernetes.io/docs/concepts/workloads/pods/

In Kubernetes `auto-healing` implies that Kubernetes has the functinoality to spin up identical compute nodes when one fails. This also means that Kubernetes can automatically scale compute nodes for the cluster to match the resource usage of the workloads running on the cluster.

Kubernetes achieves High Availability by maintaining a [**ReplicaSet**](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/), in which pods have a backup deployment that can be quickly swapped out with a running job that becomes unresponsive or unhealthy.


