from decimal import *
import math

x = Decimal(input())
if (x < 0):
    print(math.ceil(x)//10)
else:
    print(math.floor(x)//10)
