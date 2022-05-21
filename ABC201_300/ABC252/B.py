
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxV = max(A)
cansIdx = []
for i in range(N):
    a = A[i]
    if(a == maxV):
        cansIdx.append(i + 1)

flag = False
for idx in cansIdx:
    if(idx in B):
        flag = True
        break

if(flag):
    print("Yes")
else:
    print("No")
