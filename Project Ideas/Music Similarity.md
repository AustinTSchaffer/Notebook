# Music Similarity

## Related notes
- [[AISA Course Project Ideas]]

## Inspiration
- https://dubolt.com/
- https://spotify-audio-analysis.glitch.me/analysis.html
- https://www.riffusion.com/
- Google's MusicLM
	- https://arxiv.org/abs/2301.11325
	- https://google-research.github.io/seanet/musiclm/examples/

## Issues
- no comprehensive training data set

## Papers
- https://www.spiedigitallibrary.org/conference-proceedings-of-spie/3299/0000/Perceptual-image-similarity-experiments/10.1117/12.320148.short?SSO=1
- https://openaccess.thecvf.com/content_cvpr_2014/html/Wang_Learning_Fine-grained_Image_2014_CVPR_paper.html
- https://www.sciencedirect.com/science/article/abs/pii/S0003347299914161
- https://link.springer.com/chapter/10.1007/978-3-642-11674-2_14

## Data Sources
- Spotify API

## Rough Algorithm
- Download the song's audio
- Determine song sections (Spotify API)
- Select some number of (fixed-width?) time chunks from the audio based on the song sections
- Generate spectrograms of the song sections
	- store these spectrograms in blob storage
	- store the metadata in a relational database, with links to the spectrogram blobs
- 

