from math import sqrt, floor

def countDiv(n):
    count = 0
    max = floor(sqrt(n))
    for i in range(1,max):
        if n%i==0:
            count+=2
    if n%max==0:
        count+=1
    return count

def triangle(max_div):
    n = 1
    triangle = int(n*(n+1)/2)
    
    while countDiv(triangle)<max_div:
        n +=1
        triangle = int(n*(n+1)/2)
    
    print(triangle)

triangle(500)
