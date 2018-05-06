import pandas as pd
import re
from datetime import datetime

# Read pre-downloaded twitter data
df = pd.read_csv('pollen_MelPollen.csv',sep = ',')
# Keep text and posted date of the tweet
keep =['Text','Created-At']
df = df[df.columns.intersection(keep)]
df.columns = ["date","text"]

# Regular expression to extract information
station_pattern = r'(#)\w+'
pollen_pattern = r"(\d+) grass"

# Extract information from tweet
df1 = df.copy()
# Loop through DataFrame:
for index, row in df.iterrows():
    pollen = re.findall(pollen_pattern, row["text"])
    station = re.findall(station_pattern, row["text"])
    # - get pollen count if any, return 0 if none
    if len(pollen) == 0:
        df1.loc[index,"pollen"] = 0
    else:
        df1.loc[index,"pollen"] = pollen[0]
    # - get station name, return empty string if no station mentioned
    if len(station) == 0:
        df1.loc[index,"station"] = "dummy"
    else:
        s = station[0].replace("#","")
        df1.loc[index,"station"] = s
    # transform datatime to date
    datetime_object = datetime.strptime(row["date"], '%Y-%m-%d %H:%M:%S').date()
    df1.loc[index, "datetime"] = datetime_object
# Drop the original text and date column
df1.drop(["date","text"],axis = 1, inplace=True)
# Write to csv for Excel handling tasks
df1.to_csv("pollen_twitter.csv")