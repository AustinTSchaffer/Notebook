---
tags: OMSCS, AISA
---
# Module 4 - Block 8 - Localization Techniques

| Triangulation                 | Trilateration                   |
| ----------------------------- | ------------------------------- |
| Measure angles from known APs | Measure distance to known APs   |
| Compute intersection lines    | Compute intersection of circles |

- Location based services (LBS)
	- mobile information service that extends spatiotemporal information processing capability to end users on the move via internet and wireless communications
	- Delivery of information services is continuous and location aware
	- information content delivered can either be location (or time) dependent or independent
- Typical Location-Based services
	- Location (basic position)
	- Navigation (routing)
	- Tracking (monitoring movement)
	- Mapping (maps of the world)
	- Timing (bringing precise timing to the world)

## Examples
- Finding Your Way Around
	- Phone learns your habits based on where you are and where you're heading
	- Personalized location remindters: "Remind me to pick up my dry cleaning on my way home."
- Targeted advertisements
	- Take a pic of a product in the physical store
	- Get a notification later when the product is on sale at that store
- Fitness assistant
	- Wearable sensors to track heart rate, blood pressure, acceleration
	- App connects to and controls the wearable sensors
	- App tracks fitness progress

## Location Data

### Who Has It?
- Wireless service providers (mobile phone and wireless LAN)
- ISPs (wired connections)
- Geolocation providers
- Toll road operators
- Courier services
- Taxi services
- Vendors with PoS systems
- Transportation 

### Why is it hard to get?
- Business value
- Location acq tech
	- interfacing with a wide variety of mobile devices
	- interfacing with a wide variety of location data types
		- geometric location (lat, lon, alt)
		- symbolic location (street addr / building/floor/room)
		- network location (IP addr)		- virtual locations (IM address)
- Privacy
	- real location data is personal and can be dangerous in the wrong hands
	- well-known dilemma: customers want location data control and coupons (plus personalized services)

## LBSs: Problems and Assumptions
- Location is dynamically changing information
- Cost of communication is asymmetric
	- broadcast vs point-to-point comm
- Severe power restrictions on mobile hosts
	- battery life
- Limited storage available on mobile hosts
	- resource constraints
- Frequent disconnections
- Security issues due to mobility of hosts
	- location security
	- location privacy

## Location Acq Techniques
- Cellular network based localization
- GPS
- Cell-based localization
- Wifi based localization
- other sensor or data analytics based localization

### Cell-Based Localization
- number of cell towers in USA is steadily growing
- GPS location method is mandated to have certain accuracy
	- 150 meters 95% of the time
	- 50 meters 67% of the time
- Network location method is mandated to be within
	- 300 meters 95% of the time
	- 100 meters 67% of the time
- Can track current location when phone is on standby
	- phone broadcasts cell number to towers
- Triangulation
	- cell phone transceiver is located within the overlapping service area of multiple cell towers
	- Area where each cell tower overlaps the phone is where it is pinpointed

![[Pasted image 20230131185502.png]]

![[Pasted image 20230131185514.png]]

### WiFi Localization
- Similar to cell-based, except using wifi APs instead of cell towers
- Can also leverage RSSI to get approximate distance to the AP
- APs have SSIDs
- Fingerprint database of locations of AP SSIDs can be queried to get approximate location
- Wardriving
	- Drivers use GPS enabled devices and scan for Wifi APs
	- Data is uploaded and AP locations are calculated
	- User device scans local environment
	- LBS client asks server for estimated location (can be client calculated)
	- Driving on roads that are critical but missed in previous passes
	- Driving repeatedly on certain selected roads for historical comparison of APs

![[Pasted image 20230131190250.png]]


- Design of Municipal WiFi networks
- Metropolitan mesh networks
- wifi location privacy and security
- Look-ahead map matching
	- basic alg using arc-based look-ahead MM
	- creates all possible paths from current arn out Ns arcs forward and backward
	- Wifi APs are compared to all arcs in the possible graph in order to cull untenable routes from graph
	- process  can create large number of possible paths even though a small number of them are actual candidate routes

![[Pasted image 20230131190853.png]]


- Optimization of basic look-ahead map match
	- use geographic constraints to improve results
	- arc consistency
	- arc bearing
	- path smoothness
	- "break" curve if necessary
	- localized greed best-fit path
	- project / interpolated point match to path

![[Pasted image 20230131191030.png]]


## Multi-Signal Map-Based Localization

![[Pasted image 20230131191201.png]]

![[Pasted image 20230131191248.png]]

## Generating Synthetic Locations
- GT Mobility Simulator
	- Generates mobility traces of moving objects in a road network
	- Visualizes a road network and generated mobility traces
	- Open source
	- https://code.google.com/p/gt-mobisim
- Supported vector map formats
	- GT-MobiSim zip file includes a road network of northwest Atlanta by default
		- `configs/maps/Northwest_Atlanta_GA_24k.svg`
- ESRI Shapefile (`.shp`)
	- U.S. Census Bureau
	- TIGER/Line Shapefiles (`.shp`)
- GlobalMapper-exported USGS data (`.svg`)
	- USGS
	- Digital Line Graphs (DLG)
	- Spatial Data Transfer Standard (SDTS)
	- https://earthexplorer.usgs.gov

