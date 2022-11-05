
N = int(input())
P = list(map(int, input().split()))

idx = N - 2
while(P[idx] < P[idx + 1]):
    idx -= 1

k = N - 1
while(P[idx] < P[k]):
    k -= 1

tmp = P[idx]
P[idx] = P[k]
P[k] = tmp
print(*P[:idx + 1], *P[:idx:-1])