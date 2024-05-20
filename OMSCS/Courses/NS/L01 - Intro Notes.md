---
tags:
  - OMSCS
  - NS
---
# L01 - Intro Notes

Course textbook is an online resource
- Errata: http://networksciencebook.com/translations/en/resources/NetworkScienceErrata.pdf
- Book: http://networksciencebook.com/

## Knowledge Quiz
- Network science is the study of complex systems through their network representation.
- The network architecture of a complex system is not sufficient to understand the system's functions and dynamics.
- Centrality
	- Centrality metrics aim to rank nodes (or edges) based on "importance"
	- There are many metrics/algorithms for defining/finding centrality
	- In ring networks, all nodes have the same centrality
	- Pagerank is a good example of an algorithm/system which ranks nodes in a network by importance
- dynamics on networks describe a process through which the state of network nodes changes over time even if the network topology is static

## What is Network Science?
 > _The study of complex systems focusing on their architecture, i.e., on the network, or graph, that shows how the system components are interconnected._
 
- Many and heterogeneous components
- Components that interact with each other through a _(non-trivial)_ network
- Non-linear interactions between components

## Network Complexity/Topology
![[Pasted image 20240517174214.png]]

![[Pasted image 20240519060119.png]]

- regular networks
	- rings
	- cliques
	- lattices
- random networks
	- connections between nodes are determined randomly
- most technological, biological, and information systems do not have a regular/random architecture
- a major difference between network science and graph theory
	- network science is an applied data-science discipline that focuses on complex networks encountered in real-world systems
	- graph theory is a mathematical field that focuses mostly on regular/random graphs

## The brain of a C.elegans Worm
- worm is 1mm in length
- roughly 300 neurons
- has many standard animal behaviors
- Its been fully mapped using various techniques, and network science allows you to analyze it

## Main Premise
> even if we don’t know every little detail about a system and its components, simply knowing the map or “wiring diagram” that shows how the different system components are interconnected provides sufficient information to answer a lot of important questions about that system.

> if our goal is to design a new system (rather than analyze an existing system), network science suggests that we should first start from its network representation, and only when that is completely done, move to lower-level design and implementation.

![[Pasted image 20240519060119.png]]

> Suppose that we are to design a communication system of some sort that will interconnect 6 sites. The first question is: what should be the network architecture?

- Line
	- cheapest
	- vulnerable to disconnects
	- inefficient
- Ring
	- strict upgrade over line
	- only slightly more expensive
- Fully connected
	- most expensive
	- efficient
	- resilient
- Mesh
	- good balance of tradeoffs

