---
tags: OMSCS, AISA
---
# Course Review (2 of 4)

I'll start by saying that the bitcoin lectures don't feel well designed.

The bitcoin lectures go on way too long and contain a lot of duplicated information. Some of the information is factually incorrect. The lectures are also littered with typos and grammatical issues.

The Bitcoin and blockchain lectures could be greatly shortened and improved by having a preface lecture which focuses solely on the core technologies that underpin blockchain technology, without focusing the discussion on blockchain itself. Without such a primer, the lectures duplicate information, misrepresent some of it, and generally feel incomplete and inexact. Such technologies would include

- Cryptography Terminology
	- Plaintext vs Ciphertext
	- Ecryption vs Decryption
	- Digital Signatures
- A primer on Public-Key Cryptography
	- Key generation algorithms (Just ECDSA would be sufficient, but RSA is the most common option outside of CryptoCurrency)
	- Encryption
	- Digital Signature Generation
- cryptographic hash functions (Namely the "Secure Hash Algorithm", or "SHA")
- Merkle Trees (Used by Bitcoin, also used by Git)

The bitcoin lectures have the most content of any previous module in this course, but the information barely has any value, because the lectures barely describe the technical systems that Bitcoin uses.

The bitcoin lectures don't describe how a user's wallet balance is calculated, which is important to understanding how double-spending and over-spending are prevented.

The Proof-of-Work (PoW) component of Bitcoin is discussed as a security feature, when it actually functions as a method of limiting the rate of block generation, in order to allow nodes to reach consensus easier. The lectures mention at least once that it's computationally harder to brute force a SHA256 hash that contains a series of leading zeros, compared to a regular SHA256 hash. That is not true. The computational complexity is exactly the same for both.

One of the lectures touches on the energy usage issues of Bitcoin, but it does not discuss _why_ it's an issue. The discussion needs more context, such as comparing the per-transaction energy cost of bitcoin versus other systems.

Speaking of the per-transaction energy inefficiencies, the lectures also don't discuss the Bitcoin scalability problem. Bitcoin's artificially imposed limiters prevent Bitcoin from scaling to process transactions efficiently and expediently. Bitcoin effectively has a maximum transaction throughput of 10 per second globally, which it has never sustained for an entire day.

If we're not going to cover these topics, what is even the point of including Bitcoin as a case study? Why are we learning about a computationally-inefficient system which physically can't scale beyond a certain point, in a course that is supposed to be focused on internet-scale technology? Why are we only going to discuss its positives, and vaguely point to its implementation?

In my view, technology is a discipline that is laser focused on pros and cons, advantages and disadvantages, pluses and minuses. There is no perfect system, and there is no premier example of this concept than the "CAP theorem" from distributed systems. To me, it doesn't feel like we've been given a space that fosters discussions relative to the disadvantages of the technologies in this course, _unless_ those disadvantages are addressed by some other technology, which is also being discussed in the course.

In addition to that, this course doesn't foster discussions relative to the social, political, nor economic implications of any piece of technology, when those implications are an indictment of the technology. However, this course does seem to foster discussions about the social, political, and economic implications of a piece of technology when the implications are an endorsement of the technology. I believe that this imbalance is preventing students from being able to paint a full picture of the course's content.

As a result of all of this, I do not feel as though my paper submissions are evidence of my best work. Even my P3 submission, which was selected as an "exemplary assignment," felt lacking in substance and rigor when I submitted it. My grades in this course feel arbitrary and subjective. My grades appear to trend higher when I focus my efforts toward what I feel the instructor and the TAs want to see. My grades appear to trend lower when I focus my efforts toward work that aligns with my judgement, my understanding of the technology, and my values.

In my view, this course is not well motivated and requires a full redesign before I'd be willing to recommend that any student takes it.
