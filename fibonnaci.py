def fibonacci(n, fib={}):
    if n in fib: # base condintion
        return fib[n]
    if n <=1:
        return n
    result = fibonacci(n-1, fib)+ fibonacci(n-2,fib)
    fib[n]= result
    return result

n= int(input("enter the number: "))
print(f"the fibonnaci series is : {fibonacci(n)}")