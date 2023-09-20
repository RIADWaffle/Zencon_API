import json
import pandas as pd
import plotly
import plotly.graph_objects as go

data = pd.read_csv('datos3.csv')
corr = data.corr()

def plot():
    fig = go.Figure(data=go.Heatmap(
        z=corr,
        x=corr.columns,
        y=corr.columns,
        colorscale="Tealgrn"
    ))

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'font_color' : 'rgb(225,225,225)'
    })

    

    return plotly.io.to_json(fig, validate=True)

