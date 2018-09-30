import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def main():
	train = pd.read_csv('train.csv')
	print(train.head())

if __name__ == "__main__":
	main()