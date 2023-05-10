# Learning about the dictionary comprehension
# syntax : new_dict = {new_key:new_value for item in list}
# syntax : new_dict = {new_key:new_value for (key,value) in dict.items()}
import random

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
new_dict = {students: random.randint(10, 100) for students in names}
print(new_dict)
pass_dict = {key: value for (key, value) in new_dict.items() if value > 60}
print(pass_dict)