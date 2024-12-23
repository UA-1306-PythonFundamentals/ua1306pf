from collections import OrderedDict


def count_characters_order_preserved(string):
    """Counts character occurrences preserving original order."""
    if not string:
        return OrderedDict()

    char_counts = OrderedDict()
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return dict(char_counts)


input_string = "hello"
result = count_characters_order_preserved(input_string)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
