import numpy as np

NKQ=np.array(input().split(),dtype=np.int32)

N=NKQ[0]
K=NKQ[1]
Q=NKQ[2]

score=[K]*N
score=np.array(score,dtype=np.int32)

A=[]
for i in range(Q):
    A.append(int(input())-1)

A=np.sort(A)

score=score-Q

for i in A:
    score[i]+=1
    

for i in range(N):
    if(score[i]<=0):
        print("No")
    else:
        print("Yes")
