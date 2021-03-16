import numpy as np

SW=np.array(input().split(" "),dtype=np.int32)
S=SW[0]
W=SW[1]

if(W>=S):
    print("unsafe")
else:
    print("safe")
