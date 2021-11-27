
N, W = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

sortedA = sorted(A)[::-1]

ans = 0
for i in range(N):
    if(W - min(W, sortedA[i][1]) < 0):
        break
    ans += sortedA[i][0]*min(W, sortedA[i][1])
    W = W - min(W, sortedA[i][1])

print(ans)
