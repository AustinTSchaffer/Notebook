---
tags: OMSCS, AIES, ML
---
# Lesson 16 - AI and ML Techniques - Predictive Algorithms

## What are predictive algorithms?
![[Pasted image 20230705203404.png]]

Amazon used predictive algorithms to determine where to put same-day delivery centers, which excluded low income neighborhoods.

![[Pasted image 20230705203416.png]]

![[Pasted image 20230705211244.png]]

![[Pasted image 20230705211315.png]]

- Classification
- Regression
- Clustering

![[Pasted image 20230705211423.png]]

### Classification
- Supervised Learning
- New data is classified based on training set

### Prediction
- Models continuous valued functions (predicts unknown/missing values)

![[Pasted image 20230705211443.png]]

![[Pasted image 20230705211601.png]]

![[Pasted image 20230705211609.png]]

Issues
- incomplete data
- missing important attributes
- missing hidden correlations between records

![[Pasted image 20230705211702.png]]

![[Pasted image 20230705212608.png]]

Important metrics for predictive models
- Precision
- Recall / Sensitivity
- Specificity
- Speed and scalability
- Interpretability

![[Pasted image 20230705214550.png]]

- Always have a test set when training models. **ALWAYS**

## Predictive Algorithm Examples
![[Pasted image 20230705215003.png]]

![[Pasted image 20230705215020.png]]

![[Pasted image 20230705215112.png]]

![[Pasted image 20230705215128.png]]

![[Pasted image 20230705215137.png]]

## Learning Methods
![[Pasted image 20230705215216.png]]

- Supervised Learning
	- Depends on labeled data
	- Regression
		- Linear Regression
		- Decision Tree
		- Random Forest
	- Classification
		- Logistic Regression
		- Naive Bayes
		- Decision Tree
		- Random Forest
		- Neural Networks / Deep NN
- Unsupervised Learning
	- Finds hidden / obscure connections between data points
	- Clustering
		- K-means Clustering

![[Pasted image 20230705215431.png]]

## Clustering
![[Pasted image 20230705215541.png]]

![[Pasted image 20230705215608.png]]

![[Pasted image 20230705220217.png]]

![[Pasted image 20230705220240.png]]

![[Pasted image 20230705220314.png]]

## Regression
![[Pasted image 20230705220415.png]]

![[Pasted image 20230705220525.png]]

![[Pasted image 20230705220701.png]]

![[Pasted image 20230705220745.png]]

## Decision Tree
![[Pasted image 20230705220851.png]]

![[Pasted image 20230705220902.png]]

![[Pasted image 20230705220931.png]]

![[Pasted image 20230705221234.png]]

## Regression Algorithm Examples Appendix

### Linear Regression
```python
x_train,x_test, y_train, y_test = train_test_split(
	data['x'],
	data['y'],
	test_size=0.3,
	random_state=1,
)
regr = LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

r2_score = 'R2 score: %f' % r2_score(y_test, y_pred)
intercept = 'Intercept: %f' % regr.intercept_
coefficients 'Coefficients: %s' % str(regr.coef_)
```

### How to find the best regression line?

Here are some methods which check for error:

- Sum of all errors (∑error)
- Sum of absolute value of all errors (∑|error|)
- Sum of square of all errors (∑error^2)

![[Pasted image 20230705221519.png]]

### Binary Classification Example

**Diabetes Data Set**
- Detect Diabetes Disease based on analysis
- Dataset Attributes:
	1. Number of times pregnant
	2. Plasma
	3. Diastolic blood pressure (mm Hg)
	4. Triceps skin fold thickness (mm)
	5. 2-Hour serum insulin (mu U/ml)
	6. Body mass index
	7. Diabetes pedigree function
	8. Age (years)
	9. Class variable (0 or 1)

### K-Means Clustering
![[Pasted image 20230705221720.png]]

