# import necessary library
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import pickle

# import dataset
df = pd.read_csv("data/hospitalisation-20152016_pyready.csv")
df["change"] = df["max"] - df["min"]

# Rename columns name for user friendly reason
logtrain = pd.DataFrame(data = {'max': df["max"],"min":df["min"],"change":df["change"],"pollen":df["pollen"], "rainfall":df["rainfall"],"hosp":df["hosp_rate_35yo"]})
logtrain = logtrain[['change', 'max', 'min', 'pollen', 'rainfall', 'hosp']]
# Initialize linear models
logmodel = linear_model.LogisticRegression(penalty = 'l2', fit_intercept = True)

# logistic regression training
log_train = logtrain.drop(["hosp"],axis = 1)
labels = logtrain["hosp"]
x_train, x_test, y_train, y_test = train_test_split(log_train, labels, test_size = 0.25,random_state = 5)

log_model = logmodel.fit(x_train,y_train)

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(log_model.score(x_test, y_test)))

# Pickle the model
with open('log_model_pickle.pkl', 'wb') as f:
    pickle.dump(log_model, f,2)