"""Loads in all the csvs, formats them, and created target attribute."""
# coding: utf-8
from os import listdir
import pandas as pd
import numpy as np
import functools
from sklearn import preprocessing


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


def load_clean_data():
    data_files = []
    direct = listdir('./')

    for file in direct:
        if file.endswith('.csv'):
            data_files.append(file)

    final = pd.DataFrame()
    list_dfs = []
    for file in data_files[0:200]:
        final = pd.read_csv('./' + file, delimiter='\t', header=None)
        # drop unneeded columns
        final = final.drop(final.columns[[0, 1, 2, 3, 4, 6, 16, 36, 38,
                                          41, 43, 45, 48, 50, 52, 55, 56, 57]], axis=1)

       # checks if elements are finite numbers
        final = final[np.isfinite(final[30])]

        # creating target atrribute--reduces variable from 10 levels too 3

        # upper threshold of data
        upper = np.percentile(final.ix[:, 30], 75)

        # lower threshold
        lower = np.percentile(final.ix[:, 30], 25)

        # applying function to reduce levels
        final['target'] = final[30].apply(lambda x: check(x, upper, lower))

        # filtering to categories of interest
        final = final.drop(final[final['target'] == -1].index)
        print("Appending " + file + " to list.")
        list_dfs.append(final)

    print("Concatenating dataFrames")
    finaldf = pd.concat(list_dfs)
    print("Done Concatenating")

    return finaldf

finaldf = load_clean_data()
index = 0
for i in finaldf.columns:
    while finaldf[i].values[index] is np.nan:
        finaldf[i].fillna('unknown', inplace=True)
    if type(finaldf[i].values[index]) == str:
        finaldf[i].fillna('unknown', inplace=True)
        finaldf[i] = finaldf[i].astype('category')

# preprocessing
category_le = preprocessing.LabelEncoder()

categorical_columns = finaldf.select_dtypes(include=['category']).columns
for i in categorical_columns:
    finaldf[i] = category_le.fit_transform(finaldf[i])

tempdf = finaldf.select_dtypes(exclude=['category']).interpolate()
del finaldf

print("Number of observations" + str(len(tempdf)))

numobs = input("Enter number of observations: ")

finaldf = tempdf.sample(int(numobs), replace=False, random_state=2017)
del tempdf
