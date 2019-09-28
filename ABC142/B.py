import numpy as np

NK=np.array(input().split(),dtype=np.int32)

N=NK[0]
K=NK[1]

H=np.array(input().split(),dtype=np.int32)
H=np.sort(H)[::-1]

count=0
for i in range(N):
    if(H[i]>=K):
        count+=1
    else:
        break

print(count)