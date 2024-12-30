number_input=input("What is your number?")

# Перевірка на те чи введено чотиризначне число
if not number_input.isdigit() or len(number_input) != 4:
    print("Please, enter a four-digit number!")
# Випадок, якщо починаеться з нуля. Такий самий як для інших випадків, тільки з додатковим коментарем
elif number_input[0]=='0':
    print("Ok, you can do it this way too")
    num1=int(number_input[0])
    num2=int(number_input[1])
    num3=int(number_input[2])
    num4=int(number_input[3])
    print("Product of digits:", num1*num2*num3*num4)
    print("Reverce:", number_input[::-1])
    sorted_digits = ''.join(sorted(number_input))
    print("Sort:", sorted_digits)
# Множення цифр, зворотне число, відсортоване число
else:
    num1=int(number_input[0])
    num2=int(number_input[1])
    num3=int(number_input[2])
    num4=int(number_input[3])
    print("Product of digits:", num1*num2*num3*num4)
    print("Reverce:", number_input[::-1])
    sorted_digits = ''.join(sorted(number_input))
    print("Sort:", sorted_digits)
