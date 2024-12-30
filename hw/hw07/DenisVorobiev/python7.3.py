def count(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


input_string = input("Enter: ")
result = count(input_string)
print(result)