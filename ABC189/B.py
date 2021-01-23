import numpy as np

NX=input().split()
N=int(NX[0])
X=int(NX[1])

VP=[]
for i in range(N):
    vp=[]
    tmp=input().split()
    vp.append(int(tmp[0]))
    vp.append(int(tmp[1]))
    VP.append(vp)

S=0
ans=-1
for i in range(N):
    drink=VP[i][0]*VP[i][1]
    S+=drink
    if(S>X*100):
        ans=i+1
        break

print(ans)
