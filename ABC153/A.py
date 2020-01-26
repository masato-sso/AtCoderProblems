import numpy as np

HA=np.array(input().split(" "),dtype=np.int32)
H=HA[0]
A=HA[1]

print(int(np.ceil(H/A)))