# LIST COMPREHENSION
# syntax : new_list = [new_item for item in numbers]
# example
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)
# the above code is using list comprehension

# Now using the normal methord
no = [1, 2, 3]
new_l = []
for number in no:
    add = number + 1
    new_l.append(add)
print(new_l)
# this is pretty lengthy ....

# trying with strings

name = 'fur'
l = [letter for letter in name]
print(l)

# trying angela's challenge
x = [a * 2 for a in range(1, 5)]
# the above list comprehension will double the given numbers value
print(x)

# learning about the conditional list comprehension
# Syntax : new_list = [new_item for item in list if test]
names = ['alex', 'betty', 'dave', 'caroline']
newl = [let.upper() for let in names if len(let) > 5]
print(newl)

# challenge 3
num = [1, 1, 2, 3, 8, 13, 21, 34, 55]
squared_list = [i * i for i in num]
print(squared_list)
result = [j for j in num if j % 2 == 0]
print(result)
