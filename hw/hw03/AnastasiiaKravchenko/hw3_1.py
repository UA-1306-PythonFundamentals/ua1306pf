# TODO: - Count the number of occurrences of the word "better", "never", "is" in the text below.
#       - Uppercase the text.
#       - Replace all "i" with "&".

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

better_num = zen.count('better')
never_num = zen.count('never')
is_num = zen.count('is')
print(f'better: {better_num}\nnever: {never_num}\nis: {is_num}\n')

zen_upper = zen.upper()
print(f'UPPER CASE:\n{zen_upper}\n')

zen_replaced = zen.replace('i', '&')
print(f'REPLACED:\n{zen_replaced}')


# TODO: - Find the product of the digits of the number.
#       - Reverse number.
#       - Sort the digits of the number in ascending order.

number = 4738
product = 4*7*3*8
print(f'Product: {product}\n')

reverse_number = int(str(number)[::-1])
print(reverse_number)

sorted_number = int(''.join(sorted(str(number))))
print(sorted_number)


# TODO: - Interchange the values of the variables.
a = 'A value'
b = a
print(f'b = {b}')
b = 'B value'
a = b
print(f'a = {a}\n')


# Other option
a = 'A value'
b = 'B value'
a, b = b, a
print(f'a = {a}\nb = {b}\n')
