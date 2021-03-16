import numpy as np

N=int(input())
A=np.array(input().split(),dtype=np.int32)
B=np.array(input().split(),dtype=np.int32)

result=0
for i in range(N):
    if A[i]>B[i] and B[i]!=0:
        result+=B[i]
        A[i]=A[i]-B[i]
        B[i]=0
    else:
        result+=A[i]
        B[i]=B[i]-A[i]
        A[i]=0
        if A[i+1]>B[i]:
            result+=B[i]
            A[i+1]=A[i+1]-B[i]
            B[i]=0
        else:
            result+=A[i+1]
            B[i]=B[i]-A[i+1]
            A[i+1]=0

print(result)
