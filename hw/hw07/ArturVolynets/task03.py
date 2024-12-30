# Task3. Write a function that calculates the number of characters
# included in given string.
# • input: "hello"
# • output: {"h":1, "e": 1,"|":2,"0":1}

def words_symbols_counter(word):
    """
    Calculates the frequency of characters in the given string.

    Parameters:
    word (str): The input string to analyze.

    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    result = {}

    for symbol in word:
        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1

    return result


input_word = input("Enter your word: ")
output = words_symbols_counter(input_word)
print(f"Results: {output}")

