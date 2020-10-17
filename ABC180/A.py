import numpy as np

NAB=np.array(input().split(" "),dtype=np.int64)

N=NAB[0]
A=NAB[1]
B=NAB[2]

print(N-A+B)