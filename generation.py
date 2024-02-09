import pandas as pd

# Replace with the actual file paths for your data
file_paths = [
    './data/country_classification.csv',  # Country classifications
    './data/population.csv',  # Population
    './data/electricity_generation.csv',  # Electricity generation
    './data/installed_electricity_capacity.csv',  # Installed capacity
    './data/installed_renewable_electricity_capacity.csv',  # Installed renewable electricity capacity
    './data/renewable_electricity_generation.csv'   # Renewable electricity generation
]

# Create empty DataFrames to store data
country_classifications = pd.DataFrame()
population_data = pd.DataFrame()
electricity_generation = pd.DataFrame()
installed_capacity = pd.DataFrame()
installed_renewable_capacity = pd.DataFrame()
renewable_generation = pd.DataFrame()

# Read each file into respective DataFrames
country_classifications = pd.read_csv(file_paths[0], encoding='utf-8-sig')
population_data = pd.read_csv(file_paths[1], encoding='utf-8-sig')
electricity_generation = pd.read_csv(file_paths[2], encoding='utf-8-sig')
installed_capacity = pd.read_csv(file_paths[3], encoding='utf-8-sig')
installed_renewable_capacity = pd.read_csv(file_paths[4], encoding='utf-8-sig')
renewable_generation = pd.read_csv(file_paths[5], encoding='utf-8-sig')

# PSEUDO - table that compares electricity generation per region and electricity generation per capita for all regions
# Merge the necessary DataFrames based on the common column "CountryName".
# Calculate the total electricity generation per region. Filter electricity generation data for the year 2022
# Calculate the total population per region.
# Calculate electricity generation per capita for each region.
# Create a table to display the results.

# 1. Merge the necessary DataFrames based on the common column "CountryName"
merged_electricity = pd.merge(electricity_generation, country_classifications, on="CountryName")
merged_population = pd.merge(population_data, country_classifications, on="CountryName")

# 2. Calculate the total electricity generation and enewable electricity generation per region
# Filter electricity generation data for the year 2021
electricity_generation_2021 = merged_electricity[merged_electricity["Year"] == 2021]

# Sum generation per country and technology for the year 2021
summed_generation_per_country = electricity_generation_2021.groupby(['CountryName'], as_index=False)['ElectricityGeneration'].sum()

# Merge the summed generation back to the original DataFrame
# merged_electricity = pd.merge(merged_electricity, summed_generation_per_country, on='CountryName', suffixes=('', '_Total'))

# Meergeeee
merged_electricity_summed = pd.merge(summed_generation_per_country, country_classifications, on="CountryName")

total_generation_per_region = merged_electricity_summed.groupby("Region")["ElectricityGeneration"].sum().reset_index()

# 3. Calculate the total population per region
total_population_per_region = merged_population.groupby("Region")["2021"].sum().reset_index()

# 4. Calculate electricity generation per capita and renewable energy generation per capita for each region
generation_per_capita = pd.merge(total_generation_per_region, total_population_per_region, on="Region")
generation_per_capita["ElectricityGenerationPerCapita"] = generation_per_capita["ElectricityGeneration"] / generation_per_capita["2021"]

# 5. Calculate the percentage of each region's ElectricityGenerationPerCapita relative to the total electricity generation per capita
total_electricity_generation = total_generation_per_region["ElectricityGeneration"].sum()
total_electricity_generation_percapita = generation_per_capita["ElectricityGenerationPerCapita"].sum()
generation_per_capita["PercentageOfTotalGenerationPerCapita"] = (generation_per_capita["ElectricityGenerationPerCapita"] / total_electricity_generation_percapita) * 100

# 6. Create tables to display the results
result_table = generation_per_capita[["Region", "ElectricityGeneration", "ElectricityGenerationPerCapita", "PercentageOfTotalGenerationPerCapita"]]

# Print or display the result table
print(result_table)
