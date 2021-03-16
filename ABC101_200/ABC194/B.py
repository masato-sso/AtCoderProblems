import numpy as np

N=int(input())

A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

np_A=np.array(A)
np_B=np.array(B)
sort_A_idx=np.argsort(A)
sort_B_idx=np.argsort(B)

a_idx=sort_A_idx[0]
b_idx=sort_B_idx[0]

work1=1000000
if(a_idx==b_idx):
    work1=np_A[a_idx]+np_B[b_idx]
else:
    work1=max(np_A[a_idx],np_B[b_idx])
work2=max(np_A[a_idx],np_B[sort_B_idx[1]])
work3=max(np_A[sort_A_idx[1]],np_B[b_idx])

works=[work1,work2,work3]

print(min(works))
