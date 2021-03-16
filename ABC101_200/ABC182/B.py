import numpy as np

N=int(input())

A=np.array(input().split(" "),dtype=np.int64)

max_gcd=0
ans_k=2
for k in range(2,max(A)+1):
    gcd=0
    for n in A:
        if(n%k==0):
            gcd+=1
    if(max_gcd<=gcd):
        max_gcd=gcd
        ans_k=k

print(ans_k)