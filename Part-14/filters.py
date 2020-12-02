from api import industry_list
import dash_html_components as html
import dash_core_components as dcc

def IndustryFilter():
    return html.Div([
        html.H6("行业选择", className="p-2"),
        html.Hr(),
        dcc.Dropdown(
            id="dpd",
            options=[{"label": idt, "value": idt} for idt in industry_list],
            value="制造业"
        ),
    ], className="mt-5 rounded-lg shadow bg-dark")