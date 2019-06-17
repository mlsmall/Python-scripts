# This function will calculate the fibonacci sequence for any given number.

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 11):
    print(n, "->", fib(n))