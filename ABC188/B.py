import numpy as np

N=int(input())

A=np.array(input().split(),dtype=np.int64)
B=np.array(input().split(),dtype=np.int64)

dot=np.dot(A,B)

if(dot==0):
    print("Yes")
else:
    print("No")
