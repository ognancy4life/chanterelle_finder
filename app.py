import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="mushroom", layout="wide")
st.title("Chanterelle Finder")
st.subheader("by Nancy Williams")
st.write('This app ... using Streamlit on a Heroku app.')
#st.caption("*Note that ...")


df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)
