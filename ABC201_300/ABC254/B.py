
N = int(input())

A = [[1]]
for i in range(1, N):
    tmp = [1]
    if(1 < i):
        for j in range(1, i):
            tmp.append(A[i-1][j-1]+A[i-1][j])
    tmp.append(1)
    A.append(tmp)

for a in A:
    tmp = list(map(str, a))
    print(" ".join(tmp))