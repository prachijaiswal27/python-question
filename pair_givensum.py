array=[2,3,4,5,6,7]
target=9
seen=set()
pair=[]
for num in array:
    complement=target-num
    if complement in seen:
        pair.append((complement,num))
    seen.add(num)
print("pair",pair)