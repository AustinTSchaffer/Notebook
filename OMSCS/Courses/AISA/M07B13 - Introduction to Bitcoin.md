---
tags: OMSCS, AISA
---
# M07B13 - Introduction to Bitcoin

## What is Bitcoin?
- decentralized p2p overlay network
- crowd computing with incentives
- transactions + blockchain
- cryptography
	- hash
	- key (public/private key cryptography)
	- digital signature
	- hash "games"

## Size of Bitcoin Economy
- total number of coins cannot exceed 21 million
- current bitcoin circulation 19.30M (Feb 19, 2023)
	- https://ycharts.com/indicators/bitcoin_supply
- Unstable price
	- https://www.coindesk.com/price/bitcoin/
- Bitcoin scalability
	- https://crypto.com/university/blockchain-scalability
	- https://en.wikipedia.org/wiki/Bitcoin_scalability_problem
	- https://ycharts.com/indicators/bitcoin_blockchain_size
- Visa stats
	- https://usa.visa.com/dam/VCOM/global/about-visa/documents/aboutvisafactsheet.pdf

## Where does it come from?
- first decentralized digital/virtual currency
	- Crypto P2P currency
- Electronic payment system based on cryptographic proof instead of centralized trust and third-party trust
- Developed by a person or group under the pseudonym of Satoshi Nakamoto in 2008 / operational since early 2009
- [[The Bitcoin Paper by Satoshi Nakamoto.pdf]]
- No financial institutions manage bitcoin
- Clearly we're not going to talk about
	- scaling issues
	- power usage / inefficiency issues
	- the fact that bitcoin has been the currency of choice for 
		- the perpetrators of ransomware attacks
		- online sales of sexual abuse materials
		- for ordinary people, Bitcoin is no longer an anonymous currency. Getting into the network via an exchange requires forms of identity

![[Pasted image 20230220160356.png]]

- Bitcoin is a decentralized P2P network enabled crypto-currency system
- each node in the Bitcoin P2P network represents a user account
- 2 users who do not know each other can transfer bitcoins between each other via the Bitcoin network
- Makes a bitcoin transfer transaction from A to B secure
- Keeps a global accounting on all bitcoin transactions made through the bitcoin network
	- include the balance per node (account)
	- include how and where the balance of bitcoins was coming from using the transaction history

## Bitcoin Transactions
- Every user who joins the Bitcoin network will store and use a blockchain
- The bitcoin client software will give the user a public key and a private key
- every user must keep their private key secure and not reveal it to anyone
- The public key on the other hand is used as the node ID of the user's computer and can be revealed to everyone.

### Pseudo Anonymous
- using public key cryptography, specifically elliptic curve cryptography due to producing strong and shortish keys
- transactions are sent to public key "address"

### Cryptography
- both public and private keys have a unique property
- private key can  be used to sign any message to create a digital signature
- all digital signatures can be verified using the corresponding public key
	- anyone who has a digital signature can verify whether a person truly signed the message, using the signer's public key
- both keys, combined with message signing to create digital signatures and the blockchain, will provide "the cryptography in blockchains"

### Transactions
- A wishes to send 10 BTC to Bob and record the transaction on the Bitcoin blockchain
- She writes the message (transaction) and encrypts it with Bob's public key, and signs it using her private key to create a digital signature
- **digital signing** is hashing a message and then encrypting the hash of the message using the signers private key. This can be verified by encrypting the signature with the signers public key.
- her message combined with the signature is a transaction

## Public-Key Cryptography (Refresher)
- Symmetric public/private key pair
- Keys are generated in pairs
- Cannot find a key given the other key
- What is encrypted with one key can be decrypted with the other
- Encrypting with public key means holder of private key is the only entity that can decrypt the message
- Encrypting a message (or a hash of the message) with your private key is known as signing. Generally you sign a hash of the message, not the whole message. Receivers of the message can verify the message by decrypting the hash with your public key, and then verifying the hash using the same hash algorithm.

![[Pasted image 20230220170843.png]]

### Application of Signatures in Bitcoin

![[Pasted image 20230220172245.png]]

## Bitcoin Security

![[Pasted image 20230220173113.png]]

![[Pasted image 20230220173615.png]]

![[Pasted image 20230220174019.png]]

![[Pasted image 20230220174055.png]]

![[Pasted image 20230220174220.png]]

![[Pasted image 20230220174510.png]]

![[Pasted image 20230220174602.png]]

![[Pasted image 20230220174615.png]]

![[Pasted image 20230220174709.png]]

![[Pasted image 20230220174724.png]]

## P2P Overlay
- Node ID: Hash of node's public key
- Node IP addr:
- each node provides pub key and IP addr during membership establishment
- neighbor relationship via periodic ping pong messaging
- example: Kademlia DHT in Ethereum

- P2P decentralized routing
	- using unstructured P2P overlay
	- broadcasting through neighbors using preset # hop count
	- for both transaction propagation and block propagation, it does not set the fixed number of hops count (no time out) to ensure the sender transaction reaches all nodes

![[Pasted image 20230220175130.png]]

	