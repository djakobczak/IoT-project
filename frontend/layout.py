from dash import dcc, html


layout = html.Div(
    children = [
        html.Div(children = [
            html.H1("Operator dashboard", className="header-title"),
            html.P("Panel przedstawiający statystyki z przejść dla pieszych",
                   className="header-description"),
        ], className="header"),
        html.Div(children = [
            dcc.Graph(id='test-graph'),
        ], className="wrapper"),
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
