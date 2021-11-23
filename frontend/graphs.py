from datetime import datetime, timedelta

from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go

from app import app
from layout import dash_page


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
                "text": "No matching data found",
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

@app.callback(
    Output("test-graph", "figure"),
    [Input("crosswalk-filter", "value"),
     Input("graph-checklist", "value"),])
def update_graph(crosswalk: str, graph_checklist: str):
    # request data
    stats_df = app.client.get_stats(
        [crosswalk] if crosswalk else None)

    if stats_df.empty:
        return NOT_MATCHING_DATA

    now = datetime.today()
    x_range = [now - DEFAULT_RANGE, now]

    # generate graph
    fig = px.scatter(
        x=stats_df["timestamp"],
        y=stats_df["pedestrians"],
        template="plotly_white",
        trendline="lowess" if 'trendline' in graph_checklist else None,
        range_x=x_range,
    )
    print(stats_df["timestamp"])
    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1h", step="hour", stepmode="backward"),
                dict(count=12, label="12h", step="hour", stepmode="backward"),
                dict(count=1, label="1d", step="day", stepmode="backward"),
                dict(count=7, label="7d", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
            ]),
        ),
        rangeslider={
            "autorange": False,
            "visible": True,
        }
    )

    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Liczba pieszych",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        xaxis={ "autorange": False },
    )
    return fig


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dash":
        return dash_page
    elif pathname == "/crosswalks":
        return html.P("This is the content of page 1. Yay!")

    return html.Div(
        dbc.Container(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="py-3",
    ))


# !TODO add graph: histogram with sum per crosswalk