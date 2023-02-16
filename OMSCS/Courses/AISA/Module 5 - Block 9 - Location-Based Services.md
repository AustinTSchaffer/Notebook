---
tags: OMSCS, AISA
---
# Module 5 - Block 9 - Location-Based Services

## Spatial Alarms
- Location query use request/response paradigm
- Push based location services uses pub/sub model for info dissemination
- spatial alarms extend the concept of time-based alarms to spatial dimension
- remind us when we enter some pre-defined location of interest in the future
- Fundamental capability for location-based advertisement and location-based alerts, e.g. location-based ad systems, factory danger zone alert system, sex offender monitoring system, etc

![[Pasted image 20230207192226.png]]

- components
	- name
	- alarm region
	- validity period
	- subscribers
- categories
	- private
	- shared
	- public
- processing
	- triggered when subscriber enters alarm region
	- key observations
		- clients do not move, no alarms triggered
		- clients move but far away from spatial alarms, no alarms triggered
	- requirements
		- accuracy vs efficiency
- challenges
	- naive approach
		- periodic evaluation of alarms when clients are on the move
		- dilemma in interval setting
			- short interval, high accuracy, high cost
			- long interval, low accuracy, low cost

## Spatial Alarms Optimizations
Incorporating motion-awareness and alarm locality awareness to guide the alarm processing decision
- motion aware: avoid/reduce alarm processing for mobile clients far away from their alarms
- locality aware: avoid/reduce alarm processing for mobile clients who move away from their spatial alarms

## Safe Region Approach
- spatial region is a special area which encloses the current location of the mobile client, such that the probability of the client triggering any relevant alarms is zero
- Example: ![[Pasted image 20230207194312.png]]
- grid bitmap encoded safe region
	- bitmap encoded safe region represents a safe region $\Psi_S$ for subscriber S using a bitmap B
	- A bit value of 1 indicates that a predefined region (cell) belonging to the safe region, whereas a 0 bit indicates the opposite
	- GBSR is unable to represent safe region accurately, even with finer granularity

![[Pasted image 20230207194620.png]]

|               | Rectangle                           | Bitmap                                                   |
| ------------- | ----------------------------------- | -------------------------------------------------------- |
| Advantages    | Lightweight                         | Personalize safe region per client                       |
|               | Compact representation              | Quick and efficient representation using bitmap encoding |
|               | Fast containment check              |                                                          |
| Disadvantages | smaller size regions                | Harder containment check                                 |
|               | Fail to utilize client capabilities |                                                          |

![[Pasted image 20230207195044.png]]

- finer resolution splitting of grid cell allows for more accurate representation of grid cell
- uses a much larger bitmap to represent safe region
- different regions have different alarm densities
- how to determine appropriate grid cell side?
- GBSR fails to represent safe regions accurately and efficiently

![[Pasted image 20230207195320.png]]

## Pyramid Bitmap Encoded Safe Region
- split cells in base grid with value zero into UxV smaller cells
- Process repeated for several iterations to form a pyramid data structure of height "h"
- more accurate/efficient representation compared to GBSR approach
- height of pyramid allows us to control accuracy of safe region representation by computing a larger bitmap for more accurate representation
- coverage and bitmap size
- optimized by precomputing a bitmap for each level of the pyramid
- cleitn need current tile bounds and bitmap

![[Pasted image 20230207195620.png]]

![[Pasted image 20230207195735.png]]

![[Pasted image 20230207195918.png]]

![[Pasted image 20230207200041.png]]

## Road Network Spatial Alarms
- capitalizes both spatial constraints on road networks and mobility patterns of mobile users
	- increase the hibernation time of mobile users (energy saving) leading to less frequent wakeup at clients
	- reduce computation cost of alarm checks, leading to significant reduction of unnecessary alarm evaluations
- Unique features
	- road network aware alarm evaluation
	- motion aware optimization: techniques for scaling alarm processing
	

![[Pasted image 20230207200447.png]]

Road network distance options
- segment length based
	- path having the shortest length between 2 network locations
- travel time based
	- a path having the fastest travel time between 2 network locations
	- computed using length of road segments and their max speed

Key concepts
- speed
	- max speed: speed limit of each road segment
	- global max speed: max among all speed limits
	- expected speed: calculate based on previous location / traffic conditions
- border points
	- a set of points on the road network which bound a star-shaped spatial alarm
- hibernation time
	- time interval during which a mobile object does not need to wake up
	- each mobile object has own hibernation time
	- upon the expiration of its old hibernation time, the mobile object will auto-contact the alarm server to obtain new hibernation time

## Road Alarm: Basic Approach
- find nearest border point based on 2 filters
- subscriber based filter
	- consider only the alarms (A) that are subscribed by the mobile object (O)
- Euclidean lower bound (ELB) filter
	- minimize the number of shortest path computations between current location of O to each border point of A by filtering out some irrelevant border points
	- definition of ELB: the segment length based distance between 2 network locations $L_1$ and $L_2$ is at least equal to or longer than the Euclidean distance between $L_1$ and $L_2$
- ELB filtering
	- if the Euclidean distance from point C to point A is longer than the segment length based distance from point C and point B ($Euclidean(C,A) > SegLenDist(C,B)$), then
		- point B is closer to C than point A
		- point A cannot be closer to point C that point B in terms of segment lengths

## Motion Aware Optimizations
- Further remove irrelevant border points and reduce the search space of hibernation time
- Steady motion assumption.

Suite of optimizations
- direction-based motion-aware filter
- destination-based motion-aware filter
- shortest path based motion-aware filter

![[Pasted image 20230207202001.png]]

![[Pasted image 20230207202039.png]]

![[Pasted image 20230207202105.png]]

## Experimental Evaluation
Metrics
- alarm hit rate
- alarm miss rate
- alarm accuracy (success rate)

![[Pasted image 20230207202411.png]]

![[Pasted image 20230207202453.png]]

![[Pasted image 20230207202550.png]]

![[Pasted image 20230207202639.png]]

![[Pasted image 20230207202724.png]]

![[Pasted image 20230207202747.png]]

![[Pasted image 20230207202941.png]]

![[Pasted image 20230207203009.png]]

## Course Project Ideas
- self-driving car collision avoidance
- crime alert assistant (CompStat)
- lost in klaus (CS building on GA Tech's campus)
	- indoor positioning system
	- complete finger map
	- how to find shortest path to classrooms/labs/offices/restrooms/break-areas
	- challenges
		- 3D shortest path algorithm
		- current precise location
- Think big and bold for course projects
