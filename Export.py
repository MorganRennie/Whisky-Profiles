import requests
import geopandas as gpd
import pandas as pd

# Define the URL for layer 5
layer_url = "https://services.arcgis.com/jIL9msH9OI208GCb/ArcGIS/rest/services/Scotch_Whisky_Distilleries_and_Regions_WFL1/FeatureServer/5/query"

# Define parameters for the request
params = {
    "where": "1=1",  # Get all features
    "outFields": "*",  # Retrieve all fields
    "geometryType": "esriGeometryPolygon",  # Ensure polygons are returned
    "returnGeometry": "true",  # Include geometry
    "f": "geojson"  # Output format
}

# Send the request
response = requests.get(layer_url, params=params)

# Check if request was successful
if response.status_code == 200:
    with open("layer_5.geojson", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Export successful! Data saved as 'layer_5.geojson'.")
else:
    print(f"Error: {response.status_code}, {response.text}")

-----------------

# Geojson file then imported into QGIS to convert into a shape file.
