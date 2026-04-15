text=input("enter the  alphabat:-")
vowels=0
consonat=0
for char in text:
    if char.isalpha():
        if char in "aeiouAEIOU":
            vowels+=1
        else:
            consonat+=1
print("vowels",vowels)
print("consonat",consonat)