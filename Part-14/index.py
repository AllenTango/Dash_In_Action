from app import app
from filters import IndustryFilter
import dash_bootstrap_components as dbc

app.layout = dbc.Row([
            dbc.Col([IndustryFilter()], width=3, className="sidebar"),
            dbc.Col([],width=9),
            ], className="vh-100 vw-100")


if __name__=="__main__":
    app.run_server(debug=True)