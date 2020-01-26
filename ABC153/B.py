import numpy as np

HN=np.array(input().split(" "),dtype=np.int32)
H=HN[0]
N=HN[1]

A=np.array(input().split(" "),dtype=np.int32)

damage=np.sum(A)

if(H<=damage):
    print("Yes")
else:
    print("No")
