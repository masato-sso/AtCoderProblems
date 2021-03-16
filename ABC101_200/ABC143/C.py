
N=int(input())
S=input()

res=[]
tmp=""
for i in range(N):
    if i==0:
        tmp=S[0]
        res.append(S[0])
    else:
        if(tmp==S[i]):
            continue
        else:
            tmp=S[i]
            res.append(S[i])

print(len(res))
