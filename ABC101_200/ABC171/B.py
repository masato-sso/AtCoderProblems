import numpy as np

NK=np.array(input().split(" "),dtype=np.int64)
N=NK[0]
K=NK[1]

p=np.array(input().split(" "),dtype=np.int64)

sorted_p=np.sort(p)

L=sorted_p[:K]

print(sum(L))
