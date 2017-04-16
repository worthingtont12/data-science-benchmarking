
"""Read all data files into local"""
import os

years = range(2014, 2016)
months = ["%.2d" % i for i in range(03)]
dates = ["%.2d" % i for i in range(03)]

for year in years:
        for month in months:
                for date in dates:
                        os.system("aws s3 cp s3://gdelt-open-data/events/" + str(year) + str( month) + str(date) + ".export.csv .")
