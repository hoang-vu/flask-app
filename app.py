"""Filename: app.py
  """

from flask import Flask, jsonify, request
import pickle
import pandas as pd
from sklearn import linear_model
from sklearn.externals import joblib
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources = {r"/get": {"origin": "https://aspronto-pal.ml"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return("Hello world")

@app.route('/get', methods = ['GET'])
@cross_origin(origin='https://aspronto-pal.ml', headers=['Content-Type','Authorization'])
def get():
    if request.method == 'GET':
        try:
            def pred():
                # Load model pickle
                pkl_file = open('log_model_pickle.pkl', 'rb')
                model = pickle.load(pkl_file)

                # Read arguments
                min = request.args.get("min")
                min = float(min)
                max = request.args.get("max")
                max = float(max)
                rainfall = request.args.get("rainfall")
                rainfall = float(rainfall)
                change = max - min
                pollen = 0 # default value of pollen

                df = pd.DataFrame([[change, max, min, pollen,rainfall]])
                res = model.predict(df)

                # Determine threshold
                result = {"risk_level":res[0]}
                return(jsonify(result))
        except ValueError:
            print("Unexpected errors encountered")
    return(pred())

@app.route("/retrain")
def retrain():
    print("This function is under construction")

# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug=True)

