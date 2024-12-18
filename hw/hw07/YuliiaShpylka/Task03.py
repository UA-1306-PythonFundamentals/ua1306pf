def count_charect(word):
    """This function calcualtes the number of characters in word"""

    new_dict = {}
    for char in word:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1

    return new_dict
    


text = "Sometestword"
print(count_charect(text))

      
