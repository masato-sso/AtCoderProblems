from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

sortedKey = sorted(d)[::-1]

for key in sortedKey:
    print(d[key])

diff = N - len(sortedKey)
for i in range(diff):
    print(0)
