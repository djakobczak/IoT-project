import dash
import dash_bootstrap_components as dbc


from layout import layout


# !TODO export as config
external_stylesheets = [
    {

        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    dbc.themes.SPACELAB
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = layout
