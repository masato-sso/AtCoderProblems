import collections

N=int(input())

A=list(map(int,input().split()))

c = collections.Counter(A)

keys=c.keys()

ans_flag=False
for k in keys:
    if(c[k]>=2):
        ans_flag=True
        break

if(ans_flag):
    print("No")
else:
    print("Yes")
