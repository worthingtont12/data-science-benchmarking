"""Parallelized Random Forest Code for Benchmarking EC2."""
import logging
import timeit
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sklearn.feature_extraction.text as text
from sklearn import model_selection
from sklearn import metrics
from load_data import finaldf

# log updates
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# split testing and training
finaldf['is_train'] = np.random.uniform(0, 1, len(finaldf)) <= .80
train, test = finaldf[finaldf['is_train'] == True], finaldf[finaldf['is_train'] == False]

# splitting target attribute from examples
features = train[train.columns[:-1]]
train_target = np.array(train.loc[:, 'target'])

test_features = test[test.columns[:-1]]
test_target = np.array(test.loc[:, 'target'])

# start timer
start_time = timeit.default_timer()

# initialize random forest
rf = RandomForestClassifier(n_jobs=-1, random_state=2017, n_estimators=100)

# train random forest
rf.fit(features, target)

# end timer
print('Time to train model: ' + str(timeit.default_timer() - start_time) + ' seconds')

# predict on test data
target_pred = rf.predict(test_features)

# compare accuracy
accuracy = metrics.accuracy_score(test_target, target_pred)

# confusion_matrix
metrics.confusion_matrix(test_target, target_pred)

# output accuracy
print('Test Error: ' + str(1 - accuracy))
