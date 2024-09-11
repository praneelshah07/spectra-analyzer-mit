import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


  # Compute wavelength from wavenumber
    wavenumber = np.arange(4000, 500, -1)
    wavelength = 10000 / wavenumber  # convert to microns

    # Filter spectra data
    # Assuming 'SMILES' and 'Normalized_Spectra_Intensity' are columns in your dataframe
    target_spectra = df[df['SMILES'] == 'C']['Normalized_Spectra_Intensity'].values
    spectra_data = df[df['SMILES'] != 'C']['Normalized_Spectra_Intensity'].values

    # Create a plot
    fig, ax = plt.subplots(figsize=(16, 6.5))

    # Plot all spectra in black with low opacity (optimized)
    for spectra in spectra_data:
        ax.fill_between(wavelength, 0, spectra, color="k", alpha=0.01)

    # Plot the target spectra (e.g., CH$_4$) in red
    if target_spectra.any():
        ax.fill_between(wavelength, 0, target_spectra[0], color="r", alpha=0.5, label="CH$_4$")

    # Set axis properties
    ax.set_xscale('log')
    ax.set_xlim([2.5, 20])
    ax.set_xticks([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20])
    ax.set_xticklabels(["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "15", "20"])
    ax.set_xlabel("Wavelength ($\mu$m)", fontsize=22)
    ax.set_ylabel("Absorbance (Normalized to 1)", fontsize=22)

    # Show legend
    plt.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)
