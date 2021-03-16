import numpy as np

DTS=np.array(input().split(" "),dtype=np.int64)
D=DTS[0]
T=DTS[1]
S=DTS[2]

time=float(D/S)

if(T>=time):
    print("Yes")
else:
    print("No")