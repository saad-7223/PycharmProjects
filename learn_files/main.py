file = open("my_file.txt", mode="a")
file.write("but still he is my cute lil brother ..:)")
with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
file.close()
