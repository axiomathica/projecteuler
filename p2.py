a = 1
b = 2
sum = 0

while b <= 4000000:
    if b%2 == 0:
        sum += b
    
    c = a+b
    a = b
    b = c

print (sum)
    

##*********************************************##

def sum_even_fibonacci(limit):
    a, b = 1, 2
    total_sum = 0
    
    while b <= limit:
        total_sum += b  # b starts as 2, and then every third number
        a, b = b, a + b  # First odd
        a, b = b, a + b  # Second odd
        a, b = b, a + b  # Third (even)
    
    return total_sum

# Usage
print(sum_even_fibonacci(4000000))
