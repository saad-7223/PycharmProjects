# import csv
#
# temperature = []
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1]!= "temp":
#             temperature.append(row[1])
# print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
temp = data['temp'].to_list()
print(data)
print(temp)
