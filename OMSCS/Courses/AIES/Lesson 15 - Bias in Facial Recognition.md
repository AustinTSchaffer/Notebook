---
tags: OMSCS, AIES
---
# Lesson 15 - Bias in Facial Recognition

## Issues with Facial Recognition Algorithms
![[Pasted image 20230704164831.png]]

- Kairos: Company built around facial recognition technology

![[Pasted image 20230704165107.png]]

![[Pasted image 20230704165145.png]]

## Bias in Facial Recognition
![[Pasted image 20230704165301.png]]

- ACLU used an 80% confidence threshold, the default
- Amazon fired back saying that they should have used a 99% confidence threshold
- Who's to say that some other incompetent implementer of the technology understands the nuances behind confidence thresholds?

![[Pasted image 20230704165531.png]]

`and there it is.gif`

![[Pasted image 20230704165635.png]]

![[Pasted image 20230704165652.png]]

- The dataset used to train facial recognition software reflects the biases of our society's demographic makeup.
- HOWEVER, when these models are used by law enforcement, the demographics of people who are being arrested do not match society's overall demographic makeup.
- This causes the AI to be more likely to erroneously fail.
- Conclusion, it's not enough for a model's training data to match the current demographic breakdowns, especially if the model is to be deployed in an environment which does not match that demographic makeup.

Links
- https://www.nytimes.com/2018/07/26/technology/amazon-aclu-facial-recognition-congress.html
- https://www.telegraph.co.uk/news/2018/05/05/police-defend-facial-recognition-technology-wrongly-identified/
- http://gendershades.org/overview.html
- https://www.perpetuallineup.org/

## Why does this happen?
![[Pasted image 20230704170033.png]]

![[Pasted image 20230704170120.png]]

![[Pasted image 20230704170216.png]]

![[Pasted image 20230704170255.png]]

![[Pasted image 20230704170309.png]]

Links
- http://biometrics.cse.msu.edu/Publications/Face/HanJain_UnconstrainedAgeGenderRaceEstimation_MSUTechReport2014.pdf
- https://techcrunch.com/2017/04/28/someone-scraped-40000-tinder-selfies-to-make-a-facial-dataset-for-ai-experiments/
- https://www.theverge.com/2017/8/22/16180080/transgender-youtubers-ai-facial-recognition-dataset
- https://arxiv.org/abs/1712.00193
- https://www.wired.com/story/how-coders-are-fighting-bias-in-facial-recognition-software/
- https://pypi.org/project/opencv-python/
- https://pypi.org/project/face_recognition/
