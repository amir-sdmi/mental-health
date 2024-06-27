from flask import abort
import pandas as pd
import os

def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        abort(404, description=f"File not found: {filepath}")

#Load csv files
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
mental_health_data = load_data(os.path.join(base_path, 'Cleaned_Mental_Health_Data.csv'))
world_happiness_data = load_data(os.path.join(base_path, 'Cleaned_World_Happiness_Report_2005-2021.csv'))
gdp_data = load_data(os.path.join(base_path, 'GDP_per_cap.csv'))

#Preprocess GDP data
gdp_data = gdp_data.melt(id_vars=['Country-name'], var_name='Year', value_name='GDP')
gdp_data['Year'] = gdp_data['Year'].astype(int)

#list of available countries
available_countries = mental_health_data['Country-name'].unique()
