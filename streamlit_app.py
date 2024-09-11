import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.style import use
from scipy.spatial.distance import pdist, squareform
from fastcluster import linkage
use('fast')

# Set title
st.title('Spectra Visualization App')

# File uploader for data input
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
