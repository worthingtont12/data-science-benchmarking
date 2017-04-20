
# coding: utf-8

from os import listdir
import pandas as pd
import numpy as np
import functools

def check(x, high, low):
    if x > high:
        return 1
    elif x < low:
        return 0
    else:
        return -1

def load_clean_data():
    data_files = []
    direct = listdir('./data/')

    for file in direct:
        if file.endswith('.csv'):
            data_files.append(file)


    final = pd.DataFrame()
    list_dfs = []
    for file in data_files:
        df = pd.read_csv('./data/' + file, delimiter = '\t', header = None)
        list_dfs.append(df)

    final = pd.concat(list_dfs)

    final = final.drop(final.columns[[0,1,2,3,4,6,16,36,38,41,43,45,48,50,52,55,56,57]], axis=1)
    final = final[np.isfinite(final[30])]
    
    upper = np.percentile(final.ix[:,30],75)
    lower = np.percentile(final.ix[:,30],25)

    final[41] = final[30].apply(lambda x: check(x, upper,lower))

    final = final.drop(final[final[41] == -1].index)

    return final

test = load_clean_data()

print(test)