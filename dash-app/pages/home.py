import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1("Bogota Transportation Trends"),
    html.P("This dashboard provides insights into transportation patterns in Bogota, Colombia."),
    html.Hr(),
    html.Div([
        html.H3("Welcome!"),
        html.P("Use the navigation bar to explore different visualizations:"),
        html.Ul([
            html.Li("Map View: Interactive maps showing transportation data"),
            html.Li("Statistics: Charts and graphs of key transportation metrics")
        ]),
        html.Img(src="/assets/placeholder.png", style={"max-width": "100%"}),
    ])
])