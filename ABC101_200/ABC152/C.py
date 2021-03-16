import numpy as np

N=int(input())

P=np.array(input().split(" "),dtype=np.int32)

count=1

t=P[0]
for i in range(0,N-1):
    if(t>=P[i+1]):
        t=P[i+1]
        count+=1


print(count)
