import numpy as np

X=np.array(input(),dtype=np.int64)

P=100
step=0
while(P<X):
    P+=P//100
    step+=1

print(step)