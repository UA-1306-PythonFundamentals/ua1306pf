import this
import codecs
zen_of_python = str(codecs.decode(this.s, 'rot13'))


print(f"<{'='*60}>\n<{'='*60}>")
print("1.1 - find separately the number of occurrences of the words - 'better', 'never' and 'is' in the given line")
print(f"<{'='*60}>\n<{'='*60}>\n\n")
input_line=input("""Give me the line from zen of python
printed above and i find for you number
of occurrences of the words - 'better', 'never' and 'is'
in the given line:
""")
words=['better','never','is']
lines_of_zen = zen_of_python.splitlines()
if input_line in lines_of_zen:
    for a in words:
        print(f"There is an: {input_line.count(a)} occurence of word '{a}'")
else:
    print(f"There are no line like: {input_line} in zen of python")
    
    
print(f"\n\n<{'='*60}>\n<{'='*60}>")
print("1.2 - you need to display all text in uppercase (all letters in uppercase)")
print(f"<{'='*60}>\n<{'='*60}>\n\n")
input("Press enter to proceed")
print(zen_of_python.upper())


print(f"\n\n<{'='*60}>\n<{'='*60}>")
print("1.3 replace all occurrences of the symbol “i” with “&”")
print(f"<{'='*60}>\n<{'='*60}>\n\n")
input("Press enter to proceed")
print(zen_of_python.replace('i','&'))

