---
tags:
  - OMSCS
  - AI
  - AIMA
  - NLP
---
# AIMA - Chapter 23 - Natural Language Processing

These notes will be relatively sparse, given that NLP is not a focus of this course, and that there is another OMSCS course which focuses on NLP.

- speaker
	- goal
	- knowledge
	- plans
	- representation
- listener / reader
	- perception
	- inference
- 3 primary goals of NLP
	- communication
	- learning
	- scientific understanding

## 23.1 Language Models

- grammar defines the syntax
- semantic rules define the meaning
- not so simple
	- language judgements vary by person and by time
	- natural language is ambiguous and vague
	- mapping from symbols to objects is not formally defined
- often we don't use booleans in NLP, but instead floats for representing probabilities
- language models are a probability distribution for describing the likelihood of any string.
	- can suggest completion
	- can suggest improved grammar

### bag of words model
- can use naive bayes to classify sentences into categories, based on the words present.
- Pretty simple application of bayes formula
- $P(Class|w_{1:N})=\alpha P(Class)\prod_jP(w_j|Class)$
- training occurs on a **corpus** of text. each segment of text is labeled with a class.
- $P(Class)$ is determined by counting the probability of each category
- We can use counts to estimate the conditional probability of each word given the category ($P(w_x|Class)$)
- "if within the *business* category we have seen 100,000 words and the word *stocks* appeared 700 times, then we can estimate $P(stocks|Class=business) \approx \frac{700}{100,000}$"
- word vectors tend to be sparse, so feature selection is important.
- dropping articles, words that are common to all classes
- dropping rare words, words that have high variance in their predictive power
- add in other metadata
	- words in title/subject
	- sender/receiver (in case of email)
	- attachments?
	- nonstandard punctuation?
### N-gram word models
- "*quarter* is common in both business and sports"
- four-word sequences are likely to be more category-specific
- N-gram word model is a markov chain which considers the n-1 previous words when evaluating the probability of the current word.
- $P(w_j|w_{1:j-1})=P(w_j|w_{j-n+1:j-1})$
- $P(w_{1:N})=\prod_{j=1}^NP(w_j|w_{j-n+1:j-1})$
- great for
	- classifying newspaper sections
	- spam detection
	- sentiment analysis
	- author attribution
- Other n-gram models
	- character-level model
		- classification of unknown words
		- languages that run words together (Danish and German)
		- language identification
	- skip-gram model
		- count words near each other
		- skip a word between them
		- helps deal with conjugation
### smoothing n-gram models
- high frequency n-grams have low variance
- low frequency n-grams have high variance
- models will perform better if they can smooth out that variance
- evaluating out-of-vocabulary words will otherwise cause $P(w_{1:N})=0$
- solutions
	- using markup as a solution
		- replace unknown words with a token `<unk>`
		- replace email addresses with `<email>`
		- use `<s>` to denote the start and stop of a text
		- "what are the previous N words?" queries at the beginning of a text will be filled with `<s>` to avoid out-of-bounds errors.
	- use a backoff model
		- linear interpolation smoothing is an example
### word representations
- dictionaries
- WordNet
	- open-source machine readable dictionary
	- can be used to distinguish nouns from verbs
### Part-of-speech (POS) tagging
- AKA lexical category
- AKA tag (noun, verb, adj)
- HMMs are commonly used for tagging
	- evidence is the sequence of words $W_{1:N}$
	- hidden states are the lexical categories $C_{1:N}$
	- use the **Viterbi algorithm** to find the most probable sequence of tags

![[Pasted image 20240330163932.png]]

### Model Types
- Naive Bayes and Hidden Markov models are **generative models**.
	- They learn a joint probability distribution $P(W,C)$
	- They can generate a random sentence by sampling from that joint distribution to generate sentences one word at a time.
- Logistic regression is a **discriminative model**
	- It learns a conditional probability distribution $P(C|W)$
	- It can assign categories given a sequence of words
	- cannot generate random sentences
- discriminative models tend to have a lower error rate
	- they model the intended output directly
	- they make it easier for an analyst to create additional features
- generative models tend to converge more quickly
	- preferred when the available training time is short
	- preferred when there is limited training data
	- preferred when the goal is to build a generative model

### Comparing Language Models
![[Pasted image 20240331153912.png]]

> There is a limit to n-gram models, as n increases, they produce fluent language which reproduces passages from their training data verbatim.

> GPT-2 is a **transformer model.**

## 23.2 Grammar
- A grammar is a set of rules that define the tree structure of allowable phrases
- A language is the set of sentences that follow those rules
- Natural language
	- does not have a hard boundary between allowable and unallowable sentences
	- do not have a single definitive tree structure for each sentence
- meta-structures
	- **syntactic categories**
	- **phrase structure**
	- **semantics**

![[Pasted image 20240331154812.png]]

## 23.3 Parsing
- the process of analyzing a string of words to uncover its phrase structure, according to the rules of a grammar.
- It's a "search" for a valid parse tree whose leaves are the words of the string.

(skipped)

## 23.4 Augmented Grammars
(skipped)

## 23.5 Complications of Real Natural Language
- quantification
- quasi logical form
- pragmatics
- indexicals
- speech act
- long-distance dependencies
- time and tense
- ambiguity
	- lexical ambiguity
	- semantic ambiguity
- metonymy
- metaphor
- disambiguation
	- world model
	- mental model
	- language model
	- acoustic model

## 23.6 Natural Language Tasks
- speech recognition
- text-to-speech
- machine translation
- information extraction
- question answering
