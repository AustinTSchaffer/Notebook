---
tags: OMSCS, AISA
---
# M10B19 - Cloud Computing Basics
> Everything as a Service (EaaS) Computing Paradigm

![[Pasted image 20230315180505.png]]

![[Pasted image 20230315180522.png]]

![[Pasted image 20230315180536.png]]

![[Pasted image 20230315180552.png]]

![[Pasted image 20230315180654.png]]

## Cluster Computing: Hadoop Distributed File Systems (HDFS)

HDFS
- Single namespace for entire cluster
- replicates data 3x
- composed of modules that work together to create the Hadoop framework

Spark
- In memory computing
- streaming distributed computing
- run on external distributed file system

MapReduce
- Executes user jobs specified as "map" and "reduce" functions
- manages work distribution and fault tolerance

![[Pasted image 20230315180904.png]]

![[Pasted image 20230315180936.png]]

HDFS
- splits files into 128MB _blocks_
- Blocks are replicated across several _datanodes_ (usually 3 -> Triple Modularity)
- Single _namenode_ stores metadata (file names, block locations, etc)
- Optimized for large files, sequential reads
- Files are append only

![[Pasted image 20230315181214.png]]

## MapReduce
- Simple programming model for processing large dataset on a large cluster
- Works like a pipeline
- When configuring a MapReduce Cluster for a given task, we need to define
	- number of map nodes
	- number of reduce nodes

![[Pasted image 20230315181306.png]]

Focus on the problem, let the library deal with the messy details
- data type: key-value records
- Map function: $map(K_{in}, V_{in}) \rightarrow list(K_{inter}, V_{inter})$
- Reduce function: $reduce(K_{inter}, list(V_{inter})) \rightarrow list(K_{out}, V_{out})$
- MapReduce software system takes care of
	- distributing data
	- distributing code
	- running at scale

### Example 1

![[Pasted image 20230315181721.png]]

![[Pasted image 20230315181801.png]]

Python pseudocode

```python
# mapper.py
import sys

for line in sys.stdin:
    for word in line.split():
        print(word.lower() + "\t" + 1)

# reducer.py
import sys
from collections import defaultdict

counts = defaultdict(int)
for line in sys.stdin:
    word, count = line.split("\t")
    dict[word] += int(count)
for word, count in counts.items():
    print(word.lower() + "\t" + count)
```

### Example 2: Inverted Index
- **Input:** (filename, text) records
- **Output:** the list of files containing each word

Map pseudo-code
```python
def map(text, filename):
	for word in text.split():
	    output(word, filename)
```

Combine: union filename for each word

Reduce pseudo-code
```python
def reduce(word, filenames):
    output(word, sort(filenames))
```

- always have multiple mapper nodes for parallel processing of input to generate proper key-value pairs
- if too many distinct words to fit in memory, using multiple reducer nodes will scale the inverted index creation process
- Getting metrics on memory usage of each node can help determine how to balance the system.

### Example 3: Most Popular Words
- **Input:** (filename, text) records
- **Output:** top 100 words occurring in the most files

2-stage solution
- Job 1: Crete an inverted index (refer to example 2)
- Job 2
	- Map each (word, list(file)) to (count, word)
	- Tip: first compute (word, count), but store it as (count, word)
	- Sort these records by count as in sort job

Optimizations
- Map to (word, 1) instead of (word, file) in job 1, then count files in job 1's reducer, rather than job 2's mapper
- Estimate count distribution in advance and drop rare words
	- Unlikely to be a top 100 word: serendipitously

## MapReduce Computation Model
- A MR job consists of one or more rounds of Map and Reduce processing
- Each round of Map-Reduce processing consists of multiple map tasks (N) and multiple reduce tasks (M)
- The input data to a MR job is partitioned by HDFS into small chunks of equal size (64KB)
	- number of chunks = N (number of map tasks) and M << N

MapReduce computation is distributed and parallelized in 3 phases
- Map phase
	- multiple map tasks are executed in parallel
	- each execute the map code with map input on a map worker
	- each map task `map()` partitions input data into k/v pairs as map output
- Shuffle phase
	- After all `map()` tasks are complete, for each map task, consolidate all emitted values for each unique emitted key and partition the map output into R partitions, where R is the number of reduce tasks
- Reduce phase
	- run `reduce()` in parallel and aggregate the values for each key collected from M map tasks

![[Pasted image 20230315184647.png]]

![[Pasted image 20230315184753.png]]

## Coordination
Master data structures
- task status (idle, in-progress, completed)
- idle tasks get scheduled as Map workers become available
- when a map task completes
	- it produces its map output file and sends the master the location and sizes of its R intermediate files, one for each reducer
	- master pushes this info to reducers when starting shuffle phase
- Master pings workers periodically to detect failures

Master Worker
- Report to Master once it's done
- asks master for map tasks

Reduce Worker
- Master informs reduce workers to start shuffle phase
- Reduce work reports to master once it completes shuffle
- Reduce work reports to master once it completes reduce task

Failure handling
- master pings workers periodically to detect failures

Speculation
- when a map slot is done and no more map tasks are left, the map slot is available for speculation task (helping stragglers)

Speculative Execution
- if a task is going slowly (straggler), then the idle mappers can be chosen to help running the map task of the stragglers

## Fault Tolerance in MapReduce
- task crashes? (map or reduce) Master will reassign the task to another worker
- node crashes? master will reassign all map tasks that did not complete upon crash to other workers
- master crashes? MR job terminates (failed)

![[Pasted image 20230315185419.png]]

## Summary
- By providing a data parallel programming model, MapReduce can control job execution in useful ways
	- Automatic division of a job into tasks
	- Automatic placement of computation near data (or vice-versa)
	- Automatic load balancing
	- Recovery from failures and stragglers
- Users can focus on application, not on distributed computing

## Hadoop MapReduce: Distributed Stage Barrier
- The MR model uses a barrier in the Shuffle stage between the Map and Reduce stages
	- Shuffle cannot start until all map tasks are successfully completed
	- reduce cannot start until shuffle is completed
- Advantage
	- provides simplicity in both programming and implementation
- Disadvantage
	- overly restrictive in many situations
	- may hurt performance

> The shuffle step occurs to guarantee that the results from mapper which have the same key (of course, they may or may not be from the same mapper) will be send to the same reducer. So, the reducer can further reduce the result set.
> 
> From: (https://datascience.stackexchange.com/questions/11049/why-does-map-reduce-have-a-shuffle-step)

![[Pasted image 20230315185819.png]]

Intermediate data
- data generated in between stages
- similar to traditional intermediate data in traditional file systems (e.g. `.o` files
- critical to produce the final output
- short-lived, written-once and read-once, and used-immediately

![[Pasted image 20230315190034.png]]

## Optimizing Stage Barrier with Early Shuffle
- Standard Shuffle
	- Start Shuffle phase only when all maps have been completed
	- The master node keeps the accounting
	- How
		- each map task reports to the master when it completes its map task execution
		- status report includes the location and size of the map input file, the time to complete the map task
- Early shuffle
	- unpon the completion of a certain percentage (e.g. 5%) of the total map tasks, shuffle phase can start
	- improves latency and throughput

## Computational Barriers + Failures
![[Pasted image 20230315191031.png]]

![[Pasted image 20230315191120.png]]

![[Pasted image 20230315191106.png]]

![[Pasted image 20230315191158.png]]

