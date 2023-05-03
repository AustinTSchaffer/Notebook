# Advanced Topics in Machine Learning for Trading
*by Silviu Burz*

## Summary of ML4T
- Reinforcement Learning
- Supervised Learning
- Investing and Trading
- Make Money, Live Better

## How do we do more? Challenges involved with real trading?
- Simplifications in ML4T
	- One time frame, one price per day
	- No worries about having enough money to trade, position sizes, wash sales, taxes, etc.
- How are you executing trades?
	- Is there a timeframe you are concerned with?
	- Defining success (profit)
	- Losses due to impact
- Data source
	- Is your data in UTC?
	- What about DST?
	- What about "adjusted hours" days?
	- Stock halts? FOMC rate decisions? Clearly technical analysis is not the full story.

## Building an Agent to trade for you
Assuming you've solved all the challenges so far, we are still not ready
- What are we predicting?
	- A price?
	- A decision (buy/sell/short)?
	- Probability of X?
	- Or even a boolean?
- Train your data?
- Now you must make inferences
- What about data drift? Can we set up a training pipeline?
- Does our API move fast enough for the timeframe we have selected?
- What if the strategy does not work? Do we go back to step 1?
- Impact: buying and selling are not free actions. Transaction fees.

## This is Hard. Can we just copy successful people?
- Find people to copy
- Identify targets?
	- Some govt figures might work, but the disclosure time can be too long to be helpful
	- Social media? Twitter? Stocktwits?
- Can we build tools to quantify the success of a target? What are the challenges?
	- Harvesting, cleaning, and joining the data to real market prices
	- Simulation
	- Calculate metrics (cumulative return, sharpe ratio, average daily return, etc)
- Assumptions
	- If they make a post that they buying, they got it at the highest price of the day
	- What's the probability that they made a profit? Observe price for 5 days.

## Can we query on more than one person?
- Maybe we can aggregate data?
- Build a tool?
- SEC website

## Closing Thoughts
- Market Psychology Chart
- burz.org/links
