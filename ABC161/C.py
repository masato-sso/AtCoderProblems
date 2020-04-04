import numpy as np

NK=np.array(input().split(" "),dtype=np.int64)

N=NK[0]
K=NK[1]

x=N%K

abs_x=abs(x-K)

if(x<abs_x):
    print(x)
else:
    print(abs_x)

