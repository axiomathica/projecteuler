from math import sqrt, floor
# a = m^2-n^2 // b=2mn // c=m^2+n^2

# a+b+c = 1000 <=> 2m^2+2mn = 1000 <=> m^2+mn = 500 <=> m(m+n) = 500


max = floor(sqrt(500))

for div in range(2,max+1):
    if 500%div==0:
        other_div = int(500/div)
        diff = other_div-div
        if diff < div:
            a = div**2-diff**2
            b = 2*div*diff
            c = div**2+diff**2

            print(a*b*c)
        
