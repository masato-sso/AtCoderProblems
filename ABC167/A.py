
S=input()
T=input()

if(S==T[:len(S)] and len(S)+1==len(T)):
    print("Yes")
else:
    print("No")

