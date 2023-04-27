file = open("my_file.txt", mode="a")
file.write("but still he is my cute lil brother ..:)")
with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
file.close()
# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# print("Original array : \n", arr)
# print("Transpose array : \n", arr.T)
