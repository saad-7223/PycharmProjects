# # LIST COMPREHENSION
# # syntax : new_list = [new_item for item in numbers]
# # example
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# # print(new_list)
# # the above code is using list comprehension
#
# # Now using the normal methord
# no = [1, 2, 3]
# new_l = []
# for number in no:
#     add = number + 1
#     new_l.append(add)
# # print(new_l)
# # this is pretty lengthy ....
#
# # trying with strings
#
# name = 'fur'
# l = [letter for letter in name]
# # print(l)
#
# # trying angela's challenge
# x = [a * 2 for a in range(1, 5)]
# # the above list comprehension will double the given numbers value
# # print(x)
#
# # learning about the conditional list comprehension
# # Syntax : new_list = [new_item for item in list if test]
# names = ['alex', 'betty', 'dave', 'caroline']
# newl = [let.upper() for let in names if len(let) > 5]
# # print(newl)
#
# # challenge 3
# num = [1, 1, 2, 3, 8, 13, 21, 34, 55]
# squared_list = [i * i for i in num]
# # print(squared_list)
# result = [j for j in num if j % 2 == 0]
# # print(result)
#
# # challenge 5 : look inside file1 and file2 , they contain a bunch of numbers
# # your task is to create a list called result which contains the numbers that are common in both files

with open("file1.txt", mode='r') as f1:
    num_f1 = f1.readlines()

with open('file2.txt', mode='r') as f2:
    num_f2 = f2.readlines()

num_result = [int(r) for r in num_f1 if r in num_f2]
print(num_result)
