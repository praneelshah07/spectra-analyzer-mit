import streamlit as st
import pandas as pd
import plotly.express as px
from scipy.signal import find_peaks, savgol_filter

st.title("Spectra Visualization App")
st.write("Upload your chemical data in CSV format to start analyzing.")
# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
