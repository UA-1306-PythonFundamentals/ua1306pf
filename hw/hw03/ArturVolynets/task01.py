zen_of_python = (
    "The Zen of Python, by Tim Peters. "
    "Beautiful is better than ugly. "
    "Explicit is better than implicit. "
    "Simple is better than complex. "
    "Complex is better than complicated. "
    "Flat is better than nested. "
    "Sparse is better than dense. "
    "Readability counts. "
    "Special cases aren't special enough to break the rules. "
    "Although practicality beats purity. "
    "Errors should never pass silently. "
    "Unless explicitly silenced. "
    "In the face of ambiguity, refuse the temptation to guess. "
    "There should be one-- and preferably only one --obvious way to do it. "
    "Although that way may not be obvious at first unless you're Dutch. "
    "Now is better than never. "
    "Although never is often better than *right* now. "
    "If the implementation is hard to explain, it's a bad idea. "
    "If the implementation is easy to explain, it may be a good idea. "
    "Namespaces are one honking great idea -- let's do more of those!"
)

# number of occurrences of the words

word_count = zen_of_python.count("better")
print(f"The word BETTER appears in Zen Of Python {word_count} times.")

word_count = zen_of_python.count("never")
print(f"The word NEVER appears in Zen Of Python {word_count} times.")

word_count = zen_of_python.count("is")
print(f"The word IS appears in Zen Of Python {word_count} times.")

# display all text in uppercase

print(zen_of_python.upper())

# replace all occurrences of the symbol "i" with "&"

zen_of_python = zen_of_python.replace("i", "&")
print(zen_of_python)
