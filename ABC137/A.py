import numpy as np

I=np.array(input().split(),dtype=np.int32)

A=I[0]
B=I[1]

plus=A+B
sub=A-B
mul=A*B

a=[]

a.append(plus)
a.append(sub)
a.append(mul)

print(max(a))
