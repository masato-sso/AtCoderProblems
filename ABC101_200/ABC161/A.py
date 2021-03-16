
XYZ=input().split(" ")
X=XYZ[0]
Y=XYZ[1]
Z=XYZ[2]

tmp=X
X=Y
Y=tmp

tmp=X
X=Z
Z=tmp

print("{} {} {}".format(X,Y,Z))