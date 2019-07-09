# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    string1, string2 = text.split(' ')
    if string1[0] == string2[0]:
        return True
    else:
        return False