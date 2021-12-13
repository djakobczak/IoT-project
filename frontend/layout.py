from datetime import timedelta

from dash import dcc, html
from dash.dependencies import Output
import dash_bootstrap_components as dbc


# !TODO split file
BOX_CLASSES = "box shadow p-3 bg-white rounded"
UPDATE_INTERVAL = 5000


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


ALL_BTN_ID = 'time-btn-auto'
TIME_BTNS = {
    "time-btn-1h": timedelta(hours=1),
    "time-btn-3h": timedelta(hours=3),
    "time-btn-12h": timedelta(hours=12),
    "time-btn-1d": timedelta(days=1),
    "time-btn-1w": timedelta(days=7),
    "time-btn-1m": timedelta(days=30),
    "time-btn-1y": timedelta(days=365),
    ALL_BTN_ID: timedelta(days=3*365),
}


time_buttons = html.Div(
    [
        html.Div(html.Label("Zakres obserwacji")),
        *[html.Button(
            btn_id.split('-')[-1], id=btn_id, className="btn btn-outline-primary border rounded my-btn col-sm m-1"
        )
        for btn_id in TIME_BTNS]
    ]
)

TIME_AGGR_BTNS = {
    "1s": "1S",
    "10s": "10S",
    "30s": "30S",
    "1 min": "1Min",
    "5 min": "5Min",
}

time_aggr_buttons = html.Div(
    [
        html.Div(html.Label("Poziom agregacji")),
        *[html.Button(
            btn_id.split('-')[-1], id=btn_id,
            className="btn btn-outline-primary border rounded my-btn col-sm m-1"
        )
        for btn_id in TIME_AGGR_BTNS]
    ],
    className="mt-2 ml-3"
)

time_opts = html.Div(
    [time_buttons, time_aggr_buttons],
    className="col-sm"
)


GRAPH_TYPE_SCATTER = 'scatter'
GRAPH_TYPE_LINEAR = 'linear'

graph_checklist = html.Div(
    children=[
        dcc.RadioItems(
            id="graph-type-radio",
            options=[
                {'label': 'Punktowy', 'value': GRAPH_TYPE_SCATTER},
                {'label': 'Liniowy', 'value': GRAPH_TYPE_LINEAR},
            ],
            value=GRAPH_TYPE_SCATTER,
            className="mt-3 mb-3",
            labelStyle={"paddingRight": "10px"}
        ),
        dcc.Checklist(
            id='graph-checklist',
            options=[
                {'label': ' Linia trendu', 'value': 'trendline'},
            ],
            value=['trendline'],
            labelStyle={'display': 'inline-block'},
        ),
    ],
    className="col-sm",
)


stat_histogram = html.Div(
    children=[
        dcc.Graph(id='stat-histogram')
    ]
)


histogram_slider = html.Div(
    [
        dcc.Slider(
            id="histogram-slider",
            min=0,
            max=10,
            step=1,
            value=5,
            tooltip={"placement": "bottom", "always_visible": True},
        )
    ]
)

# cards
sum_card = dbc.Card(
    dbc.CardBody(
        children = [
            html.H5("Sumaryczna liczba pieszych", className="card-title text-center h-50"),
            html.Hr(),
            html.P(id="sum-badge", className="text-center h-50 h5")
        ]
    ),
    className="h-100"
)


avg_card = dbc.Card(
    dbc.CardBody(
        children = [
            html.H5("Średnia liczba pieszych w ostatnim tygodniu", className="card-title text-center h-50"),
            html.Hr(),
            html.P(id="avg-badge", className="text-center h-50 h5")
        ]
    ),
    className="h-100"
)


dash_page = html.Div(
    children = [
        html.Div(children = [
            html.H1("Panel administratora", className="header-title"),
            html.P("Statystyki z przejść dla pieszych",
                   className="header-description"),
        ], className="header"),
        html.Div(children = [
            dbc.Row(
                html.Div(
                    children = [
                        dbc.Col(sum_card, lg=3, className=BOX_CLASSES + " lr-margin"),
                        dbc.Col(avg_card, lg=3, className=BOX_CLASSES)
                    ],
                    className="d-flex align-items-stretch"
                )

            )
        ]),
        html.Div(
            children=[
                html.Div(
                    children=[crosswalk_dropdown, graph_checklist, time_opts],
                    className="row"
                ),
                html.Div(children = [
                    dcc.Graph(id='test-graph'),
                ], className="wrapper"),
            ], className=BOX_CLASSES
        ),
        html.Div(children=[
            histogram_slider,
            stat_histogram
        ], className=BOX_CLASSES),
        dcc.Interval(
            id='interval-component',
            interval=UPDATE_INTERVAL, # in milliseconds
            n_intervals=0
        )
    ]
)


content = html.Div(id="page-content", className="content")
layout = html.Div([dcc.Location(id="url"), sidebar, content])
