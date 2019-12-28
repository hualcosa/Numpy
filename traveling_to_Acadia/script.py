#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:39:36 2019

@author: hugo
"""

import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")


# Plot the histograms
plt.figure(1)
plt.subplot(211)

plt.hist(flights, range=(0, 365), bins=365, edgecolor="black")
plt.title("flower blooms and flights by day")
plt.ylabel("flight count")
plt.subplot(212)
plt.hist(in_bloom, range=(0,365), bins=365, edgecolor="green")
plt.xlabel("days of the year")
plt.ylabel("bloom count")
plt.show()