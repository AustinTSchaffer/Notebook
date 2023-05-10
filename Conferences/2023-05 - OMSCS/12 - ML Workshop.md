# ML Workshop

- ML is more ubiquitous than ever
- models are huge, expensive to train/run
- Model sizes keep increasing
- ChatGPT 3 releases 500 tonnes of CO2 Equivalent Emissions
- How to make ML training more energy efficient?
	1. Optimize hardware usage. Achieve 100% compute utilization
	2. Prioritize carbon-efficient energy sources. Consider data center instances with lower carbon footprints.
	3. Use computationally efficient algorithms. Highly model dependent.
- Does GPU utilization really matter?
- How common is it to underutilize GPUs?
	- Incredibly common
	- Hard to estimate memory usage that your process will require
	- Mean might be 30% of GPU utilization
- How to choose energy efficient data centers?
	- ML CO2 impact. Calculator based on runtime and GPU (https://mlco2.github.io/impact/)
	- Cloud carbon footprint. Web app to monitor your usage. (https://www.cloudcarbonfootprint.org/)
	- Both of these tools are retrospective
	- Predictive tool: Deep View (https://github.com/centml/deepview.profile)


