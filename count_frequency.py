text=input("enter the string:-")
count={}
for ch in text:
    count[ch]=count.get(ch,0)+1
print("frequency",count)