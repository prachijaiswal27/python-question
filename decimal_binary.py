def decimal_binary(n):
    if n==0:
        return 0
    result=""
    while n>0:
        reminder=n%2
        result=str(reminder)+result
        n=n//2
    return result
print(decimal_binary(13))