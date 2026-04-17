arr=[2,4,6,8,9]
max=arr[0]
min=arr[0]
for num in arr:
    if num>max:
        max=num
    if num<min:
        min=num
print("max element",max)
print("min element",min)
    