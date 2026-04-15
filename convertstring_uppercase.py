text=input("enter the text:-")
result=""
for char in text:
    if "a"<= char <="z":
        result+=chr(ord(char)-32)
    else:
        result+=char
print("uppercase",result)
