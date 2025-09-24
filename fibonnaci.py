def fibonacci(n, fib={}):
    if n in fib: # base condintion
        return fib[n]
    if n <=1:
        return n
    result = fibonacci(n-1, fib)+ fibonacci(n-2,fib)
    fib[n]= result
    return result
def fibonnaci_series(n):
    fib_series = []
    for i in range(n+1):
        fib_series.append(fibonacci(i))
    return fib_series
n= int(input("enter the number: "))
print(f"the fibonnaci series is : {fibonacci(n)}")
print(f"The Fibonacci series up to {n} is: {fibonnaci_series(n)}")