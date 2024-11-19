import re
print(f"<{'='*60}>\n<{'='*60}>")
print("""Home Task - 2
A four-digit natural number is specified: 
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number""")
print(f"<{'='*60}>\n<{'='*60}>\n\n")
natural_number=input("Specify four-figit natural number: ")
regex_match = re.fullmatch(r"\d{4}", natural_number)
if regex_match:
    digits = list(map(int, natural_number))
    product = 1
    for a in digits:
        product *= a
    print(f"Product of digits is: {product}")
    print(f"Number in reverse order is: {natural_number[::-1]}")
    sorted_number = sorted(natural_number)
    print(f"Sorted number in ascending order: {"".join(sorted_number)}")
    