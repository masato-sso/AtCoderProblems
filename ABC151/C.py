import numpy as np

NM=np.array(input().split(" "),dtype=np.int32)

result={}
tmp=[]

for i in range(NM[1]):
    s=input().split(" ")
    result.setdefault(s[0],[]).append(s[1])

corrects=0
penalty=0
keys=result.keys()

for k in keys:
    L=result[k]
    if('AC' in L):
        idx=L.index('AC')
    else:
        idx=-1
    if(idx==-1):
        continue
    else:
        penalty+=idx
        corrects+=1

print("{} {}".format(corrects,penalty))

