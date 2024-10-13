import csv
from collections import defaultdict
import matplotlib.pyplot as plt

# Define population data for both cities
population_data_chicago = {
    2020: 2743329,
    2021: 2704101,
    2022: 2672660,
    2023: 2664452
}

population_data_los_angeles = {
    2020: 3895848,
    2021: 3832573,
    2022: 3822782,
    2023: 3820914
}

# Function to count total crimes from a CSV file
def count_crimes(file_path, city='chicago'):
    crime_counts = defaultdict(int)
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            if city == 'chicago':
                year = int(row['Year'])
            else:  # For Los Angeles
                date_occ = row['DATE OCC']  # Get the date of occurrence
                year = int(date_occ.split('/')[2].split()[0])  # Extract year from 'MM/DD/YYYY HH:MM:SS AM/PM'

            # Count only if the year is in either population data
            if year in population_data_chicago or year in population_data_los_angeles:
                crime_counts[year] += 1

    return crime_counts

# Count crimes in Chicago and Los Angeles
chicago_crime_counts = count_crimes(r"C:\Users\jaden\Downloads\Crimes_-_2001_to_Present.csv", city='chicago')
los_angeles_crime_counts = count_crimes(r"C:\Users\jaden\Downloads\Crime_Data_from_2020_to_Present_Los_An.csv", city='los_angeles')

# Calculate crime per capita for each city and each year
crime_per_capita_chicago = {year: chicago_crime_counts[year] / population_data_chicago[year] for year in population_data_chicago}
crime_per_capita_los_angeles = {year: los_angeles_crime_counts[year] / population_data_los_angeles[year] for year in population_data_los_angeles}

# Prepare data for plotting
years = list(population_data_chicago.keys())
chicago_rates = [crime_per_capita_chicago[year] for year in years]
la_rates = [crime_per_capita_los_angeles[year] for year in years]

# Plotting the comparison
plt.figure(figsize=(10, 6))

plt.plot(years, chicago_rates, marker='o', label='Chicago', color='blue')
plt.plot(years, la_rates, marker='o', label='Los Angeles', color='orange')

plt.title('Crime Rate Per Capita Comparison: Chicago vs Los Angeles (2020-2023)\nIs the cold and crime correlated?')
plt.xlabel('Year')
plt.ylabel('Crimes per Capita')
plt.xticks(years)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='City')
plt.tight_layout()

# Save the plot
plt.savefig('crime_rate_comparison.png')
plt.show()
