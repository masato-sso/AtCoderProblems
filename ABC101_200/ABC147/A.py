import numpy as np

A=np.array(input().split(),dtype=np.int32)

s=np.sum(A)

if(s>=22):
    print("bust")
else:
    print("win")
