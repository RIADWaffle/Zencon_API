import plotly.express as px
import pandas as pd

data = pd.read_csv('datos3.csv')
corr = data.corr()


def plot():
    fig = px.imshow(corr , color_continuous_scale = "Tealgrn" )
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'font_color' : 'rgb(225,225,225)'
    })

    return fig

