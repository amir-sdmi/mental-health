
from flask import abort
import pandas as pd
import os

# Define a function to load data from CSV file
def load_data(filepath):
    try:

        return pd.read_csv(filepath)
    except FileNotFoundError:
        # If the file is not found, abort the execution and return a 404 error
        abort(404, description=f"File not found: {filepath}")

# Set the base path to the 'assets' directory
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))

# Load data from .CSV files
mental_health_data = load_data(os.path.join(base_path, 'Cleaned_Mental_Health_Data.csv'))
world_happiness_data = load_data(os.path.join(base_path, 'Cleaned_World_Happiness_Report_2005-2021.csv'))
gdp_data = load_data(os.path.join(base_path, 'GDP_per_cap.csv'))

#--------------------------------------
# Preprocess the GDP data and Melt it to convert it from wide format to long format
gdp_data = gdp_data.melt(id_vars=['Country-name'], var_name='Year', value_name='GDP')

# Convert the 'Year' column to integer type
gdp_data['Year'] = gdp_data['Year'].astype(int)

# Get the list of available countries from the mental health data
available_countries = mental_health_data['Country-name'].unique()