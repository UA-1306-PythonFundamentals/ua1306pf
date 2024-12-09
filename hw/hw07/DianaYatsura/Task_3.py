characters_dict = {}

def number_char():
    word = list(input('Please, enter smth '))
    for el in list(word):
        characters_dict[el]=word.count(el)


number_char()
print(characters_dict)