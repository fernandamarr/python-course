# Functions #9: pick evens
# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

def myfunc(*args):
    list = []
    for num in args:
        if num % 2 == 0:
            list.append(num)
    return list
    