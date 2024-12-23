def count_letters(s):
    letter_count = {}
    for letter in s:
        if letter.isalpha():  
            letter = letter.lower() 
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

text = "hello"
letter_counts = count_letters(text)
print("Letter counts:", letter_counts)