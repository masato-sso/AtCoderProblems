import numpy as np

NM=np.array(input().split(" "),dtype=np.int32)
N=NM[0]
M=NM[1]

A=np.array(input().split(" "),dtype=np.int32)

total=sum(A)

th=total*(1/(4*M))

count=0

for a in A:
    if(a>=th):
        count+=1

if(count>=M):
    print("Yes")
else:
    print("No")
