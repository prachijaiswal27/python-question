array=[2,3,4,5,6,7]
even=0
odd=0
for num in array:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("even count",even)
print("odd count",odd)