import numpy as np

N=int(input())

A=np.array(input().split(" "),dtype=np.int32)

tA=list(set(A))

if(len(A)==len(tA)):
    print("YES")
else:
    print("NO")