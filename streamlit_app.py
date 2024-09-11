import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json  # Don't forget to import json!
from matplotlib.style import use
use('fast')
import plotly.express as px
from scipy.signal import find_peaks, savgol_filter
from scipy.cluster.hierarchy import linkage

st.title("Spectra Visualization App")
st.write("Upload your chemical data in CSV format to start analyzing.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Preview the data to check for column names
    st.write(data.head())

    # Assuming 'Raw_Spectra_Intensity' is stored as a JSON string in the CSV
    # Step 1: Convert JSON string to lists
    data['Raw_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(json.loads)

    # Step 2: Convert lists to numpy arrays
    data['Raw_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(np.array)

    # Step 3: Normalize the spectra intensity
    data['Normalized_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(lambda x: x / max(x))

    # Preview the changes
    st.write(data[['Raw_Spectra_Intensity', 'Normalized_Spectra_Intensity']].head())

