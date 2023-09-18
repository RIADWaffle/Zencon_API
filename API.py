# Import the necessary libraries
import plotly.graph_objects as go
import pandas as pd
from flask import Flask

#Read the dataset and get the correlation
url = 'https://raw.githubusercontent.com/RIADWaffle/Zencon_API/e8bcca1fb64d7d47226f90df2b3b51e2a34b264b/datos3.csv?token=GHSAT0AAAAAACHX2Q44OV3CD2QB7VZQQRT4ZIIRPUA'
data = pd.read_csv(url, index_col=0)
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
