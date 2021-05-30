from collections import defaultdict

d = defaultdict(int)

N,K = map(int,input().split())

for i in range(N):
    a,b=map(int,input().split())
    d[a]+=b

A=d.keys()
A_size=len(A)
sorted_A=sorted(A)
K_reach=K

for i in range(A_size):
    if(sorted_A[i]<=K_reach):
        K_reach+=d[sorted_A[i]]
    else:
        break

print(K_reach)