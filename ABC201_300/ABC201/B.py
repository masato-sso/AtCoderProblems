import numpy as np

N=int(input())

S=[]
T=[]
for i in range(N):
    s,t=map(str,input().split())
    S.append(s)
    T.append(int(t))

sorted_T=np.argsort(T)[::-1]

print(S[sorted_T[1]])