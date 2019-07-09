def myfunc(string):
    result = ''
    for idx, ch in enumerate(string):
        if idx % 2 == 0:
            result += ch.upper()
        else:
            result += ch.lower()
    return result