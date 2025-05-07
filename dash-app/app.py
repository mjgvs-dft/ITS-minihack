import dash
from dash import html
import dash_bootstrap_components as dbc

# Initialize the app with a bootstrap theme
app = dash.Dash(__name__, 
                use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout with navigation
app.layout = html.Div([
    dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("Bogota Transportation Trends", href="/"),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Home", href="/")),
                dbc.NavItem(dbc.NavLink("Map View", href="/map")),
                dbc.NavItem(dbc.NavLink("Generated Trips Map", href="/gen-map")),
                dbc.NavItem(dbc.NavLink("Statistics", href="/statistics")),
            ]),
        ]),
        color="dark",
        dark=True,
        className="mb-4",
    ),
    
    dbc.Container([
        dash.page_container
    ]),
])

# Add this line for App Engine/Gunicorn to use
server = app.server

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)