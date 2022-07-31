from collections import defaultdict

N, M = map(int, input().split())
UV = defaultdict(list)
for i in range(M):
    u,v = map(int, input().split())
    UV[u].append(v)

ans = 0
for a in range(1, 101):
    tmp = UV[a]
    for j in tmp:
        blist = UV[j]
        for val in blist:
            if(val in tmp):
                ans += 1

print(ans)

