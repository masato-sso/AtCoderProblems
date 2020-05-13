import numpy as np

ABCK=np.array(input().split(" "),dtype=np.int64)

A=ABCK[0]
B=ABCK[1]
C=ABCK[2]
K=ABCK[3]

total=0
cnt=1

if(A<=K):
    total+=1*A
    K=K-A
    if(B<=K):
        K=K-B
        if(0<K):
            total+=-1*K
        else:
            pass
    else:
        pass
else:
    total+=1*K

print(total)
