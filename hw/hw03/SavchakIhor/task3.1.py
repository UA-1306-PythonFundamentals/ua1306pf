zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# Counting words
word_counts = {word: zen.count(word) for word in ["better", "never", "is"]}
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Uppercasing the text
zen_upper = zen.upper()
print("\nUPPER CASE:")
print(zen_upper)

# Replacing "i" with "&"
zen_replaced = zen.replace("i", "&")
print("\nREPLACED:")
print(zen_replaced)

number = 2645

# Product of digits
from functools import reduce
product = reduce(lambda x, y: x * y, map(int, str(number)))
print(f"\nProduct of digits: {product}")

# Reverse the number
reverse_number = int(str(number)[::-1])
print(f"Reversed number: {reverse_number}")

# Sort digits in ascending order
sorted_number = int(''.join(sorted(str(number))))
print(f"Sorted number: {sorted_number}")


# Interchanging variables
a, b = "A value", "B value"
a, b = b, a
print(f"\nAfter swapping:\na = {a}\nb = {b}")
