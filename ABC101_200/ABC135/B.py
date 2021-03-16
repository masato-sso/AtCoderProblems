import numpy as np

N=int(input())
P=np.array(input().split(),dtype=np.int32)


if (np.sort(P) == P).all():
    print("YES")
else:
    sort_P=np.sort(P)
    count=0
    for i in range(N):
        if sort_P[i]!=P[i]:
            count+=1
    if count==2:
        print("YES")
    else:
        print("NO")