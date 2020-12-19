import numpy as np

NW=np.array(input().split(),dtype=np.int64)

N=NW[0]
W=NW[1]

print(int(N/W))