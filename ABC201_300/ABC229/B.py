
A,B = map(str, input().split())

flag = False

for i in range(min(len(A), len(B))):
    if(len(A) < len(B)):
        a = int(A[i])
        b = int(B[i + len(B) - len(A)])
    elif(len(B) < len(A)):
        a = int(A[i + len(A) - len(B)])
        b = int(B[i])
    else:
        a = int(A[i])
        b = int(B[i])
    
    if(9 < a + b):
        flag = True
        break

if(flag):
    print("Hard")
else:
    print("Easy")
