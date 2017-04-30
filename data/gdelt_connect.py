"""Read all data files from s3 into local"""
import os

# years of interest
years = range(2014, 2018)

# months of interest
months = ["%.2d" % i for i in range(13)]

# days of interest
dates = ["%.2d" % i for i in range(32)]

# loop through all files downloading those that match conditions above
for year in years:
    for month in months:
        for date in dates:
            # command to connect to s3
            os.system("aws s3 cp s3://gdelt-open-data/events/" +
                      str(year) + str(month) + str(date) + ".export.csv .")
