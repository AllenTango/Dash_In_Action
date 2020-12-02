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


def Slider():
    return html.Div([
        html.H6("技术指标"),
        html.Hr(),
        html.P("市盈率"),
        dcc.RangeSlider(
            id="PErate",
            min=0,
            max=10,
            value=[0,50],
            step=1
        ),
        html.P("换手率"),
        dcc.RangeSlider(
            id="TRrate",
            min=0,
            max=10.0,
            value=[0,10.0],
            step=0.1
        )
    ], className="mt-4 px-2")

@app.callback(Output("table", "filter_query"), [Input("PErate", "value"), Input("TRrate", "value")])
def slider_control(PErate, TRrate):
    p_min, p_max = PErate
    t_min, t_max = PErate
    p_code = "{PERation}"
    t_code = "{TurnoverRate}"
    p_query = f"{p_code} > {p_min} and {p_code} < {p_max}"
    t_query = f"{t_code} > {t_min} and {t_code} < {t_max}"
    query = p_query + " and " + t_query
    return query