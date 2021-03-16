import numpy as np

N=int(input())
V=np.sort(np.array(input().split(),dtype=np.float))

for i in range(1,N):
    V[i]=(V[i-1]+V[i])/2.0

print(np.max(V))
