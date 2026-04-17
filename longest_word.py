text=input("enter the sentence:-")
words=text.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print("longest word in sentence:-",longest)