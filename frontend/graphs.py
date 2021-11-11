from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import requests
import plotly.express as px
import plotly.graph_objs as go

from app import app
from layout import dash_page


@app.callback(
    Output("test-graph", "figure"),
    [Input("crosswalk-filter", "value"),
     Input("data-range-filter", "value"),])
def update_graph(crosswalk: str, data_range: str):
    print("debug", crosswalk, data_range)
    # request data
    stats = app.client.get_stats()
    print(stats)
    # process data
    ped_num = []
    for record in stats:
        ped_num.append(record["pedestrians"])

    # generate graph
    fig = px.scatter(
        x=range(len(ped_num)),
        y=ped_num,
        template='plotly_white'
    )

    # transparent background
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)'
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
