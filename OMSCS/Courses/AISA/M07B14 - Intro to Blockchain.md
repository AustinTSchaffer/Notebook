---
tags: OMSCS, AISA
---
# M07B14 - Intro to Blockchain

Required reading: 
- [[The Bitcoin Paper by Satoshi Nakamoto.pdf]]
- [[Implementing a blockchain from scratch.pdf]]

## Bitcoin v Blockchain
- Bitcoin is a blockchain

## Blockchain
- distributed insert-only (append only) database
- blocks/entries linked via cryptographic hash chains
- https://en.wikipedia.org/wiki/Merkle_tree
- An internet software protocol running on a network of computer nodes on the internet
- Prevents backdating / tampering
- once data in a verified block is recorded on the chain, removing/altering the data often requires consensus by >50% of the network
- open for anyone on the network to access
- core characteristics are decentralization, accountability, security

## Bitcoin Transactions Revisited
- [[Module 7 - Block 13 - Introduction to Bitcoin]]
- Bitcoins are "memoryless".
	- A single bitcoin or a fraction of a bitcoin have no memory of the account's they've been transferred to/from.
	- Each bitcoin is effectively fungible.
- Determining the number of bitcoins in a single wallet is super complicated. "How much I have to spend" is actually "how many unspent outputs do I have access to?"
	- https://bitcoin.stackexchange.com/questions/22997/how-is-a-wallets-balance-computed
- Receiver of a transaction (also neither the sender of a transaction) don't have to be online when the transaction is confirmed

## Blockchain in Bitcoin (Bitcoin's Blockchain)
- every viable transaction is stored in a public ledger
- transactions are placed in blocks, which are linked by SHA256 hashes
- https://blockchain.info
- Bitcoin effectively invented the use of the tech for currency purposes.
- Decentralized consensus procedure
- Bitcoin's novelty is preventing double-spending
- "Genesis Block" is the first block. All subsequent blocks contain the ID (hash) of the previous block in the chain
- Each block contains
	- list of transactions (typically between 500 and 2500)
		- sender
		- recipient
		- amount
		- There's a lot of nuance here
	- SHA256 hash of all data in the block (unique fingerprint/ID)
	- ID of the previous block
- Hashes are tamper resistant. Changing one block requires all subsequent blocks to be changed
- Proof-of-Work
- Decentralized time protocol

![[Pasted image 20230222194522.png]]

- chain isn't stored on one node. Instead it's stored on all nodes in a P2P network. Every node has a copy of the blockchain
- Network makes constant checks to make sure that the blockchain is the same across all nodes

### Decentralization Management
- Digital wallet operates in a P2P mode
- On startup, bootstraps to find other wallets
	- Originally used Internet Relay Chat (IRC)
	- Now based on DNS and "seed nodes"
- Wallet synchronizes with the network by downloading all transactions starting from the GENESIS block if necessary
	- Bitcoin is hundreds of GBs in size
	- Merkel Tree is used as an optimization for finding blocks
- Using a broadcast, the wallets share all transaction information with their peers
	- Optimization: a "gossip protocol" (flooding) or other messaging protocols

### Defining Distributed Consensus
- There are N nodes, each have an input value
- A distributed consensus protocol has following 2 properties
	1. protocol terminates and all honest nodes agree on the same value
	2. this value must have been proposed by some honest node
- At any time in the bitcoin P2P network
	- All nodes have a sequence of blocks of transactions that they've reached consensus on
	- Each node has a set of outstanding transactions it's aware of (but not yet included in the block chain)
		- AKA "mempool"
		- For these transactions "consensus has not happened yet" meaning "no one has wasted fuckloads of electricity on purpose-built hardware to generate a SHA256 hash with a ridiculous 0-prefix constraint, with the point being to slow down the creation of new blocks to 1 per ~10 minutes so that "work" isn't "duplicated".
		- Each node may have a slightly different outstanding transaction pool.
