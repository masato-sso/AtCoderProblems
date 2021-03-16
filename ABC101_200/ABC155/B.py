import numpy as np

N=int(input())
A=np.array(input().split(),dtype=np.int32)

out=A[A%2==0]

flag=False
for i in range(len(out)):
    if(out[i]%3==0 or out[i]%5==0):
        pass
    else:
        flag=True

if(flag):
    print("DENIED")
else:
    print("APPROVED")
