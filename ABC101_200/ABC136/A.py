import numpy as np

I=input()
L=np.array(I.split(),dtype=np.int32)

A=L[0]
B=L[1]
C=L[2]

diff=A-B


if(C-diff<0):
    print(0)
else:
    print(C-diff)
