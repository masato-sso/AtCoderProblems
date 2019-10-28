import numpy as np

N=int(input())

ans=pow(10,13)
for i in range(1,int(np.sqrt(N))+1):
    if(N%i!=0):
        continue
    j=N/i
    ans=min(ans,i+j-2)

print(int(ans))
