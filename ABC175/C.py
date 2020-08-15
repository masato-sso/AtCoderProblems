
XKD=input().split(" ")
X=int(XKD[0])
K=int(XKD[1])
D=int(XKD[2])

X=abs(X)

if(X>=K*D):
    print(X-K*D)
else:
    k=int((X-X%D)/D)
    if((K-k)%2==0):
        print(X%D)
    else:
        print(abs(X%D-D))

