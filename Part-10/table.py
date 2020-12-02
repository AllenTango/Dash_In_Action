import os
import re
import pandas as pd
from app import app
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# 仿 React 组件，虽不符合 PEP8
def PersonalTable():
    df = pd.read_excel("./data/1月账单.xlsx", index_col=0)
    return html.Div([
        dcc.Dropdown(
            id="dpd",
            options=[{"label": f[:-5], "value": f[:-5]}
                    for f in sorted(os.listdir('data'), key=lambda x: int(re.findall("\d+", x)[0]))],
            value="1月账单"
        ),
        dash_table.DataTable(
            id="table",
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
            page_size=12,)
    ], className="shadow mt-3")

@app.callback(
    Output("table", "data"),
    [Input("dpd", "value")])
def update_table(selected):
    return pd.read_excel(f"./data/{selected}.xlsx", index_col=0).to_dict("records")