import logging

import dash
import dash_auth
import dash_bootstrap_components as dbc

from client import Client
from manager import ClientManager
from layout import layout
from settings import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', level=logging.DEBUG)


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
app.client = ClientManager(
    Client(
        settings.BACKEND_URL,
        settings.OPERATOR_USERNAME,
        settings.OPERATOR_PASSWORD
    )
)
