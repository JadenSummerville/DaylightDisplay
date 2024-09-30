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
        axs[index].bar(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], self.getSunMonths())
        axs[index].set_title(self.getCityName() + ' (' + str(round(float(self.getLatitude()))) + ' degrees N latitude)')
        axs[index].set_ylabel('Mean daylight\nhours per day', rotation=0, labelpad=50)
        axs[index].set_ylim(0, 12)

        print(self.cityName, self.longitude, self.latitude)
        for i in range(12):
            print(i, ":", self.sunHoursList[i])
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

fig, axs = plt.subplots(len(cityList), 1, figsize=(10, 1000))
for i in range(len(cityList)):
    cityList[i].display(i)

# Display the graph
#plt.tight_layout()
plt.suptitle('Does High Latitude Extend Summer Daylight Hours And Decrease Winter Daylight Hours?', fontsize=20)
plt.subplots_adjust(hspace=1)
plt.show()
print("Test")