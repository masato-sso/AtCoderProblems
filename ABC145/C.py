import numpy as np
import itertools

N=int(input())

X=[]
Y=[]
for i in range(N):
    XY=input().split(" ")
    X.append(float(XY[0]))
    Y.append(float(XY[1]))

def get_dist(x1,y1,x2,y2):
    return np.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

seq=range(1,N+1)
p=list(itertools.permutations(seq))

totals=[]
for i in range(len(p)):
    route=list(p[i])
    S=0
    for k in range(len(route)-1):
        S+=get_dist(X[route[k]-1],Y[route[k]-1],X[route[k+1]-1],Y[route[k+1]-1])
    totals.append(S)

print(np.average(totals))