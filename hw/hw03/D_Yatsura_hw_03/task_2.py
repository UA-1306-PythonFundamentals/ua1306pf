# print (2024 % 10)
# print (2024 // 10 % 10)
# print (2024 // 100 % 10)
# print (2024 // 1000 % 10)

number = list(input("Please, input a four-digit natural number "))

#task 2.1
print ('The product of the digits =', int(number[0])*int(number[1])*int(number[2])*int(number[3]))

# task 2.2
number.reverse()
print ('Reverse order', ''.join(number))

# task 2.3
number.sort()
print('Ascending order', ''.join(number))