# Import the necessary libraries
import plotly.graph_objects as go
import pandas as pd
from flask import Flask

#Read the dataset and get the correlation
data = pd.read_csv('datos3.csv')
corr = data.corr()

# Create a Flask app
app = Flask(__name__)


# Define the route for the API
@app.route('/corelation', methods=['GET']) # type: ignore


def api():
    # Create a heatmap
    fig = go.Figure(data=go.Heatmap(
        x=corr.columns,
        y=corr.columns,
        z=corr,
        colorscale="Tealgrn",
        transpose= True
    ))

    # Return the response
    return fig.to_json()



# Run the app
if __name__ == '__main__':
    app.run()
