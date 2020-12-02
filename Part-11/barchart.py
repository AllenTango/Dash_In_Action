import pandas as pd
from app import app
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

def BarChart():
    fig = px.bar()
    return html.Div([dcc.Graph(figure=fig, id="chart")], className="mt-3 shadow")

@app.callback(Output("chart", "figure"), [Input("table", "data")])
def update_chart(data):
    df = pd.DataFrame(data)
    return px.bar(x=df.columns, y=df.sum().to_list(), range_y=[0, 4000])