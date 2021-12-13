import logging
import os

import dash
import dash_auth
import dash_bootstrap_components as dbc
from dotenv import load_dotenv

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

load_dotenv()
CREDENTIALS = {
    os.getenv('OPERATOR_USERNAME'): os.getenv('OPERATOR_PASSWORD')
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.server.config.SECRET_KEY = os.getenv("SECRET_KEY")
auth = dash_auth.BasicAuth(app, CREDENTIALS)
app.layout = layout
app.client = ClientManager(
    Client(
        settings.BACKEND_URL,
        settings.OPERATOR_USERNAME,
        settings.OPERATOR_PASSWORD
    )
)
