import numpy as np

N=int(input())

xy=[]
x=[]
for i in range(N):
    xy.append(np.array(input().split(" "),dtype=np.int64))

flag=False
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            x1=xy[i][0]
            y1=xy[i][1]
            x2=xy[j][0]
            y2=xy[j][1]
            x3=xy[k][0]
            y3=xy[k][1]
            
            x1=x1-x3
            x2=x2-x3
            y1=y1-y3
            y2=y2-y3
            
            if(x1*y2==x2*y1):
                flag=True
                break
        if(flag):
            break
    if(flag):
        break

if(flag):
    print("Yes")
else:
    print("No")
