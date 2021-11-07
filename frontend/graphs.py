from dash.dependencies import Output, Input
import requests
import plotly.express as px

from app import app


DATA_ENDPOINT = 'http://localhost:8000/api/v1/data'


@app.callback(Output('test-graph', 'figure'),
              [Input("test-filter", "value")])
def update_graph(test_filter):
    data = requests.get(DATA_ENDPOINT)
    ped_num = []
    crosswalks = []
    for record in data.json():
        ped_num.append(record["numPedestrians"])
        crosswalks.append(record['name'])
    fig = px.scatter(
        x=crosswalks,
        y=ped_num
    )
    return fig
