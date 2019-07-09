# Functions # 10: Skyline
# Define a function called myfunc that takes in a string, returns a matching string where every even letter is uppercase, and every odd letter is lowercase

def myfunc(string):
    result = ''
    for idx, ch in enumerate(string):
        if idx % 2 == 0:
            result += ch.upper()
        else:
            result += ch.lower()
    return result