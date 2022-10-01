
N, Q = map(int, input().split())
La = []
for i in range(N):
    tmp = list(map(int, input().split()))
    La.append(tmp)

ST = []
for i in range(Q):
    s, t = map(int, input().split())
    ST.append([s, t])

for i in range(Q):
    s = ST[i][0]
    t = ST[i][1]
    print(La[s - 1][t])