import numpy as np

NK=np.array(input().split(" "),dtype=np.int64)
N=NK[0]
K=NK[1]

H=np.array(input().split(" "),dtype=np.int64)

sort_H=np.sort(H)[::-1]

remain_H=np.sum(sort_H[K::])

print(remain_H)

