import numpy as np

N,K=map(int,input().split())
a=list(map(int,input().split()))

a=np.array(a)
sorted_idx_a=np.argsort(a)

remains=K
ans=[0]*N

div=int(remains//N)
mod=remains%N
if(div>0):
    for i in range(N):
        ans[i]+=div
if(mod>0):
    for i in range(mod):
        ans[sorted_idx_a[i]]+=1

for a in ans:
    print(a)