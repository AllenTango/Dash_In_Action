import re
import os
import pandas as pd
from app import app
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def TabChart():
    return html.Div([
        dbc.Tabs([
            dbc.Tab(label="月消费", tab_id="tab-1"),
            dbc.Tab(label="年消费", tab_id="tab-2"),],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div([month_chart(hidden=True), year_chart(hidden=False)], id="content"),], className="mt-4 rounded")

def month_chart(hidden=False):
    style = {"display": "none"} if hidden else {}
    fig = px.bar()
    return dcc.Graph(figure=fig, id="month_chart", style=style)

@app.callback(Output("month_chart", "figure"), [Input("table", "data")])
def update_chart(data):
    df = pd.DataFrame(data)
    return px.bar(x=df.columns, y=df.sum().to_list(), range_y=[0, 2500])


def year_chart(hidden=False):
    style = {"display": "none"} if hidden else {}
    total = []
    for f in sorted(os.listdir('data'), key=lambda x: int(re.findall(r'(\d+)', x)[0])):
        df = pd.read_excel(f"./data/{f}", index_col=0)
        month_total = sum(df.sum().to_list())
        total.append(month_total)
    fig = px.bar(x=[f"{i}月" for i in range(1, 13, 1)], y=total, range_y=[0, 8000])
    return dcc.Graph(figure=fig, id="year_chart", style=style)


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return html.Div([month_chart(), year_chart(hidden=True)])
    elif at == "tab-2":
        return html.Div([month_chart(hidden=True), year_chart()]) 
    return html.P("无法获取当前数据......")