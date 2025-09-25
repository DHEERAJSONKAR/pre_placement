def armstrong(num):
    digit = str(num)
    power = len(digit)
    total = sum(int(d) ** power for d in digit)
    return total == num


def armstrong_series(limit):
    armstrong_numbers = []
    for num in range(limit + 1):
        if armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


num = int(input("enter the number: "))
if armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

limit = int(input("enter the limit: "))
print(f"Armstrong numbers up to {limit}: {armstrong_series(limit)}")
