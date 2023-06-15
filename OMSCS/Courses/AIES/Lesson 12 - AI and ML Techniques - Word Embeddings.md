---
tags: OMSCS, AIES
---
# Lesson 12 - AI and ML Techniques - Word Embeddings

## Word Embedding (NLP)
- Word embeddings are a set of techniques in NLP for identifying similarities between words in a corpus by using some type of model to predict the co-occurence of words within a small chunk of text.
- Word embeddings transform human language meaningfully into a numerical form. This allows computers to understand the nuances implicitly encoded into our languages.

![[Pasted image 20230614201139.png]]

![[Pasted image 20230614201350.png]]

## Word Similarity and Relatedness
- Representing words has become a convenient way to compute similarities
- Relatedness measures the semantic similarity between words
- Car is similar to truck, but is related to driving and highways
- How similar is pizza to pasta?
- How related is pizza to Italy?
- Vectorization is the process of converting text to numbers. This conversion helps us to measure the similarity between words
- A vector space model is an algebraic model for representing text as a vector of identifiers in which semantically similar words are mapped to proximate points in geometric space

### Document Occurrence
Assign identifiers corresponding to the count of words in each document (from a cluster of documents) in which the word occurs.

![[Pasted image 20230614202420.png]]

### Word Context
Quantify co-occurrence of terms in a corpus by constructing a co-occurrence matrix which captures the number of times a term appears in the context of another term.

- Chocolate is the best dessert in the world
- GT is the best university in the world
- The world runs on chocolate

![[Pasted image 20230614202605.png]]

### Example
![[Pasted image 20230614202751.png]]

![[Pasted image 20230614202801.png]]

![[Pasted image 20230614202837.png]]

## Cosine Similarity & Word Analogy
We can use cosine similarity to compute the similarity between two word vectors. However, this notion of similarity depends on what vector representation is selected to represent the words found in the corpus

![[Pasted image 20230614203122.png]]

![[Pasted image 20230614203128.png]]

![[Pasted image 20230614203225.png]]

- word analogy problems have become one of the standard tools for evaluating context-based word vectors
- The task consists of questions like "a is to b as c is to \_\_\_"
- To solve the analogy problem, we need to find the word vector that is most similar to the result vector of $c+b-a$.
- Example: $king + woman - man \approx X$

## Word Embeddings (`word2vec`)
- Stores each word as a point in space, where it is represented by a vector of a fixed number of dimensions (generally 300)
- Unsupervised, built just by reading a huge corpus of data
- For example, "chocolate" might be represented as `[1, 0, 1, 1, 0, 2]`
- As discussed before, dimensions are projections along different axes.

![[Pasted image 20230614204147.png]]

Vector Space Models
- One representation: Predict the context of a given word by learning probabilities of co-occurrence from a corpus (e.g. skip-gram neural network models, `word2vec`)
- On theory, words that share similar contexts tend to have similar meanings. As such, instead of counting co-occurrences directly, we should be able to generate word vectors that can predict the context of a word based on its surrounding words by learning from a corpus of data.

![[Pasted image 20230614205003.png]]

- Notes
	- possible to optimize word2vec by using different corpuses (e.g. wikipedia or Twitter)

![[Pasted image 20230614205045.png]]

![[Pasted image 20230614205101.png]]

![[Pasted image 20230614205222.png]]

![[Pasted image 20230614205354.png]]

![[Pasted image 20230614205408.png]]

![[Pasted image 20230614205456.png]]

![[Pasted image 20230614205527.png]]

![[Pasted image 20230614205605.png]]

![[Pasted image 20230614205641.png]]

- Notes
	- Important parameters: Window size, iterations
	- Useful python libraries: nltk, gensim

