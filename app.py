"""Filename: app.py
  """

from flask import Flask, jsonify, request
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
                modelln = joblib.load('./linear_simple.pkl')
                coef = pd.Series(modelln.coef_).to_json()

                # Read arguments
                #min = request.args.get("mintemp")
                #min = float(min)
                #max = request.args.get("maxtemp")
                #max = float(max)
                #rainfall = request.args.get("rainfall")
                #rainfall = float(rainfall)
                #change = max - min

                # t = pd.DataFrame({'mintemp': min, 'maxtemp': max, 'change': change, 'rainfall' = rainfall}, index = [0])
                # arr = t.as_matrix()
                #data = {'mintemp': min, 'maxtemp': max, 'change': change}
                #__data__ = pd.Series(data).to_frame()
                #arr = np.array([max,min,change])
                #temp = [max,min,change]
                #arr = [temp]
                #pred = model_ln.predict(arr)
                return(coef)
        except ValueError:
            print("errors")
    return(pred())

@app.route("/retrain")
def retrain():
    print("This function is under construction")

# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug=True)

