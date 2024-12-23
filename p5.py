import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def even_div(n):
    num = 1
    for i in range(2,n+1):
        if is_prime(i):
            num *= i**math.floor(math.log(n,i))
    return num      

print(even_div(20))
