import csv

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
r = pandas.read_csv('nato_phonetic_alphabet.csv')
phone_frame = pandas.DataFrame(r)
new_dict = {}

for (index, row) in phone_frame.iterrows():
    new_dict[row.letter] = row.code

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word : ").upper()

# using the list comprehension to create a list of phonetic codes
phonetic_codes = [row.code for letters in word for (index, row) in phone_frame.iterrows() if letters == row.letter]
print(phonetic_codes)