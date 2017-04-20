"""Parallelized Random Forest Code for Benchmarking EC2."""
import logging
import timeit
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sklearn.feature_extraction.text as text
from sklearn import model_selection
from load_data import df

# log updates
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# splitting target attribute from examples
X = df[df.columns[:-1]]
Y = np.array(df.loc[:, ['negative_impact']])

# Random Forest Model
seed = 2017
rf = RandomForestClassifier(n_jobs=-1)

# Cross Validate
kfold = model_selection.KFold(n_splits=10, random_state=seed)
results = model_selection.cross_val_score(rf, X, Y.ravel(), cv=kfold)

# results
print(results.mean())
