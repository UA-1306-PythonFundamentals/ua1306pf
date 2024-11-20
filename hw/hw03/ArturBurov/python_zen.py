zen_of_python = """Beautiful is better than ugly
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
Namespaces are one honking great idea -- let's do more of those!"""


def analyze_zen(text):
    # 1. Count occurrences of "better", "never", "is"
    words = text.split()
    better_count = words.count("better")
    never_count = words.count("never")
    is_count = words.count("is")

    # 2. Convert text to uppercase
    uppercase_text = text.upper()

    # 3. Replace all "i" with "&"
    modified_text = text.replace("i", "&")

    print(f"Number of occurrences of 'better': {better_count}")
    print(f"Number of occurrences of 'never': {never_count}")
    print(f"Number of occurrences of 'is': {is_count}\n")
    print(f"Uppercase text:\n{uppercase_text}\n")
    print(f"Modified text:\n{modified_text}")


analyze_zen(zen_of_python)
