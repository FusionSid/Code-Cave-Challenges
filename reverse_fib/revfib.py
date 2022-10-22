from functools import cache

start = int(input("Enter the start number: "))
stop = int(input("Enter the amount of numbers: "))

numbers = []

# @cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for num in range(stop):
    numbers.append(fib(start))
    start += 1

print("\n".join(str(i) for i in numbers[::-1]))
print("Sum: ", sum(numbers))