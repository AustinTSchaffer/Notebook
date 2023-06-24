---
tags: Inferentuial, Statistics, OMSCS, AIES
---
# Lesson 09 - Inferential Statistics & Sampling Bias

## Introduction
> There are 2 kinds of statistics, the kind you look up, and the kind you make up.

![[Pasted image 20230624093150.png]]

**Chain of Reasoning for Inferential Statistics**
- Numerical indications of how likely it is that a given event will occur (**General Definition**)
- **Statistical Probability**: The odds that what we observed in the sample did not occur because of errors (random and/or systematic)
- In other words, the probability associated with a statistic is the **level of confidence** we have that the sample group we measured actually represents the total population

![[Pasted image 20230624093325.png]]

Common Mistake: Not all samples will lead to good predictions about an entire population.
- How tall are college students? Randomly select students from one dorm. Oops, you accidentally selected the dorm which contained all of the college's basketball students, biasing the result.

## Warm Up Exercise
![[Pasted image 20230624093636.png]]

- Faculty might be overwhelmingly Brazilian
- The "population" is faculty, not the entire campus

![[Pasted image 20230624093802.png]]

![[Pasted image 20230624093835.png]]

- Aerospace engineering has an 80/20 gender mix.
- The statement is true, but misleads the reader as to what the survey was asking.

## Simpson's Paradox
- A phenomenon in probability and statistics in which a trend appears in several different groups of data, but disappears or reverses when these groups are combined.

![[Pasted image 20230624094103.png]]

![[Pasted image 20230624094120.png]]

- UCB was admitting prospective students at different rates, based on gender
- Men were overwhelmingly applying to a department with a high acceptance rate.
- A roughly equal share of men and women were applying to a department with a low acceptance rate.
- Across most departments, the acceptance rate for women was near to the acceptance rate for men.

## Biased Sampling
- We want to estimate the mean weight of all women aged 15-44 living in Atlanta. Suppose there are 50k women in this population. Suppose the true mean weight is 61.7kg.
- We select a sample of 200, interview them, ask their weight.
- The sample mean weight is 59.4kg.

![[Pasted image 20230624094719.png]]

![[Pasted image 20230624094813.png]]

![[Pasted image 20230624094844.png]]

### Area Bias
Introduced by conducting the study in a specific area that does not include a representative sampling of the population being studied

> Ex: Surveying the height of the students at a college and collecting the sample from a dorm which contains unusually tall students.
>
> Ex: Surveying the number of people who run in a city, but conducting the survey at the entrance to a running trail.

### Selection Bias
introduced by the selection of individuals, groups, or data for analysis in such a way that proper randomization is not achieved. This ensures that the sample obtained is not representative of the population intended to be analyzed.

> Ex: Survey to determine the absolute best job in the world, but sampling professionals who are all professors.

### Self-Selection Bias
A participant's decision to participate may be correlated with traits that affect the study, making the participants a non-representative sample. Arises in any situation in which individuals select themselves into a group, causing a biased sample with non-probability sampling.

> Ex: Set up a booth in a shopping center to ask people about their grooming habits. Fewer people are going to walk up and tell on themselves.
>
> Ex: Survey on underage drinking.

### Leading Question Bias
A leading question biases respondents by giving them a clue to the desired answer or leads respondents to answer a question a certain way, resulting in the tendency to respondents to agree with the direction of the leading question.

> Ex: Don't you think that CS GRAs are paid too little? (a) Yes they should earn more (b) No they should not earn more (c) No opinion.
>
> Ex: (Alternative phrasing) Do you think that CS GRAs should earn X compared to Engineering GRAs (a) More (b) Less (c) The Same (d) No Opinion

### Social Desirability Bias
A type of response bias that is the tendency of respondents to answer question in a manner that will be viewed favorably by others.

> Ex: Do you brush your teeth in the morning? Do you brush your teeth every morning? Did you brush your teeth _this_ morning?
>
> Ex: Do you believe that female computer scientists should earn the same as male computer scientists? (vs) Can I record this? (same question)

## Biased Sampling Example

![[Pasted image 20230624100037.png]]

- A. High Variability, High Bias
- B. Low Variability, Low Bias
- C. High Variability, Low Bias
- D. Low Variability, High Bias

Assuming that the arrow on each plot is the true mean, Graph B potentially had the best sampling, assuming a perfectly normal distribution in the population for the metric being surveyed, which may not be true. Graph C may better represent the population. More studies should be done.

## Types of Randomized Sampling
- Randomization can reduce issues with sampling bias
- Randomizing makes sure that one the average the sample looks like the rest of the population
- Randomizing enables us to make rigorous probabilistic statements concerning possible error in the sample
- Randomization Methods
	- Random Sampling
	- Simple Random Sampling

### Random Sampling
![[Pasted image 20230624100639.png]]

- Requires that the entire population is indexed.

### Systematic Sampling
- All data is sequentially numbered.
- Every nth piece of data is chosen.
- **Does each member of the population have an equal probability of being in the sample? Is there bias in the order of the identifiers?**

### Systemic Random Sampling
- Sometimes we draw a sample by selecting individuals systematically
- For example, start the systematic selection from a randomly selected individual. Then survey every 10th person.
- **Does each member of the population have an equal chance of being in the sample?**

![[Pasted image 20230624100812.png]]

### Stratified Random Sampling
- Data is divided into subgroups (strata)
- Strata are based on specific characteristics
- Randomly sample within each strata.
- **Does each member of the population have an equal probability of being in the sample?**

![[Pasted image 20230624100950.png]]

### Review
![[Pasted image 20230624101213.png]]

### Cluster Random Sampling
- Sometimes stratifying isn't practical and simple random sampling is difficult.
- Splitting the population into similar parts or clusters might be more practical.
- Each cluster should be a miniature version of the entire population.
- Then we can select a few clusters are random, and select a simple random sample from each chosen cluster
- If a cluster is fairly representative of the full population, cluster random sapling will give an unbiased sample

### Non-Probability Sampling
![[Pasted image 20230624101814.png]]

**There is no true measure for the bias for data collected on internet users.**

## Sampling Bias Example Experiments
![[Pasted image 20230624101938.png]]

- Overestimated
- Only looked at the smoking parking lot
- Sampling bias

![[Pasted image 20230624101950.png]]

- underestimated
- social desirability bias - students are interviewed IN FRONT OF THEIR PARENTS.

![[Pasted image 20230624102011.png]]

- Simpson's Paradox
- Teenage hangout might be more representative. Might have been overestimate.
- Principal's selection might have been "model students". Might have been underestimate
- No guarantee that averaging the 2 rates results in true mean.

![[Pasted image 20230624102623.png]]

- Study was opt-in.
- Self-selection bias

![[Pasted image 20230624102724.png]]

- Social desirability bias
- self-selection bias
- Area bias, schools are not far apart

