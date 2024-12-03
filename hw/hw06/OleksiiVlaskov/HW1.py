list_even=[]
list_odd=[]
list_none=[]
for a in range(1,10):
    if a%2 == 0:
        list_even.append(a)
    if a%2 != 0 and a%3 == 0:
        list_odd.append(a)
    if a%2 != 0 and a%3 != 0:
        list_none.append(a)
print(f"{list_even=}{list_odd=}{list_none=}")


#ANother way
# list_even=[]
# list_odd=[]
# list_none=[]
# for a in range(1,10):
#     if a%2 == 0:
#         list_even.append(a)
#     elif a%3 == 0:
#         list_odd.append(a)
#     else:
#         list_none.append(a)
# print(f"{list_even=}{list_odd=}{list_none=}")