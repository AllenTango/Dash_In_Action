from app import app
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

def Card(name, cost, color="bg-primary"):
    return html.Div([
        html.H5(name),
        html.Hr(),
        html.H1(cost, id=name)
    ], className=f"shadow text-white p-3 rounded {color}")

def InfoCards():
    return dbc.Row([
        dbc.Col([Card("本月消费", "---", color="bg-info")]),
        dbc.Col([Card("季度消费", "---", color="bg-warning")]),
        dbc.Col([Card("年度消费", "---")]),
    ], className="mt-5")

@app.callback(
    [Output("本月消费", "children"),
     Output("季度消费", "children"),
     Output("年度消费", "children")],
    [Input("dpd", "value"),
     Input("year_chart", "figure")])
def update_cards(month, fig):
    data = fig["data"][0]["y"]
    curr_month = int(month[:-3])
    curr_month_cost = data[curr_month-1]
    curr_seanson_cost = None
    curr_year_cost = sum(data)
    
    seansons = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    for s in seansons:
        if curr_month in s:
            m_1, m_2, m_3 = s
            curr_seanson_cost = data[m_1-1] + data[m_2-1] + data[m_3-1]
    return curr_month_cost, curr_seanson_cost, curr_year_cost