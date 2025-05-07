# Read Viajesmex data
file_path = '../data/input/encuesta-19/ViajesEODH2019.csv'
import pandas as pd
# Create OD-matrix using origin locations (zat_origen) and destination location (zat_destino)
# OD Matrix
viajes = pd.read_csv(file_path, sep=';', encoding='latin1')
viajes = viajes[viajes.modo_principal == "TransMilenio"]
viajes = viajes[viajes.p29_id_municipio == 11001] # filter for city center only?
viajes = viajes[viajes.zat_origen != 0] # filter out missing origin
viajes = viajes[viajes.zat_destino != 0] # filter out missing destination
od_matrix = viajes.groupby(['zat_origen', 'zat_destino']).size().reset_index(name='journey_count')
print(od_matrix)

# Origin journeys
origin_journeys = viajes.groupby(['zat_origen']).size().reset_index(name='journey_count')

# Destination journeys
destination_journeys = viajes.groupby(['zat_destino']).size().reset_index(name='journey_count')

# combine with a shapefile to obtain the coordinates
import geopandas as gpd
# Read the shapefile
input_file = '../data/input/zat/ZAT.shp'
zat_data = gpd.read_file(input_file)

# Merge the origin journeys data with the shapefile data
zat_data_merged = zat_data.merge(origin_journeys[origin_journeys['zat_origen'] != 0], left_on='ZAT', right_on='zat_origen', how='left')

import folium

# Make sure the CRS is correct for web mapping (WGS 84)
zat_data_merged = zat_data_merged.to_crs(epsg=4326)

# Create an interactive map
m = folium.Map(location=[4.6097, -74.0817], zoom_start=11)  # Coordinates for Bogotá

# Add choropleth layer for journey_count
journey_count_layer = folium.Choropleth(
    geo_data=zat_data_merged,
    name='Survey Trips',
    data=zat_data_merged,
    columns=['ZAT', 'journey_count'],
    key_on='feature.properties.ZAT',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Public Transport Trips surveyed in 2019'
).add_to(m)

# Add choropleth layer for GEN_2019
gen_2019_layer = folium.Choropleth(
    geo_data=zat_data_merged,
    name='Generated Trips',
    data=zat_data_merged,
    columns=['ZAT', 'GEN_2019'],
    key_on='feature.properties.ZAT',
    fill_color='PuBu',  # Different color scheme
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Trips Generated in 2019'
).add_to(m)

# Add hover functionality
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}

folium.features.GeoJson(
    zat_data_merged,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['ZAT', 'GEN_2019', 'journey_count', 'ATR_2019', 'INGRESO', 'COSTO_PUT'],
        aliases=['Zone ID', 'Trips Generated', 'trips surveyed', 'Trips Attracted', 'Avg Income', 'Transport Cost'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map
m.save('../figures/folium/zat_interactive_map.html')
