---
tags: Ideas, Programming, Architecture
---

# Coming up with ideas for a side project

https://www.youtube.com/watch?v=JTOJsU3FSD8

## Foreward

> Ideas are cheap. Execution is everything.

Basically, there's no bottom to the well of good ideas. Most good ideas are not unique. Just pick one.

## News Archiver (Data Aggregation)

One common app idea is to aggregate data and add value to it. One such example would be an app that scrapes news headlines over time.

- Web scraper
  - Cloud cronjob that runs every 15 minutes
  - Uses a headless browser (puppeteer/pyppeteer/Selenium) to scrape information from the targeted web pages
  - Store the data in a Cloud-based database/bucket
- Frontend
  - Could be a calendar UI that allows users to navigate to each day and see the headlines that were present on that day


Monitization
  - ADs? Depending on the content you're scraping, might not fall under fair use. Probably should check with a lawyer.
  - Web Archiving as a Service. Could try to sell the service to companies to use the app for monitoring their web deployments.

## Data Analysis and Prediction

One of the problems of data-driven apps is access to high-quality data. Google/Facebook generate their own data. You can get good data from Kaggle (https://www.kaggle.com/).

- Get some source data
- Find a way to use the data for something productive, like visualizing the increasing frequency of events that might be related to global warming
- Find a way to process/store the data in a format that better suits the application

Other data sources / programming competition sites:

- https://data.worldbank.org/
- https://www.crowdanalytix.com/community
- https://innocentive.wazoku.com/#/community/9396a088f8614c2eac89aacf2ae1c624/home-page
- https://www.topcoder.com/challenges
- https://www.hackerrank.com/dashboard
- https://hdsc.nws.noaa.gov/hdsc/pfds/pfds_map_cont.html
- https://github.com/awesomedata/awesome-public-datasets
- https://guides.loc.gov/datasets/repositories#s-lib-ctab-22713457-7
- https://datasetsearch.research.google.com/
- https://archive.ics.uci.edu/ml/index.php

You can also join data competitions on [Kaggle](https://kaggle.com/) and [DrivenData](https://www.drivendata.org/competitions/), some with cash prizes.

## ASCII Images from Photos

Generate artistic photo filters based on ASCII characters

- app that captures images or allows image uploads
- convert pixels to ASCII characters

## Google Maps MMO (Realtime Games)

Geoguesser is pretty cool, but what if it were an MMO? Battle Royale?

## APIs

There are tons of APIs out there that you can leverage and build value on top of. For example, you can imagine a use case for sending texts to people's phones, and use Twilio to add that functionality.

## Cloud Calculator (Surveys and Reports)

People like online portals that allow them to put in information and get back immediate analysis. For example: tax/net worth calculations are pretty neat.

Build an app that runs a survey about cloud costs, then returns price optimizations. Maybe find the cheapest cloud provider. Maybe a cross-cloud kubernetes would be cool (except node-node networking would be crappy).

## Slack Video Chat (Video Streaming)

Yeah ok I'm probably not going to bother with this.

## Hosting Provider

Create an app that automates the setup and management of servers.
