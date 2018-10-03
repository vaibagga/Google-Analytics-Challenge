
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def main():
	''' To read the data and print the head of the data'''
	train = pd.read_csv('train.csv')
	print(train.head())

if __name__ == "__main__":
	main()
