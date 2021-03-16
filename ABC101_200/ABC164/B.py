import numpy as np
import math

ABCD=np.array(input().split(" "),dtype=np.int32)

A=ABCD[0]
B=ABCD[1]
C=ABCD[2]
D=ABCD[3]

Aturn=math.ceil(A/D)
Cturn=math.ceil(C/B)

if(Aturn>=Cturn):
    print("Yes")
else:
    print("No")

