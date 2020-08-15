import numpy as np

N=int(input())

L=np.array(input().split(" "),dtype=np.int64)

cnt=0
for idx in range(N):
    for jdx in range(idx,N):
        for kdx in range(jdx,N):
            a=L[idx]
            b=L[jdx]
            c=L[kdx]
            if(a!=b and b!=c and a!=c):
                if(a+b>c and b+c>a and c+a>b):
                    cnt+=1

print(cnt)
