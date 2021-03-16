import numpy as np

N=int(input())

S=[]
count_S={}
for i in range(N):
    s=input()
    S.append(s)
    count_S[s]=0

for key in S:
    count_S[key]+=1

keys=np.array(list(count_S.keys()))
values=np.array(list(count_S.values()),dtype=np.int32)
out=np.where(values==np.max(values))
result=np.sort(keys[out])

for r in result:
    print(r)
