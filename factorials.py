# Function to calculate a factorial number

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

for n in range(1, 11):
    print(n, "->", factorialFun(n))