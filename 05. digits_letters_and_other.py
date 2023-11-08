# First task from the lecture

text = input()

numbers = ''
strings = ''
characters = ''

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        strings += char
    else:
        characters += char
        
        
print(numbers)            
print(strings)            
print(characters)
            
# Second task from me

