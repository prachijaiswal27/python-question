#prime number
num=int(input("enter the number:-"))
if num>1:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num,"not a prime")
            break
    else:
        print(num,"is prime")
else:
    print(num,"not a prime")