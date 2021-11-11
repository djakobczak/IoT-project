import logging

from dash.dependencies import Output, Input
import requests

from app import app


CROSSWALKS_URL = 'http://localhost:8000/api/v1/crosswalks'  # !TODO create client
LOG = logging.getLogger(__name__)


@app.callback(
    Output("crosswalk-filter", "options"),
    Input("crosswalk-filter", "search_value")
)
def update_options(search_value):
    crosswalks = requests.get(CROSSWALKS_URL)
    crosswalks_names = [{"label": cross['name'], "value": cross['id']}
                        for cross in crosswalks.json()]
    if search_value:
        crosswalks_names = list(
            filter(lambda opt: search_value in opt['label'],
                   crosswalks_names))
    return crosswalks_names
