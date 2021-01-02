import numpy as np

AB=np.array(input().split(),dtype=np.int64)

A=str(AB[0])
B=str(AB[1])

sa=0
for a in A:
    sa+=int(a)

sb=0
for b in B:
    sb+=int(b)

if(sa>=sb):
    print(sa)
else:
    print(sb)
