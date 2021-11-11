from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import requests
import plotly.express as px
import plotly.graph_objs as go

from app import app
from layout import dash_page



DATA_ENDPOINT = 'http://localhost:8000/api/v1/statistics'


@app.callback(Output('test-graph', 'figure'),
              [Input("test-filter", "value")])
def update_graph(test_filter):
    # reqeust data
    data = requests.get(DATA_ENDPOINT)
    print(data.json())

    # process data
    ped_num = []
    for record in data.json():
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
