from app import app
from filters import IndustryFilter, Slider
from table import StockTable
from stock_kline import StockKline
import dash_bootstrap_components as dbc

app.layout = dbc.Row([
            dbc.Col([IndustryFilter(), Slider()], width=2, className="sidebar border-r"),
            dbc.Col([StockTable()], width=3, className="border-r"),
            dbc.Col([StockKline()], width=7)
            ], className="vh-100 vw-100")


if __name__=="__main__":
    app.run_server(debug=True)