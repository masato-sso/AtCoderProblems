import numpy as np

N=int(input())
H=np.array(input().split(),dtype=np.int32)

flag=True

for i in range(N-1,0,-1):
    if(H[i]>=H[i-1]):
        continue
    else:
        H[i-1]=H[i-1]-1
        if(H[i]<H[i-1]):
            flag=False

if(flag):
    print("Yes")
else:
    print("No")