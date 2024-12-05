print("""Task3. Write a function that calculates the number of characters 
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}""")


def num_char(word):
    dic={}
    for c in word:
        dic[c] = dic.get(c, 0) + 1
    return(dic)
    
        

user_input=input("Enter any string:\n")

print(num_char(user_input))