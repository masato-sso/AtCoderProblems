import numpy as np

NM=np.array(input().split(),dtype=np.int32)
N=NM[0]
M=NM[1]

A=np.array(input().split(),dtype=np.int32)

calc=N-sum(A)
if(calc>=0):
    print(calc)
else:
    print(-1)
