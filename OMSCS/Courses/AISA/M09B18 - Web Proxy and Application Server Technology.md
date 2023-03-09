---
tags: OMSCS, AISA
---
# M09B18 - Web Proxy and Application Server Technology

Required reading: [[FLASH - An efficient and portable web server.pdf]]

Semi-continuation of: [[M09B17 - Web Server Technology]]

![[Pasted image 20230308224720.png]]

![[Pasted image 20230308224804.png]]

![[Pasted image 20230308224851.png]]

The Demilitarized Zone (DMZ)
- the part of the network which lies between the internet and the internal network (intranet)
- the DMZ shields the rest of the intranets from the threats of the open internet

DMZ Characteristics
- More exposed to the threads of the internet than the internal hosts
- more stringent security measures must be taken on that zone

![[Pasted image 20230308225745.png]]

![[Pasted image 20230308230045.png]]

Web proxy server uses
- permitting/restricting client access to the internet
	- client IP addresses
- caching documents for internal requests
- selectively controlling access to the internet and subnets
	- submitted URL
- providing internet access for companies using private networks
	- AWS VPC "Internet Gateway" for example
- Converting data to HTML format so it is readable by the browser
	- typically not performed by the proxy server but ok?
	- This feels like an application detail.
	- Also the browser will do this on JSON/XML/YAML formats

## Web Proxy Architecture
![[Pasted image 20230308230502.png]]

![[Pasted image 20230308230558.png]]

![[Pasted image 20230308230657.png]]

![[Pasted image 20230308230738.png]]

![[Pasted image 20230308230833.png]]

Continue here: https://gatech.instructure.com/courses/303644/pages/block-18-web-proxy-and-application-server-technology?module_item_id=2938510

