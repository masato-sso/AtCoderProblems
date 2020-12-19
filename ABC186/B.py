import numpy as np

HW=np.array(input().split(),dtype=np.int64)

H=HW[0]
W=HW[1]

A=[]
min_A=101
for i in range(H):
    tmp=np.array(input().split(),dtype=np.int64)
    min_tmp=min(tmp)
    if(min_tmp<min_A):
        min_A=min_tmp
    A.append(tmp)

ans=0
for i in range(H):
    for j in range(W):
        t=A[i][j]
        ans+=t-min_A

print(ans)