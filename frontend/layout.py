from dash import dcc, html
from dash.dependencies import Output
import dash_bootstrap_components as dbc


sidebar = html.Div(
    [
        html.H2("Menu", className="display-5 text-light"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Panel", href="/dash", active="exact"),
                dbc.NavLink("Przejścia", href="/crosswalks", active="exact")
            ],
            vertical=True,
            pills=True,
            className="fs-5"
        )
    ],
    className="sidenav bg-dark"
)


crosswalk_dropdown = html.Div(
    [
        html.Div(children="Przejście"),
        dcc.Dropdown(id="crosswalk-filter")
    ],
    className="col-sm"
)

data_range_dropdown = html.Div(
    children=[
        html.Div(children="Zakres obserwacji"),
        dcc.Dropdown(
            id="data-range-filter",
            options=[
                {"label": "Dzienny", "value": "d"},
                {"label": "Tygodniowy", "value": "w"},
                {"label": "Od początku rejestracji", "value": "a"},
            ]
        )
    ],
    className="col-sm"
)

graph_checklist = html.Div(
    children=[
        dcc.Checklist(
            id='graph-checklist',
            options=[
                {'label': ' Linia trendu', 'value': 'trendline'},
            ],
            value=['trendline'],
            labelStyle={'display': 'inline-block'},
        )
    ],
    className="col-sm row-element",
)


dash_page = html.Div(
    children = [
        html.Div(children = [
            html.H1("Panel administratora", className="header-title"),
            html.P("Statystyki z przejść dla pieszych",
                   className="header-description"),
        ], className="header"),
        html.Div(
            children=[crosswalk_dropdown, graph_checklist],
            className="row"
        ),
        html.Div(children = [
            dcc.Graph(id='test-graph'),
        ], className="wrapper")
    ]
)


content = html.Div(id="page-content", className="content")
layout = html.Div([dcc.Location(id="url"), sidebar, content])
