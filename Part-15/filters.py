from app import app
import api
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

def IndustryFilter():
    return html.Div([
        html.H6("行业选择", className="p-2"),
        html.Hr(),
        dcc.Dropdown(
            id="dpd",
            options=[{"label": idt, "value": idt} for idt in api.industry_list],
            value="制造业"
        ),
    ], className="mt-5 rounded-lg shadow bg-dark")

@app.callback(Output("table", "data"), [Input("dpd", "value")])
def update_table(industry_name):
    return api.choose_industry(industry_name)