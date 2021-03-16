import numpy as np

VTSD=np.array(input().split(),dtype=np.int64)

V=VTSD[0]
T=VTSD[1]
S=VTSD[2]
D=VTSD[3]

x0=T*V
if(x0>D):
    print("Yes")
else:
    D=D-x0
    vx=(S-T)*V
    if(D-vx<=0):
        print("No")
    else:
        print("Yes")