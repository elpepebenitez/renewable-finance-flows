import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
energy_data = pd.read_csv('./data/electricity_generation.csv', encoding='utf-8-sig')
country_classification = pd.read_csv('./data/country_classification.csv', encoding='utf-8-sig')
population_data = pd.read_csv('./data/population.csv', encoding='utf-8-sig')

merged_data = pd.merge(energy_data, country_classification, on='CountryName')

# Group by region
region_grouped = merged_data.groupby('Region')

# Group by income group
income_grouped = merged_data.groupby('IncomeGroup')

# Example: Total energy generation by region
total_energy_by_region = region_grouped['ElectricityGeneration'].sum()

total_energy_by_income = income_grouped['ElectricityGeneration'].sum()

# Example: Bar chart of total energy generation by region
total_energy_by_region.plot(kind='bar', title='Total Energy Generation by Region')

plt.show()