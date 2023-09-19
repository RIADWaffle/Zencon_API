# Import the necessary libraries
import plotly.graph_objects as go
import pandas as pd
from flask import Flask, jsonify

import PCA, RNA
import correlationMatrix as corr

#Read the dataset and get the correlation

app = Flask(__name__)

@app.route('/PCA', methods=['GET'])
def route1():

    return jsonify(PCA.plot(4).to_json())

@app.route('/correlation', methods=['GET'])
def route2():
    return jsonify(corr.plot().to_json())

@app.route('/RNA', methods=['GET'])
def route3():
    return jsonify(RNA.plot('BMI').to_json())

if __name__ == '__main__':
    app.run(debug=True)



# Run the app
if __name__ == '__main__':
    app.run()
