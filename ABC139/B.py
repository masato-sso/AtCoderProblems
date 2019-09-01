import numpy as np

AB=input().split()

A=int(AB[0])
B=int(AB[1])

count=1

T=B-A

count=T/(A-1)+count

print(int(np.ceil(count)))