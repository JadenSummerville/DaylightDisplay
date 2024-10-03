import csv
import matplotlib.pyplot as plt
#import numpy as np
class City:
    def __init__(self, cityName, longitude, latitude):
        if not isinstance(cityName, str):
            raise ValueError("cityName not valid")
        self.cityName = cityName
        self.longitude = longitude
        self.latitude = latitude
        self.sunHoursList = [0]*12
    def getCityName(self):
        return self.cityName
    def getLongitude(self):
        return self.longitude
    def getLatitude(self):
        return self.latitude
    def setSunMonths(self, i, num):
        days = 0
        i = int(i)
        if i == 1:
            days = 28
        elif i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
            days = 31
        elif i == 3 or i == 5 or i == 8 or i == 10:
            days = 30
        else:
            raise ValueError("Invalid month " + str(i))
        self.sunHoursList[int(i)] = int(num)/days
    def getSunMonths(self):
        return self.sunHoursList
    def display(self, index):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # Define two alternating colors for month labels
        month_colors = ["#1f77b4", "#d62728"]  # Dark blue and dark red

        axs[index].bar(months, self.getSunMonths(), color="skyblue")  # Keep bar colors uniform
        axs[index].set_title(self.getCityName() + ' (' + str(round(float(self.getLatitude()))) + ' degrees N latitude)')
        
        if index % 3 == 0:  # Only show ylabel for the leftmost plots
            axs[index].set_ylabel('Mean daylight\nhours per day', rotation=0, labelpad=50)
        else:
            axs[index].set_ylabel('')  # No label for other subplots

        axs[index].set_ylim(0, 12)

        # Rotate month labels and color them in alternating colors
        axs[index].set_xticklabels(months, rotation=45, ha="right", color="black")
        
        # Apply alternating colors to the tick labels (month names)
        for i, tick_label in enumerate(axs[index].get_xticklabels()):
            tick_label.set_color(month_colors[i % 2])
        #axs[index].bar(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], self.getSunMonths())
        #axs[index].set_title(self.getCityName() + ' (' + str(round(float(self.getLatitude()))) + ' degrees N latitude)')
    
        #if index % 3 == 0:  # Only show ylabel for the leftmost plots
        #    axs[index].set_ylabel('Mean daylight\nhours per day', rotation=0, labelpad=50)
        #else:
        #    axs[index].set_ylabel('')  # No label for other subplots
        #axs[index].set_ylim(0, 12)
def getCities(fileName, cities):
    with open(fileName, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file) 
        # Iterate over each row in the CSV file
        for row in csv_reader:
            if row[0] == 'city':
                continue
            if row[0] in cities:
                cities[row[0]].setSunMonths(row[4], row[5])
            else:
                city = City(row[0], row[1], row[2])
                city.setSunMonths(row[4], row[5])
                cities[row[0]] = city
fileName = 'sunshine.csv'
cities = dict()
cityList = []
getCities(fileName, cities)
for city in cities:
    cityList.append(cities[city])
cityList = sorted(cityList, key=lambda x: x.getLatitude())

#fig, axs = plt.subplots(len(cityList), 1, figsize=(10, len(cityList) * 3))

rows = (len(cityList) + 2) // 3  # Adjust rows based on number of cities
fig, axs = plt.subplots(rows, 3, figsize=(15, 5 * rows))  # Adjust figure size based on rows
axs = axs.flatten()  # Flatten the 2D array of subplots to 1D for easier iteration

for i in range(len(cityList)):
    cityList[i].display(i)

# Display the graph
#plt.tight_layout()
plt.suptitle('Does High Latitude Extend Summer Daylight Hours And Decrease Winter Daylight Hours?', fontsize=20)
plt.subplots_adjust(hspace=0.6)

plt.savefig('daylight_hours.pdf', bbox_inches='tight')

plt.show()
print("Test")