#Subtask 1
number = input("Please enter a four-digit natural number: ")
product = 1
for i in number:
    product = product * int(i)
print("Product of number", product)

#Subtaks 2 
new_list = []
for i in number:
    new_list += i
reversed_list = reversed(new_list)
right_order_list = []
for j in reversed_list:
    right_order_list.append(j)
revert_list_to_string = "".join(right_order_list)
print(revert_list_to_string)

#Subtask 3
new_string = []
for i in number:
    new_string += i
new_string.sort()
new_string2 = "".join(new_string)
print("Ascending order of digits in number", new_string2)
