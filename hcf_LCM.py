a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
x=a
y=b
while b!=0:
    a,b=b,a%b
hcf=a 
lcm=(x*y)//hcf
print("hcf is",hcf)
print("lcm is",lcm)