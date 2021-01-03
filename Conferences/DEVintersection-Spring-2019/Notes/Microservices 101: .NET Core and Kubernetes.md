# Microservices 101: .NET Core and Kubernetes

## Sample App - Rochambot

- Rock Paper Scissors game
    - humans play an army of bots
    - each bot is a microservice
- ground rules
    - data is written via topics, never direct
    - microservices don't share databases
    - minimal shared code between microservices

## App Flow

- Tech
    - Web and Workers deployed to a Kubernetes service (AKS)
    - Configured from Azure App Configuration
        - Azure "Configuration Explorer"
        - classes use the built-in `IConfiguration` interface
    - Azure Service Bus (Messaging queues (think Kafka, SignalR, EventHubs))
        - matchmaking
        - plays
        - results
    - `new SubscriptionClient`
    - `new ResponseClient`
    - Game-Master service hosts a `gRPC` API for
        - player logins
        - score updates for the player UI client

- 3 agents
    - game master service
    - bot player service
    - web client (UI service)
- Player requests a game (pub to matchmaking queue)
- Player bot accepts game (subbed to matchmaking queue)
- Game master sees match start (subbed to matchmaking queue)
- Game Master records match start (dumps info to a DB, not shared with other entities)
- Player and bot make a play individually
    - game master sees the move (subbed to plays queue)
    - game master records the moves (dumps info to a DB, not shared with other entities)
- Game master determines winner
    - game master posts results (pub to results queue)
    - game master saves results (dumps info to a DB, not shared with other entities)
    - player & bot get results individually (subs to results queue)
- UI updated via `gRPC` API

## Dev Publish Flow

- Kubernetes Cluster
- Package code into Container Images
- Publish images to container registries
- Author Helm deployment templates
- Apply the Helm templates to the Kubernetes cluster
