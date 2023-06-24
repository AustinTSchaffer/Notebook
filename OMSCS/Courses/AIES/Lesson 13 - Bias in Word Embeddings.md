---
tags: OMSCS, AIES
---
# Lesson 13 - Bias in Word Embeddings

How to learn word2vec embeddings
- Start with N random 300-dimension vectors as initial embeddings
- Using a machine learning classifier
	- take a corpus and take pairs of words that co-occur as positive examples
	- take pairs of words that don't co-occur as negative examples
	- train the classifier to distinguish these by slowly adjusting all the embeddings to improve the classifier performance
	- throw away the classifier code and keep the embeddings

![[Pasted image 20230614213731.png]]

## Why Does this Happen? (Word Embeddings)
![[Pasted image 20230614214121.png]]

Bias in Embeddings
- Cultural Biases
- Biased Framings of Women
- Ethnic Stereotypes

- African-American names are associated with unpleasant words (more than European-American names)
- Male names are associated more with career words
- Female names are associated more with family words
- Competence adjectives are biased towards men
	- Smart, wise, brilliant, resourceful, etc

![[Pasted image 20230614214341.png]]

![[Pasted image 20230614214355.png]]

![[Pasted image 20230614214409.png]]

![[Pasted image 20230614214413.png]]

![[Pasted image 20230614214524.png]]

