
K=int(input())
S=input()

SL=len(S)

if(SL<=K):
    print(S)
else:
    print(S[:K]+"...")
