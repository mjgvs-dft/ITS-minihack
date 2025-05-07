# Geospatial Analysis Project
This project uses Python with geospatial libraries to analyze and visualize geographic data.

## Set up your environment

### Initial setup

```python
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install geopandas pandas matplotlib folium contextily

# Save the environment dependencies
pip freeze > requirements.txt
```

### Loading from a saved state

```python
# Create a virtual environment (if not already created)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### Getting started

```python
# Import libraries
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium
import contextily as ctx
```

# Translation of Dataset Attributes (Zonas de Análisis de Transporte - ZAT)

The following table provides translations and descriptions of the attributes found in the ZAT dataset:

| Attribute   | Translation                                                                                     | Description                                                                                                        |
|-------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ZAT         | Transport Analysis Zone ID                                                                      | Identifier for the Transport Analysis Zone.                                                                        |
| GEN_2019    | Public Transport Trips Generated in 2019                                                        | Number of public transport trips generated in 2019 (as per SDM projections).                                       |
| ATR_2019    | Public Transport Trips Attracted in 2019                                                        | Number of public transport trips attracted in 2019 (as per SDM projections).                                       |
| GEN_2026    | Public Transport Trips Generated in 2026 (No COVID)                                             | Number of public transport trips projected to be generated in 2026 (without considering COVID).                    |
| ATR_2026    | Public Transport Trips Attracted in 2026 (No COVID)                                             | Number of public transport trips projected to be attracted in 2026 (without considering COVID).                    |
| GEN_2030    | Public Transport Trips Generated in 2030 (No COVID)                                             | Number of public transport trips projected to be generated in 2030 (without considering COVID).                    |
| ATR_2030    | Public Transport Trips Attracted in 2030 (No COVID)                                             | Number of public transport trips projected to be attracted in 2030 (without considering COVID).                    |
| VIAJ_MUJ    | Public Transport Trips by Women                                                                 | Number of public transport trips made by women (based on EODH 2019).                                               |
| VIAJ_HOM    | Public Transport Trips by Men                                                                   | Number of public transport trips made by men (based on EODH 2019).                                                 |
| VIAJ_TRANS  | Public Transport Trips by Transgender Individuals                                               | Number of public transport trips made by transgender individuals (based on EODH 2019).                             |
| PRC_MUJ     | Percentage of Public Transport Trips by Women                                                   | Percentage of public transport trips made by women (based on EODH 2019).                                           |
| INGRESO     | Average Monthly Household Income                                                                | Average monthly income of households (based on EODH 2019).                                                         |
| COSTO_PUT   | Average Monthly Public Transport Expenses                                                       | Average monthly public transport expenditure of households (based on EODH 2019).                                   |
| PRC_ING     | Percentage of Monthly Income Spent on Public Transport                                           | Average percentage of monthly household income spent on public transport (based on EODH 2019).                     |
| T_PUT       | Average Duration of Public Transport Trips                                                      | Average duration of public transport trips attracted to the zone (based on EODH 2019).                             |
| VIAJ_TRAB   | Work-Related Public Transport Trips                                                             | Number of work-related public transport trips made to the zone (based on EODH 2019).                               |

## Notes
- **SDM**: Secretaría Distrital de Movilidad (District Department of Mobility, Bogotá D.C.).
- **EODH 2019**: Encuesta Origen-Destino a Hogares 2019 (Origin-Destination Household Survey 2019).
- For detailed information, visit the [SDM Open Data Portal](https://www.simur.gov.co/portal-simur/datos-del-sector/encuestas-de-movilidad/).