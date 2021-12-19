import itertools

N, M = map(int, input().split())
A = [[False] * N for i in range(N)]
B = [[False] * N for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    A[a][b] = True
    A[b][a] = True

for i in range(M):
    c, d = map(int, input().split())
    c = c - 1
    d = d - 1
    B[c][d] = True
    B[d][c] = True

flag = False
for p in itertools.permutations(range(N)):
    exist = True
    for i in range(N):
        for j in range(N):
            if(A[i][j] != B[p[i]][p[j]]):
                exist = False
    if(exist):
        flag = True
        break

if(flag):
    print("Yes")
else:
    print("No")
