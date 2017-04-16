"""Read all data files into local"""
from subprocess import call

call(['aws s3 cp', 's3://gdelt-open-data/20130530.export.csv ./data'])
