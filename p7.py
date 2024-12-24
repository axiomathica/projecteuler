from math import sqrt, floor

#List of primes that will be updated everytime a new prime is found (2 is ignored as we will ignore all even numbers)
primes = [3]
#Count starts at 2 because 2 and 3 are two primes
count = 2 
n = primes[0]

while count<10001:
    n += 2
    max = floor(sqrt(n))
    is_prime = True

    for i in primes:
        if i>max:
            break
        if n%i==0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)
        count += 1

print(primes[-1])



