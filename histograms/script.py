#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:30:00 2019

@author: hugo
"""

# Import packages
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values
minimum_cost = np.amin(cost)
maximum_cost = np.amax(cost)

# Use plt.hist() below
plt.hist(cost, range=(minimum_cost, maximum_cost), bins=10, edgecolor="black")