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

# 1. Merge the necessary DataFrames based on the common column "CountryName"
merged_installed_capacity = pd.merge(installed_capacity, country_classifications, on="CountryName")
merged_population = pd.merge(population_data, country_classifications, on="CountryName")

# 2. Filter installed capacity data for the year 2021
installed_capacity_2021 = merged_installed_capacity[merged_installed_capacity["Year"] == 2021]

# 3. Calculate the total installed capacity per region
total_installed_capacity_per_region = installed_capacity_2021.groupby("Region")["InstalledElectricityCapacity"].sum().reset_index()

# 4. Calculate the total population per region
total_population_per_region = merged_population.groupby("Region")["2021"].sum().reset_index()

# 5. Calculate installed capacity per capita for each region
capacity_per_capita = pd.merge(total_installed_capacity_per_region, total_population_per_region, on="Region")
capacity_per_capita["InstalledCapacityPerCapita"] = capacity_per_capita["InstalledElectricityCapacity"] / capacity_per_capita["2021"]

# 5. Calculate the percentage of each region's ElectricityGenerationPerCapita relative to the total electricity generation per capita
total_electricity_capacity = total_installed_capacity_per_region["InstalledElectricityCapacity"].sum()
total_electricity_capacity_percapita = capacity_per_capita["InstalledCapacityPerCapita"].sum()
capacity_per_capita["PercentageOfTotalCapacityPerCapita"] = (capacity_per_capita["InstalledCapacityPerCapita"] / total_electricity_capacity_percapita) * 100

# 6. Round the percentages to two decimal places (if needed)
# capacity_per_capita["InstalledCapacityPerCapita"] = capacity_per_capita["InstalledCapacityPerCapita"].round(2)

# 7. Merge with the existing result table
result_table = capacity_per_capita[["Region", "InstalledElectricityCapacity", "InstalledCapacityPerCapita", "PercentageOfTotalCapacityPerCapita"]]

# Print or display the updated result table
print(result_table)