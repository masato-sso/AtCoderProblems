import numpy as np

AB=np.array(input().split(),dtype=np.int32)

A=AB[0]
B=AB[1]

res=A-2*B

if(res<=0):
    print(0)
else:
    print(res)