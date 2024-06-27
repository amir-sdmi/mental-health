from flask import abort
import pandas as pd

def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        abort(404, description=f"File not found: {filepath}")

# Load data
mental_health_data = load_data('./app/assets/Cleaned_Mental_Health_Data.csv')
world_happiness_data = load_data('./app/assets/Cleaned_World_Happiness_Report_2005-2021.csv')
gdp_data = load_data('./app/assets/GDP_per_cap.csv')

# Preprocess GDP data
gdp_data = gdp_data.melt(id_vars=['Country-name'], var_name='Year', value_name='GDP')
gdp_data['Year'] = gdp_data['Year'].astype(int)

# Get list of available countries for validation
available_countries = mental_health_data['Country-name'].unique()
