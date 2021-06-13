import math

A,B,C=map(float,input().split())

Aneg_flag=False
Bneg_flag=False
if(A<0):
    A=(-1)*A
    Aneg_flag=True
if(B<0):
    B=(-1)*B
    Bneg_flag=True

if(A!=0 and B!=0):
    logA=math.log2(A)
    logB=math.log2(B)
else:
    if(A==0 and B!=0):
        logA=0
        logB=math.log2(B)
    elif(A!=0 and B==0):
        logA=math.log2(A)
        logB=0
    else:
        logA=0
        logB=0

if(C%2==1):
    if(Aneg_flag):
        logA=(-1)*logA
    if(Bneg_flag):
        logB=(-1)*logB

if(logA>logB):
    print(">")
elif(logA<logB):
    print("<")
else:
    print("=")
