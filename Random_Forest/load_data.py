"""Loads in all the csvs, formats them, and created target attribute."""
# coding: utf-8
import pandas as pd
import numpy as np


def check(x, high, low):
    """
    Bins data into one of three categories.
    """
    if x > high:
        return 1
    elif x < low:
        return 0
    else:
        return -1

# loading data

# drop unneeded columns
df = df.drop(df.columns[[0, 1, 2, 3, 4, 6, 16, 36, 38, 41, 43, 45, 48, 50, 52, 55, 56, 57]], axis=1)

# checks if elements are finite numbers
df = df[np.isfinite(df[30])]


# creating target atrribute--reduces variable from 10 levels too 3

# upper threshold of data
upper = np.percentile(df.ix[:, 30], 75)

# lower threshold
lower = np.percentile(df.ix[:, 30], 25)

# applying function to reduce levels
df[30] = df[30].apply(lambda x: check(x, upper, lower))
