
N = int(input())

data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append((a,1))
    data.append((a+b,-1))

data.sort(key=lambda x: x[0])

ans = [0]*(N+1)
cnt = 0
for i in range(len(data) - 1):
    cnt += data[i][1]
    ans[cnt] += data[i+1][0] - data[i][0]

print(*ans[1:])
