# def nth_smallest(arr, n):
    
#     if n > len(arr):
#         return None
#     else:
#         arr.sort()
#         return arr[n-1]


# arr =[1,7,4]

# arr.sort()
# print(arr)


# def add_indexes(numbers):
    
#     result = []  # This will store the modified values
#     for index, value in enumerate(numbers):
#         result.append(index*value)
#     return result


# def probability(lst, num):
    
#     favourable = [x for x in lst if x >= num]
    
#     total = len(lst)
    
#     probability = 100 * len(favourable) / total
    
#     return probability



# print(probability([12,343,12312],4))





# def remove_strings(lst):


#     filtered_list = [x for x in lst if isinstance(x, int) and x >= 0]

#     unique_list = []
#     seen = set()

#     for num in filtered_list:
#         if num not in seen:
#             unique_list.append(num)
#             seen.add(num)
#     return unique_list



# def find_odd(lst):
    
    
    
    
#     counts = {}
    
# # Loop through the list to count occurrences
#     for num in lst:
#         if num in counts:
#             counts[num] += 1  # Increment count if the number is already in the dictionary
#         else:
#             counts[num] = 1  # Initialize count to 1 if it's not in the dictionary
#             filtered_list = [x for x in lst if isinstance(int) and counts[num]=1]


# 1 even
def find_odd(lst):
     
    filtered_list = [x for x in lst if x % 2 ==0 ]     
    
    return filtered_list

print(find_odd([1,2,3,43,2]))       


# 2 odd 
def find_odd(lst):
     
    filtered_list = [x for x in lst if x % 2 == 0 and x % 3 == 0]  
    
    return filtered_list

    print(find_odd([1,2,3,43,2]))  



# 3 that are not devisible by 2 and 3

def find_odd(lst):
     
    filtered_list = [x for x in lst if x % 2! == 0 and x % 3! == 0]  
    
    return filtered_list

    print(find_odd([1,2,3,43,2])) 