---
tags: OMSCS, AISA
---
# M02B03 - Search Engine Crawlers and Indexers
> Crawlers and Indexers

Required reading: [[The Anatomy of a Large-Scale Hypertextual Web Search Engine.pdf]]

- Deep search
- Web crawlers
- Web indexers
- Result retrieval
- Ranking algorithms

The web is
- online
- searchale
- distributed
- large scale
- rapidly growing
- social networks, online communities, dictionaries, encyclopedias

3 primary standards
- URLs
- HTML
- HTTP(s)

## Public (aka Surface) Web vs Deep Web
### Public Web
- Static web pages, physically reside in one of the internet servers
- Server-side rendered pages
- excludes pages that are not indexed by major search engines due to
	- auth requirements
	- robots exclusion protocol (REP)
	- not reachable by robots / crawlers

### Deep Web
- aka invisible/hidden web
- client-side (dynamically) rendered pages
- Web crawlers would prefer to not run arbitrary javascript/WASM when determining what's on a page
- Web crawlers would also prefer to not input data into forms in order to determine what's accessible from and connected to the current page
- Estimated that the "deep web" is 500x larger than the surface web

## URL Components
- Uniform Resource Locator (URL)
	- access control (protocol) (ex: `http://`)
	- page name
		- host name / domain name
		- path
	- query parameters
		- Generally not used by static web pages

- (hyper)link: pointer from one page to another, load the other page if clicked on
- document == web page
- web site: a colloquial term which usually is identified by the domain name, defining a collection of pages, but isn't as clear of a term anymore.

## Big Research Questions
- how do you find information on the web?
	- search engines
	- can find information from <40% of the surface web
- how do you find information that search engines cannot reach?
	- searching the deep web? huge challenge
	- you need your robots to act as human users
- How do search engines find info on the public web?
	- crawl
	- index
	- rank
	- retrieval

## Search Engine for the Surface Web

- 1994
	- webcrawler
	- infoseek
	- lycos
- 1995
	- altavista -> Yahoo!
	- Excite
- 1996
	- Inktomi -> Yahoo!
	- Ask Jeeves -> Ask.com
- 1997
	- Northern Light
- 1998
	- Google
	- Goto.com -> Overture -> Yahoo!
- 1999
	- Baidu
- 2000
	- Teoma -> ask.com
- 2004
	- Yahoo! Search
	- MSN Search
- 2009
	- Bing

## Search Engine General Architecture
- A search engine is a computer system that responds to user query requests, by searching through databases of documents gathered by software robots

3 key components
- robots/spiders/crawlers
	- URL databases
- indexer
	- keyword -> URL mapper
- ranker
	- page rank
- retrieval software
	- retrieval engine
	- graphical user engine

### Web Crawlers
- Load page
- Follow links
- Store contents of web pages, identified by URL, in a database
- traverses web's hypertext structure, retrieving documents, then recursively retrieves all documents that are referenced in that document (directly or indirectly)
- Also called robots or spiders
- Software agents
- goes out to the web to gather information about the content of pages being crawled
- 2 main tasks
	- data extraction
		- extract subjects from the page
		- identify new URLs to add to the to-be-crawled list
	- change detection
		- has this page changed?
		- what's been changed?

### How does a robot crawl the web?
- For each URL from the list, the crawler will
	- extract subjects from the page
	- extract urls from the page
	- make decision based on URL resolution
		- if new, add to the "to be crawled" list
		- if crawled before, check if the page has been changed significantly
- Crawler selects next page to crawl, based on a chosen traversal strategy

### Web as a Big Graph: A Robot View
![[Pasted image 20230114113508.png]]

- crawling strategies
	- depth-first navigation
	- breadth-first navigation
	- hybrid strategy
	- strategy doesn't really matter if your goal is to index all of the pages

### Simple Example + Architecture
- Start with a known list of URLs (seed list)
- Add urls to "to be crawled" list

![[Pasted image 20230114113824.png]]

![[Pasted image 20230114113922.png]]

