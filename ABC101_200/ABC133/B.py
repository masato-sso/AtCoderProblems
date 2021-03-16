import numpy as np
S=input()

tmp=S.split()
N=int(tmp[0])
D=int(tmp[1])

X=[]
for i in range(N):
    X.append(np.array(input().split(),dtype=np.int32))

import math

def calc_dist(x_i,x_j):
    s=0
    for i in range(len(x_i)):
        s+=pow((x_i[i]-x_j[i]),2)
    return math.sqrt(s)

count=0
for i in range(N):
    for j in range(i+1,N):
        result=calc_dist(X[i],X[j])
        
        if(result.is_integer()):
            count+=1

print(count)

