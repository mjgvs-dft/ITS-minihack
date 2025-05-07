import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

dash.register_page(__name__, path='/statistics')

# Generate some placeholder data
def generate_sample_data():
    dates = pd.date_range(start='2024-01-01', periods=30)
    transports = ['Bus', 'Car', 'Bicycle', 'Walking']
    
    data = []
    for transport in transports:
        base = np.random.randint(100, 1000)
        trend = np.random.choice([1, 1.5, 0.8])
        noise = np.random.normal(0, 50, len(dates))
        values = [max(0, base * (trend ** i) + noise[i]) for i in range(len(dates))]
        
        for i, date in enumerate(dates):
            data.append({
                'date': date,
                'transport': transport,
                'count': values[i]
            })
    
    return pd.DataFrame(data)

df = generate_sample_data()

layout = html.Div([
    html.H1("Transportation Statistics (using placeholder data)"),
    html.P("Statistical analysis of transportation trends in Bogota."),
    html.Hr(),
    
    html.Div([
        html.H4("Select Transportation Type"),
        dcc.Dropdown(
            id='transport-dropdown',
            options=[{'label': t, 'value': t} for t in df['transport'].unique()],
            value=df['transport'].unique()[0],
            clearable=False
        ),
        
        dcc.Graph(id='time-series-chart')
    ])
])

@callback(
    Output('time-series-chart', 'figure'),
    Input('transport-dropdown', 'value')
)
def update_graph(selected_transport):
    filtered_df = df[df['transport'] == selected_transport]
    
    fig = px.line(filtered_df, x='date', y='count',
                 title=f'{selected_transport} Usage Over Time')
    
    return fig