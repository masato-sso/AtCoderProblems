import numpy as np

NK=np.array(input().split(),dtype=np.int32)

N=NK[0]
K=NK[1]

count=1
th=K
while(True):
    if(N>=th):
        count+=1
        th=th*K
    else:
        break

print(count)