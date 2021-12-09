import logging
from operator import itemgetter

import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import dash_table
import dash_bootstrap_components as dbc

from app import app


BOX_CLASSES = "box shadow p-3 bg-white rounded"
LOG = logging.getLogger(__name__)

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
crosswalks_df = app.client.get_crosswalks_df()


table = dash_table.DataTable(
        id='crosswalks-datatable',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True}
            for i in crosswalks_df.columns
        ],
        data=crosswalks_df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        column_selectable="single",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
        style_cell_conditional=[
            {'if': {'column_id': 'Nazwa'},
            'width': '30%'},
            {'if': {'column_id': 'Opis'},
            'width': '70%'},
        ],
        style_cell={'padding': '5px'},
        style_header={
            'backgroundColor': '#efefef',
            'fontWeight': 'bold'
        },
)

confirm_deletion = dcc.ConfirmDialog(
    id='confirm-danger',
    message='Uwaga, czy na pewno chcesz wyrejestrować to przejście?',
)


delete_btn = html.Div(
    [
        html.Button("Usuń", id='crosswalk-delete-btn', className="btn btn-sm border rounded col-sm m-1 btn-danger mb-3")
    ],
    className="col-sm"
)


@app.callback(Output('confirm-danger', 'displayed'),
              Input('crosswalk-delete-btn', 'n_clicks'))
def display_confirm(n_clicks):
    if n_clicks:
        return True
    return False


@app.callback([Output("alert-delete", "is_open"),
              Output("alert-no-action", "is_open"),
              Output('crosswalks-datatable', 'data'),
              Output('crosswalks-datatable', 'selected_rows'),
              Output('confirm-danger', 'submit_n_clicks')],
              [Input('confirm-danger', 'submit_n_clicks'),
               Input('interval-component', 'n_intervals')],
              [State('crosswalks-datatable', 'selected_rows'),
              State('crosswalks-datatable', 'data'),
              State("alert-delete", "is_open"),
              State("alert-no-action", "is_open"),
              State('confirm-danger', 'displayed')])
def submit_deletion(submit_n_clicks, n_intervals, selected_rows, data, delete_is_open, no_action_open, displayed):
    LOG.debug("displayed: %s submit: %s selected: %s", displayed, submit_n_clicks, selected_rows)
    if not displayed and not submit_n_clicks:
        df = app.client.get_crosswalks_df()
        return delete_is_open, no_action_open, df.to_dict('records'), selected_rows, submit_n_clicks

    if not submit_n_clicks:
        return delete_is_open, no_action_open, dash.no_update, selected_rows, submit_n_clicks

    if not selected_rows:
        return delete_is_open, not no_action_open, dash.no_update, selected_rows, submit_n_clicks

    selected_rows_data = itemgetter(*selected_rows)(data)
    if not isinstance(selected_rows_data, (list, tuple)):
        selected_rows_data = [selected_rows_data]
    crosswalk_names = [cross["Nazwa"] for cross in selected_rows_data]
    LOG.info("Crosswalks to be deleted: %s", crosswalk_names)
    for cross in crosswalk_names:
        app.client.client.delete_crosswalk(cross)

    crosswalks_df = app.client.get_crosswalks_df()
    data = crosswalks_df.to_dict('records')
    return not delete_is_open, no_action_open, data, list(), 0



mgmt_page = html.Div(
    children = [
        dbc.Alert(
            "Przejście zostało usunięte",
            id="alert-delete",
            is_open=False,
            duration=3000,
            color="success"
        ),
        dbc.Alert(
            "Przejście nie zostało wybrane - brak akcji",
            id="alert-no-action",
            is_open=False,
            duration=3000,
            color="secondary"
        ),
        delete_btn,
        confirm_deletion,
        table,
        dcc.Interval(
            id='interval-component',
            interval=2500, # in milliseconds
            n_intervals=0
        )
    ]
)
