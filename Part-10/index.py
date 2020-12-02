from app import app
from table import PersonalTable
import dash_bootstrap_components as dbc

app.layout = dbc.Row([dbc.Col(width=3, className="bg-dark"), dbc.Col([PersonalTable()],width=9)], className="vh-100")


if __name__=="__main__":
    app.run_server(debug=True)