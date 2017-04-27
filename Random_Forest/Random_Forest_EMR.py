    """Random Forest Code for Benchmarking EMR."""
import timeit
import logging
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
from pyspark import SparkContext
from pyspark.sql import SQLContext
from load_data import finaldf

# spark context
sc = SparkContext()
sqlCtx = SQLContext(sc)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# convert from pandas df to spark df
df = sqlCtx.createDataFrame(finaldf)

# transform spark df to labeled point
transformedData = df.rdd.map(lambda x: LabeledPoint(x['target'], x[:-1]))

# split training and testing
trainingData, testingData = transformedData.randomSplit([.8, .2], seed=2017)

# start timer
start_time = timeit.default_timer()

# train random forest
model = RandomForest.trainClassifier(
    trainingData, numClasses=2, categoricalFeaturesInfo={}, numTrees=100, seed=2017)

# stop timer
print('Time to train model: ' + str(timeit.default_timer() - start_time) + ' seconds')

# Evaluate model on test instances and compute test error
predictions = model.predict(testingData.map(lambda x: x.features))
labelsAndPredictions = testingData.map(lambda lp: lp.label).zip(predictions)
testErr = labelsAndPredictions.filter(
    lambda seq: seq[0] != seq[1]).count() / float(testingData.count())

# print test error
print('Test Error = ' + str(testErr))
