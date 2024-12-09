import math

primes = [2,3]

x = 600851475143
y = math.floor(math.sqrt(x))

for n in range(5, y+1, 2):
    
    s = math.floor(math.sqrt(n))
    is_prime = True

    for i in primes:
        if i > s:
            break
        if n%i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)

l = len(primes)

for i in range(1, l+2):
    if x%primes[l-i]==0:
        print(primes[l-i])
        break
    

#*****************************************************#

def largest_prime_factor(n):
    # Remove factors of 2
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 2  # if n was 2^k, the largest prime factor is 2
    
    largest_factor = 1
    
    # Check odd factors from 3 upwards
    factor = 3
    max_factor = math.isqrt(n)  # Integer square root of n
    
    while factor <= max_factor:
        while n % factor == 0:
            n //= factor
            largest_factor = factor
            max_factor = math.isqrt(n)  # Update max_factor because n has changed
        
        factor += 2  # Move to the next odd number

    # If n is still greater than 1, then n itself is a prime factor
    if n > 1:
        largest_factor = n
    
    return largest_factor

# Example Usage
n = 600851475143
print(largest_prime_factor(n))  # Output: 6857