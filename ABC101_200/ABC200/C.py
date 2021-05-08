from collections import defaultdict
from math import factorial

def cmb(n,r):
    return factorial(n) // factorial(r) // factorial(n - r)

N=int(input())
A=list(map(int,input().split()))

count_dict=defaultdict(int)
for a in A:
    mod=a%200
    count_dict[str(mod)]+=1
    
keys=list(count_dict.keys())
ans=0
for key in keys:
    value=count_dict[key]
    if(value>=2):
        ans+=cmb(value,2)

print(ans)