import numpy as np

ABC=np.array(input().split(),dtype=np.int32)

ABC=np.sort(ABC)

if(ABC[0]==ABC[1]):
    if(ABC[1]==ABC[2]):
        print("No")
    else:
        print("Yes")
elif(ABC[1]==ABC[2]):
    if(ABC[0]==ABC[1]):
        print("No")
    else:
        print("Yes")
else:
    print("No")