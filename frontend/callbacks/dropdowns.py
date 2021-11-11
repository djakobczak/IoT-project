import logging

from dash.dependencies import Output, Input

from app import app


LOG = logging.getLogger(__name__)


@app.callback(
    Output("crosswalk-filter", "options"),
    Input("crosswalk-filter", "search_value")
)
def update_options(search_value):
    crosswalks_names = app.client.get_crosswalks_names()
    crosswalks_names = [{"label": cross, "value": cross}
                        for cross in crosswalks_names]
    if search_value:
        crosswalks_names = list(
            filter(lambda opt: search_value in opt['label'],
                   crosswalks_names))
    return crosswalks_names
