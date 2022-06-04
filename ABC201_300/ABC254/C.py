
N, K = map(int, input().split())
A = list(map(int, input().split()))

if(K == 1):
    print("Yes")

else:
    for i in range(K + 1):
        A[i-1::K] = sorted(A[i-1::K])
    
    if(sorted(A) == A):
        print("Yes")
    else:
        print("No")