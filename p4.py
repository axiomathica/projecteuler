import math

def largest_palindrome():

    for x in range(997,99,-1):
        palindrome = x*1000+int(str(x)[::-1])
        max_d = math.floor(math.sqrt(palindrome))

        for d in range(max_d, 99, -1):
            if (palindrome % d == 0 ):
                other = palindrome // d
                if 100 <= other <= 999:
                    print(palindrome)
                    return
                      

largest_palindrome()

    

