import numpy as np

NXT=np.array(input().split(" "),dtype=np.int64)
N=NXT[0]
X=NXT[1]
T=NXT[2]

print(int(np.ceil(float(N/X))*T))