from dash import dcc, html


layout = html.Div(
    children = [
        html.H1("Operator dashboard"),
        html.P("Panel przedstawiający statystyki z przejść dla pieszych"),
        dcc.Graph(id='test-graph'),
        dcc.Dropdown(
            id="test-filter",
            options=[
                {"label": val, "value": val}
                for val in range(10)
            ],
            value="data1",
            clearable=False,
            className="dropdown",
        )
    ]
)
