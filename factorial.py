def fact(n):
    if n<0:
        return "factorial not possible"
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n= int(input("enter the number: "))
print(f"the factorial of {n} is : {fact(n)}")