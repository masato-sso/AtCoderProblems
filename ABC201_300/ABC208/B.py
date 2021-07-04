
def func(n):
    if(n==1):
        return 1
    else:
        return n*func(n-1)

P=int(input())

vals=[]
for i in range(1,11):
    vals.append(func(i))

target_idx=0

for i in range(len(vals)):
    v=vals[i]
    if(P<v):
        break
    target_idx=i

ans=0
remains=P
for i in range(target_idx,-1,-1):
    ans+=int(remains/vals[i])
    remains=remains%vals[i]

print(ans)