
N = int(input())
P = list(map(int, input().split()))

parent = {}
i = 2
for p in P:
    parent[i] = p
    i += 1

target = P[N - 2]
ans = 1
for i in range(N):
    if(target == 1):
        break
    val = parent[target]
    ans += 1
    if(val == 1):
        break
    target = val

print(ans)
