"""Parallelized Random Forest Code for Benchmarking EC2
"""
import logging
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sklearn.feature_extraction.text as text
from sklearn import model_selection
from boto.s3.connection import S3Connection

# log updates
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# import data
# connect to s3
conn = boto.connect_s3()

# connect to gdelt
gdelt = conn.get_bucket('gdelt-open-data')
gdelt.list()

# splitting target attribute from examples
X = tfidfs[tfidfs.columns[:-1]]
Y = np.array(tfidfs.loc[:, ['random']])

# Random Forest Model
seed = 7
rf = RandomForestClassifier(n_jobs=-1)

# Cross Validate
kfold = model_selection.KFold(n_splits=10, random_state=seed)
results = model_selection.cross_val_score(rf, X, Y.ravel(), cv=kfold)

# results
print(results.mean())
