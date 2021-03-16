import numpy as np

NM=np.array(input().split(" "),dtype=np.int64)

N=NM[0]
M=NM[1]

result=0

if(N>=2):
    result+=N*(N-1)/2

if(M>=2):
    result+=M*(M-1)/2

print(int(result))