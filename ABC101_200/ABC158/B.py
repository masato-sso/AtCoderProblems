import numpy as np

NAB=np.array(input().split(" "),dtype=np.int64)

N=NAB[0]
A=NAB[1]
B=NAB[2]

div=int(N//(A+B))
mod=N%(A+B)

blue=0
if(mod<=A):
    blue=mod
else:
    blue=A

print(A*div+blue)