- Consensus is difficult in Bitcoin because
	- Nodes may crash
	- Nodes my be malicious
	- P2P network is imperfect
		- Not all pairs of nodes connected (and may participate)
		- network faults
		- latency, no notion of "global time"
	- Constraints on set of consensus algorithms that can be used

### Simplified Consensus Algorithm
1. New transactions are broadcast to all nodes
2. Each node collects new transactions that pass its verification into a block
3. In each round, a random node gets to broadcast its block upon completing the **proof of work** (PoW)
	- PoW is a compute intensive operation, to intentionally slow down the network from being able to generate new blocks. This makes it unlikely that 2 nodes will complete a block at the same time.
4. Other nodes accept the block only when they verify PoW of the block, and all transactions in the block are valid (unspent, valid signatures)
5. odes express their acceptance of the block by including its hash in the next block they create

## Proof-of-Work Algorithms
### Ingredient 1: Hashes
- secure hash algorithms like SHA-256 or SHA-512
- Single bit changes in input results in cryptographically random changes in the hash function's output
- Arbitrary length inputs
- Fixed-length outputs
- Properties of cryptographic hash function
	- **Consistent:** `hash(x)` always yields the same results
	- **One-way**: Given `y`, hard to find `x` such that `hash(x) -> y`
	- **Collision resistant:** Given `hash(w) -> z`, hard to find `x` such that `hash(x)` is also `z`.

### Ingredient 2: Hashcash Puzzle
- Hashcash
	- a mechanism that creates a puzzle, a function of the message, was sufficiently difficult to compute, but efficient to verify
- In bitcoin, this is modifying the message with a nonce until the message's hash starts with some number of 0s
- Number of 0s is chosen to make new blocks generate at a rate of 1 per ~10 min
- **Goal:** Find nonce `s` such that `sha256(x || s)` such that the first `X` bits are `0`

Honest party computing $m$ hashes to solve the PoW challenge
$$
P(solved)=1-(1-2^{-N})^m \approx \frac{m}{2^N}
$$
Features
- Honest users can produce PoW with probability `~= m/(2^N)` by investing peer nodes (work units)
- tunable hardness parameter N
- efficient verification without interaction

Security
- No shortcuts to solving PoW
- Adversary with $m$ work units cannot do better

- Large content (long messages) M takes longer to hash than short content
- We can keep the content size similar by adding prefixes (W) to the hash of the message M $hash(W || hash(M))$
- Difficulty is adjusting by changing values of N
- Searching for a hash result with N leading 0 bits: $hash(W||hash(M))<2^{256-N}$

Hash game depends on
- Luck (averages out with many messages)
- Computer speed and quality of code (all bitcoin hashing is done on ASICs these days)
- Value of N

![[Pasted image 20230222212600.png]]

![[Pasted image 20230222212755.png]]

![[Pasted image 20230222212723.png]]

![[Pasted image 20230222212624.png]]

- https://en.wikipedia.org/wiki/Proof_of_work
	- Thought it would initially be used to deter DoS attacks, by making service requesters (clients) prove to the server that they did work on their end. This would deter botnets from incurring the associated cost

![[Pasted image 20230222213743.png]]

![[Pasted image 20230222213759.png]]

![[Pasted image 20230222213345.png]]

The 2nd point is actually not necessary. Any SHA256 hash is sufficient.

## Distributed Mining of Bitcoin Transactions

![[Pasted image 20230222213642.png]]

![[Pasted image 20230222213823.png]]

![[Pasted image 20230222213839.png]]

![[Pasted image 20230222214018.png]]

![[Pasted image 20230222214107.png]]

![[Pasted image 20230222214208.png]]

![[Pasted image 20230222214259.png]]

## Incentives for Bitcoin Mining

![[Pasted image 20230222214425.png]]

![[Pasted image 20230222214605.png]]

![[Pasted image 20230222214953.png]]

![[Pasted image 20230222215239.png]]

![[Pasted image 20230222220113.png]]

![[Pasted image 20230222220325.png]]

![[Pasted image 20230222220348.png]]

