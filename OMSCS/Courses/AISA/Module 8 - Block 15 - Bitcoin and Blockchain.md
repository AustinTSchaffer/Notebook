---
tags: OMSCS, AISA
---
# Module 8 - Block 15 - Bitcoin and Blockchain

## All virtual currency must address following challenges
- Creation of a virtual coin/note/token
	- How is it created in the first place?
	- How do you prevent inflation?
- Validation
	- How is the coin legitimized?
	- How do you prevent double-spending?

Bitcoin uses a fully decentralized coordination architecture
- Infrastructure-less approach
- Rely on crypto-chain + proof of work + decentralized consensus
- Antithetical to authoritative-party-based trust
- No central bank or clearing house

## Bitcoin Design Ideas
Validation
- Is the coin legit? (PoW)
	- Use of cryptographic hashes + signature + hash challenge
- How do you prevent a coin from double-spending?
	- Replicate blockchain + broadcast every spending to all nodes

Creation of a virtual coin/note
- how is it created in the first place?
	- Provide incentives for miners
- How do you prevent inflation?
	- Limited max supply of bitcoin
	- Few rewarded for completing a block.

## Desired Security Requirements
- privacy of user identity
- unforgeability of digital vouchers
- consistency of the blockchain across the network
- tamper-resistance
- Anti-DDoS

## Security
4 properties in secure communication
1. Authentication
2. Confidentiality
3. Integrity
4. Availability

### Security + Bitcoin
1. Authentication (Public key Crypto: Digital Signatures)
	1. Am I paying the right person? Not some other impostor?
2. Integrity (Digital Signatures + Cryptographic Hashes)
	1. Can an attacker reverse or change transactions?
	2. Is the coin double-spent?
3. Availability (PoW + Replicated P2P Ledger)
	1. Can I make a transaction any time I want?
4. Confidentiality (Infrastructureless + Public Ledger)
	1. No anonymity, only pseudonymity
	2. Privacy beyond pseudonymity is important, but it's not part of the original design

#### Alter transactions?
- Cannot alter transactions
- No one can fake transactions to use Alice's bitcoins without Alice's private key to sign the transactions
- Any change to a transaction included in a block will cause the hash of the block to change, breaking the crypto-chain

#### Transactions with Chain of Signatures
Make player ID = public key
- We can now make transactions by
	- signing messages
	- sending messages to everyone in the network
- Signed transactions are
	- unalterable
	- verifiable by anyone
	- from key to key, not tied to a real identity

#### Cheating
- cannot alter transactions
- double spending or spending more than you have?
- cheating and colluding with validator of the transaction?
	- to add double spending of transactions into a block
	- to add bad/inconsistent/tampered block into the chain

#### Anyone can verify each bitcoin in the system
- Electronic coin == chain of digital signatures
- bitcoin transfers can only be initiated from the owner's public key, signed by the owner's private key
- Anyone can verify
	- Alice is the current owner of the BTCs
	- For each BTC in Alice's wallet, the previous (n-1)th owner before alice, who transferred it to the nth owner (Alice)
- Anyone can follow the history

![[Pasted image 20230304135549.png]]

![[Pasted image 20230304140120.png]]

![[Pasted image 20230304140231.png]]

![[Pasted image 20230304140741.png]]

![[Pasted image 20230304141053.png]]

![[Pasted image 20230304141116.png]]

## Optimization
> Merkle tree, size

![[Pasted image 20230304141759.png]]

![[Pasted image 20230304141854.png]]

![[Pasted image 20230304141922.png]]

![[Pasted image 20230304142113.png]]

![[Pasted image 20230304142138.png]]

![[Pasted image 20230304142220.png]]

![[Pasted image 20230304142300.png]]

![[Pasted image 20230304142338.png]]

## Broadcast vs Gossip
![[Pasted image 20230304142502.png]]

![[Pasted image 20230304142512.png]]

![[Pasted image 20230304142657.png]]

## Ethereum P2P Networks
- each node is represented by (node ID, IP, port)
	- NodeID is SHA256 hash of public key
- Each node has N (<=25) active neighbors
- Each node checks/rebuilds neighbor connections every 7200ms

Routing cost optimization
- Each time a node sends a block to only $\sqrt{N}$ neighbors
- send the block ID to the remaining $N-\sqrt{N}$ neighbors

## Proof of Work (PoW) Alternative
> Proof of Stake, PoS

![[Pasted image 20230304143558.png]]

![[Pasted image 20230304143636.png]]

![[Pasted image 20230304144118.png]]

![[Pasted image 20230304144132.png]]

## Alternative Architectures
![[Pasted image 20230304144237.png]]

![[Pasted image 20230304144252.png]]

![[Pasted image 20230304144321.png]]

![[Pasted image 20230304144352.png]]

![[Pasted image 20230304144407.png]]

![[Pasted image 20230304144427.png]]

![[Pasted image 20230304144442.png]]

## Blockchain Use Cases
![[Pasted image 20230304144507.png]]

![[Pasted image 20230304144524.png]]

![[Pasted image 20230304144533.png]]

![[Pasted image 20230304144557.png]]

![[Pasted image 20230304144614.png]]

