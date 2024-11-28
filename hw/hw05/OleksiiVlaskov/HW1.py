print('''Task1. Create a list that contains elements of integer type, then use 
the loop to change the type of these elements to a floating type.

''')
list1=[2,1,3,4,5,6,7,8]
# list2=[]
# for a in list1:
#     list2.append(float(a))

# print(f"{list2=}, where objects {type(list2[0])=} ")
    
for a, b in enumerate(list1):
    list1[a]=float(b)
print(list1)
