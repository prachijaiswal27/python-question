num=int(input('enter the number:-'))
temp=num
sum=0
n=len(str(num))
while num>0:
    digit=num%10
    sum+=digit**n
    num=num//10
if sum==temp:
    print("number is armstrong")
else:
    print("Not")