## Robot Summary
- Every search engine has its own (likely proprietary) robot crawling logic
- Robots return to web sites on regular basis to look for changes
- The use of robots come at a price, especially when the are operated remotely on the internet
	- operational costs and dangers
	- don't flood sites with robot traffic, be a good citizen of the web
	- bad implementation of robots
		- black holes
		- not recognizing syntactically equivalent URLs
		- etc.
	- robot exclusion protocol (REP) (please don't crawl this page/site)
	- The Robot META tag

## Web Crawler (Mercator) (AT&T Research)
![[Pasted image 20230114114624.png]]

## Internet-Scale Web Crawler Examples
- **PULSE**: web crawler for Intel's Intranet
- **HyperBee**: A P2P crawler for the web
- **Apoidea**: A distributed hash table (DHT) based decentralized P2P crawler
- **PeerCrawl**: A broadcast-based P2P crawler

### Motivation and Objectives
- How big of a problem are we talking about?
	- How large is the crawlable web? GBs? TBs? PBs? EBs? ZBs?
	- Can we optimize "pages crawled per unit of time"?
	- Can we optimize "storage requirements per unit of web content?"
	- How much additional information needs to be stored so the indexers / rankers can be effective?
	- How much storage do we need?
	- How often do we need to re-crawl the web?
	- How much traffic can each site handle? How do we make sure our robots don't exceed it?
- To quantify the amount of work performed in building a web crawler or a search indexer, how many URLs are in the intranet of a website such as `cc.gatech.edu` or `intel.com`?

### `PULSE` Crawler Project
- key components
	- Visual Basic 5.0 + MS Access + HTML/ASP
	- semi-configurable
	- A search database to contain URLs searched and subjects found

**Status pane**
![[Pasted image 20230114115836.png]]

**Seed/Results DBs**
![[Pasted image 20230114115917.png]]

**Subject extraction, search strategy, max depth from seed**
![[Pasted image 20230114115941.png]]

**Pseudocode: Depth-First Search**
```
add seed URLs to search list (stack)
while search list is not empty
	pop first url from the search list (stack) 
	retrieve HTML page specified by the url
	scan page and add subjects to DB
	for each link in page
		add links to the search list (stack)
```

**Challenges**
- Not easy to
	- scan for URLs
		- How do you handle relative links?
		- What about a frame set?
		- Mailto tags?
	- scan for subjects
		- what words should we choose?
		- space requirements for subject database?
- What to do if HTML is malformed? Missing tags? Pages that aren't HTML?
- Internet is BIG (example)
	- Searching from 1 seed URL (`www.intel.com` for example)
	- Only scanning the first 1000 characters per page
	- It never ends. Remaining URLs to search remains constant because as you search each page, you keep finding more URLs

![[Pasted image 20230119193236.png]]

![[Pasted image 20230119193354.png]]

![[Pasted image 20230119193415.png]]

- If the internet contained 200million pages this web crawler...
	- would take 15.5 years to search 200 million URLs
	- would generate 4 billion subjects
	- require 71GB of storage

### Key Takeaways from PULSE
- web crawlers must be restartable without losing much (if any) progress
- web crawlers must be able to detect loops in the search list
- web crawlers must be able to handle many different file types
	- html, plaintext, docx, ppt, xls, zip, pdfs, etc
- How should the subject database be structured?
- How much of a given page do you store?
- For server-side rendered pages, how many variations of the page do you store? Can we discover all relevant variations?

## Indexers
- Indexers are a software program, and an index database
- also called the catalog
- if a web page changes, then the index needs to be updated
- indexing is a separate pipeline, uses the database generated by the crawlers

### Inverted Index Structure
For each word, keep an ordered array of all (document, position in doc) pairs, potentially compressed

![[Pasted image 20230119195621.png]]

- for each term T, the index stores a list of documents that contain T
- linked lists are generally preferred to arrays
- Sorted by document ID to reduce complexity of insertions and lookups

![[Pasted image 20230119195735.png]]

constructed by
- making a queue of documents to be indexed
- tokenizing the documents
- use stemming to find all linguistically equivalent to each token, collapsed to a single entry in that web. Remove common words like "the", "a", "it"
- insert tokens into database

Other options / optimizations
- term-document-term frequency inverted index
- index term selection (term assignment)
- distributed indexes when the index DB is too large

Distributing index
- partition index by term or by document?
- by term?
	- hot terms? cold terms?
	- query multiple terms?
	- need query frequency and term co-ocurrence 
- by document?
	- results from each machine need to be merged
	- workload balancing?
	- every node is involved in every search
