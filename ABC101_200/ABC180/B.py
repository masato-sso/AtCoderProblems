import numpy as np

N=int(input())
X=np.array(input().split(" "),dtype=np.int64)

abs_X=[]
for i in range(N):
    abs_X.append(abs(X[i]))

print(np.sum(abs_X))

u=0
for i in range(N):
    u+=pow(abs_X[i],2)

print(np.sqrt(u))

print(np.max(abs_X))
