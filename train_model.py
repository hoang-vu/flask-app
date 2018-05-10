# import necessary library
import pandas as pd
import numpy as np
import re
import itertools as it
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.externals import joblib


# import dataset
df = pd.read_csv("hospitalisation-20152016_pyready.csv")
df["change"] = df["max"] - df["min"]

# Rename columns name for user friendly reason
train = pd.DataFrame(data = {'max': df["max"],"min":df["min"],"change":df["change"],"hosp":df["2yo"],"pollen":df["pollen"]})

# Initialize linear models
reg = LinearRegression()
# model building
ridge = linear_model.Ridge(alpha = 0.05)

# Model training
traindata = train.drop(["hosp"],axis = 1)
labels = train["hosp"]
x_train, x_test, y_train, y_test = train_test_split(traindata, labels, test_size = 0.25,random_state = 5)

model = ridge.fit(x_train,y_train)

# save model as pickle
joblib.dump(model, 'linear_simple_1.pkl', 2)