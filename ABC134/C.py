import numpy as np

N=int(input())

X=[]
for x in range(N):
    X.append(int(input()))

Y=[]
Y=np.sort(X)[::-1]

for i in range(N):
    ans=Y[0]
    if ans==X[i]:
        ans=Y[1]
    print(ans)
