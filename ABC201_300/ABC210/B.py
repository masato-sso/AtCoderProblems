
N=int(input())
S=input()

ans=""
for i in range(N):
    if(S[i]=="1"):
        if(i%2==0):
            ans="Takahashi"
        else:
            ans="Aoki"
        break

print(ans)
