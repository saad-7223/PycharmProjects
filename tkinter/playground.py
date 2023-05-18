# the below function cab=n take unlimited arguments
# these arguments are called POSITIONAL arguments
def add(*args):
    # basically this function adds all the given arguments and returns the sum
    sum = 0
    for i in args:
        sum += i
    return sum

