import numpy as np

ABN=np.array(input().split(" "),dtype=np.int64)
A=ABN[0]
B=ABN[1]
N=ABN[2]

x=min(B-1,N)
calc=int(A*x/B)-A*int(x/B)

print(calc)