## Examples in the wild
- [Chains of Affection: The Structure of Adolescent Romantic and Sexual Networks](https://www.cis.upenn.edu/~mkearns/teaching/NetworkedLife/teensex.pdf)
-  [Rise of China in the International Trade Network: A Community Core Detection Approach](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4138169/)
- [Predicting the Fission Yeast Protein Interaction Network](https://pdfs.semanticscholar.org/0595/6042c6bd23eb49b5071964ce2d04edb26921.pdf?_ga=2.238092041.829074902.1579584841-796840842.1579584841)
- [Networking Our Way to Better Ecosystem Service Provision](https://www.sciencedirect.com/science/article/pii/S0169534715003006)
- [Influence of fake news in Twitter during the 2016 US presidential election](https://www.nature.com/articles/s41467-018-07761-2)​
- [Wireless Data Center with Millimeter Wave Network](https://ieeexplore.ieee.org/document/5684121) 
- [Data visualization for social network analysis](https://cambridge-intelligence.com/use-cases/social-networks/)​
- [The bottlenose dolphin community of Doubtful Sound features a large proportion of long-lasting associations](https://link.springer.com/article/10.1007/s00265-003-0651-y)
- [The synapse, Khan Academy](https://www.khanacademy.org/science/biology/human-biology/neuron-nervous-system/a/the-synapse)​
- [Action potentials and synapses, The University of Queensland](https://qbi.uq.edu.au/brain-basics/brain/brain-physiology/action-potentials-and-synapses)​
- [Alterations in Brain Network Topology and Structural-Functional Connectome Coupling Relate to Cognitive Impairment](https://www.frontiersin.org/articles/10.3389/fnagi.2018.00404/full)
- [The Measurement Standard, Carma](http://www.themeasurementstandard.com/wp-content/uploads/2016/04/network-of-swords.jpg%E2%80%8B)
- [Schizophrenia interactome with 504 novel protein–protein interactions](https://www.nature.com/articles/npjschz201612%E2%80%8B)

## Network Centrality
![[Pasted image 20240519060747.png]]

- co-authorship network for a set of Network Science researchers
	- nodes are researchers
	- researchers are connected if they published a paper together

![[Pasted image 20240519060855.png]]

- Characters from GoT: A Storm of Swords
	- nodes are connected if the 2 characters interacted
	- the weight of the edge represents the length of that interaction
	- 2 different centrality measurements are present in this diagram
		- the size of a node refers to PageRank score
		- the size of a node's label refers to the node's "betweenness. The betweenness of a node v relates to the number of shortest paths that traverse node v, considering the shortest paths across all node pairs.
	- both centrality metrics show that Jon and Tyrion are the most "central" characters, with Daenerys, Robb, and Sansa following
	- This diagram drives home why GRRM will never finish his novel.

## Communities (Modules) in Networks
![[Pasted image 20240519061622.png]]

- communities are clusters of highly interconnected nodes
- the density of connections between nodes of the same community are much higher than the density of connections between communities

> Returning to the previous Game of Thrones visualization, each color represents a different community – with a total of 7 communities of different sizes.

Later in the course, we'll discuss nodes which can be identified as being part of 2 communities.

## Dynamics of Networks
![[Pasted image 20240519121304.png]]

- systems that change over time through natural evolution, growth, or other dynamic rewiring processes
- Dynamic Processes on Networks
	- there is a dynamic process that is gradually unfolding on that network
	- the network structure remains the same
	- ex: an epidemic that spreads through an underlying social network

## Influence and Cascade Phenomena
- "information contagion"
	- Facebook
	- Twitter
- not all dynamic processes are physical
	- ideas
	- opinions
	- social trends
	- hypes

![[Pasted image 20240519122221.png]]

> The study used network science to identify the most influential spreaders of fake news as well as traditional news.

> An important but still open research question is whether it is possible to develop algorithms that can identify influential spreaders of false information in real-time and block them.

## Machine Learning and Network Science
> We will also study problems at the intersection of Network Science and Machine Learning.

- NS focuses on the graph models - statistical models of static or dynamic networks that can capture the important properties of real-world networks.
- network below comes from a paper about schizophrenia https://www.nature.com/articles/npjschz201612
	- interactions between genes associated with schizophrenia
	- drugs that target either specific genes/proteins or protein-protein interactions
	- ML models have been used to predict previously unknown interactions
	- legend
		- round green nodes: drugs
		- square nodes: genes
		- purple nodes: drugs in clinical trials

![[l1-ml-ns.png]]

## History of Network Science
Roots of NS
- graph theory
- statistical mechanics
- nonlinear dynamics
- graph algorithms
- statistics
- machine learning
- theory of complex systems

NS focuses on real-world networks and their properties

NS provides a general framework to study complex networks independent of the specific application domain.

## Birth of Network Science

- Small-World paper by Watts and Strogatz in 1998
	- empirical study of the "six degrees of separation" phenomenon
- Emergence of Scaling in Random Networks by Barabási and Albert in 1999
	- Real-world networks are "scale free".
	- The number of connections that a node has is highly skewed
	- Some nodes are hubs
	- number of connections that a node has follows a power law distribution
	- networks have a "rich get richer" property
	- referred to as "preferential attachment"

