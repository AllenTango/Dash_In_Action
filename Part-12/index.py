from app import app
from sidebar import SideBar
from table import PersonalTable
from tabchart import TabChart
import dash_bootstrap_components as dbc

app.layout = dbc.Row([
            dbc.Col([SideBar()], width=3, className="bg-dark"), # slider
            dbc.Col([TabChart(), PersonalTable()],width=9),     # content
            ], className="vh-100 vw-100")


if __name__=="__main__":
    app.run_server(debug=True)