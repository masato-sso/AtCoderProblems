import numpy as np

size=input()
pro=input()

p=np.array(pro.split(" "),dtype=np.int32)
p=np.sort(p)

me=int(len(p)/2)

print(p[me]-p[me-1])
