
S = input()

change_idx = [False] * len(S)

for idx,s in enumerate(S):
    if(s=='6' or s=='9'):
        change_idx[idx] = True

ans=""
for chidx,flag in enumerate(change_idx):
    if(flag):
        if(S[chidx]=='6'):
            ans+='9'
        elif(S[chidx]=='9'):
            ans+='6'
    else:
        ans+=S[chidx]

reverse_ans=ans[::-1]
print(reverse_ans)