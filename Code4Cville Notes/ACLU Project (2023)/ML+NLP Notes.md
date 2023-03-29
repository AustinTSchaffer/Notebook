---
tags: ML, NLP
---
# ML+NLP Notes
> If you checkout spacy, it does a lot of the work for you too

> this is all you need for what you're trying to do: [https://spacy.io/usage/linguistic-features](https://spacy.io/usage/linguistic-features)

Essentially our steps will look like:
- remove stop words/punctuation
- decide if you want lemmatization/stemming
- vectorize/tf-idf for ngrams and visuals.
- then your ML will look like usual..
	- take the vectors and create feature
	- take your labeled data
	- split into train/test
	- etc etc

> hardest part in NLP sometimes is the first few steps since they can significantly change the output

See also: [[Anubha's Quick ML Explainer]]