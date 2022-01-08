import itertools
import math

N = int(input())
points = []
for i in range(N):
    x,y = map(int, input().split())
    points.append([x, y])

def calcDist(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

cans = list(itertools.combinations(points, 2))
ans = -1
dist = 0
for can in cans:
    dist = calcDist(can[0], can[1])
    if(dist > ans):
        ans = dist

print(ans)
