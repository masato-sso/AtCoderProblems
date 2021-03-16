
S=input()
T=input()

cnt=0
for i in range(len(S)):
    if(S[i]==T[i]):
        pass
    else:
        cnt+=1

print(cnt)