text=input("enter the string:-")
count={}
for ch in text:
    count[ch]=count.get(ch,0)+1
for ch in text:
    if count[ch]==1:
        print("first non-repeating character",ch)
        break
else:
    print("no non repeating chara found ")
