
N = int(input())
A = []
for i in range(N):
    A.append(input())

flag = False
for i in range(N):
    for j in range(N):
        if(i == j):
            continue
        if(A[i][j] == "W" and A[j][i] == "L"):
            continue
        elif(A[i][j] == "L" and A[j][i] == "W"):
            continue
        elif(A[i][j] == "D" and A[j][i] == "D"):
            continue
        flag = True
        break
    if(flag):
        break

if(flag):
    print("incorrect")
else:
    print("correct")
