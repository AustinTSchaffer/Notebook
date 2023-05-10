# Running a Kaggle Competition Team
*Insights and Lessons from BirdCLEF with Data Science @ Georgia Tech*  

*by Anthony Miyaguchi*

## Links
- https://github.com/dsgt-birdclef/birdclef-2022
- https://www.kaggle.com/code/acmiyaguchi/motif-join-and-embedding/notebook
- https://arxiv.org/abs/2206.04805

## What is Kaggle?
- A platform for outsourcing data science through competitions that have cash prizes.
- Kaggle got Anthony into Graduate School. "Web Traffic Time Series Forecasting"

## Why Kaggle?
- good start to a research project

## BirdCLEF 2022
- identify bird calls in soundscapes
- built a team of 5 people from DS@GT (DS club at GT)
- 3 masters students and 2 undergraduates
- Technical approach
	- Motif Mining with SiMPLe-Fast. finds all pairs similarity in a time-series.
	- Spatial Embedding with Tile2Vec. 2 points in the high dimensional space that are close together should also be close together in the embedded space.
	- Unsupervised Representation Learning via Triplet Loss
	- Have to borrow techniques from signal processing
- Not going to have an equal representation of birds
- The data sets aren't labelled

Results
- Won the best working notes award
- had a unique approach
- Bottom 10%
- Won $2500 in GCP credits

Takeaways
- Building a team is great!
- 6 weeks is not enough time

## BirdCLEF 2023
- Luigi - DAG workflow tool
- MixIT - audio separation tool
- Ongoing!

