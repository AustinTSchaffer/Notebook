# Urban Home Gardener

## Strugglefest USA 2023
When setting up my new raised bed planter boxes for this season (and all future seasons), here are a few things I struggled with:

- Determining whether to use in-ground vs raised beds
- Should I hang plants on the fence?
- Determining where to put the raised beds
	- Uneven terrain
	- Inability to dig in our yard due to stones existing everywhere right beneath the topsoil (thanks Ryan Homes)
- Determining how to build the raised beds
	- Concrete castle blocks from Lowe's plus loads of 2x6s (and similar easy-DIY solutions)
		- Pros
			- Modular
			- Stackable
			- Can be constructed into pretty much any 3D shape (as long as it only has right angles)
			- Super easy to conceptualize and assemble
			- Resistant to imprecision
		- Cons
			- Concrete is heavy
			- If the blocks aren't oriented perfectly parallel to each other (vertically), then adding more layers exacerbates the difference. This is fine for 2 layers, but it gets sketchier as you add more 
	- DIY fully wood built
		- Pros
			- Freedom to design anything
		- Cons
			- Freedom to design anything, you need to pick a plan and hope that you execute it right.
			- Doesn't really fix the terrain problem unless you're an expert, or if it's fully elevated.
			- Takes longer. Likely more expensive due to lumber requirements and tools required.
- Determining how large to make those raised beds
	- More Width:
		- Pro: More growing space
		- Con: Covers more terrain, exacerbating issues related to uneven terrain
	- More Depth:
		- Pro: More growing space
		- Con: Reduced ability to access all of the plants
	- More Height:
		- Pro: Can plant plants that require deeper soil (potatoes, onions)
		- Con: Exacerbates terrain issues
- Determining which plants to plant in each bed
	- Trellising required/recommended?
	- Companion plants? Incompatible plants?
	- Light levels required?
	- Future planning
		- "Will this plant block the light required by this other plant?"
	- Watering requirements?
	- Maintenance requirements
		- "Can I go away for a week without calling a friend to come water it?"
- Determining when to pull the crops out and replant new crops.

## Technological Solutions

- Monitoring
	- Soil moisture sensors?
	- Sunlight level monitoring?
	- Temperature monitoring?
		- Determine cumulative "degree days" for the season. Useful metric for determining when plants may start to flower or produce fruit.
		- https://www.eia.gov/energyexplained/units-and-calculators/degree-days.php
		- http://climatesmartfarming.org/tools/csf-growing-degree-day-calculator/
- Automation
	- Can we combine the previous 2 points to make a system which automatically waters the plants?
- Schedule Planning
	- Weather forecasting
		- precipitation
		- sunlight
		- temperature
		- cloud coverage
	- Can we predict when the home gardener needs to water each plant? Can we efficiently determine the optimal times to water all of their plants, or the optimal times to water each garden bed?
	- Can we help the home gardener plant certain plants together based on their water requirements? Is this required? Do most home garden plants require roughly the same amount of water?
	- Can we show the estimated health of each plant?
		- Resetting these health trackers will require that the gardener actively uses the app, which I something I wouldn't want to do.
	- Can we take all of the fun out of gardening?
- Sunlight
	- This is the part of the problem that would be most useful to me. Determining how much sunlight each of my beds gets has been mostly guesswork up to this point.
	- Given the lat/lon of my yard, and a 3D model of my fence, house, garage, and neighborhood, it should be possible to calculate the amount of time that each voxel sees light each day. The gardener should be able to input their growing surfaces, and the model should be able to output the number of hours that the surfaces see sunlight each day. Note that this result will vary slightly throughout the growing season, due to a variety of factors. These calculations can probably assume 0% cloud coverage.
	- Has this already been done? This exists for estimating how much sunlight roofs get during the day: https://sunroof.withgoogle.com/

