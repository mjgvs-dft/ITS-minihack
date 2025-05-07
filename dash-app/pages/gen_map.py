import dash
from dash import html, dcc, callback, Input, Output
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx
import base64
import io
import os

dash.register_page(__name__, path='/gen-map', name='Generated Trips Map')

def create_contextily_map():
    """Create a map using contextily and matplotlib"""
    try:
        # Check if data file exists
        if not os.path.exists('../data/input/zat/ZAT.shp'):
            return html.Div([
                html.H4("Data file not found"),
                html.P("Please ensure the ZAT shapefile is in the correct location: ../data/input/zat/ZAT.shp")
            ])
        
        # Load the shapefile
        zat_data = gpd.read_file('../data/input/zat/ZAT.shp')
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(12, 12))
        
        # Plot the data
        zat_data.plot(column='GEN_2019',
                     figsize=(18, 18), 
                     edgecolor='white',
                     linewidth=0.3,
                     alpha=0.5,
                     cmap='viridis',
                     legend=True,
                     ax=ax)
                     
        # Add title and remove axis labels
        ax.set_title('Generated Trips 2019', fontsize=16)
        ax.set_axis_off()
        
        # Add the basemap
        cx.add_basemap(ax, crs=zat_data.crs.to_string(), 
                      source=cx.providers.CartoDB.Voyager)
        
        # Convert plot to image
        buffer = io.BytesIO()
        plt.tight_layout()
        fig.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
        buffer.seek(0)
        
        # Convert image to base64 string
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        # Close the plot to free memory
        plt.close(fig)
        
        return html.Img(
            src=f'data:image/png;base64,{img_base64}',
            style={'width': '100%', 'max-width': '1000px', 'margin': '0 auto', 'display': 'block'}
        )
        
    except Exception as e:
        return html.Div([
            html.H4(f"Error creating map: {str(e)}"),
            html.P("Please check your data files and try again.")
        ])

# Define the page layout
layout = html.Div([
    html.H1("Generated Trips Map"),
    html.P("Static map showing trip generation patterns across Bogotá zones."),
    html.Hr(),
    
    # Map controls section
    html.Div([
        html.Button("Refresh Map", id="refresh-gen-map-button", className="btn btn-primary mb-3"),
    ], className="mb-4"),
    
    # Map container
    html.Div([
        html.Div(id="gen-map-container", children=[create_contextily_map()]),
    ], className="border rounded p-3 bg-light text-center"),
    
    # Map description
    html.Div([
        html.H4("About this Map", className="mt-4"),
        html.P([
            "This map visualizes the number of trips generated (GEN_2019) across different transportation ",
            "analysis zones (ZATs) in Bogotá. Darker colors indicate higher numbers of generated trips."
        ]),
        html.P([
            "The base map is provided by CartoDB Voyager through the contextily library."
        ])
    ])
])

@callback(
    Output("gen-map-container", "children"),
    [Input("refresh-gen-map-button", "n_clicks")],
    prevent_initial_call=True
)
def refresh_gen_map(n_clicks):
    """Refresh the map when the button is clicked"""
    if n_clicks:
        return [create_contextily_map()]
    return dash.no_update