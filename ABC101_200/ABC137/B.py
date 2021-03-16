import numpy as np

I=np.array(input().split(),dtype=np.int32)

K=I[0]
X=I[1]

result=""

for x in range(X-(K-1),X+K):
    result=result+str(x)+" "

print(result)