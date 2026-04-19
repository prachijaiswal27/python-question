array=[2,7,4,5,6,3,8]
array=list(set(array))
array.sort()
if len(array)<2:
    print("no second largest found")
else:
    print("second largest",array[-2])