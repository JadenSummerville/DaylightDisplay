import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Define the population data for each year
population_data = {
    2020: 2743329,
    2021: 2704101,
    2022: 2672660,
    2023: 2664452
}

# Initialize a dictionary to count crimes by year and month
crime_counts = defaultdict(int)

# Load the CSV file and count crimes by month
with open(r"C:\Users\jaden\Downloads\Crimes_-_2001_to_Present.csv", mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        year = int(row['Year'])
        if year in population_data:
            date = row['Date']
            month = int(date.split('/')[0])  # Extract month from the date
            crime_counts[(year, month)] += 1

# Prepare data for plotting
months = list(range(1, 13))
years = list(population_data.keys())
monthly_crimes = {year: [0] * 12 for year in years}

# Fill the monthly crime data
for (year, month), count in crime_counts.items():
    monthly_crimes[year][month - 1] = count  # month - 1 for 0-based indexing

# Calculate crime per capita for each month
monthly_crime_per_capita = {
    year: [monthly_crimes[year][month - 1] / population_data[year] if population_data[year] > 0 else 0 for month in months]
    for year in years
}

# Plotting the crime per capita
plt.figure(figsize=(12, 6))

for year in years:
    plt.plot(months, monthly_crime_per_capita[year], marker='o', label=str(year))

plt.title('Is heat and Crime Correlated?')
plt.xlabel('Month')
plt.ylabel('Crimes per Capita')
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Year')
plt.show()
