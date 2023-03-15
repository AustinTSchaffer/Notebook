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

![[Pasted image 20230309094551.png]]

![[Pasted image 20230309094618.png]]

ad-hoc
- cache when created
- cache-then-serve

![[Pasted image 20230309094708.png]]

![[Pasted image 20230309094815.png]]

![[Pasted image 20230309095157.png]]

![[Pasted image 20230309095427.png]]

## Proxy Server Design Properties
![[Pasted image 20230309095513.png]]

![[Pasted image 20230309095538.png]]

Proxy types
- General firewall proxies
- Departmental proxies
- Specialized proxies
	- proxies between clients and other proxies
	- accelerators
- Reverse proxies

### Departmental Proxy Servers
![[Pasted image 20230309095726.png]]

### Reverse Proxy
- inverted role of proxy server
- primary purposes
	- replication of content for distribution
	- replication of content for load balancing

![[Pasted image 20230309095827.png]]

![[Pasted image 20230309095917.png]]

![[Pasted image 20230309105602.png]]

## Application Server Technology
![[Pasted image 20230309122131.png]]

![[Pasted image 20230309122151.png]]

![[Pasted image 20230309122626.png]]

![[Pasted image 20230309122713.png]]

![[Pasted image 20230309122836.png]]

![[Pasted image 20230309122823.png]]

![[Pasted image 20230309123043.png]]

![[Pasted image 20230309123148.png]]

![[Pasted image 20230309123221.png]]

![[Pasted image 20230309123229.png]]

![[Pasted image 20230309123244.png]]

## Cookies
![[Pasted image 20230309123404.png]]

![[Pasted image 20230309123424.png]]

![[Pasted image 20230309123436.png]]

![[Pasted image 20230309123503.png]]

![[Pasted image 20230309123521.png]]

![[Pasted image 20230309123527.png]]

