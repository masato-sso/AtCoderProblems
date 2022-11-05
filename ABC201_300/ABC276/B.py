from collections import defaultdict

dic = defaultdict(list)

N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for i in range(1, N + 1):
    vals = dic[i]
    vals.sort()
    print(len(vals),*vals)

