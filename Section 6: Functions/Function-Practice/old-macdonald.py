# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name   
# old_macdonald('macdonald') --> MacDonald
    
def old_macdonald(name):
    name = name.capitalize()
    name = list(name)
    name[3] = name[3].capitalize()
    name = ''.join(name)
    return name


# shorter version

def old_macdonald(name):
    return name[0].capitalize() + name[1:3] + name[3].capitalize() + name[4:]