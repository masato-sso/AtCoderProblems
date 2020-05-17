import numpy as np
import math

ABHM=np.array(input().split(" "),dtype=np.int32)

A=ABHM[0]
B=ABHM[1]
H=ABHM[2]
M=ABHM[3]

minutes=H*60+M
long_angle=6*minutes%360
small_angle=0.5*minutes%360

angle=0
if(long_angle>small_angle):
    angle=long_angle-small_angle
else:
    angle=small_angle-long_angle

if(angle==180):
    S=A+B
else:
    S=np.sqrt(pow(A,2)+pow(B,2)-2*A*B*np.cos(np.radians(angle)))
print(S)




