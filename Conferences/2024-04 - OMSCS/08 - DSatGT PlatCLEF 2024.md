---
tags:
---
# 08 - DS@GT PlatCLEF 2024
https://omscs.gatech.edu/dsgt-plantclef-2024-plant-biodiversity-identification-using-deep-learning

> Plant Biodiversity Identification Using Deep Learning
>
> By Murilo Gustineli

- Data Scientist
- 5 semesters of OMSCS
- From Brazil
- Got involved with project by meeting Anthony at OMSCS Conf 2023
	- [[07 - Running a Kaggle Competition Team]]
	- BirdCLEF competition

## About this Talk
- intersection of 
	- Information retrieval
	- deep learning
	- research
- PlantCLEF
- DSatGT Kaggle Team
- Competition overview
- solution overview

## PlantCLEF
- pronounced "clay"
- It's french
- identifying plants in images
- multi-label classification problem
- training data has 8k species, 1.4M images, 281GB
- training metadata and a pretrained ViT model (vision transformer)
- main challenges
	- test data is multi-label
	- training data is single-label images of individual plants
	- evaluation is based on ability to predict all plant species in image
- intra-class variation
	- multiscale
	- color
	- viewpoint
	- illumination
	- background
	- growth stage

## DS@GT Kaggle Team
- 11 teams of ~3 each
- some people in multiple teams
- mix of on-campus, OMSCS, and OMSA students

## Tech Stack
- GCP - cloud provider
- Apache Spark - Distributed data processing
- Petastorm - Distributed data loading
- PyTorch - DL training
- Weights and Biases

![[PXL_20240501_180604689.MP.jpg]]

Crop/resize reduced dataset size from 300GB to 15GB.

## DINOv2
- self-supervised vision transformer
- extracts knowledge from images with the need for labeled data
- enables multi-modality classification

## Preprocessing Pipeline
- Discrete Cosine Transform (DCT)
- downscale image
- train model on embeddings

## Future Work
- Collage pipeline
	- collaborative filtering - using LSH, ANN, ALS
		- Locality Sensitive Hashing
		- Approx-Nearest Neighbor Search
		- Alternating Least Squares
	- recommender system
- Increase DCT dimensionality from 64 to 1024 features
	- minimize information loss
- Use the CLS token (first token) from DINOv2 for classification
	- capture something something

