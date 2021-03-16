import numpy as np

N=int(input())

xy=[]
for i in range(N):
    xy.append(np.array(input().split(),dtype=np.float64))

ans=0
for i in range(N-1):
    for j in range(i+1,N):
        a=(xy[j][1]-xy[i][1])/(xy[j][0]-xy[i][0])
        if(-1<=a and a<=1):
            ans+=1

print(ans)
