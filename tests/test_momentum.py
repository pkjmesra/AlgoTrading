import pandas as pd
import sys
sys.path.append('../')
from algotrading.backtest import Backtest
from algotrading.agents.momentum_agent import Momentum_Agent
from algotrading.evaluation import Evaluation

def test(year, stock):
	filename = "../Historical Data/%s/%s-%s.csv" %(year, stock, year)
	prices = pd.read_csv(filename)["Close"]

	'''
	Parameters for the Moving Momentum algorithm:
	1. Small SMA (default 20)
	2. Large SMA (default 150)
	3. Stochastic oscillator sensitivity (default 14)
	4. Stochastic oscillator oversold threshold (default below 20)
	5. Stochastic oscillator overbought threshold (default above 80)
	6. Small EMA (default 12)
	7. Large EMA (default 26)
	8. Signal Line (default 9)
	'''

	agent = Momentum_Agent(10000, 150, 20, 150, 14, 20, 80, 12, 26, 9)

	test = Backtest(agent)

	output = test.run(prices)

	# class Evaluation takes for initialization - prices, output, name of algorithm, name of security
	evaluator = Evaluation(prices, output, "Moving Momentum", "FB")
	evaluator.complete_evaluation()

if __name__ == "__main__":
	test(sys.argv[1], sys.argv[2])