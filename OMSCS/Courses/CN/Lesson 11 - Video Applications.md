---
tags:
  - OMSCS
  - CN
---
# Lesson 11 - Video Applications
> First, we study VoIP which is the technology behind many popular applications. We study how audio is encoded in VoIP and also see the basic principles used in VoIP to maximize the QoS metrics. 

> We then look at how video is streamed and we learn the fundamentals in video compression techniques. Finally, we look at bitrate adaption, which is an optimization for better quality of video streaming. Bitrate adaption techniques were introduced given the diversity of devices that people use for video applications which may require different bitrate.

## Readings and Resources
- VoIP: A comprehensive survey on a promising technology  
[https://www.sciencedirect.com/science/article/abs/pii/S1389128609001200](https://www.sciencedirect.com/science/article/abs/pii/S1389128609001200)
- MPEG: A Video Compression Standard for Multimedia Application  
[https://web.stanford.edu/class/ee398a/handouts/papers/Gall%20-%20MPEG.pdf](https://web.stanford.edu/class/ee398a/handouts/papers/Gall%20-%20MPEG.pdf)
- The JPEG Compression standard  
[https://ieeexplore.ieee.org/document/125072](https://ieeexplore.ieee.org/document/125072)
- JPEG File Interchange Format  
[https://www.w3.org/Graphics/JPEG/jfif3.pdf](https://www.w3.org/Graphics/JPEG/jfif3.pdf)
- Watching Video over the Web: Part 1: Streaming Protocols  
[https://ieeexplore.ieee.org/document/5677508](https://ieeexplore.ieee.org/document/5677508)
- A Quest for an Internet Video: Quality-of-Experience Metric  
[https://www.cs.cmu.edu/~xia/resources/Documents/Balachandran-hotnets2012.pdf](https://www.cs.cmu.edu/~xia/resources/Documents/Balachandran-hotnets2012.pdf)
- Confused, Timid, and Unstable: Picking a Video Streaming Rate is Hard  
[https://dl.acm.org/doi/pdf/10.1145/2398776.2398800](https://dl.acm.org/doi/pdf/10.1145/2398776.2398800)

## Video and Audio Characteristics
- video has a high bit rate, generally between 100 kbps to over 3 Mbps
- there are techniques for **compressing** video, with varying levels of compression and video quality

| Type       | 24-30 fps     | 48-60 fps       |
| ---------- | ------------- | --------------- |
| 8K         | 80 - 160 Mbps | 120 to 240 Mbps |
| 2160p (4K) | 35–45 Mbps    | 53–68 Mbps      |
| 1440p (2K) | 16 Mbps       | 24 Mbps         |
| 1080p      | 8 Mbps        | 12 Mbps         |
| 720p       | 5 Mbps        | 7.5 Mbps        |
| 480p       | 2.5 Mbps      | 4 Mbps          |
| 360p       | 1 Mbps        | 1.5 Mbps        |

- Audio has a lower bit rate than video
- glitches in audio are generally more noticeable than glitches in video.
- video conferencing software generally prioritizes audio streams over video streams, allowing video streams to interrupt to preserve audio quality
- audio can also be compressed at varying quality levels

## Types of Multimedia Applications and Characteristics
The different kinds of multimedia applications can be organized into three major categories.
1. streaming **_stored_** audio and video, such video clips on Udacity for our OMSCS courses
2. streaming **live** audio and video, such as the graduation ceremony for GATech on graduation day.
3. **conversational** voice and video over IP, such as Skype

### 1. Stored Video
- stored video is streamed
	- the video starts playing as data is received
	- antithesis is waiting for the whole file
- the stream is interactive
	- pause, resume, fast forward, rewind
- the stream should have a continuous playout
	- it should play the same way it was recorded
	- no mid-stream freezing or hitching is desired
- generally stored on a CDN rather than in just one data center
- can also be implemented in a P2P model

### 2. Live Audio/Video
- very similar to streaming stored video or audio
- uses similar techniques to stored video/audio streaming
- here are generally **many simultaneous users**, sometimes in very different geographic locations
- They are **delay-sensitive**, but not as much as conversational voice and video applications are - generally, a ten second delay is ok

### 3. Conversational VoIP
> Voice over IP

- like phone service that goes over the Internet instead of through traditional circuit-switched telephony network.
- often involve three or more participants
- real-time and involve human users interacting, these applications are highly **delay-sensitive**.
- A ~400ms delay would be noticeable
- these applications are **loss-tolerant**.
- There are techniques that can conceal occasional glitches

## Voice over IP (VoIP)
- the Internet is “best effort” and makes no promises that a datagram will actually make it to its final destination
- datagrams arrive out of order, not at all, late, early
- 3 properties of VoIP which apply to other multimedia applications to varying degrees
	- encoding
	- signaling
	- Quality-of-Service (QoS)

### VoIP Encoding
- analog audio by nature is represented as a continuous wave
- digital data by nature is discrete
- Therefore, all digital representations of analog audio are only approximations. 
- audio is encoded by taking some number of samples per second (thousands), and rounding each sample’s value to a discrete number within a particular range.
- This “rounding” to a discrete number is called **quantization**.
- PCM (Pulse Code Modulation) is one technique used with speech
	- takes 8000 samples per second
	- each sample’s value is 8 bits
	- PCM with an audio CD takes 44,100 samples per second, with each sample value being 16 bits.
- The three major categories of encoding schemes are
	- narrowband
	- broadband
	- multimode (which can operate on either)
- the schemes come with different characteristics and tradeoffs.
- For VoIP, the the audio needs to be interpretable, but low bandwidth
- Audio is compressable, but this has tradeoffs.

### Signaling
- In traditional telephony, a signaling protocol takes care of how calls are set up and torn down.
- Signaling protocols are responsible for four major functions
	- User location - the caller locating where the callee is.
	- Session establishment - handling the callee accepting, rejecting, or redirecting a call.
	- Session negotiation  - the endpoints synchronizing with each other on a set of properties for the session.
	- Call participation management - handling endpoints joining or leaving an existing session. 
- VoIP also uses signaling protocols to perform the same functions.
- The SIP (Session Initiation Protocol) is just one example of a signaling protocol used in many VoIP applications.

### QoS for VoIP
- QoS metrics measure the quality of service. There are three major QoS metrics for VoIP:
	- end-to-end delay
	- jitter
	- packet loss

#### QoS for VoIP: End-to-End Delay
- "end-to-end delay", is the total delay "from mouth to ear."
- This includes delay from:
	- the time it takes to encode the audio (which we discussed earlier),
	- the time it takes to put it in packets, 
	- all the normal sources of network delay that network traffic encounters such as queueing delays, 
	- "playback delay," which comes from the receiver’s playback buffer (which is a mitigation technique for delay jitter, which we’ll be discussing next),
	- and decoding delay, which is the time it takes to reconstruct the signal.
- End-to-end delay is the accumulation of all of these sources of delay, and VoIP applications are sensitive to these delays.
	- In general, an end-to-end delay of below 150ms is not noticeable by human listeners.
	- A delay between 150ms and 400ms is noticeable, but considered acceptable, depending on the purpose of the VoIP call and the human users’ expectations
	- we might be more accepting of delays if we are calling a more remote region, for instance.
	- An end-to-end delay greater than 400ms starts becoming unacceptable, as people start accidentally talking over each other.
- VoIP applications frequently have delay thresholds, such as at 400ms, and discard any received packets with a delay greater than that threshold. Packets that are delayed by more than the threshold are effectively lost.

#### QoS for VoIP: Delay Jitter
- different voice packets can end up with different amounts of delay.
- ex. one voice packet may be delayed by 100ms, and another by 300ms.
- this phenomenon is called "jitter"
- jitter is problematic for VoIP, because it interferes with reconstructing the analog voice stream.
- With large jitter, we end up with more delayed packets that end up getting discarded, and that can lead to a gap in the audio.
- Too many dropped sequential packets can make the audio unintelligible.
- The human ear is pretty intolerant of audio gaps, but audio gaps should ideally be kept below 30ms. Depending on the type of voice codec used and other factors, audio gaps between 30 to 75ms can be acceptable.
- The main VoIP application mechanism for mitigating jitter is maintaining a buffer, called the “jitter buffer” or the “play-out buffer.”
- This mechanism helps to smooth out and hide the variation in delay between different received packets, by buffering them and playing them out for decoding at a steady rate.
- There’s a tradeoff here.
	- A longer jitter buffer reduces the number of packets that are discarded because they were received too late, but that adds to the end-to-end delay.
	- A shorter jitter buffer will not add to the end-to-end delay as much, but that can lead to more dropped packets, which reduces the speech quality.

#### QoS for VoIP: Packet Loss
- TCP vs UDP
	- TCP retransmits lost packets
	- However, packets are not useful after 400ms
	- If the sender resends lost packets, that will likely just waste bandwidth for both the sender and the receiver
	- Lost packets also results in a lowering of the senders transmission rate,  thanks to congestion control algorithms. This can result in the transmission rate becoming lower than the receiver's drain rate, meaning the receiver will run out of buffered audio.
	- VoIP protocols typically use UDP.
- VoIP packet loss
	- In VoIP, a packet is lost if it never arrives or if it arrives after its scheduled playout.
	- VoIP can tolerate loss rates of between 1 and 20 percent
	- This depends on the codec used and other factors
	- VoIP has 3 major methods for dealing with packet loss
		- Forward Error Correction (FEC)
		- Interleaving
		- Error concealment
##### Forward Error Correction (FEC)
- FEC works by transmitting redundant data alongside the main transmission
- allows the receiver to replace lost data with the redundant data
- 2 primary methods
	- The redundant data could be a copy of the original data, by breaking the audio into chunks and cleverly using exclusive OR (XOR) with _n_ previous chunks
	- The redundant data could also be a lower-quality audio stream transmitted alongside the original stream
- The more redundant data transmitted, the more bandwidth that is consumed.
- Some FEC techniques require the receiving end to receive more chunks before playing out the audio, increasing the playout delay.

![[Pasted image 20231118115922.png]]

##### Interleaving
- Interleaving does not transmit any redundant data
- Does not add extra bandwidth requirements or overhead
- works by mixing chunks of audio together, so that if one set of chunks is lost, the lost chunks aren't consecutive.
- Many smaller audio gaps are preferable to one large audio gap, as long as gaps are smaller than 30ms.
- Receiving side has to wait longer to receive consecutive chunks of audio before beginning playout, increasing overall latency.
- Limited usefulness for VoIP, but can have good performance for live streaming and streaming stored audio.

![[Pasted image 20231118120239.png]]

##### Concealment
- error concealment is basically "guessing" what the lost audio packet might be
- With small audio snippets, between 4ms and 40ms, there is some similarity between one audio snippet and the next
- This is effectively compression, except the network is the part of the algorithm that decides how much data to discard.
- Can be achieved by repeating previously un-dropped packets.
- Can be achieved by interpolating the gaps between un-dropped packets.
- There's probably AI-accelerated interpolation now.

## Live Streaming vs On Demand Streaming
- Various enabling technologies and trends have led to the development of consuming media content over the Internet.
	- bandwidth for both the core network and last-mile access links have increased tremendously
	- video compression technologies have become more efficient, enabling sufficient-quality moderate-bandwidth video streams.
	- the development of Digital Rights Management technologies has encouraged content providers to put their content on the Internet
- The types of content that is streamed over the Internet can be divided into two categories
	- Live
		- video content is created and delivered to the clients simultaneously
		- streaming of sports events, music concerts etc
	- On-demand
		- includes streaming stored video based on users’ convenience.
		- watching videos on Netflix, non-live videos on YouTube etc
- The constraints for streaming live and on-demand content differ slightly.
	- there is not a lot of room for pre-fetching content in the case of live streaming.
	- streaming live at large-scale and on-demand content are similar apart from a few details such as video encoding

![[Pasted image 20231118122112.png]]

At a high level
- The raw recorded content is typically at a high quality.
- It is then compressed using an encoding algorithm.
- This encoded content is then secured using DRM and hosted over a server. 
- Typically content providers have their own data centers such as Google or use third-party CDNs to replicate the content over multiple geographically distributed servers. This makes sure that the content can be delivered in a scalable manner.
- The end-users download the video content over the Internet.
- The downloaded video is decoded and rendered on the user’s screen.

### Video Compression
- Video compression reduces the size of the video by compressing it. The compression can be of two types
	- lossy: we can not recover the high quality video
	- loss-less: the original video can be recovered.
- lossy compression gives higher savings in terms of bandwidth and hence that is what is used by video compression algorithms these days. 
- The goal of a compression algorithm is to cut down data by removing "similar" information from the video while not compromising a lot with the video quality.
- A video is essentially a sequence of digital pictures, where each picture is a 2D sequence of pixels.
- An efficient compression can be achieved in two-ways
	- within an image
		- pixels that are nearby in a picture tend to be similar
		- spatial redundancy
		- JPEG is a compression format
	- across images
		- in a continuous scene, consecutive pictures are similar
		- temporal redundancy

- encode images as JPEGs
- transmit the first image as a JPEG (I-frame)
- transmit subsequent images by sending the frame-to-frame diff ("predicted" frame, aka P-frame)
- When the scene changes, transmit a new I-frame instead of sending a diff where all of the pixels are different.
- The sender will also send fresh I-frames periodically as well. This allows the receiver to more easily interact with the stream.
- All of the frames between 2 consecutive I-frames are called a Group of Pictures (GoP)
- There are also Bi-directional frame (B-frame), which is a function of past and future frames. 

![[Pasted image 20231118151521.png]]

![[Pasted image 20231118151505.png]]

![[Pasted image 20231118152448.png]]

![[Pasted image 20231118152636.png]]

## UDP vs TCP
- the video needs to be decoded at the client. This decoding might fail if some data is lost.
- If an I-frame is lost partially, the receiver may not be able to obtain the RGB matrices correctly. Also, the subsequent P-frames cannot be decoded. 
- Content providers ended up choosing TCP for video delivery as it provides reliability. An additional benefit of using TCP was that it already provides congestion control which is required for effectively sharing bandwidth over the Internet.
- Video conferencing applications may choose UDP instead for video streams. Old data is not useful for the receiving end.

## Why do we use HTTP?
![[Pasted image 20231118153114.png]]

- The original vision was to have specialized video servers that remembered the state of the clients.
- These servers would control the sending rate to the client.
- If the client paused the video, it would send a signal to the server and the server would stop sending video.
- All of the intelligence would be stored at a centralized point and the clients, which can be quite diverse, would have to do minimal amount of work.
- This would require content providers to buy specialized hardware.
- Another option was to use the already existing HTTP protocol.
	- the server is essentially stateless and the intelligence to download the video will be stored at the client.
	- A major advantage of this is that content providers could use the already existing CDN infrastructure.
	- Moreover, it also made bypassing middleboxes and firewalls easier as they already understood HTTP.

## Progressive Download vs Streaming
![[Pasted image 20231118153101.png]]

- all the intelligence to stream the video lies at the client-side.
- One way to stream the video would be to send an HTTP GET request for video, downloading the file
- The server will send the data as fast as possible, with the download rate limited only by the TCP rate control mechanisms.
- While quite simple, this has some disadvantages:
	1. Users often leave the video mid-way. Thus, downloading the entire file can lead to a waste of network resources. 
	2. The video content that has been downloaded but not played so far would have to be stored. The client will need to buffer the video in memory. Clients will run out of space for long and/or HD videos.
- instead the client tries to pace it.
	- This can be done by sending **byte-range** requests for part of the video instead of requesting the entire video.
	- Once the video content has been watched, it sends request for more content.
	- Ideally, this should be enough for streaming without stalls. 
- Note that the internet is "best effort", so some data might come quickly, some slowly.
- To account for these variations, client pre-fetches some video ahead and stores it in a **playout buffer.** The playout buffer is usually defined in terms of number of seconds of video that can be downloaded in advance or in terms of size in bytes.
- Once the video buffer becomes full, the client will wait for it to get depleted before asking for more content. Streaming in this manner typically has two states:
	- **Filling state**
		- This happens when the video buffer is empty and the client tries to fill it as soon as possible.
		- In the beginning of the playback, the client tries to download as fast as possible until the buffer becomes full.
	- **Steady state**
		- After the buffer has become full, the client waits for it to become lower than a threshold.
		- After which, the client sends a request for more content.
		- The steady state is characterized by ON-OFF patterns.

![[Pasted image 20231118153509.png]]

## Network and User Device Diversity
- Different displays require different quality settings (bitrate)
- Different networks can handle different throughputs
	- Fiber optic vs cable
	- Ethernet vs Wifi vs LTE/Cellular
- a single-bitrate encoded video is not the best solution given the diversity in streaming context.
	- content providers encode their video at multiple bitrates chosen from a set of pre-defined bitrates
	- the video is chunked into segments of usually equal duration
	- each segment is encoded at multiple bitrates and distributed across their CDNs
	- Client requests also specify the quality.
- This is known as "bitrate adaption"
- Video content is downloaded by the video player at the client.
- At the beginning over every video session, the client downloads a manifest which contains metadata about the video content, available qualities, available bitrates, etc.

## DASH and Bitrate Adaption
- The concepts from the previous section(s) are called "Dynamic Streaming over HTTP" or "DASH".
- Multiple implementations of DASH. Most popular:
	- HLS
	- MPEG-DASH
- Implementations differ in detail such as the encoding algorithms, segment sizes, DRM support, bitrate adaption algorithms, etc.
- Videos are divided into chunks which are encoded at multiple bitrates
- Each time the video player needs to download a video chunk, it calls the bitrate adaptation function. The function outputs the bitrate of the chunk to be downloaded.
- The bitrate adaptation algorithm at the client adapts the video bitrate based on its estimation of network conditions.

![[Pasted image 20231118155829.png]]

### Quality of Experience (QoE)
- bitrate adaptation algorithms try to optimize the user’s experience. A good quality of experience (QoE) is usually characterized by the following:
	1. Low or zero re-buffering: users typically tend to close the video session if the video stalls a lot
	2. High video quality: Better the video quality, better the user QoE. A higher video quality is usually characterized by high bitrate video chunk. 
	3. Low video quality variations: A lot of video quality variations are also known to reduce the user QoE. 
	4. Low startup latency: Startup latency is the time it takes to start playing  the video since the user first requested to play the video. Players typically fill up the video buffer a little before playing the video. For this lesson, we will skip considering startup latency and focus on the other three metrics. 
- In my experience, bitrate adaption algorithms try to balance the user's experience with the cost of streaming high quality content
- the different metrics characterizing QoE are conflicting.
	- In order to have a high video quality, the player can download the higher bitrate chunks.
	- However, it can lead to re-buffering if the network conditions are not good.
	- To avoid re-buffering, player can change either download the lowest bitrate, which leads to a low video quality, or change the video bitrate as soon as it notices a change in the network conditions, which leads to high video quality variations.
- A good bitrate adaptation algorithm considers the trade-offs and maximizes the overall QoE.

### Algorithms
different signals that can serve as an **input** to a bitrate adaptation algorithm:

- Network Throughput
	- Ideally, you would want to select a bitrate that is equal to or lesser than the available throughput.
	- Bitrate adaptation using this signal is known as rate-based adaptation.
- Video Buffer
	- if the video buffer is nearly full, then the player can possibly afford to download high-quality chunks.
	- if the video buffer is nearly depleted, the player can download low-quality chunks so as to quickly fill up the buffer and avoid any re-buffering. 
	- Bitrate adaptation based on the video buffer is known as buffer-based adaptation.

#### Throughput-Based Adaption
- The buffer-filling rate is essentially the network bandwidth divided by the chunk bitrate.
	- assume the available bandwidth is 10 Mbps
	- assume the bitrate of the chunk is 1 Mbps
	- in 1 second we can download 10s of video
	- Thus the buffer-filling rate is 10
	- the buffer-depletion rate is 1. 1 second of video gets played in 1 second.

![[Pasted image 20231118162338.png]]

#### Rate-Based Adaption
- A simple rate-based adaptation algorithm has the following steps: 
	1. Estimation
		- The first step involves estimating the future bandwidth.
		- This is done by considering the throughput of the last few downloaded chunks.
		- Typically, a smoothing filter such as moving average, or the harmonic mean is used over these throughputs to estimate the future bandwidth. 
	2. Quantization
		- In this the continuous throughput is mapped to discrete bitrate. 
		- Basically, we select the maximum bitrate that is less than the estimate of the throughput, including a factor in this selection.
- Why do we add a factor?
	- We want to be a little conservative in our estimate of the future bandwidth to avoid any re-buffering
	- If the chunks are VBR-encoded, their bitrate can exceed the nominal bitrate
	- Finally, there are additional application and transport-layer overheads associated with downloading the chunk and we want to take them into account
- Once the chunk-bitrate is decided, the client sends the HTTP GET request for the next chunk.
- Once the new chunk is downloaded, its download throughput is also taken into account in estimating the next chunk’s bitrate and the same process is repeated for downloading the next chunk.

#### Buffer-Based Adaption
> Use the buffer occupancy to inform bitrate selection. In other words, the bitrate of the chunk is a function of the buffer occupancy

>  R_next  = f(buffer_now) 

> Now how should the function look like. The idea is quite simple: If the buffer occupancy is low, the player should download a low bitrate chunk and increase the chunk quality if the buffer occupancy increases. Thus, the bitrate adaptation function should be an increasing function with respect to the buffer occupancy. Figure below shows example functions, which are all increasing with respect to the buffer occupancy.

![[Pasted image 20231118163435.png]]

> Using buffer-based adaptation can overcome the errors in bandwidth estimation that we saw in rate-based adaptation:

> 1. It avoids unnecessary re-buffering. As long as the download throughput is more than the minimum available bitrate, the video will not re-buffer. This is because, as the buffer occupancy becomes very low, it selects the minimum available bitrate.  
> 2. It also fully utilizes the link capacity and does not suffer from bandwidth underestimation. This is because it avoids the on-off behavior as long as the video bitrate is less than the maximum available bitrate. Once the buffer occupancy is close to full, it starts requesting the maximum possible video bitrate.

> Here is an example buffer-based function. It has three regions of buffer occupancy. The reservoir region corresponds to low buffer occupancy and the player always selects the minimum available bitrate in this region. Similarly, when the buffer occupancy is in the upper reservoir region, the highest available bitrate is selected. Finally, in the middle or the cushion region, the bitrate is a linear function of the buffer occupancy. For instance, if the buffer is between B1 and B2, rate R1 is selected. The figure also shows example values for these regions.

![[Pasted image 20231118163513.png]]

> Even buffer-based adaptation has some issues. 

> 1. In the startup phase, the buffer occupancy is zero. Therefore, the player will download a lot of  low quality chunks which may be unnecessary.
> 2. It can lead to unnecessary bitrate oscillations. For instance, if the available bitrate is 1.5 Mbps and the available video bitrates are 1 Mbps and 2Mbps. The player will keep oscillating between these two. This is because if the player downloads 1 Mbps chunks, the buffer occupancy will increase and then it will start downloading 2 Mbps chunks. Since the available bandwidth is 1.5 Mbps, the buffer occupancy will decrease and then it will switch back again to 1Mbps. 
> 3. Finally, it requires a large-buffer to implement the algorithm efficiently. This may not always be feasible. For instance, in the case of live streaming, the buffer size is not typically more than 8-16 seconds.


### Bandwidth overestimation with Rate-Based Adaption
> Let us first look at how rate-based adaptation can lead to overestimation of bandwidth. Consider a case when the player is subjected to the following bandwidth where the bandwidth is 5 Mbps for the first 20 seconds and is then reduced to 375 kbps. 

> Let us assume the available bitrates are {250kbps, 500 kbps, 1 Mbps, 2 Mbps, 3 Mbps} and the chunk size is 3 Mbps. Initially, the player will stream at 3 Mbps. However, at t = 20 seconds, the bandwidth goes down to 375 kbps which is high enough to play at the lowest bitrate. Assume the buffer occupancy at this time was 15 seconds. 

> The video player has no way of knowing that the bandwidth has reduced. Therefore it ends up requesting a 3 Mbps chunk. To download this 5-second chunk, it will take 3Mbps * 1000 * 5sec / 375kbps or 40 seconds. Meanwhile, the video player buffer will deplete, and the video will eventually re-buffer. If the player uses a weighted average, then it may even take more time to reflect the drop in the network bandwidth, and the player may end up requesting higher bitrate than it should. 

> Thus, we can see under the case when the bandwidth changes rapidly; the player takes some time to converge to the correct estimate of the bandwidth. As observed in this specific, this can sometimes lead to an overestimation of the future bandwidth.

### Bandwidth underestimation with Rate-Based Adaption
![[Pasted image 20231118163003.png]]

> Consider the scenario when a client is watching a video over a 5 Mbps link. 


> The available bitrates are {375kbps, 560 kbps, 750kbps, 1050kbps, 1400kbps, 1750kbs}. Clearly, the client would end up streaming at 1.75 Mbps under rate-based adaptation. 

> After some time, another client joins in and starts downloading a large file. What would happen? Ideally, we would expect both clients to end up getting equal network bandwidth, i.e., 2.5 Mbps, as they are both using TCP.  This means that the video client should continue streaming at 1.75 Mbps. However, the client ends up picking a lower bitrate and eventually goes down all the way to 235 kbps. Let's see why this happens.

![[Pasted image 20231118163030.png]]

> Recall that DASH clients have an ON-OFF pattern in the steady state. This happens when the video client has the buffer filled up, and it is waiting for it to deplete before requesting the next chunk.

![[Pasted image 20231118163048.png]]

> What can happen is that in this OFF period, the TCP connection reset the congestion window. Now this can impact the throughput observed for the chunk download as the TCP flow has another competing flow. 

> Recall that while TCP is fair, it does take time for the flows to converge to their fair share of the bandwidth. In our example, the chunk download can finish before TCP actually converges to the fair share. 

> In this example, say the observed throughput for the chunk was only 1.6 Mbps. Thus, it ends up picking a lower bitrate, i.e., 1050 kbps, because of the rate estimation being conservative (recall that players use a factor of alpha). Now, would it stabilize at that bitrate? Well, as it turns out, NO.

![[Pasted image 20231118163056.png]]

> This figure shows the size of chunks for different bitrates. As you can see, as the bitrate becomes lower, the chunk size reduces. This further aggravates the problem. In the presence of a competing flow, a smaller chunk size would lower the probability for the video flow to get its fair share. Thus, the player ends up further underestimating the network bandwidth and picks up even a lower bitrate until it converges to 235 kbps. 

> Note that this problem happens because of the ON-OFF behavior in DASH. Had it been two competing TCP-flows, they would have gotten their fair share. While we have seen this problem for DASH and a competing TCP flow, it can also happen in competing DASH players leading to an unfair allocation of network bandwidth.

### 