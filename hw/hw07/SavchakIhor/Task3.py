def number_char():
    characters_dict = {}
    word = input('Please, enter something: ')
    for char in word:
        characters_dict[char] = characters_dict.get(char, 0) + 1
    return characters_dict


result = number_char()
print(result)
