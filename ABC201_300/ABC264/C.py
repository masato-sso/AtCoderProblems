
H1, W1 = map(int, input().split())
A = []
for i in range(H1):
    a = list(map(int, input().split()))
    A.append(a)

H2, W2 = map(int, input().split())
B = []
for i in range(H2):
    b = list(map(int, input().split()))
    B.append(b)

for h in range(1 << H1):
    for w in range(1 << W1):
        hvec = []
        wvec = []
        for k in range(1, H1 + 1):
            if((h & (1 << (k - 1))) == 0):
                hvec.append(k)
        for k in range(1, W1 + 1):
            if((w & (1 << (k - 1))) == 0):
                wvec.append(k)
        if(len(hvec) != H2 or len(wvec) != W2):
            continue

        match = True
        for k in range(H2):
            for l in range(W2):
                if(A[hvec[k] - 1][wvec[l] - 1] != B[k][l]):
                    match = False
                    break
        
        if(match):
            print("Yes")
            exit(0)

print("No")
