---
tags: ["Linux", "Hosting", "Networking", "DNS"]
---

# Reverse Cloud Migrations from AWS to RPi

This document was written while watching [Raspberry Pi versus AWS // How to host your website on the RPi4](https://www.youtube.com/watch?v=QdHvS0D1zAI) by [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA)

This document was also written because I needed an excuse to practice typing on my "brand new" Ergodox EZ.

This topic became popular in Programming/DevOps circles when AWS kicked Parler off of its services, for a variety of reasons. I was personnally glad that Parler got the axe and was subsequently banned from the internet, but it does highlight how much power a handful of companies have over what is "allowed" on the internet... 

![](attachments/jim-meme.jpg.png)

Anyway, disregarding all of the thorns this situation presents, this topic is referred to as a "reverse" cloud migration, since **Company A** is looking to move FROM a cloud provider, to either on-prem infrastructure, or a different cloud provider that likely offered fewer integrated services.

**ProTip:** Try not to get kicked off the cloud, especially if your app/service/infra relies on proprietary/integrated services like S3/SQS/SNS/CloudFront/whatever.

## Hardware

The lowest barrier to entry on hosting an application now a days is by getting yourself a RaspberryPi. You can pick up a kit for \$100-\$150. These devices typically run an ARM variant of Linux, typically Raspbian, which is a "Distro based on Debian".

## On-Prem vs Cloud

Self-hosting certainly sounds attractive to FOSS-nerds, but it does present a lot of challenges. Buying hardware for on-prem is more expensive up front, but over time it can be cheaper to run that hardware than it is to rent equivalent hardware in a cloud provider. That's pretty much the only advantage of on-prem hosting. Downsides include:

- wasted space
- fault tolerance
- support
- scaling
- localization for international applications (international networking)
- networking between nodes
- upgrading
- floor space, cooling
- security
- DNS management
- expandable file storage

## Networking to the World

Once you have

- A web app running on your local machine
- A web server proxying connection to that web app

then you need to set up networking so that devices from outside your Covid Quarantine WLAN can access your dumb app. To do this, you need an external IP address, which is typically provided by your Internet Service Provider (ISP). One of the problems is that you also need to make sure that your IP address is static. Your external IP by default typically changes a lot. You'll need to call your ISP and ask them for a static IP address.

**Note:** If AWS was "Totally Not Cool" with your site running on their services, your ISP will likely also be "Totally Not Cool" with your site running on their services as well. Also, your ISP will likely be looking to renegotiate your contract as a "business contract" if your dumb app (which is once again, running on an ARM SOC in your closet) starts getting a ton of traffic.

Apart from getting a static IP addresses, there's also a handful of services like [No-IP](noip.com) that allow you to set up local services that users from the Outside World can connect to, without requiring your own static IP address. The way this particular service works is by creating a Dynamic DNS record for your IP address. You then install and configure a No-IP client, which reports changes to No-IP, who updates the DDNS record accordingly.

## Letting the Traffic In

So now we have a hostname and an IP address that the world can use to access the local application, but we need to let them in (TODO: insert Eric Andre meme). Your home's router typically blocks incoming traffic by default, and we need to instruct the router to let traffic into your local network, so the outside world can access your application. One of the best/easiest ways to do this is to set up Port Forwarding on the router, which essentially maps IP ports on the router to IP ports on a device.
