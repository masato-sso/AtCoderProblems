import math

A, B = map(float, input().split())

dist = math.sqrt(A*A + B*B)

print("{} {}".format(A/dist, B/dist))
