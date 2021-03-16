
N=int(input())

S=input()

div=N/2

if(N%2==1):
    print("No")
else:
    tmp=S[0:int(div)]
    TT=tmp+tmp
    if(TT==S):
        print("Yes")
    else:
        print("No")
