
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for i in range(N):
    C.append(A[i] + B[i])

flag = [False] * N
for x in range(X):
    pos = -1
    for i in range(N):
        if(not(flag[i])):
            if(pos == -1 or A[i] > A[pos]):
                pos = i
    flag[pos] = True

for y in range(Y):
    pos = -1
    for i in range(N):
        if(not(flag[i])):
            if(pos == -1 or B[i] > B[pos]):
                pos = i
    flag[pos] = True

for z in range(Z):
    pos = -1
    for i in range(N):
        if(not(flag[i])):
            if(pos == -1 or C[i] > C[pos]):
                pos = i
    flag[pos] = True

for i in range(N):
    if(flag[i]):
        print(i + 1)