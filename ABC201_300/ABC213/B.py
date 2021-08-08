import numpy as np

N=int(input())
A=np.array(list(map(int,input().split())),dtype=np.int64)

print(np.argsort(A)[-2]+1)