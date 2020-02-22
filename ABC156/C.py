import numpy as np

N=int(input())
X=np.array(input().split(),dtype=np.int32)

ave_point=np.average(X)

can_point=[int(ave_point),int(ave_point)+1]

s1=0
s2=0
for i in range(N):
    s1+=pow((X[i]-can_point[0]),2)
    s2+=pow((X[i]-can_point[1]),2)

if(s1>s2):
    print(s2)
else:
    print(s1)
