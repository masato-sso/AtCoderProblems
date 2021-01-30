import numpy as np

ABC=np.array(input().split(),dtype=np.int64)

A=ABC[0]
B=ABC[1]
C=ABC[2]

winner=""
if(C==0):
    if(A==B):
        winner="Aoki"
    elif(A>B):
        winner="Takahashi"
    else:
        winner="Aoki"
else:
    if(A==B):
        winner="Takahashi"
    elif(A>B):
        winner="Takahashi"
    else:
        winner="Aoki"

print(winner)