import numpy as np

ABK=np.array(input().split(),dtype=np.int64)

A=ABK[0]
B=ABK[1]
K=ABK[2]

if(A>=K):
    A=A-K
else:
    if(B>=K-A):
        B=B-(K-A)
    else:
        B=0
    A=0

print("{} {}".format(A,B))