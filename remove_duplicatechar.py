text=input("enter the string:-")
seen=set()#ye duplicate value store nahi karta 
result=""
for ch in text:
    if ch not in seen:
        result+=ch
        seen.add(ch)
print("string without duplicate character:-",result)