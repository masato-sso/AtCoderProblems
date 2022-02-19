import math

H = float(input())

def calc(x):
    return math.sqrt(x * (12800000 + x))

print(calc(H))