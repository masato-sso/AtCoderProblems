import numpy as np

x=np.array(input().split(" "),dtype=np.int32)

for idx in range(len(x)):
    if(x[idx]==0):
        print(idx+1)
        break