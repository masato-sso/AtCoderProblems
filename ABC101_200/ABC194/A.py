
A,B=map(int,input().split())

X=A+B
if(X>=15 and B>=8):
    print(1)
elif(X>=10 and B>=3):
    print(2)
elif(X>=3):
    print(3)
else:
    print(4)
