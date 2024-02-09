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

# Filter out rows where Technology is not "Total renewable energy"
filtered_renewable_generation = renewable_generation[renewable_generation['Technology'] == 'Total renewable energy']
# print(filtered_renewable_generation)

# 1. Merge the necessary DataFrames based on the common column "CountryName"
merged_renewable_generation = pd.merge(filtered_renewable_generation, country_classifications, on="CountryName")
merged_population = pd.merge(population_data, country_classifications, on="CountryName")
merged_renewable_generation.dropna(subset=["Region"], inplace=True)

# 2. Calculate the total electricity generation and enewable electricity generation per region
total_renewable_generation_per_region = merged_renewable_generation.groupby("Region")["2021"].sum().reset_index()

# 3. Calculate the total population per region
total_population_per_region = merged_population.groupby("Region")["2021"].sum().reset_index()

# 4. Calculate electricity generation per capita and renewable energy generation per capita for each region
renewable_per_capita = pd.merge(total_renewable_generation_per_region, total_population_per_region, on="Region")
renewable_per_capita["RenewableEnergyGenerationPerCapita"] = renewable_per_capita["2021_x"] / renewable_per_capita["2021_y"]

# 5. Calculate the percentage of each region's ElectricityGenerationPerCapita relative to the total electricity generation per capita
total_renewable_electricity_generation = total_renewable_generation_per_region["2021"].sum()
total_renewable_electricity_generation_percapita = renewable_per_capita["RenewableEnergyGenerationPerCapita"].sum()
renewable_per_capita["PercentageOfTotalRenewableGenerationPerCapita"] = (renewable_per_capita["RenewableEnergyGenerationPerCapita"] / total_renewable_electricity_generation_percapita) * 100

# 6. Create tables to display the results
result_table_renewable = renewable_per_capita[["Region", "2021_x", "RenewableEnergyGenerationPerCapita", "PercentageOfTotalRenewableGenerationPerCapita"]]
result_table_renewable.columns = ["Region", "TotalRenewableEnergyGeneration", "RenewableEnergyGenerationPerCapita", "PercentageOfTotalRenewableGenerationPerCapita"]

# Print or display the result table
print(result_table_renewable)
