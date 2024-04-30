---
tags:
---
# 03 - MuseChat - A Conversational Music Recommendation System for Videos
> By Zhikang Dong

https://omscs.gatech.edu/musechat-conversational-music-recommendation-system-videos

> Zhikang Dong is a Ph.D. student at Stony Brook University. His research topics include Multimodal Learning, Large Language Model and AI for science. He received his master's degree at Columbia University in New York City. He has published papers at prestigious conferences such as CVPR, NeurIPS, WACV, and IEEE conferences. During his spare time, he loves basketball, Japanese anime, and video games.

- Paper: https://arxiv.org/abs/2310.06282
- DOI: [https://doi.org/10.48550/arXiv.2310.06282](https://doi.org/10.48550/arXiv.2310.06282)
## Introduction
- what is a music rec system? why do we need it?
	- enhanced viewer experience
	- personalization
	- time efficiency
- limitations of current music recommendation system
	- individual user prefs are neglected
	- over-reliance on historical prefs may not align with current video content
	- lack of explicit explanations for recommendations, reducing their persuasiveness
- interacting with the system through conversation could be a highly efficient and convenient method to guide the recommendation results
- what is a conversational music rec system?
	- user can interacti with the recommendation engine, refine recommendations by providing textual prefs / context
	- conversational rec system provides clear explanations for its recommendations, increasing user understanding and trust
- core challenges
	- datasets
	- joint modality learning
	- prediction reasoning

## MuseChat
- introduce a novel dataset tailored for dialogue-driven music recommendations and reasoning within the context of videos
- present a tri-model arch designed for music-video matching
- augment something something

## Datasets
- YouTube-8M
	- large labeled video dataset
	- offers thousands of labels that span a broad array of categories
- Music-Video Pretrained (MVP) model
- Prompt Constructor (GPT-3.5)
	- incorporates 5 music tags drawn from 2 tagging systems (MTT, MSD)
	- also includes metadata, song/artist/album/etc

## Methodology
- music rec module
	- either process video input
	- use a composite of video / user prompt / previously suggested music
- sentence generator module
	- linear projection layer is used to align music embeddings with text tokens
	- LoRA (Low-Rank Adaptation)
- extract embedding from music, video, and text
- transfer learning
- OMSCS Deep Learning course was very influential

## Results
- correctness - music and artist identification
- musicality - description of music traits
- clarity - response understandability and coherence

https://dongzhikang.github.io/musechat/

## Takeaway
We're about to watch the glorious demise of short-form content, thanks to an endless flood of AI-generated content.