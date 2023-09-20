import pandas as pd
import plotly
import plotly.express as px


def plot(var):
    data = pd.read_csv('datos4.csv')

    bmi_data = data[var]
    time_axis = range(len(bmi_data))

    color_palette = ['#008080', '#2E8B57', '#3CB371', '#90EE90']

    # Plot the "BMI" values over time
    fig = px.line(data , time_axis, bmi_data, labels={'x': 'Months worked'}, color_discrete_sequence=color_palette)
    fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            'font_color' : 'rgb(225,225,225)'
    })

    return plotly.io.to_json(fig, validate=True)
