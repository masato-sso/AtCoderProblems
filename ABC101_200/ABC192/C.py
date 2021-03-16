#import numpy as np

#NK=np.array(input().split(),dtype=np.int64)
N,K = map(int,input().split())

def g(x):
    str_x=str(x)
    w=[]
    for s in str_x:
        w.append(int(s))
    #out1=np.sort(w)
    out1=sorted(w)
    out2=out1[::-1]
    g1=""
    for t in out1:
        if(t==0):
            continue
        else:
            g1=g1+str(t)
    if(len(g1)==0):
        g1="0"
    g2=""
    for t in out2:
        g2=g2+str(t)
    if(len(g2)==0):
        g2="0"
    
    return int(g1),int(g2)

def f(x):
    g1,g2=g(x)
    return g2-g1

a=N
for i in range(1,K+1):
    a=f(a)

print(a)