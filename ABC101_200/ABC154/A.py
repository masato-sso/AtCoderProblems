import numpy as np

ST=np.array(input().split(" "))
S=ST[0]
T=ST[1]
AB=np.array(input().split(" "),dtype=np.int32)
A=AB[0]
B=AB[1]
U=input()

if(S==U):
    A=A-1
elif(T==U):
    B=B-1

result="{} {}".format(A,B)
print(result)