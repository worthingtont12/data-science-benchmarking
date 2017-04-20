
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv('sample.csv', delimiter= '\t', header = None)
df = df.drop(df.columns[[0,1,2,3,4,6,16,36,38,41,43,45,48,50,52,55,56,57]], axis=1)
df = df[np.isfinite(df[30])]
upper = np.percentile(df.ix[:,30],75)
lower = np.percentile(df.ix[:,30],25)

print(df[1:5][30])

def check(x, high, low):
    if x > high:
        return 1
    elif x < low:
        return 0
    else:
        return -1

df[30] = df[30].apply(lambda x: check(x, upper,lower))

print(df[:][30])

# I was trying to write a loop at this point to assign values(1,0) to the upper 25% and
# lower 25% and then drop all the other values. For some reason it wasn't reassigning
# all the values that I was hoping it would and the runtime was pretty long just for one
# day. I'm not familiar enough with Python to know if there is an apply type function
# that would be faster than a loop. Nonetheless, this removes all the unnecessary variables
# and the Goldstein Scale is column 30. I think we should just deal with the highest and
# lowest values and drop all the neutral results. 
