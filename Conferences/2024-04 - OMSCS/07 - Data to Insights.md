---
tags:
---
# 07 - Data to Insights
https://omscs.gatech.edu/data-insights-deep-dive-djangos-fusion-d3js-and-bokeh

> By Drishti Jain

- software developer / ML
- published technical book author
- social entrepreneur
- international tech speaker
- career coach - SkillUp with Drishti

Deep dive into Django's Fushion with D3.js and Bokeh

## D3.js
- JS lib for data visualization
- it's implemented as a collection of 30 discrete libraries/modules
- D3 has no default presentation of your data - there's just the code you write yourself
- capabilities
	- scatterplot with shapes
	- solar terminator - day/night map
	- difference chart
	- volcano contours

## Bokeh
- a python library for creating interactive visualizations for modern web browsers
- sharable - can be published in web pages or jupyter notebiiks
- interactive
- powerful - add custom JS to support advanced/specialized cases
- examples
	- interactive explorer for movie data

## Django Channels
- real-time data streaming
- `pip install channels`
- Django uses request/response pattern: `Browser <-> Django API <-> View Function`
	- View only exists for the duration of a single request
- Channels allow Django to support web sockets
- work across a network
- allow producers/consumers to run transparently across many dynos and/or machines
- task queues - messages get pushed onto the channel by producers, and then given to one of the consumers listening on that channel
- handle real time data easily

## Time-Series Data

## Machine Learning

## ML+Django

## Visualize the world and powerup Django!
