import numpy as np

N=int(input())
B=np.array(input().split(),dtype=np.int32)

min_list=[]
min_list.append(B[0])
for i in range(0,N-1-1):
    min_list.append(min(B[i],B[i+1]))
min_list.append(B[-1])
#print(min_list)
print(sum(min_list))