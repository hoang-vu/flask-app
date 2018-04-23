# import necessary library
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# import dataset
min_temp = pd.read_csv("MelbournePark_min_temp_2014_Data.csv")
max_temp = pd.read_csv("MelbournePark_max_temp_2014_Data.csv")
rainfall = pd.read_csv("MelbournePark_rainfall_2014_Data.csv")
hospt = pd.read_csv("hospitalisation-20152016.csv")

data = pd.read_csv("python_hospitalisation_2014.csv")
# Rename columns name for user friendly reason
data.columns =["season","year","month","week","2yo","5yo","15yo","35yo","65yo","min_temp","max_temp","rain"]

# Create sub datasets
subdata = pd.DataFrame(data = {"season":data["season"],"week": data["week"],"min": data["min_temp"],"max":data["max_temp"],"rain":data["rain"],"2yo":data["2yo"]})
subdata["week"] = subdata["week"].astype('category')
subdata["season"] = subdata["season"].astype('category')
season_dummies = pd.get_dummies(subdata["season"])
week_dummies = pd.get_dummies(subdata["week"])
subdata = pd.concat([subdata, season_dummies, week_dummies], axis = 1)

# model building
lasso = linear_model.Lasso(alpha = 0.5)

train = subdata.drop(["season","2yo","week"],axis = 1)
labels = subdata["2yo"]
x_train, x_test, y_train, y_test = train_test_split(train, labels, test_size = 0.25,random_state = 1)

model = lasso.fit(x_train,y_train)

# save model as pickle
joblib.dump(model, 'linear_simple.pkl')