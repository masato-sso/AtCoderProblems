import math

a, b, d = map(int, input().split())

ans_x = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
ans_y = b*math.cos(math.radians(d)) + a*math.sin(math.radians(d))

print("{} {}".format(ans_x, ans_y))