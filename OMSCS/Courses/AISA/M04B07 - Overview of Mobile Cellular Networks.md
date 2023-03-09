---
tags: OMSCS, AISA
---
# M04B07 - Overview of Mobile Cellular Networks

Required reading: [[RADAR: An In-Building RF-based User Location and Tracking System.pdf]]

## Location based services
- Location-based traffic monitoring and emergency services
	- Location based mining
		- traffic patterns
	- Shortest path query
		- pathing search
		- estimated arrival time
- Location-based advertisements/entertainment
	- location based mining
		- How many mobile users in the theater are residents of Atlanta? 
		- What distribution in terms of their age group?
	- Location Triggers / Spatial Alarms
		- Send eCoupons to all customers within 5 miles
- Location Finder
	- Where are the gas stations within 5 miles of my location?
	- Where is the nearest movie theater?

## LBSs
- Digital maps
- places database
- location to place mapping

## Localization
> Family of technologies for location acquisition

- GPS
- Mobile triangulation
- Wifi access point positioning
- network-based positioning

- Cell mobile network - mobile computing infra
	- each wireless cell has a unique id - cell ID
	- wireless channel: uplink/downlink channels
- Mobile clients and fixed hosts (MSS)
	- Some fixed hosts are called mobule support stations (MSS) or base stations, augmented by wireless interfaces
	- A MSS can communicate with mobile clients within its radio coverage area, called a wireless cell
	- Entire coverage area is a group of cells. The size of a cell depends on the power of each base station

### Cell Network Organization
- Use multiple low-power transmitters (100W or less)
- Areas divided into cells
	- Each served by its own antenna
	- Served by base station consisting of transmitter, receiver, and control unit
	- band of freqs allocated
	- cells set up such that antennas of all neighbors are equidistant (ideally)
- Use of several carrier freqs
- Not the same freq in adjoining cells
- Cell sizes vary from 100m up to 35km, depending on user density, geography, transceiver power, etc
- Hex shape of cells is idealized
- If a mobile user changes cells, handover of the connection to the neighbor cell

![[Pasted image 20230130205029.png]]

![[Pasted image 20230130205104.png]]

![[Pasted image 20230130205127.png]]

![[Pasted image 20230130205216.png]]

## Location Models / Data
- Absolute location
	- Source: GPS receivers, mobile phone network, geocoding
	- Geometric location of user
		- lat/lon, elevation, error margain
	- Direction indicator (speed / heading)
- Symbolic location (Address)
	- Source: reverse geocoding, fixed beacon, manual entry
	- e.g. company/building/floor/office, airline/airplane/flight/seat
- Network location
	- Source: any computer / device
	- Host name, domain name, IP addr
	- WiFi AP based positioning

### Geometric model
- A location is specified by a 3D coordinate. Lat, lon, timestamp
- A set of coords determining an area's bounding geometric shape (polygon)
- Point, Curve, and Surface Geometry
- Segmented Curve
- Geometric Surface

### Symbolic model
- location space is divided into discrete zones. Zones are IDed by unique names
- Examples: cell infra, postal addresses

### Geocoding facilities
- used to map loc data produced by location sensors such as GPS to real-world entities to describe the loc space and vice versa

### Vector Data Representation
- vector data are constructed from geometric  objects
- points, line segments, triangles, other polygons, cylinders, spheres, cuboids, polyhedrons in 3D

### Vector format often used to represent map data
- Roads are 2D and represented by lines and curves
- Some feature, such as rivers, may be represented as either complex curves or polygons, depending on relevancy of width
- Features such as regions and lakes can be depicted as polygons

## Types of Spatial Location Queries
- Point queries: Where am I? What is here?
- Spatial range queries
	- query has associated region (location, boundary) and answer includes overlapping or contained data regions
	- Find all cities within 50 miles of Maiden GA
- Nearest-Neighbor Queries
	- Results must be ordered by proximity
	- Find the 10 cities nearest to Maiden, GA
- Distance scan
	- Find object within certain distance of an identified object where distance is made increasingly larger
- Spatial join queries
	- Find all cities near this lake
	- Expensive, join conditions are complicated

## Location Acquisition
- people mobility vs device mobility
- what location are we sensing
- how do we compute location information
- Location acq enforcement for emergency response
	- US Enhanced 911 initiatives
	- EU " 112 "
- Self-positioning devices
	- processing power at device
	- provides privacy and parallelism
- infra-based solution
	- Requires transmission power at device
	- provide broader device compatibility
	- centralized vs distributed location acq
		- devices continuously report their positions to a centralized location server
		- detection of or by nearby objects
			- radio or visual contact or scan (radar, bluetooth)
			- record and match "radio fingerprints"

### Core Positioning Technologies
- GPS-based
	- GPS
	- Differential GPS (D-GPS)
	- Assisted GPS (A-GPS)
- Cell Network based
	- cell global ID (CGI)
	- + timing advance (GCI+TA)
	- + round trip time (GGI+RTT)
	- Enhanced observed time difference (E-OTD)
	- Uplink time difference of arrival (U-TDOA)
	- Advanced forward link trilateralization (AFLT)
	- angle of arrival (AOA)
	- Time of flight (TOF)
- Internet-based
	- IP-address as position and position-based DNS
	- WiFi AP based positioning techniques
- Machine Learning Based
	- Crowd sourcing + image classification

## Communication Satellites
- GEO - Geostationary Earth Orbit
- MEO - Medium-Earth Orbit (Used by GPS)
- LEO - Low-earth orbit

![[Pasted image 20230130212152.png]]

## GPS Overview
- Long-distance wireless: one-way comms
- 34 to 32 MEO satellites in 6 orbital planes continuously transmitting timed radio signals
- GPS satellites continuously transmit digital radio signals to earth-bound receivers
- The orbits are arranges so that at any time, anywhere on earth, there are at least 4 satellites "visible" in the sky.
- Accurate within 3 to 50 feet, norm accuracy of 10 feet
- timing of received signals indicates distance to satellites, which can be used to position receiver's lat, lon, and altitude

## Location Acq: Computational Categorization
- Trilateration
	- Known distance to at least 3 base stations
	- GPS as an example
- Triangulation
	- measure angles from known stations
- Resections
	- Measure distances (or angles) **to** known stations
- Dead reckoning
	- Compute new position based on old position, compass direction and distance traveled
	- Location estimation / approximation










