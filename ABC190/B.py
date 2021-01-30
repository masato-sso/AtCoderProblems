import numpy as np

NSD=np.array(input().split(),dtype=np.int64)
N=NSD[0]
S=NSD[1]
D=NSD[2]

XY=[]
for i in range(N):
    XY.append(np.array(input().split(),dtype=np.int64))

damage=False
for i in range(N):
    X=XY[i][0]
    Y=XY[i][1]
    out=False

    if(X>=S):
        out=True
    if(Y<=D):
        out=True
    
    if(out):
        continue
    else:
        damage=True

if(damage):
    print("Yes")
else:
    print("No")
