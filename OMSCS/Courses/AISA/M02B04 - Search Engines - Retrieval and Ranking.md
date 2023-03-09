
---
tags: OMSCS, AISA
---
# M02B04 - Search Engines - Retrieval and Ranking
> Ranking and retrieval

Required reading: [[The Anatomy of a Large-Scale Hypertextual Web Search Engine.pdf]]

Continuation of [[Module 2 - Block 3 - Search Engine Crawlers and Indexers]]

Retrieval program needs to sift through the index and find matches to a search and rank them based on estimated relevancy

Relevance reasoning
- most relevant? based on keywords of the documents?
- frequency? link popularity? Number of times linked to?
- This is a cat and mouse game for the public web. Everyone's trying to game whatever algorithm you choose. For intranet search indexers, pick something sensible and move on.

Query processing
- how to search through a distributed index to find all matching documents
- this will depend on data structure chosen
- indexer should take this into account

Document ranking
- Term-Frequency based ranking
- Citation-Based / Connectivity based ranking (Google's PageRank)

![[Pasted image 20230119202041.png]]

## A simple approach to term-freq based ranking

$V=\frac{(FTD)(FTR)}{N}$

- $FTD$ - Frequency of term in document
- $FTR$ - Frequency of term in all documents
- $N$ - Number of documents in all the retrieved set
- $V$ - ranking value of a term for a particular document

Page ranking is dependent by query. Multi-term queries

## Connectivity-based ranking
> 2 types of connectivity based ranking algorithms

**Query Dependent**
- HITS (Kleinberg98)
	- Hub (good sources of links) and Authority (good sources of content)
- An important content page is highly linked to among initially retrieved pages and their neighbors.

**Query Independent**
- PageRank (BrinPage98)
- an important page is linked by many pages or by other important pages

## Google PageRank
> Query independent connectivity-based ranking

Assumption
- every page has some number of forward links (out edges) and back links (in edges)
- A link from page A to page B as a vote, by page A, for page B

![[Pasted image 20230119202814.png]]

- Page quality is related to the number of other pages with direct citation links
- page should rank higher if
	- links from many pages
	- links from other high-rank pages

Factors
- number of citation sources
- ranking score of citation sources
- out-degree of each citation source

$$R(u)=d\sum_{v{\in}B_u}{\frac{R(v)}{N_v}}$$
- $u$ - a page
- $v$ - a page that has a link to $u$
- $N_v$ - number of links from $v$
- $B_u$ - set of pages that point to $u$
- $d$ - damping factor from 0 to 1 for normalization
- $F_u$ - set of pages $u$ points to (not used)

Page ranks are initialized to 1.

This equation is recursive, and computed by starting with any set of ranks and iteration the computation until it converges.

![[Pasted image 20230119203904.png]]

**Rank Sink**: If 2 pages point to each other, but to no other page, during the iteration, the loop will accumulate rank, but never distribute any rank.

![[Pasted image 20230119204106.png]]

**Modified Definition**

$$R(u)=d\sum_{v{\in}B_u}{\frac{R(v)}{N_v}}+(1-d)E(u)$$
$E(u)$ is some vector over the web pages that corresponds to a source of rank. For example, jump to other pages with uniform probability or to a favorite page with high probability etc.
	- $E(u)$ is a user designated param. In PageRank, it follows a uniform distribution
	- $d$ is a decay factor. $0.85$ is a well-known damping factor.

- **Random surfer model**. The definition corresponds to the probability distribution of a random walk on the web graph.
- The probability of the serfer reaching one page is the sum of probabilities for the random surfer following links to this page
- $E(u)$ can be thought as the random surfer who does not follow (click on) an infinite number of links, and instead, it gets bored sometimes and randomly jumps to a different page
- The PageRanks then form a probability distribution over web pages
	- the sum of all pages values will be N, the total number of pages, and the average page rank of a page is 1
- surfer jumps to a random page with probability $(1-d)$
- With probability $d$ they follow a random hyperlink on the current page
- PageRank is a Markov Chain

Transition probability matrix $A$

$$d*A*R+(1-d)*U$$
- $U$ - uniform distribution
- $A$ - adjacency matrix of $N$ by $N$
- $R$ - rank vector of $N$ pages

![[Pasted image 20230119205751.png]]

![[Pasted image 20230119205825.png]]

- PageRank is considered as a model of user behavior, where a surfer clicks on links at random with no regard towards content
- probability that the random surfer clicks on one link is solely related to the number of links on that page
- the random surfer visits a web page with a certain probability, which is derived from the page's pagerank, and the number of ongoing links on that page
	- one page's pagerank is not completely passed on to a page it links to, but is divided by the number of links on that page
- does not rank the whole website
- page rank is determined per page individually
- pagerank of A is recursively defined by the page rank of pages which link to A
- The damping factor is the probability that a random surfer clicks on links on a page vs going to some other potentially unlinked page
- The higher $d$ is, the more likely the random surfer will click links vs randomly navigating

## Page Rank Example
1. Start each page at 1
2. On each iteration, have each page $p$ contribute $\frac{rank_p}{neighbors_p}$ to its neighbors
3. set each page's rank to $0.15 + d * contribs$
4. Keep going until the algorithm converges. Picking a low precision helps the algorithm converge.

![[Pasted image 20230119211129.png]]

## Example 2

![[Pasted image 20230119211444.png]]

![[Pasted image 20230119211504.png]]

![[Pasted image 20230119211611.png]]

- Page and Brin's 1999 paper states that 100 iterations are necessary to get a good enough approx of PageRank for the whole web.
- Sum of all pages pageranks still converges to the total number of pages (meaning the average is 1)

## Other Ranking Criteria in Google
- Location/Capitalization information for all hits
- Extensive use of proximity for multiword search
- The use of some visual presentation details
	- words in larger or bolder font are weighted higher than other words on the same page
- Google combines the IR score with the PageRank of a document to give a final rank to the document

## Technical Challenges
**Scalability**
- when the graph and its intermediate results are too big to fit into main memory, the algorithm can be slow and hard to optimize
- Google can only refresh pageranks once a year or once every half year

![[Pasted image 20230119212535.png]]

**Ranking Quality**: spam and rank sinks

**Spider Traps / Rank Sinks**: A group of pages is a spider trap if there are no links from within the group to outside the group

**Dangling Links**: A page contains a dangling link if the hypertext points to a page with no outgoing links

**Dead Ends:** pages with no outgoing links

