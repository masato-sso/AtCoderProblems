import numpy as np

N=int(input())
p=list(map(int,input().split()))
p=np.array(p,dtype=np.int64)

sorted_idx=np.argsort(p)
Q=sorted_idx+1

ans=""
for idx,q in enumerate(Q):
    ans=ans+str(q)
    if(idx!=len(Q)-1):
        ans=ans+" "

print(ans)