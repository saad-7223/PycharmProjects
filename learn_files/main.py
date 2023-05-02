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
# print(data)

# maximum = data['temp'].max()
# print(maximum)

friday = (data[data.day == 'Friday']).temp
cal_to_fahrenheit = (friday * (9 / 5)) + 32
# print(cal_to_fahrenheit)

# creating dataframe from scratch
student = {
    "names": ['saad', 'saarif', 'tazkiya', 'ajmal'],
    "marks": [25, 50, 60, 50]
}
student_data = pd.DataFrame(student)
student_data.to_csv("student.csv")

