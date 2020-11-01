import numpy as np

N=int(input())

AB=[]
for i in range(N):
    AB.append(np.array(input().split(" "),dtype=np.int64))

ans=0
for i in range(N):
    a=AB[i][0]
    l=AB[i][1]
    n=l-a+1
    ans+=n*(a+l)/2

print(int(ans))