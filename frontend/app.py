import logging

import dash
import dash_bootstrap_components as dbc

from layout import layout

from client import Client
from manager import ClientManager


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# !TODO export as config
BACKEND_URL = 'http://localhost:8000/api/v1'

external_stylesheets = [
    {

        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    dbc.themes.SPACELAB
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = layout
app.client = ClientManager(Client(BACKEND_URL))
