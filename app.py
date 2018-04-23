"""Filename: app.py
  """

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world(username=None):
    return("Hello")

@app.route('/get', methods = ['GET'])
def get():
    if request.method == 'GET':
        try:
            r = request.args.get('temp')
        except ValueError:
            print("erros")
    return(r * 10)

@app.route('/post', methods = ['POST'])
def post():
    if request.method == 'POST':
        try:
            data = "lkjasd"
        except ValueError:
            print("value error encountered")

        return(r)
        #return jsonify(lin_reg.predict(x_pred).tolist())

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=1200)