"""Filename: app.py
  """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world(username=None):
    return("Hello")

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            lin_reg = joblib.load("./linear_simple.pkl")
        except ValueError:
            print("value error encountered")

        return print(data)
        #return jsonify(lin_reg.predict(x_pred).tolist())

if __name__ == "__main__":
    app.run()