import numpy as np

N=int(input())

A=np.array(input().split(),dtype=np.int64)

size=pow(2,N)
div=int(size/2)

sub1=A[:div]
sub2=A[div:]

sub1_max=np.max(sub1)
sub2_max=np.max(sub2)

loser=0
if(sub1_max>sub2_max):
    loser=sub2_max
else:
    loser=sub1_max

ans_idx=np.where(A==loser)[0][0]

print(ans_idx+1)