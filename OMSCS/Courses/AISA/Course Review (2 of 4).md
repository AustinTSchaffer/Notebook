---
tags: OMSCS, AISA
---
# Course Review (2 of 4)

The bitcoin lectures don't feel well designed.

These bitcoin lectures go on way too long and contains way too much duplicated information. Some of the information appears factually incorrect. The lectures are also littered with typos and grammatical issues. For example, "private key" and "privacy key" are used interchangeably when talking about public key cryptography.

The lectures could be greatly shortened and improved by having a preface lecture which focuses on
- public key cryptography
- cryptographic hash functions
- merkle trees

The bitcoin lectures have the most content of any previous module in this course, but the information barely has any value, because the lectures barely describe the technical systems that Bitcoin uses.

The bitcoin lectures don't describe how a user's wallet balance is calculated, which is important to understanding how double-spending and over-spending are prevented.

The Proof-of-Work (PoW) component of Bitcoin is discussed as a security feature, when it actually functions as a method of limiting the rate of block generation, in order to allow nodes to reach consensus easier. The lectures mention at least once that it's computationally harder to brute force a SHA256 hash that contains a ton of leading zeros, compared to a regular SHA256 hash. That is not true. The computational complexity is exactly the same for both.

One of the lectures touches on the energy usage issues of Bitcoin, but it does not discuss _why_ it's an issue. The discussion needs more context, such as comparing the per-transaction energy cost of bitcoin versus other systems.

Speaking of the per-transaction energy inefficiencies, the lectures also don't discuss the Bitcoin scalability problem. Bitcoin's artificially imposed limiters prevent Bitcoin from scaling to process transactions efficiently and expediently. Bitcoin effectively has a maximum transaction throughput of 10 per second GLOBALLY, which it has NEVER sustained for an entire day.

If we're not going to cover these topics, what is even the point of including Bitcoin as a case study? Why are we learning about a computationally-inefficient system which physically CAN'T scale beyond a certain point, in a course that is supposed to be focused on internet-scale technology, if we're only going to talk about its positives, and vaguely point to its implementation?

These lectures feel like they were written by someone who does not understand the technology very well. The writer of these lectures also heralds the technology as if it is the most well-designed system ever conceived, and insinuates that participating in the network is a virtuous exercise. 

Technology has always been about pros and cons. To me, it doesn't feel like we've been given a space to discuss the cons of the technologies in this course, _unless_ those cons are addressed by some other technology which was also discussed in this course.

This course doesn't appear at though it wants students to discuss the negative social, political, nor economic implications of any piece of technology in this course. However, this course seems to wholeheartedly accept discussions about the POSITIVE social, political, and economic implications of any piece of technology. This imbalance is preventing students from being able to paint a full picture of the course's content.

As a result, I did not feel as though my latest paper submissions, including my papers which were selected as "exemplary assignments", were my best work, nor did I feel as though they were intellectually motivated assignments. My grades in this course feel arbitrary and subjective. My grades trend higher when I focus my efforts toward what I feel the TAs and instructor want to see. My grades trend lower when I focus my efforts toward work that aligns with my judgement, my understanding of the technology, and my values.

In my view, this course is not well motivated and requires a full redesign. I don't believe that it will be possible to fix this course while also keeping the same instructor.