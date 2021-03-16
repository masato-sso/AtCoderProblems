import numpy as np


AB=np.array(input().split(),dtype=np.int32)
A=AB[0]
B=AB[1]

result=-1
if(1<=A and A<=9):
    if(1<=B and B<=9):
        result=A*B

print(result)

