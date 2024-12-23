n = 7654

#find the product of the digits of this number

# method 1
p = (n // 1000) + (n % 1000 // 100) + (n % 100 // 10) + (n % 10)
print(p)

# method 2
s = str(n)
p = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
print(p)

# write the number in reverse order

s = str(n)
reverse_s = s[::-1]
print(reverse_s)

# in ascending order, you need to sort the numbers included in the given number

sorted_s = ''.join(sorted(s))
print(sorted_s)
