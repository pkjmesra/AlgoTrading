import pandas as pd
import sys
sys.path.append('../')
from algotrading.backtest import Backtest
from algotrading.agents.tema_agent import TEMA_Agent
from algotrading.evaluation import Evaluation

def test(year, stock):
	filename = "../Historical Data/%s/%s-%s.csv" %(year, stock, year)
	prices = pd.read_csv(filename)["Close"]

	agent = TEMA_Agent(10000, 10, 0.05, 0.05)

	test = Backtest(agent)

	output = test.run(prices)

	# class Evaluation takes for initialization - prices, output, name of algorithm, name of security
	evaluator = Evaluation(prices, output, "TEMA", "AXBK")
	evaluator.complete_evaluation()

if __name__ == "__main__":
	test(sys.argv[1], sys.argv[2])