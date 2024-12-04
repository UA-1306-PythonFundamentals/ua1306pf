def getProduct(num): 
  
    product = 1
  
    while (num != 0): 
        product = product * (num % 10) 
        num = num // 10
  
    return product 
  
num = 5467

ascending = "".join(sorted(str(num)))

print('Product number:', getProduct(num)) 
print('Reversed number:',str(num)[::-1])
print("Numbers sorted asc:", int(ascending))

