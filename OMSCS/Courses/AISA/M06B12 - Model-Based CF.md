---
tags: OMSCS, AISA
---
# M06B12 - Model-Based CF

Required reading: [[Collaborative Filtering beyond the User-Item Matrix.pdf]]

## Overview of Memory-Based CF

![[Pasted image 20230215213522.png]]

![[Pasted image 20230215213736.png]]

![[Pasted image 20230215213745.png]]

## Model-Based CF Approaches
- based on an offline pre-processing or "model-learning" phase
- at run-time, only the learned model is used to make predictions
- models are updated / re-trained periodically
- large variety of techniques used
- model-building and updated can be computationally expensive

![[Pasted image 20230215214002.png]]

### Approaches
- matrix factorization techniques, statistics
- Association rule mining
- probabilistic models
- Deep Neural Network models

## Matrix Factorization Approach
![[Pasted image 20230215214129.png]]

![[Pasted image 20230215230052.png]]

TL;DR: Basically the goal is to condense the data as much as possible into a simplified representation. The example offered was converting a user's discrete movie scores into a breakdown that shows how the user feels about each movie genre, which makes it easier for the recommendation engine to figure out what kinds of future movies to recommend to the user.

![[Pasted image 20230215233529.png]]

![[Pasted image 20230215234328.png]]

![[Pasted image 20230215234335.png]]

![[Pasted image 20230215234353.png]]

![[Pasted image 20230215234628.png]]

## Accuracy Problems with CF
- Cold Start: hard to recommend items that have no user ratings or insufficient number of other user ratings in the system
- First Rater: Cannot recommend an item that has not been previously rated
- Sparsity: If the user/ratings matrix is spare
	- hard to find users that have rated the same items
	- it is also hard to find items that have been rated by the same set of users
	- Population Bias: Cannot recommend unpopular items to someone with unique tastes

Solutions
- Recognize that these systems depend on loads of high-quality data in order to work properly. Maybe your app wasn't designed with recommendation engines in mind. Get more good data, get more better analytics.
- on-the-fly preference prediction.
- Force users to rate a set of items.
- Content-based recommendation. Finds similar items based on user interactions and content features.
- Implicit ratings
	- clicks
	- page views
	- time spent on page
	- demo downloads
- Use better algorithms

## Uses for CF
- Many items
- Many ratings
- Many more users than items recommended
- Users rate multiple items
- For each user of the community, there are other users with common needs or tastes
- Item evaluation requires personal taste
- Item persists
- Taste persists
- Items are homogeneous

## Evaluation Metrics
- Mean Absolute Error (MAE): measures average of the absolute difference among predicted ratings and true values.

![[Pasted image 20230216000811.png]]

- Root Mean Squared Error (RMSE): It emphasizes the contributions of the absolute errors between the predictions and real values

![[Pasted image 20230216000919.png]]

- Precision: computes the rate of the provided recommendations that are pertinent

![[Pasted image 20230216001052.png]]

- Recall: computes the rate of recommendations that are provided

![[Pasted image 20230216001108.png]]

## Ideas and Solutions
Course Project Ideas

![[Pasted image 20230216001141.png]]