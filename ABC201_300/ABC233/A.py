import math

X, Y = map(float, input().split())

diff = Y - X
if (diff < 0):
    print(0)
else:
    print(math.ceil(diff/10))
