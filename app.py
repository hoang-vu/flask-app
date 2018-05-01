"""Filename: app.py
  """

from flask import Flask, jsonify, request
import pandas as pd
from sklearn import linear_model
from sklearn.externals import joblib
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources = {r"/get": {"origin": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world(username=None):
    return("Hello")

@app.route('/get', methods = ['GET'])
@cross_origin(origin='*', headers=['Content- Type','Authorization'])
def get():
    if request.method == 'GET':
        try:
            def pred():
                #min = request.args.get("mintemp")
                #min = float(min)
                #max = request.args.get("maxtemp")
                #max = float(max)
                #change = max - min
                modelln = joblib.load('./linear_simple.pkl')
                co = pd.Series(modelln.coef_).to_json()
                # t = pd.DataFrame({'mintemp': min, 'maxtemp': max, 'change': change}, index = [0])
                # arr = t.as_matrix()
                #data = {'mintemp': min, 'maxtemp': max, 'change': change}
                #__data__ = pd.Series(data).to_frame()
                #arr = np.array([max,min,change])
                #temp = [max,min,change]
                #arr = [temp]
                #my_fuckingy = model_ln.predict(arr)
                return(co)
        except ValueError:
            print("erros")
    return(pred())


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=1200)