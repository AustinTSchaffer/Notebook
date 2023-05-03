# Forecasting Demand for Decarbonized Energy Grids
*by Chang Sun, Pei-Chuan Chao, Matt Carney*

> This was a group effort.

# Goal
- improve demand forecasting to improve grid operations
- managing load is critical for grid operations
- accurate forecasts improve economics of grids with renewable inputs
- improves long-term economics of renewable generation projects
- matching demand with supply is key!

## Dataset
- PSML
- PSML is an open access dataset containing extensive time series data on grid load, renewable availability, and weather conditions
- https://github.com/tamu-engineering-research/Open-source-power-dataset
- Multiple possible use cases
- intended to drive ML-enabled research on improving electric grid operations
- Contains benchmarks for various traditional and ML approaches
- We use data from CAISO, which operates California's grid

## Hypothesis
- newer deep learning architectures may outperform benchmarks
- ARIMA and exponential smoothing (ETS) both perform well on benchmarks
- Used
	- Spacetimeformer
	- DeepAR
	- Temporal Fusion Transformer

## Why use Temporal Fusion Transformer?
- architecture well suited to multi-horizon forecasting
- better interpretability than previous DL-based forecasting methods
- Good name

## Experimental Process
- Trained using an RTX 3080
- Found `pytorch-forecasting`, a library with a TFT impl.
- Used optuna for more efficient hyperparameter tuning
- Academic code can be difficult to adapt
- Don't try creating bespoke implementations, use off-the-shelf ones when possible
- Had to reduce scope given project constraints

## Results
- promising
- did not outperform ARIMA nor ETS

## Conclusion
- ARIMA and ETS are still the top benchmarks for now
- TFT outperformed vanilla transformer benchmark and most other DL methodologies
- Transformers adapted to time series forecasting challenges show potential
- need more SOTA models trained on energy demand forecasting and grid management
- would be useful to have models with pre-trained weights for transfer learning
- need to improve multi-horizon forecasting of availability of renewables
- Could also tackle the supply-side of the equation.

## Q&A
- top 3 courses for learning how to do this? 
	- Deep Learning (this project was done as part of taking this course)
	- Machine Learning (yasssss -Divya)
- Heavily regulated industry, model explainability?
	- Didn't think about it as part of the project.
