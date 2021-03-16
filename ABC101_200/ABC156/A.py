import numpy as np

NR=np.array(input().split(),dtype=np.int32)

N=NR[0]
R=NR[1]

if(N>=10):
    print(R)
else:
    out=R+100*(10-N)
    print(out)
