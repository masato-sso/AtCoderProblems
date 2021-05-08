
N,K=map(int,input().split())

ans=N
for k in range(K):
    if(ans%200==0):
        ans=int(ans/200)
    else:
        str_ans=str(ans)
        str_ans=str_ans+"200"
        ans=int(str_ans)

print(ans)