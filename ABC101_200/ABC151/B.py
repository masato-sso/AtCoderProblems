import numpy as np

NKM=input().split(" ")
N=int(NKM[0])
K=int(NKM[1])
M=int(NKM[2])
A=np.array(input().split(" "),dtype=np.int64)

P=N*M

score=sum(A)

result=-1
for s in range(K,-1,-1):
    t=score+s
    if(t>=P):
        result=s
    else:
        break

print(result)
