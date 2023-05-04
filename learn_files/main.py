import pandas as pd

# # accessing data fom csv file
# data = pd.read_csv("weather_data.csv")
# temp = data['temp'].to_list()
#
# # getting max temp fom data
# maximum = data['temp'].max()
#
# # coveting celsius data to fahrenheit
# friday = (data[data.day == 'Friday']).temp
# cal_to_fahrenheit = (friday * (9 / 5)) + 32
#
# # creating dataframe from scratch
# student = {
#     "names": ['saad', 'saarif', 'tazkiya', 'ajmal'],
#     "marks": [25, 50, 60, 50],
#     "grade": ['c', 'b', 'a', 'b']
# }
# student_data = pd.DataFrame(student)
# student_data.to_csv("student.csv")

# making a table of different furs and their count

# reads the csv file
squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# creates a dataframe to work on
squirrel_data = pd.DataFrame(squirrel)

# gets the Primary fur color and its counts
task = squirrel_data['Primary Fur Color'].value_counts()

# convert to csv file
task.to_csv("squirrel_count.csv")
