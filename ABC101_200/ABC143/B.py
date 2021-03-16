import numpy as np

N=int(input())

d=np.array(input().split(),dtype=np.int32)

s=0

for i in range(N):
    for j in range(i+1,N):
        s+=d[i]*d[j]

print(s)