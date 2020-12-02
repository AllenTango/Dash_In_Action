import api
from app import app
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State


def paint_it_black(fig):
    fig.update_xaxes(showgrid=True, gridwidth=1,
                     gridcolor="#233552", zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1,
                     gridcolor="#233552", zeroline=False)
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=450,
        font_color="#7F9BB4",
    )
    return fig


def candle_maker(s_code):
    df = api.get_60d_kline_data(s_code)
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
    return fig


def StockKline():
    fig = go.Figure()
    fig = paint_it_black(fig)
    return html.Div([
        html.H3("----", id="stname"),
        html.Hr(),
        dcc.Graph(figure=fig, id="kline")], className="mt-5")


@app.callback(
    [Output("stname", "children"),
     Output("kline", "figure")],
    [Input("table", "active_cell"),
     Input("table", "data"),
     State("table", "derived_viewport_data")])
def update_kline(c, data, curr_data):
    c = {"row": 0} if not c else c
    num = c["row"]
    data = data if not curr_data else curr_data
    s_code = data[num]["公司代码"]
    s_name = data[num]["公司简称"]
    fig = candle_maker(s_code)
    fig = paint_it_black(fig)
    return f'{s_name} - {s_code}', fig
