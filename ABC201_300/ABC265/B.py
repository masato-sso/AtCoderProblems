from collections import defaultdict

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = defaultdict(int)
for i in range(M):
    x, y = map(int, input().split())
    XY[x - 1] = y

time = T
flag = True
for i in range(N - 1):
    if(time <= 0):
        flag = False
        break
    time = time - A[i]
    time = time + XY[i]

if(time <= 0):
    flag = False

if(flag):
    print("Yes")
else:
    print("No")