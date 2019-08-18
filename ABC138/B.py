import numpy as np

N=int(input())
A=np.array(input().split(),dtype=np.int32)

S=0
for a in A:
    S+=1.0/a

print(1.0/S)