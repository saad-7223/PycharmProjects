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

