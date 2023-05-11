# Learning about the dictionary comprehension
# syntax : new_dict = {new_key:new_value for item in list}
# syntax : new_dict = {new_key:new_value for (key,value) in dict.items()}
# new challenge
weather_c = {
    'monday': 12,
    'tuesday': 14,
    'wednesday': 15,
    'thursday': 14,
    'friday': 21,
    'saturday': 22,
    'sunday': 24
}
# task :  convert each temp to fahrenheit
# formula = (temp_c * 9/5)+ 32
# twist : no using direct dictionary

# step 1: creating a dictionary
# list_of_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
fahren_temp = {day: round(((temp_c * (9 / 5)) + 32), 2) for (day, temp_c) in weather_c.items()}
for k, v in fahren_temp.items():
    print(k, v)
