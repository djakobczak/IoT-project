from datetime import datetime, timedelta

from dash import html, callback_context
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

from app import app
from layout import (
    ALL_BTN_ID, dash_page, TIME_BTNS, TIME_AGGR_BTNS,
    GRAPH_TYPE_SCATTER, GRAPH_TYPE_LINEAR)
from views.management import mgmt_page


NOT_MATCHING_DATA = {
    "layout": {
        "xaxis": {
            "visible": False
        },
        "yaxis": {
            "visible": False
        },
        "annotations": [
            {
                "text": "Brak danych",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {
                    "size": 28
                }
            }
        ]
    }
}

DEFAULT_RANGE = timedelta(hours=1)
GRAPHS_TEMPLATE = "plotly_white"

time_range = DEFAULT_RANGE
aggr_level = "1Min"


@app.callback(
    Output("test-graph", "figure"),
    [Input("crosswalk-filter", "value"),
     Input("graph-checklist", "value"),
     Input("graph-type-radio", "value"),
     Input('interval-component', 'n_intervals'),
     *[Input(btn_id, "n_clicks") for btn_id in TIME_BTNS],
     *[Input(btn_id, "n_clicks") for btn_id in TIME_AGGR_BTNS]
     ])
def update_graph(crosswalk: str,
                 graph_checklist: str,
                 graph_type: str,
                 n_intervals: int,
                 *btns):
    # request data
    stats_df = app.client.get_stats(
        [crosswalk] if crosswalk else None, groupby=["timestamp"])

    if stats_df.empty:
        return NOT_MATCHING_DATA

    global time_range
    global aggr_level
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    for btn_id in TIME_BTNS:
        if btn_id not in changed_id:
            continue
        time_range = TIME_BTNS[btn_id]

    for btn_id in TIME_AGGR_BTNS:
        if btn_id not in changed_id:
            continue
        aggr_level = TIME_AGGR_BTNS[btn_id]

    now = datetime.today()
    x_range = None
    if time_range is not None:
        x_range = [now - time_range, now]

    stats_df = stats_df.resample(aggr_level, on="timestamp").sum()
    stats_df = stats_df[stats_df["pedestrians"] != 0]
    stats_df['timestamp'] = stats_df.index
    stats_df = stats_df.reset_index(drop=True)

    # generate graph
    fig = None
    if graph_type == GRAPH_TYPE_SCATTER:
        fig = px.scatter(
            x=stats_df['timestamp'],
            y=stats_df["pedestrians"],
            template=GRAPHS_TEMPLATE,
            trendline="lowess" if 'trendline' in graph_checklist else None,
            trendline_color_override = 'red',
            range_x=x_range,
        )

    else:
        fig = px.line(
            x=stats_df["timestamp"],
            y=stats_df["pedestrians"],
            template=GRAPHS_TEMPLATE,
            range_x=x_range,
        )

    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Liczba pieszych",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        xaxis={ "autorange": False },
    )

    return fig


def _create_histogram(df, x_name, y_name, xaxis_title, yaxis_title):
    fig = px.line(
        df,
        x=x_name,
        y=y_name,
        template=GRAPHS_TEMPLATE,
    )

    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig


@app.callback(Output("stat-histogram", "figure"),
              [Input("histogram-slider", "value"),
               Input('interval-component', 'n_intervals')])
def update_stat_hisogram(slider_value: str, n_intervals: int):
    stats_df = app.client.get_stats()
    if stats_df.empty:
        return NOT_MATCHING_DATA

    stats_df_sum = stats_df.groupby("crosswalk_name")["pedestrians"].sum().reset_index(name="pedestrian_sum")
    stats_df_sum = stats_df_sum.sort_values(by="pedestrian_sum", ascending=False)
    stats_df_sum = stats_df_sum.head(slider_value)

    fig = px.histogram(
        stats_df_sum,
        x="crosswalk_name",
        y="pedestrian_sum",
        template=GRAPHS_TEMPLATE,
    )

    fig.update_layout(
        xaxis_title="Przejście",
        yaxis_title="Sumaryczna liczba pieszych",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ("/", "/dash"):
        return dash_page
    elif pathname == "/crosswalks":
        return mgmt_page

    return html.Div(
        dbc.Container(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="py-3",
    ))
