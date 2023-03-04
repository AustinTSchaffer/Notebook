---
tags: OMSCS, AISA
---
# Module 6 - Block 11 - Collaborative Recommendations

## Recommendation Problem
- Set of users $U$
- Set of items $T$ to be recommended to the users
- Let $p$ be a utility function that measures the usefulness of the item $t$ $(\in T)$ to user $u$ $(\in U)$
	- $p:U*T \rightarrow R$, where $R$ is a totally ordered set (e.g. non-negative integers or real numbers in a range.)

Objective
- Learn $p$ based on past data.
- Use $p$ to predict the utility value of each item $t$ to each user $u$

Prediction
- Predict the rating score that a user is likely to give an item that they have not seen or used before
- Rating an unseen movie for example
- Predict a ranked list of items the user might rate highly

2 types of CF recommendation systems
- user-based CF
- item-based CF

Collaborative filtering (CF) based recommendation algorithms
- K-nearest neighbor / K-means clustering
- association rules
- matrix factorization

## User-Based Collaborative Filtering (CF)
Input: Matrix of given user-item ratings

Output types:
- Numerical prediction indicating to what degree the current user will like or dislike a certain item
- A top-N list of recommended items

![[Pasted image 20230215200718.png]]

Basic ideas
- Find a set of users who liked the same items as Alice in the past and who have rated item $i$
- If users had similar tastes in the past, they will have similar tastes in the future
- User prefs remain stable and consistent over time

![[Pasted image 20230215201144.png]]

## Vector Similarity
### Pearson product-moment correlation coefficient (PPMCC/PCC)
- measure of the linear correlation (degree of linear dependence) between 2 variables $X$ and $Y$, represented by a value V where $-1 \le V \le 1$ 
- 1 is a total positive correlation
- 0 is no correlation
- -1 is total negative correlation

- Measure the rating similarity (linear dependency) between ratings for active user (a) and another user (b). 
$$
c_{a,u}=\frac{covar(r_a,r_u)}{\sigma_{r_a}\sigma_{r_u}}
$$
- $r_a$ and $r_u$ are the ratings vectors for the $m$ items rated by users $a$ and $u$ respectively
$$
covar(r_a,r_u)=\frac{\sum^{m}_{i=1}(r_{a,i}-\bar{r_a})(r_{u,i}-\bar{r_u})}{m}
$$
- $r_{i,j}$ is user $i$'s rating for item $j$
- $\bar{r_x}$ is used to quantify the variance for a set of ratings
$$
\bar{r_x}=\frac{\sum^{m}_{i=1}r_{x,i}}{m}
$$
- $\sigma_{r_x}$ is
$$
\sigma_{r_x}=\sqrt{\frac{\sum^{m}_{i=1}(r_{x,i-\bar{r_x}})^2}{m}}
$$

### Measuring User Similarity
- A popular similarity measure in user-based CF: pearson correlation
- possible similarity values between -1 and 1
- symbols
	- users: $a$, $b$
	- ratings of user $a$ for item $p$: $r_{a,p}$
	- set of items rated by both $a$ and $b$: $P$

$$
sim(a, b)=\frac{\sum_{p \in P}(r_{a,p}-\bar{r_a})(r_{b,p}-\bar{r_b})}{\sqrt{\sum_{p \in P}(r_{a,p}-\bar{r_a})^2}\sqrt{\sum_{p \in P}(r_{b,p}-\bar{r_b})^2}}
$$

![[Pasted image 20230215203408.png]]

### Making Predictions
A common prediction function:
$$
pred(a,p)=\bar{r_a}+\frac{\sum_{b \in N}(sim(a,b)(r_{b,p}-\bar{r_b}))}{\sum_{b \in N}sim(a,b)}
$$
- calc whether the neighbors ratings for the unseen item $i$ are higher or lower than their average
- combine the rating differences.
- Use the similarity with $a$ as a weight
- add/subtract the neighbors bias from active user's average and use this as a prediction

## K-Nearest Neighbor Based Recommendation
- neighbor = similar user
- generate a prediction for an item by analyzing ratings for the item from users in the user's neighborhood
- neighbors are based on past ratings/views/purchases

### Significance Weighting
- important not to trust correlations based on very few co-rated items (example uses 50 as a threshold)
- include _significance weights_ ($s_{a,u}$) based on number of co-rated items $m$
$$
w_{a,u}=s_{a,u}c_{a,u}
$$
$$
\begin{equation}
	s_{a,u} = \begin{cases}
		1 & \text{if } m > 50 \\
		\frac{m}{50} & \text{if } m \le 50
     \end{cases}
\end{equation}
$$

## Improving Metrics/Prediction
- Not all neighbor ratings might be equally "valuable"
	- agreement on commonly liked items is not so valuable info
	- agreement on controversial items is valuable
	- maybe give more weight to items that have a higher variance
- Value of number of co-rated items
	- Use significance weighting by linearly reducing weight when the number of co-rated items is low
- Case amplification
	- Intuition: give more weight to "very similar" neighbors, i.e. when the similarity value is close to 1
- Neighborhood selection
	- use similarity threshold or fixed number of neighbors

## Item-Based Collaborative Filtering (CF)
- Pretty much the same except it focuses on the items instead of the users.
- Use similarity between items to make predictions
- Look for items that are similar to Item 5
- Take Alice's ratings for those items to predict the rating for item 5.
- "Item is represented by a vector of users"

### Cosine Similarity Measure
- Produces better results in item-to-item filtering
- Ratings are seen as vector in n-dimensional space
- Similarity is calculated based on the angle between vectors
- Pretty much all the math is the same but with symbols flipped around.
$$
sim(\overrightarrow{a},\overrightarrow{b})=\frac{\overrightarrow{a} \cdot \overrightarrow{b}}{|\overrightarrow{a}|*|\overrightarrow{b}|}
$$
- Adjusted cosine similarity
	- Take average user ratings into account
	- transform original ratings
	- $U$: set of users who have rated both items $a$ and $b$
$$
sim(\overrightarrow{a},\overrightarrow{b})=\frac{\sum_{u \in U}(r_{u,a}-\bar{r_u})(r_{u,b}-\bar{r_u})}{\sqrt{\sum_{u \in U}(r_{u,a}-\bar{r_u})^2}\sqrt{\sum_{u \in U}(r_{u,b}-\bar{r_u})^2}}
$$

### Making Predictions
- Common prediction function
$$
pred(a,p)=\bar{r_a}+\frac{\sum_{b \in N}(sim(a,b)(r_{b,p}-\bar{r_b}))}{\sum_{b \in N}sim(a,b)}
$$
- neighborhood size is typically limited to specific size
- Analysis of the MovieLens dataset indicates that "in most real-world situations, a neighborhood of 20 to 50 neighbors seems reasonable

## Recommendation Categorization
- User-User based
- Item-Item based
- Content-based recommendations
- Hybrid
	- combine collaborative and content-based

![[Pasted image 20230215211048.png]]

![[Pasted image 20230215211327.png]]

![[Pasted image 20230215211406.png]]

![[Pasted image 20230215211433.png]]

TL;DR: Netflix held a $1M AI/ML challenge to figure out a sensible algorithm for their website, which is a shame because they've since then systematically removed all of the content that would be worth recommending.

![[Pasted image 20230215211910.png]]

![[Pasted image 20230215212044.png]]