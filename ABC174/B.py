import numpy as np

ND=np.array(input().split(),dtype=np.int64)
XY=[]
for i in range(ND[0]):
    XY.append(np.array(input().split(),dtype=np.int64))

D=ND[1]

cnt=0
for xy in XY:
    x=xy[0]
    y=xy[1]
    if(np.sqrt(pow(x,2)+pow(y,2))<=D):
        cnt+=1

print(cnt)

