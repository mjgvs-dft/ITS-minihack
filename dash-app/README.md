# Bogota Transport Trends Dashboard

A Dash application for visualizing transportation trends in Bogota, Colombia.

## Features

- Interactive maps using Folium
- Statistical analyses with scikit-mobility and GeoPandas
- Multiple visualization pages

## Installation

1. Clone this repository
2. Create a conda environment and install dependencies from `environment.yml`
3. Run the application locally using the command `python app.py` from the `dash-app` directory.


## Deployment

This application is configured for deployment on Google Cloud Platform. 

There is an issue with using App Engine, as Python 3.7 is no longer supported, while we can only get `scikit-mobility` to work with Python 3.7.
We can use Cloud Run instead, which allows us to run the app in a containerized environment.

However, it's tricky to implement authentication with Cloud Run.

To deploy on Cloud Run, ensure that your Dockerfile specifies Python 3.7. 

Then, make sure that `app.py` has the server variable:

```python
# Add this line for Gunicorn to use in production
server = app.server
```

Ensure that the data files are in the correct locations. The Dockerfile will copy the `data` directory into the container, so you need to ensure that the data files are in the correct subdirectories. (See the next step for details)

Then, deploy to Cloud Run in the region of your choice:

```bash
# Make sure you're in the project directory
cd dash-app

# Copy your data files to the appropriate locations
# For example:
# cp /path/to/your/ViajesEODH2019.csv data/input/encuesta-19/
# cp /path/to/your/ZAT.shp data/input/zat/

# Build and deploy to Cloud Run
# Replace XXXXX with your project ID
gcloud builds submit --tag gcr.io/XXXXX/dash-app 

# Deploy to Cloud Run in europe-west1
# Replace XXXXX with your project ID
# Warning: This will deploy the app to a public URL!
# I will take NO responsibility for any data leaks or security issues that arise from this deployment.
gcloud run deploy dash-app \
  --image gcr.io/XXXXX/dash-app \ 
  --platform managed \
  --region europe-west1 \
  --allow-unauthenticated
```

## License

[Your license information here]