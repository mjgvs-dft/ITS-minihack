import dash
from dash import html, dcc, callback, Input, Output, State
import os
import tempfile
from data.map_data import load_and_process_data, create_folium_map

dash.register_page(__name__, path='/map')

def get_folium_map():
    """Generate the folium map and return it as HTML"""
    try:
        # Check if data files exist, if not use placeholder
        data_files_exist = os.path.exists('../data/input/encuesta-19/ViajesEODH2019.csv') and \
                          os.path.exists('../data/input/zat/ZAT.shp')
        
        if not data_files_exist:
            # Return placeholder message if files don't exist
            return html.Div([
                html.H4("Data files not found"),
                html.P("Please ensure the data files are in the correct location:"),
                html.Ul([
                    html.Li("../data/input/encuesta-19/ViajesEODH2019.csv"),
                    html.Li("../data/input/zat/ZAT.shp")
                ])
            ])
        
        # Process the data
        zat_data_merged = load_and_process_data()
        
        # Create the map
        m = create_folium_map(zat_data_merged)
        
        # Save to a temporary file
        temp_html = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
        m.save(temp_html.name)
        
        # Read the saved HTML file
        with open(temp_html.name, 'r', encoding='utf-8') as file:
            folium_html = file.read()
        
        # Clean up the temp file
        os.unlink(temp_html.name)
        
        # Return the map in an iframe
        return html.Iframe(
            srcDoc=folium_html,
            style={"width": "100%", "height": "600px", "border": "none"}
        )
    except Exception as e:
        # Return error message if something goes wrong
        return html.Div([
            html.H4(f"Error loading map: {str(e)}"),
            html.P("Please check your data files and try again.")
        ])

# Layout with the map and controls
layout = html.Div([
    html.H1("Bogotá Transportation Map"),
    html.P("Interactive map showing TransMilenio usage patterns in Bogotá."),
    html.Hr(),
    
    # Map filters section (optional)
    html.Div([
        html.H4("Map Settings"),
        html.Button("Refresh Map", id="refresh-map-button", className="btn btn-primary mb-3"),
    ], className="mb-4"),
    
    # The map container
    html.Div([
        html.Div(id="map-container", children=[get_folium_map()]),
    ], className="border rounded p-3 bg-light"),
    
    # Additional information
    html.Div([
        html.H4("About this Map", className="mt-4"),
        html.P([
            "This map visualizes transportation data from the 2019 mobility survey in Bogotá. ",
            "It shows TransMilenio usage patterns across different zones (ZATs) in the city."
        ]),
        html.P([
            "Use the layer control in the top right corner to toggle between different data visualizations."
        ])
    ])
])

@callback(
    Output("map-container", "children"),
    [Input("refresh-map-button", "n_clicks")],
    prevent_initial_call=True
)
def refresh_map(n_clicks):
    """Refresh the map when the button is clicked"""
    if n_clicks:
        return [get_folium_map()]
    return dash.no_update