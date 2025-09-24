def palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
n= int(input("enter the number: "))
if palindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")