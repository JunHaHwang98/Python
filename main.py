import flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        file = request.files['image']
    if not file: return_template('index.html', label="No Files")