
S=input()
N=len(S)

flag=True
for idx in range(0,int((N-1)/2),1):
    if(S[idx]==S[-(idx)-1]):
        pass
    else:
        flag=False
        break

j=0
for idx in range(int((N+3)/2)-1,N,1):
    if(S[idx]==S[j]):
        pass
    else:
        flag=False
        break
    j+=1

if(flag):
    print("Yes")
else:
    print("No")