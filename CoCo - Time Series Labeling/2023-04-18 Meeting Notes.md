# Time Series Labeling Meeting Notes
> 2023-04-18

## Participants
- Rachel H. 
- Angela S.
- Austin S.

## Notes
- To train an ML model, you need a lot of examples of input data and output data
- For timeseries
- How do you label an example when the data is timeseries?
- Big picture, capturing timeseries data for the purposes of ML.
- A more cohesive approach
	- Actual interface should allow users to efficiently annotate
	- How to effectively capture/persist the annotations? Set of generic schemas which allow you to capture annotations.
		- Steam traps
		- finance data
		- health
		- etc
	- How do you capture and share training data for ML models? Schema definitions? S3 location?
	- Also, capture user feedback on the output of the ML model.
- The tool will be a framework and an option that organizes.
- Down the road, there will be a model trained on this data running in production which will be making predictions.
	- We start with "Model 1"
	- Need some way to check on the accuracy of the model.
	- "operationalize the models"
	- "good prediction", "bad prediction", "corrected prediction"
	- The human labelled data is effectively to bootstrap the supervised learning feedback loop.
	- "The flywheel". start slow, manually create the initial training data, eventually it builds up its own momentum.
- Book recommendation, "becoming a data head".
- Ideal here is that the timeseries labeling tool/framework will capture model predictions using the same schema as the hand-labelled/hand-annotated/human-annotated data.
	- This will make it easier to design a workflow, which allows human annotators/evaluators to evaluate the predictions made by the model.
- Designing the data interface (i.e. the schemas) will be key for this work.
- Find and express all the use cases of this work.

## Action Items
- Get some open sample data
	- Weather data
	- Stock prices
- Check on the viability of the alternatives
- Diagramming, Scope
- Find a cool project name. Currently "CoCo", "NuCo", "ExCo"