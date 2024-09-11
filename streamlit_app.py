import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import json

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

    # Calculate wavelength
    wavenumber = np.arange(4000, 500, -1)
    wavelength = 10000 / wavenumber  # in microns

    # Create Plotly traces
    traces = []
    for smiles, spectra in data[['SMILES', 'Normalized_Spectra_Intensity']].values:
        if smiles in selected_smiles:
            traces.append(go.Scatter(x=wavelength, y=spectra, mode='lines', name=f'{smiles}', line=dict(width=2)))
        else:
            traces.append(go.Scatter(x=wavelength, y=spectra, mode='lines', line=dict(color='black', width=0.5, opacity=0.1)))

    # Layout settings for the plot
    layout = go.Layout(
        xaxis=dict(title="Wavelength (μm)", type='log', range=[np.log10(2.5), np.log10(20)]),
        yaxis=dict(title="Absorbance (Normalized to 1)"),
        showlegend=True,
    )

    # Create the figure
    fig = go.Figure(data=traces, layout=layout)

    # Display the interactive plot in Streamlit
    st.plotly_chart(fig)
