# First task from the lecture

ban_list_word = input().split()
text = input()

for word in ban_list_word:
    text = text.replace(word, '*' * len(word))
    
print(text)    

# Second task from me

