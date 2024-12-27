from math import sqrt, floor

def isPrime(n):
    if n==1:
        return False
    elif n<4:
        return True
    elif n%2==0:
        return False
    elif n<9:
        return True
    elif n%3==0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        while f<=r:
            if n%f==0:
                return False
            if n%(f+2)==0:
                return False
            f += 6
    return True

sum = 0
for i in range(2,2000000):
    if isPrime(i):
        sum += i
print(sum)   

