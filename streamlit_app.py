import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.style import use
use('fast')
import json

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Convert JSON string to lists and normalize the spectra
    data['Raw_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(json.loads)
    data['Raw_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(np.array)
    data['Normalized_Spectra_Intensity'] = data['Raw_Spectra_Intensity'].apply(lambda x: x / max(x))

    # Initialize plot
    fig, ax = plt.subplots(figsize=(16, 6.5))

    # Calculate wavelength
    wavenumber = np.arange(4000, 500, -1)
    wavelength = 10000 / wavenumber  # in microns

    # Plot the spectra
    target_spectra = np.array([])  # Initialize as an empty array
    for smiles, spectra in data[['SMILES', 'Normalized_Spectra_Intensity']].values:
        if smiles == 'C':
            target_spectra = spectra
        else:
            ax.fill_between(wavelength, 0, spectra, color="k", alpha=0.01)
    
    # Highlight the target spectrum (CH$_4$)
    if target_spectra.size > 0:  # Check if target_spectra is not empty
        ax.fill_between(wavelength, 0, target_spectra, color="r", alpha=0.5, label="CH$_4$")

    # Customize plot axes and ticks
    ax.set_xscale('log')
    ax.set_xlim([2.5, 20])

    major_ticks = [3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 20]
    ax.set_xticks(major_ticks, minor=False)

    ax.tick_params(axis="x", labelsize=16)
    ax.tick_params(axis="y", labelsize=16)

    ax.set_xticks([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20])
    ax.set_xticklabels(["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "15", "20"])

    ax.tick_params(direction="in",
                   labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                   bottom=True, top=True, left=True, right=True)

    ax.set_xlabel("Wavelength ($\mu$m)", fontsize=22)
    ax.set_ylabel("Absorbance (Normalized to 1)", fontsize=22)

    # Show legend
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)
