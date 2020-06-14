import numpy as np

XN=np.array(input().split(" "),dtype=np.int32)
X=XN[0]
N=XN[1]

if(N==0):
    print(X)
else:
    p=np.array(input().split(" "),dtype=np.int32)
    p=np.sort(p)
    ABS=0
    results=[]
    length=0
    while(True):
        upper=X+ABS
        lower=X-ABS
        
        if(upper in p):
            pass
        else:
            results.append(upper)
            length+=1
        if(lower in p):
            pass
        else:
            results.append(lower)
            length+=1
        
        if(length>0):
            break
        ABS+=1
    print(min(results))