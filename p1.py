from fractions import Fraction as fr
import numpy as np
import math

m3 = [3*i for i in range(1,334)]
m5 = [5*i for i in range(1,200)]
m35 = [15*i for i in range(1,67)]

print (sum(m3)+sum(m5)-sum(m35))