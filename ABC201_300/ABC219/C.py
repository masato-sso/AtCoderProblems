import numpy as np

X=input()
N=int(input())
S=[]
for i in range(N):
    S.append(input())

num_S=[]
for s in S:
    tmp=s
    for i,x in enumerate(X):
        if(i+1<10):
            s=s.replace(x,"0"+str(i+1))
        else:
            s=s.replace(x,str(i+1))
    num_S.append("1"+s)

S=np.array(S)
ans=S[np.argsort(num_S)]

for i in range(N):
    print(ans[i])
