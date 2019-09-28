import numpy as np

N=int(input())

A=np.array(input().split(),dtype=np.int32)

A_i=np.argsort(A)

result=""

for i in range(N):
    if(i==N-1):
        result=result+"{}".format(A_i[i]+1)
    else:
        result=result+"{} ".format(A_i[i]+1)

print(result)
