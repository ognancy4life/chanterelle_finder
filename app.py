import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="mushroom", layout="wide")
st.title("Chanterelle Finder")
st.subheader("by Nancy Williams")
st.write('This app ... using Streamlit on a Heroku app.')
#st.caption("*Note that ...")

if st.text_input("Enter your starting address:", key='address'):
     ticker = st.session_state.address

st.write("Select how far you're willing to drive:")
period = st.slider('Miles',
     value=[0, 300])

#https://deckgl.readthedocs.io/en/latest/
"""
TerrainLayer
===========

Extruded terrain using AWS Open Data Terrain Tiles and Mapbox Satellite imagery
"""

import pydeck as pdk
import os

# Import Mapbox API Key from environment
MAPBOX_API_KEY = os.environ["MAPBOX_API_KEY"]
# AWS Open Data Terrain Tiles
TERRAIN_IMAGE = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
# Define how to parse elevation tiles
ELEVATION_DECODER = {"rScaler": 256, "gScaler": 1, "bScaler": 1 / 256, "offset": -32768}
SURFACE_IMAGE = f"https://api.mapbox.com/v4/mapbox.satellite/{{z}}/{{x}}/{{y}}@2x.png?access_token={MAPBOX_API_KEY}"
terrain_layer = pdk.Layer(
    "TerrainLayer", elevation_decoder=ELEVATION_DECODER, texture=SURFACE_IMAGE, elevation_data=TERRAIN_IMAGE
)
view_state = pdk.ViewState(latitude=47.6205, longitude=-122.3493, zoom=9, bearing=0, pitch=50)
deckchart = st.pydeck_chart(pdk.Deck(
    initial_view_state=view_state,
    layers=[terrain_layer],
))

# oir custom layers

#https://towardsdatascience.com/build-a-multi-layer-map-using-streamlit-2b4d44eb28f3
df = pd.DataFrame(
     np.random.randn(1000, 2) / [250, 250] + [47.6205, -122.3493],
     columns=['lat', 'lon'],)

#st.map(df)

# Can get most current soil moisture data from:
# https://nasagrace.unl.edu/data/current/
# file ending in .nc4, could import and plot using xarray?
# also available in tif

# Can get weather maps from https://home.openweathermap.org/

