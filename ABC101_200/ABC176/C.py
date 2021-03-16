import numpy as np

N=int(input())

A=np.array(input().split(" "),dtype=np.int64)

step=[0]
Max=A[0]
for i in range(1,N):
    if(Max>A[i]):
        step.append(Max-A[i])
    else:
        Max=A[i]
        step.append(0)

print(sum(step))