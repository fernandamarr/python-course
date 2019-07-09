def myfunc(*args):
    list = []
    for num in args:
        if num % 2 == 0:
            list.append(num)
    return list
    