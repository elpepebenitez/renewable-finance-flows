import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
energy_data = pd.read_csv('./data/electricity_generation.csv', encoding='utf-8-sig')
country_classification = pd.read_csv('./data/country_classification.csv', encoding='utf-8-sig')
population_data = pd.read_csv('./data/population.csv', encoding='utf-8-sig')

merged_data = pd.merge(energy_data, country_classification, on='CountryName')
merged_data = pd.merge(merged_data, population_data[['CountryName', '2022']], left_on='CountryName', right_on='CountryName', how='left')
merged_data.rename(columns={'2022': 'Population_2022'}, inplace=True)

### Inequalities in energy generation per capita between regions
# Calculate per capita energy generation
merged_data['EnergyPerCapita'] = merged_data['ElectricityGeneration'] / merged_data['Population_2022']
merged_data['AverageEnergyPerCapita'] = merged_data.groupby('Region')['EnergyPerCapita'].transform('mean')

# Calculate the total energy generation per capita for all regions
total_energy = merged_data['EnergyPerCapita'].sum()

# Calculate the percentage share for each region
merged_data['PercentageShare'] = (merged_data['AverageEnergyPerCapita'] / total_energy) * 100

# # Group by region
# region_grouped = merged_data.groupby('Region')['EnergyPerCapita'].mean().sort_values(ascending=False)

# # Plotting the bar chart
# plt.figure(figsize=(12, 6))
# bars = region_grouped.plot(kind='bar', color='skyblue')

# # Add labels inside each bar with the actual energy generation per capita
# for bar in bars.patches:
#     plt.text(bar.get_x() + bar.get_width() / 2 - 0.15, bar.get_height() / 2, f'{bar.get_height():.8f}', ha='center', va='center', color='black')

# plt.title('Average Energy Generation Per Capita by Region')
# plt.xlabel('Region')
# plt.ylabel('Energy Per Capita (MW/Person)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()

# plt.show()

# Assuming 'region_grouped' is the DataFrame with per capita data
# plt.figure(figsize=(10, 6))

# # Plotting the pie chart
# plt.pie(merged_data['PercentageShare'], labels=merged_data['Region'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

# plt.title('Share of Total Energy Generation Per Capita by Region')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# # Save the pie chart as a PNG file
# plt.show()
# plt.savefig('energy_pie_chart.png')

# Group by region
# region_grouped = merged_data.groupby('Region')
# Group by income group
# income_grouped = merged_data.groupby('IncomeGroup')

# Example: Total energy generation by region
# total_energy_by_region = region_grouped['ElectricityGeneration'].sum()
# total_energy_by_income = income_grouped['ElectricityGeneration'].sum()

# Example: Bar chart of total energy generation by region
# total_energy_by_region.plot(kind='bar', title='Total Energy Generation by Region')
# plt.show()