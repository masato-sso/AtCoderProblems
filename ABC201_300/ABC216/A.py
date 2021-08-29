
XY=input().split(".")
X=XY[0]
Y=int(XY[1])

if(0<=Y and Y<=2):
    print(X+"-")
elif(3<=Y and Y<=6):
    print(X)
else:
    print(X+"+")

