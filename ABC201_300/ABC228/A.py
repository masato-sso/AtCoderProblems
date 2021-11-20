
S,T,X = map(int, input().split())

flag = False
if(S<T):
    if(S<=X and X<T):
        flag = True
else:
    if(0<=X and X<T):
        flag = True
    if(S<=X and X<24):
        flag = True

if(flag):
    print("Yes")
else:
    print("No")
