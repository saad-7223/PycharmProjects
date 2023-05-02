import pandas as pd

# accessing data fom csv file
data = pd.read_csv("weather_data.csv")
temp = data['temp'].to_list()

# getting max temp fom data
maximum = data['temp'].max()

# coveting celsius data to fahrenheit
friday = (data[data.day == 'Friday']).temp
cal_to_fahrenheit = (friday * (9 / 5)) + 32

# creating dataframe from scratch
student = {
    "names": ['saad', 'saarif', 'tazkiya', 'ajmal'],
    "marks": [25, 50, 60, 50]
}
student_data = pd.DataFrame(student)
student_data.to_csv("student.csv")

