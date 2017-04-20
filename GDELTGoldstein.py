
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv('sample.csv', delimiter= '\t', header = None)
df = df.drop(df.columns[[0,1,2,3,4,6,16,36,38,41,43,45,48,50,52,55,56,57]], axis=1)
df = df[np.isfinite(df[30])]
upper = np.percentile(df.ix[:,30],75)
lower = np.percentile(df.ix[:,30],25)

def check(x, high, low):
    if x > high:
        return 1
    elif x < low:
        return 0
    else:
        return -1

df[30] = df[30].apply(lambda x: check(x, upper,lower))
