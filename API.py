# Import the necessary libraries
from flask import Flask, jsonify
from flask_cors import CORS
import PCA, RNA
import correlationMatrix as corr

#Read the dataset and get the correlation

app = Flask(__name__)
CORS(app)

@app.route('/PCA', methods=['GET']) # type: ignore
def route1():
    return PCA.plot(4)

@app.route('/correlation', methods=['GET']) # type: ignore
def route2():
    return corr.plot()

@app.route('/RNA', methods=['GET']) # type: ignore
def route3():
    return RNA.plot('BMI')

if __name__ == '__main__':
    app.run(debug=True)



# Run the app
if __name__ == '__main__':
    app.run()
