import numpy as np

XY=np.array(input().split(),dtype=np.int64)

X=XY[0]
Y=XY[1]

label=""
if(X<Y):
    label="A"
else:
    label="B"

if(label=="A"):
    X+=3
else:
    Y+=3

after_lb=""
if(X<Y):
    after_lb="A"
else:
    after_lb="B"

if(X==Y):
    print("No")
else:
    if(label==after_lb):
        print("No")
    else:
        print("Yes")
