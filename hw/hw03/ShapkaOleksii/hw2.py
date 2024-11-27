number = int(input("Enter four-digit number: "))
digits = [int(digit) for digit in str(number)]

#Product of digits
print("Product of digits =", digits[0]*digits[1]*digits[2]*digits[3])

#Reverse order
reversed_number = int(str(number)[::-1])
print("Reverse order =",reversed_number)

#Sorting number
print("sorted =", int("".join(sorted(str(number)))) )