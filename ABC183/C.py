import numpy as np
import itertools

NK=np.array(input().split(" "),dtype=np.int64)
N=NK[0]
K=NK[1]

T=[]
for i in range(N):
    T.append(np.array(input().split(" "),dtype=np.int64))

labels=[]
for i in range(1,N):
    labels.append(str(i))

paths=[]
for v in itertools.permutations(labels):
    paths.append([0]+list(v)+[0])

times=[]
for path in paths:
    from_p=path[0]
    time=[]
    for to in path[1:-1]:
        time.append(T[int(from_p)][int(to)])
        from_p=to
    time.append(T[int(from_p)][0])
    times.append(np.sum(time))

cnt=0
for t in times:
    if(t==K):
        cnt+=1

print(cnt)