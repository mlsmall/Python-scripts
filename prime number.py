# Function to give you a list of prime numbers

def isPrime(num):
    primelist = []
    for i in range(2, num):
        if num % i == 0:
            primelist.append(1)
        else:
            continue
           
    if len(primelist) > 0:
        return False
    else:
        return True
    
    
for i in range(1, 100):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()