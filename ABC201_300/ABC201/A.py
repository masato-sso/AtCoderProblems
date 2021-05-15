
A=list(map(int,input().split()))

sorted_A=sorted(A)
A1=sorted_A[0]
A2=sorted_A[1]
A3=sorted_A[2]

dif23=A3-A2
dif12=A2-A1



if(dif23==dif12):
    print("Yes")
else:
    print("No")