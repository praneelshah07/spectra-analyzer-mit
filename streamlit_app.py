import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.style import use
use('fast')
import json
import random
from scipy.signal import find_peaks
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage  # Using scipy instead of fastcluster

# Set up the Streamlit app
st.title("Spectra Visualization App")
st.write("Upload your chemical data in CSV format to start analyzing.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Convert JSON string to lists and normalize the spectra
    data['Raw_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(json.loads)
    data['Raw_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(np.array)
    data['Normalized_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(lambda x: x / max(x))

    # Preview the dataframe to ensure data is loaded correctly
    st.write(data.head())

    # Select SMILES for molecules you want to highlight
    unique_smiles = data['SMILES'].unique()
    selected_smiles = st.multiselect('Select molecules by SMILES to highlight:', unique_smiles)

    # Add a checkbox to enable or disable peak finding
    peak_finding_enabled = st.checkbox('Enable Peak Finding and Labeling', value=False)

    # Initialize plot with adjusted DPI for better resolution
    fig, ax = plt.subplots(figsize=(16, 6.5), dpi=100)

    # Calculate wavelength
    wavenumber = np.arange(4000, 500, -1)
    wavelength = 10000 / wavenumber  # in microns

    # Color palette for highlighted spectra
    color_palette = ['r', 'g', 'b', 'c', 'm', 'y']  # Add more colors if needed
    random.shuffle(color_palette)  # Shuffle colors to randomize highlights

    # Plot the spectra
    target_spectra = {}  # Store selected spectra for highlighting
    for
