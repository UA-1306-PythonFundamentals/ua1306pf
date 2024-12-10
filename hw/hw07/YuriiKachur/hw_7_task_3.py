def count_characters(input_string):
    """
    Counts the number of occurrences of each character in a given string
    and groups them by type (letters, digits, and other symbols).

    Parameters:
    input_string (str): The string to be analyzed.

    Returns:
    dict: A dictionary with three groups ('letters', 'digits', 'others'),
          each containing a dictionary with characters as keys and their counts as values.
    """
    grouped_char_count = {
        'letters': {},
        'digits': {},
        'others': {}
    }

    for char in input_string:
        if char.isalpha():  # Перевіряємо, чи символ є буквою
            grouped_char_count['letters'][char] = grouped_char_count['letters'].get(char, 0) + 1
        elif char.isdigit():  # Перевіряємо, чи символ є цифрою
            grouped_char_count['digits'][char] = grouped_char_count['digits'].get(char, 0) + 1
        else:  # Усі інші символи (пробіли, знаки пунктуації тощо)
            grouped_char_count['others'][char] = grouped_char_count['others'].get(char, 0) + 1

    return grouped_char_count


def print_grouped_characters(grouped_char_count):
    """
    Prints grouped characters and their counts in a vertical format.

    Parameters:
    grouped_char_count (dict): A dictionary containing groups ('letters', 'digits', 'others'),
                               each with character counts.
    """
    for group_name, characters in grouped_char_count.items():
        print(f"\n{group_name.capitalize()} (total: {sum(characters.values())}):")
        for char, count in characters.items():
            print(f"  '{char}': {count}")


# Example
input_string = "1233124_Lorem ipsum dolor sit amet_^^^$^%("
grouped_char_count = count_characters(input_string)
print(f"Character count in '{input_string}':")
print_grouped_characters(grouped_char_count)
